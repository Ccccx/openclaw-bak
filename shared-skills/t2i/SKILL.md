---
name: t2i
description: 调用ModelScope API生成图像的技能。当用户请求生成图片、文生图、使用modelscope创建图像时使用此技能。支持中文提示词自动优化为英文FLUX/SD格式，包含用量统计和结果汇总功能。
version: 1.1.0
---

# ModelScope 文生图技能

此技能用于调用ModelScope API生成图像，支持提示词优化、多种模型选择、调用次数统计和生成结果汇总。

## 功能特性

1. **提示词优化**: 将中文提示词转换为符合FLUX/SD规范的英文提示词
2. **多模型支持**: 支持从 ModelScope API 获取最新模型列表
3. **动态模型管理**: 支持序号选择模型、设置默认模型
4. **用量统计**: 跟踪每种模型的调用次数，每天自动重置
5. **结果汇总**: 生成完成后输出完整信息汇总

## 模型管理

### 1. 更新模型列表

手动从 ModelScope API 获取最新模型列表：

```
更新模型列表
```

或使用命令：
```bash
python scripts/generate_image.py --update-models
```

### 2. 查看模型列表

查看本地维护的模型列表，默认模型用 ★ 标记：

```
查看模型列表
```

或使用命令：
```bash
python scripts/generate_image.py --list-models
```

### 3. 设置默认模型

设置默认使用的模型（使用序号）：

```
设置默认模型为 2
```

或使用命令：
```bash
python scripts/generate_image.py --set-default 2
```

### 4. 查询当前默认模型

```
当前默认模型
```

或使用命令：
```bash
python scripts/generate_image.py --get-default
```

## 使用方法

### 基本调用

```
生成一张图片: [你的中文提示词]
```

### 使用序号指定模型

```
使用序号 3 的模型生成: [提示词]
```

### 使用模型ID指定模型

```
使用 Qwen/Qwen-Image-2512 模型生成: [提示词]
```

### 使用默认模型（不指定）

```
生成图片: [提示词]
```

### 自定义参数

```
使用模型 MusePublic/489_ckpt_FLUX_1, 分辨率 1024x1024, 步数 40 生成: [提示词]
```

## 实施步骤

### Step 1: 分析用户输入

1. 提取用户的中文提示词
2. 识别指定的模型参数（支持序号或模型ID）
3. 识别自定义参数（分辨率、步数等）

### Step 2: 优化提示词

将中文提示词转换为英文FLUX/SD规范提示词：

1. 提取核心描述（人物、场景、动作、服装）
2. 添加质量标签: `masterpiece, best quality, ultra detailed, 8k, photorealistic`
3. 添加光照描述: `natural lighting, soft lighting, dramatic lighting`
4. 添加风格标签: `professional photography, film grain, bokeh`

### Step 3: 检查调用配额

配额规则：
- 总计: 2000次/天
- 每模型: 500次/天

### Step 4: 执行生图

使用 scripts 目录下的 Python 脚本执行生图任务。

### Step 5: 返回结果汇总

```
=== 图像生成完成 ===

📝 原始提示词: [用户输入的中文提示词]
🔧 优化后提示词: [转换后的英文提示词]

🤖 使用模型: [模型名称]
📊 模型当日调用次数: X/500
📊 总当日调用次数: X/2000

⏱️ 生成耗时: X.X 秒
🖼️ 在线图片: [图片URL]
💾 本地保存: [本地路径]

✨ 生成成功！
```

### Step 6: JSON 返回格式

脚本直接输出 JSON 格式：

```bash
python scripts/generate_image.py "生成一只猫"
```

成功返回：
```json
{
  "code": 1,
  "msg": "",
  "original_prompt": "生成一只猫",
  "optimized_prompt": "生成一只猫, masterpiece, best quality, ultra detailed, 8k, photorealistic, highly detailed, natural lighting, soft lighting, professional lighting, chiaroscuro, professional photography, film grain, bokeh, shallow depth of field",
  "model": "Tongyi-MAI/Z-Image-Turbo",
  "model_usage": 1,
  "total_usage": 1,
  "elapsed_time": 12.5,
  "image_url": "https://xxx.jpg",
  "local_path": "/path/to/t2i/assets/generated_xxx.jpg"
}
```

失败返回：
```json
{
  "code": 0,
  "msg": "API_KEY未配置，请先去 https://modelscope.cn/my/access/token 申请"
}
```

返回字段说明：
- `code`: 1 成功，0 失败
- `msg`: 成功时为空字符串，失败时为错误消息
- `original_prompt`: 原始中文提示词
- `optimized_prompt`: 优化后的英文提示词
- `model`: 使用的模型 ID
- `model_usage`: 当前模型当日调用次数
- `total_usage`: 当日总调用次数
- `elapsed_time`: 生成耗时（秒）
- `image_url`: 在线图片 URL
- `local_path`: 本地保存路径

## 数据文件

- `models_list.json` - 本地维护的模型列表（按更新时间降序排序）
- `modelscope_config.json` - 当日用量统计和配置（包含 API_KEY、DEFAULT_MODEL、BASE_URL、output_dir）

## 注意事项

1. 每日配额在UTC+8 00:00重置
2. 首次使用需先运行 `--update-models` 获取模型列表
3. 模型列表按 LastUpdatedTime 降序排列，最新的模型排在前面
4. 支持使用序号(1,2,3...)或模型ID指定模型
5. 提示词越详细，生成效果越好
6. 可通过括号调整权重，如: `(关键词:1.5)`
