# TierSum Site

TierSum 站点内容（Markdown 知识库页面），独立于 Go 后端的前端站点内容项目。

## 项目结构

```
tiersum-site/
├── README.md              # 本文件
├── deploy/
│   └── nginx-tiersum.conf # Nginx 反向代理配置
└── site/                  # Markdown 站点内容
    ├── index.md
    ├── index.zh.md
    ├── about.md
    ├── about.zh.md
    ├── features.md
    ├── features.zh.md
    ├── documentation.md
    └── documentation.zh.md
```

## 部署方式

### Nginx 反向代理

线上部署时，Nginx 作为统一入口：
- 直接服务于 `tiersum-site/site/` 下的静态 Markdown 文件
- 将 API 请求代理到 tiersum Go 后端

详细部署配置见 `deploy/nginx-tiersum.conf`。

### 开发

```bash
# 本地调试（无需 Nginx，支持 SPA 路由回退）
python3 serve.py

# 或赋予执行权限后直接运行
chmod +x serve.py && ./serve.py
```

```bash
# 编辑站点内容后，Nginx 自动加载最新文件（无需重启）
```

## 站点内容编辑说明

- `site/index.md` — 首页/Landing 页
- `site/about.md` — 产品介绍
- `site/features.md` — 功能特性
- `site/documentation.md` — 完整文档和使用指南

中英文版本通过 `.zh.md` 后缀区分。前端 Vue SPA 根据用户语言偏好自动加载对应版本。

## 与 tiersum 后端的关系

| 组件 | 项目 | 部署方式 |
|------|------|----------|
| Vue 3 SPA 前端 | tiersum (`cmd/web/`) | Go embed 内嵌于二进制 |
| Markdown 站点内容 | tiersum-site (`site/`) | Nginx 直接服务静态文件 |
| Go API 后端 | tiersum (`cmd/`) | 由 Nginx 反向代理 |
