# -*- coding: utf-8 -*-
import sys
import io

# 修复Windows控制台编码问题
if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except:
        pass

"""
ModelScope 文生图脚本
用法: 
  python generate_image.py "中文提示词" [模型ID或序号] [分辨率] [步数]
  python generate_image.py --update-models        # 更新模型列表
  python generate_image.py --list-models          # 查看模型列表
  python generate_image.py --set-default 2         # 设置默认模型（序号）
"""
import requests
import time
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from PIL import Image
from io import BytesIO

# ========== 配置 ==========
# 从 modelscope_usage.json 读取配置
SCRIPT_DIR = Path(__file__).parent
SKILL_DIR = SCRIPT_DIR.parent  # t2i skill 根目录
CONFIG_FILE = SCRIPT_DIR / "modelscope_config.json"
USAGE_FILE = SCRIPT_DIR / "modelscope_config.json"
MODELS_FILE = SCRIPT_DIR / "models_list.json"

def load_config() -> dict:
    """从 modelscope_usage.json 加载配置"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        config = data.get("config", {})
        return {
            "API_KEY": config.get("API_KEY", ""),
            "DEFAULT_MODEL": config.get("DEFAULT_MODEL", "Tongyi-MAI/Z-Image-Turbo"),
            "BASE_URL": config.get("BASE_URL", "https://api-inference.modelscope.cn/"),
            "output_dir": data.get("output_dir", "assets")
        }
    return {
        "API_KEY": "",
        "DEFAULT_MODEL": "Tongyi-MAI/Z-Image-Turbo",
        "BASE_URL": "https://api-inference.modelscope.cn/",
        "output_dir": "assets"
    }

_config = load_config()
API_KEY = _config["API_KEY"]
DEFAULT_MODEL = _config["DEFAULT_MODEL"]
BASE_URL = _config["BASE_URL"]
OUTPUT_DIR = SKILL_DIR / _config["output_dir"]

# 确保输出目录存在
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ========== 模型列表管理 ==========
def load_models() -> dict:
    """加载本地模型列表"""
    if MODELS_FILE.exists():
        with open(MODELS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"update_time": "", "default_index": 1, "models": []}

def save_models(models_data: dict):
    """保存模型列表"""
    with open(MODELS_FILE, 'w', encoding='utf-8') as f:
        json.dump(models_data, f, indent=2, ensure_ascii=False)

def update_models_from_api() -> dict:
    """从API获取最新模型列表"""
    print("正在从 ModelScope API 获取模型列表...")
    
    url = "https://modelscope.cn/api/v1/dolphin/models"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "PageSize": 30,
        "PageNumber": 1,
        "SortBy": "Default",
        "Target": "",
        "Criterion": [
            {"category": "support_pai_model_gallery", "predicate": "contains", "values": ["deploy"]},
            {"category": "tasks", "predicate": "contains", "values": ["text-to-image-synthesis"], "sub_values": []}
        ],
        "SingleCriterion": [
            {"category": "inference_type", "DateType": "int", "predicate": "equal", "IntValue": 1}
        ]
    }
    
    response = requests.put(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    
    if data.get("Code") != 200:
        raise Exception(f"API返回错误: {data}")
    
    # 提取模型数据
    models = data.get("Data", {}).get("Model", {}).get("Models", [])
    
    # 处理每个模型，提取需要的字段
    model_list = []
    for model in models:
        last_updated = model.get("LastUpdatedTime", 0)
        model_id = model.get("BackendSupport", {}).get("model_id", "")
        name = model.get("Name", "")
        
        if model_id and last_updated:
            model_list.append({
                "model_id": model_id,
                "name": name,
                "last_updated": last_updated,
                "downloads": model.get("Downloads", 0),
                "stars": model.get("Stars", 0)
            })
    
    # 按 LastUpdatedTime 降序排序
    model_list.sort(key=lambda x: x["last_updated"], reverse=True)
    
    # 添加序号（从1开始）
    for i, model in enumerate(model_list, 1):
        model["index"] = i
    
    # 保存到本地
    models_data = {
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "default_index": 1,
        "models": model_list
    }
    save_models(models_data)
    
    print(f"✅ 模型列表更新成功！共获取 {len(model_list)} 个模型")
    return models_data

def list_models():
    """列出本地模型列表"""
    models_data = load_models()
    models = models_data.get("models", [])
    default_index = models_data.get("default_index", 1)
    
    if not models:
        print("本地模型列表为空，请先运行 --update-models 更新模型列表")
        return
    
    print("\n" + "=" * 60)
    print("📋 ModelScope 可用模型列表")
    print("=" * 60)
    print(f"更新时间: {models_data.get('update_time', '未知')}")
    print(f"默认模型: 序号 {default_index}")
    print("-" * 60)
    print(f"{'序号':<6}{'模型ID':<40}{'更新时间':<15}")
    print("-" * 60)
    
    for model in models:
        index = model.get("index", 0)
        model_id = model.get("model_id", "")
        last_updated = model.get("last_updated", 0)
        
        # 转换时间戳为可读格式
        try:
            time_str = datetime.fromtimestamp(last_updated).strftime("%Y-%m-%d")
        except:
            time_str = "未知"
        
        # 标记默认模型
        marker = " ★" if index == default_index else ""
        print(f"{index:<6}{model_id:<40}{time_str:<15}{marker}")
    
    print("=" * 60)

def set_default_model(index: int) -> bool:
    """设置默认模型"""
    models_data = load_models()
    models = models_data.get("models", [])
    
    if not models:
        print("本地模型列表为空，请先运行 --update-models 更新模型列表")
        return False
    
    if index < 1 or index > len(models):
        print(f"❌ 无效的序号 {index}，有效范围: 1-{len(models)}")
        return False
    
    models_data["default_index"] = index
    save_models(models_data)
    
    model = models[index - 1]
    print(f"✅ 默认模型已设置为: 序号 {index} - {model.get('model_id')}")
    return True

def get_model_by_index_or_id(model_input: str) -> str:
    """根据输入获取模型ID（支持序号或模型ID）"""
    models_data = load_models()
    models = models_data.get("models", [])
    default_index = models_data.get("default_index", 1)
    
    # 如果模型列表为空，使用旧的默认逻辑
    if not models:
        if not model_input or model_input == "default":
            return DEFAULT_MODEL
        return model_input
    
    # 尝试解析为序号
    try:
        index = int(model_input)
        if 1 <= index <= len(models):
            return models[index - 1]["model_id"]
        else:
            print(f"⚠️ 序号 {index} 超出范围，使用默认模型")
            return models[default_index - 1]["model_id"]
    except ValueError:
        # 不是序号，尝试作为模型ID
        # 检查是否在列表中
        for model in models:
            if model.get("model_id") == model_input:
                return model_input
        
        # 不在列表中，直接使用
        print(f"⚠️ 模型ID {model_input} 不在列表中，将直接使用")
        return model_input

def get_default_model() -> str:
    """获取当前默认模型"""
    models_data = load_models()
    models = models_data.get("models", [])
    default_index = models_data.get("default_index", 1)
    
    if not models:
        return DEFAULT_MODEL
    
    if 1 <= default_index <= len(models):
        return models[default_index - 1]["model_id"]
    return DEFAULT_MODEL

# ========== 用量统计 ==========
def load_usage() -> dict:
    """加载当日使用量"""
    if USAGE_FILE.exists():
        with open(USAGE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        today = datetime.now().strftime("%Y-%m-%d")
        if data.get("date") != today:
            return {"date": today, "models": {}, "total": 0}
        return data
    return {"date": datetime.now().strftime("%Y-%m-%d"), "models": {}, "total": 0}

def save_usage(usage: dict):
    """保存使用量"""
    with open(USAGE_FILE, 'w', encoding='utf-8') as f:
        json.dump(usage, f, indent=2, ensure_ascii=False)

def check_quota(model: str, usage: dict) -> tuple[bool, str]:
    """检查配额是否充足"""
    model_count = usage["models"].get(model, 0)
    total_count = usage.get("total", 0)

    if model_count >= 500:
        return False, f"模型 {model} 今日调用次数已达上限(500次)"
    if total_count >= 2000:
        return False, "今日总调用次数已达上限(2000次)"
    return True, ""

def increment_usage(model: str, usage: dict):
    """增加使用计数"""
    usage["models"][model] = usage["models"].get(model, 0) + 1
    usage["total"] = usage.get("total", 0) + 1
    save_usage(usage)

# ========== 提示词优化 ==========
def optimize_prompt(chinese_prompt: str) -> str:
    """将中文提示词优化为英文FLUX/SD格式"""
    quality_tags = "masterpiece, best quality, ultra detailed, 8k, photorealistic, highly detailed"
    lighting_tags = "natural lighting, soft lighting, professional lighting, chiaroscuro"
    style_tags = "professional photography, film grain, bokeh, shallow depth of field"

    optimized = f"{chinese_prompt}, {quality_tags}, {lighting_tags}, {style_tags}"
    return optimized

# ========== API调用 ==========
def create_generation_task(req_data: dict) -> str:
    """创建生图任务"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "X-ModelScope-Async-Mode": "true"
    }

    response = requests.post(
        f"{BASE_URL}v1/images/generations",
        headers=headers,
        data=json.dumps(req_data, ensure_ascii=False).encode('utf-8')
    )
    response.raise_for_status()
    data = response.json()
    return data["task_id"]

def fetch_task_result(task_id: str) -> dict:
    """查询生图任务结果"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "X-ModelScope-Task-Type": "image_generation"
    }

    start_time = time.time()

    while True:
        result = requests.get(
            f"{BASE_URL}v1/tasks/{task_id}",
            headers=headers
        )
        result.raise_for_status()
        data = result.json()

        if data["task_status"] == "SUCCEED":
            elapsed_time = time.time() - start_time
            return {
                "status": "success",
                "image_url": data["output_images"][0],
                "elapsed_time": elapsed_time
            }
        elif data["task_status"] == "FAILED":
            return {"status": "failed", "error": data.get("message", "Unknown error")}

        time.sleep(5)

# ========== 主函数 ==========
def generate_image(
    prompt: str,
    model: str = None,
    negative_prompt: str = "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry",
    size: str = "1024x1024",
    steps: int = 30,
    guidance: float = 7.5
) -> dict:
    """生成图像的主函数"""
    # 检测 API_KEY 是否配置
    if not API_KEY:
        return {
            "code": 0,
            "msg": "API_KEY未配置，请先去 https://modelscope.cn/my/access/token 申请"
        }

    # 如果未指定模型，获取默认模型
    if not model or model == "default":
        model = get_default_model()
        print(f"使用默认模型: {model}")
    else:
        # 支持序号或模型ID
        model = get_model_by_index_or_id(model)
        print(f"使用模型: {model}")
    
    # 1. 加载并检查配额
    usage = load_usage()
    can_use, error_msg = check_quota(model, usage)
    if not can_use:
        return {"code": 0, "msg": error_msg}

    # 2. 优化提示词
    optimized_prompt = optimize_prompt(prompt)
    print(f"优化后的提示词: {optimized_prompt}")

    # 3. 构建请求数据
    req_data = {
        "model": model,
        "prompt": optimized_prompt,
        "negative_prompt": negative_prompt,
        "size": size,
        "steps": steps,
        "guidance": guidance
    }

    # 4. 创建任务
    print(f"正在生成图像...")
    task_id = create_generation_task(req_data)
    print(f"任务ID: {task_id}")

    # 5. 获取结果
    result = fetch_task_result(task_id)

    if result["status"] == "success":
        # 6. 保存图片到 assets 目录
        image = Image.open(BytesIO(requests.get(result["image_url"]).content))
        save_filename = f"generated_{task_id}.jpg"
        save_path = OUTPUT_DIR / save_filename
        image.save(save_path)

        # 7. 更新用量统计
        increment_usage(model, usage)

        # 8. 返回完整信息
        return {
            "code": 1,
            "msg": "",
            "original_prompt": prompt,
            "optimized_prompt": optimized_prompt,
            "model": model,
            "model_usage": usage["models"].get(model, 1),
            "total_usage": usage.get("total", 1),
            "elapsed_time": round(result["elapsed_time"], 2),
            "image_url": result["image_url"],
            "local_path": str(save_path)
        }
    else:
        return {"code": 0, "msg": result.get("error", "Unknown error")}

# ========== 命令行入口 ==========
if __name__ == "__main__":
    # 获取命令行参数
    args = sys.argv[1:]
    
    # 处理特殊命令
    if "--update-models" in args or "-u" in args:
        try:
            update_models_from_api()
        except Exception as e:
            print(f"❌ 更新模型列表失败: {e}")
        sys.exit(0)
    
    if "--list-models" in args or "-l" in args:
        list_models()
        sys.exit(0)
    
    if "--set-default" in args:
        try:
            idx = args.index("--set-default")
            if idx + 1 < len(args):
                index = int(args[idx + 1])
                set_default_model(index)
            else:
                print("用法: python generate_image.py --set-default <序号>")
        except ValueError:
            print("序号必须是数字")
        except Exception as e:
            print(f"❌ 设置默认模型失败: {e}")
        sys.exit(0)
    
    if "--get-default" in args:
        default = get_default_model()
        print(f"当前默认模型: {default}")
        sys.exit(0)

    if not args:
        print("用法:")
        print("  生成图像:")
        print("    python generate_image.py \"中文提示词\" [模型ID或序号] [分辨率] [步数]")
        print("  更新模型列表:")
        print("    python generate_image.py --update-models")
        print("  查看模型列表:")
        print("    python generate_image.py --list-models")
        print("  设置默认模型:")
        print("    python generate_image.py --set-default <序号>")
        print(f"\n当前默认模型: {get_default_model()}")
        sys.exit(1)

    prompt = args[0]
    model = args[1] if len(args) > 1 else None
    size = args[2] if len(args) > 2 else "1024x1024"
    steps = int(args[3]) if len(args) > 3 else 30

    result = generate_image(prompt, model, size=size, steps=steps)

    # 直接输出 JSON 格式
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result.get("code") == 1 else 1)
