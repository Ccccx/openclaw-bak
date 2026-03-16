---
name: feishu-wiki-write
description: |
  写入飞书知识库文档。根据文件名和内容自动选择最合适的目录创建子文档并写入 Markdown 内容。
  知识库：AI知识库 (space_id: 7615846908665285857)
---

# feishu_wiki_write

将 Markdown 内容写入飞书知识库。根据文件名和内容关键词分析，自动选择最合适的文档目录下创建子文档。

## 目标知识库

- **名称**: AI 知识库  
- **Space ID**: 7615846908665285857
- **URL**: https://my.feishu.cn/wiki/settings/7615846908665285857

## 参数

### filename（可选）
文件名（不含扩展名）。用于：
1. 作为文档标题
2. 分析文件类型和分类

### content（必填）
Markdown 内容，要写入文档的内容。使用 Lark-flavored Markdown 格式。

## 工作流程

1. 在知识库根目录创建新文档
2. 写入 Markdown 内容
3. 返回文档链接

## 当前状态

⚠️ **权限待添加**：应用需要以下权限才能读写知识库：
- `wiki:space:readonly` - 读取知识库
- `wiki:node:create` - 创建知识库文档  
- `wiki:node:update` - 更新知识库文档

## 返回值

- **doc_url**: 文档访问链接
- **doc_id**: 文档 ID  
- **node_token**: 知识库节点 token

## 示例

```json
{
  "filename": "API设计规范",
  "content": "# API 设计规范\n\n## 概述\n\n本文档定义了 REST API 的设计标准。"
}
```

## 注意事项

- 知识库 space_id: `7615846908665285857`
- 需要在飞书开放平台开通 `wiki:space:readonly` 和 `wiki:node:create` 权限
