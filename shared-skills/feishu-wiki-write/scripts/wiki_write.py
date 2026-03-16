#!/usr/bin/env python3
"""
Feishu Wiki Write - 写入飞书知识库文档

根据文件名和内容自动选择最合适的目录创建子文档并写入 Markdown 内容。
"""

import argparse
import json
import os
import re
import sys
from typing import Optional

# 默认知识库节点
DEFAULT_WIKI_NODE = "GEkdwrXnlidRXkk3XtIc8tXrnlc"

# 分类规则：关键词 -> 目录名
CATEGORY_RULES = {
    "技术文档": ["代码", "开发", "技术", "api", "sdk", "架构", "设计模式", "实现", "源码", "编程"],
    "会议纪要": ["会议", "纪要", "周报", "月报", "例会", "讨论", "复盘", "总结"],
    "产品需求": ["需求", "产品", "prd", "功能", "特性", "spec", "用户故事", "用例"],
    "测试文档": ["测试", "qa", "用例", "测试用例", "回归", "自动化", "性能测试", "压测"],
    "运维文档": ["运维", "部署", "devops", "ci", "cd", "容器", "docker", "k8s", "集群"],
    "规划文档": ["规划", "roadmap", "战略", "目标", "okr", "愿景", "路线图", "季度", "年度"],
    "教程文档": ["教程", "指南", "手册", "文档", "如何", "入门", "学习", "使用", "说明"],
}


def analyze_category(filename: str, content: str) -> str:
    """分析文件名和内容，返回最合适的分类目录名"""
    text = (filename + " " + content).lower()
    
    scores = {}
    for category, keywords in CATEGORY_RULES.items():
        score = sum(1 for kw in keywords if kw.lower() in text)
        if score > 0:
            scores[category] = score
    
    if scores:
        return max(scores, key=scores.get)
    return "根目录"


def get_space_id(wiki_node: str) -> str:
    """从 wiki_node 获取 space_id"""
    # 这里通过调用飞书 API 获取
    # 实际上需要调用 feishu_wiki_space 工具
    import subprocess
    
    cmd = [
        "openclaw", "tool", "call", "feishu_wiki_space",
        "--arg", json.dumps({"action": "list"})
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            spaces = data.get("spaces", [])
            if spaces:
                # 返回第一个知识空间的 space_id
                return spaces[0].get("space_id", "")
    except Exception as e:
        print(f"获取知识空间列表失败: {e}", file=sys.stderr)
    
    # 如果无法获取，返回一个默认的 space_id
    # 需要根据实际知识库配置
    return ""


def list_space_nodes(space_id: str, parent_token: Optional[str] = None) -> list:
    """列出知识库节点"""
    import subprocess
    
    args = {
        "action": "list",
        "space_id": space_id
    }
    if parent_token:
        args["parent_node_token"] = parent_token
    else:
        args["parent_node_token"] = ""  # 根目录
    
    cmd = [
        "openclaw", "tool", "call", "feishu_wiki_space_node",
        "--arg", json.dumps(args)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return data.get("nodes", [])
    except Exception as e:
        print(f"获取目录列表失败: {e}", file=sys.stderr)
    
    return []


def find_category_node(nodes: list, category: str) -> Optional[str]:
    """在节点列表中查找对应分类的目录节点"""
    for node in nodes:
        title = node.get("title", "")
        if category in title:
            return node.get("node_token", "")
    return None


def create_wiki_doc(space_id: str, parent_token: Optional[str], title: str) -> dict:
    """创建知识库文档"""
    import subprocess
    
    args = {
        "action": "create",
        "space_id": space_id,
        "obj_type": "doc",
        "title": title
    }
    if parent_token:
        args["parent_node_token"] = parent_token
    
    cmd = [
        "openclaw", "tool", "call", "feishu_wiki_space_node",
        "--arg", json.dumps(args)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return data.get("node", {})
    except Exception as e:
        print(f"创建文档失败: {e}", file=sys.stderr)
    
    return {}


def write_doc_content(doc_token: str, content: str) -> bool:
    """写入文档内容"""
    import subprocess
    
    args = {
        "doc_token": doc_token,
        "markdown": content,
        "mode": "append"
    }
    
    cmd = [
        "openclaw", "tool", "call", "feishu_mcp_create_doc",
        "--arg", json.dumps(args)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return result.returncode == 0
    except Exception as e:
        print(f"写入内容失败: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="写入飞书知识库文档")
    parser.add_argument("--filename", "-f", help="文件名（不含扩展名）")
    parser.add_argument("--content", "-c", help="Markdown 内容")
    parser.add_argument("--wiki-node", "-w", default=DEFAULT_WIKI_NODE, help="知识库节点 token")
    parser.add_argument("--content-file", help="内容文件路径")
    
    args = parser.parse_args()
    
    # 获取内容
    if args.content_file:
        with open(args.content_file, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = args.content or ""
    
    filename = args.filename or "新建文档"
    
    # 分析分类
    category = analyze_category(filename, content)
    print(f"分析分类: {category}", file=sys.stderr)
    
    # 获取知识库 space_id
    wiki_node = args.wiki_node
    # 这里需要通过 API 获取 space_id
    # 暂时使用一个占位符，实际使用需要调用 API
    space_id = "7448000000000000000"  # 需要替换为实际的 space_id
    
    print(f"知识库节点: {wiki_node}", file=sys.stderr)
    print(f"Space ID: {space_id}", file=sys.stderr)
    
    # 列出根目录
    nodes = list_space_nodes(space_id, "")
    print(f"根目录节点数: {len(nodes)}", file=sys.stderr)
    
    # 查找分类目录
    parent_token = None
    if category != "根目录":
        parent_token = find_category_node(nodes, category)
        if parent_token:
            print(f"找到分类目录: {category} -> {parent_token}", file=sys.stderr)
        else:
            print(f"未找到分类目录 {category}，将创建在根目录", file=sys.stderr)
    
    # 创建文档
    node = create_wiki_doc(space_id, parent_token, filename)
    if not node:
        print("创建文档失败", file=sys.stderr)
        sys.exit(1)
    
    node_token = node.get("node_token", "")
    obj_token = node.get("obj_token", "")
    
    print(f"创建文档成功: {node_token} / {obj_token}", file=sys.stderr)
    
    # 写入内容
    if content:
        success = write_doc_content(obj_token, content)
        if not success:
            print("写入内容失败", file=sys.stderr)
            sys.exit(1)
    
    # 返回结果
    result = {
        "doc_id": obj_token,
        "node_token": node_token,
        "doc_url": f"https://my.feishu.cn/docx/{obj_token}",
        "parent_directory": category,
        "title": filename
    }
    
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
