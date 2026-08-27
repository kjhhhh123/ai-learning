# AI Engineering Learning Progress

更新时间：2026-08-26

## 总体目标

补齐软件工程实践能力，沿大模型应用开发 / AI Agent 方向学习。

长期路线：

```text
Git / GitHub
↓
Python 工程基础
↓
HTTP / API
↓
大模型 API 调用
↓
FastAPI Web 后端
↓
RAG
↓
Agent / Tool Calling
↓
Workflow / MCP
↓
Docker / 测试 / 部署
↓
PyTorch / Transformer / 微调理论
```

## 阶段进度

| 阶段 | 状态 | 主要成果 |
|---|---|---|
| Day 01：Git / GitHub | ✅ 已完成 | 掌握本地版本管理、远程协作、分支与冲突处理 |
| Day 02：Python 工程基础 | ✅ 已完成 | 完成可持久化的命令行 Prompt Manager |
| Day 03：HTTP / API | ⏭️ 下一步 | 理解 HTTP 并完成第一个 API Client |

## Day 01：Git / GitHub

状态：✅ 已完成

已掌握：

- Git 与 GitHub、本地仓库与远程仓库的区别。
- 工作区、暂存区、本地仓库、远程仓库的数据流。
- `init`、`status`、`add`、`commit`、`log`、`diff`。
- `clone`、`pull`、`push` 与远程仓库同步。
- `.gitignore`、`remote`、`origin`、`main/master`。
- 分支创建、切换、合并和冲突解决。
- `reset --soft`、`--mixed`、`--hard` 的影响范围。
- Git 命令与中文版 VS Code“源代码管理”的对应操作。

详细总结：`notes/day01-git.md`

## Day 02：Python 工程基础

状态：✅ 已完成

项目成果：命令行 Prompt Manager

当前功能：

```text
1. 查看 Prompt
2. 添加 Prompt
3. 搜索 Prompt
0. 退出
```

数据在添加后立即保存到 `prompts.json`，程序重启后可以恢复。

已掌握：

- 虚拟环境、pip、`requirements.txt` 与依赖隔离。
- 标准库、第三方库、用户模块的区别。
- List、Dict、嵌套数据、遍历、增删改查。
- 可变对象、共享引用、浅复制的基本含义。
- 函数参数、返回值、局部变量、类型提示和单一职责。
- 模块、`import`、`__name__` 与程序入口。
- `try/except/else/finally`、具体异常和主动 `raise`。
- UTF-8 文本读写、`with open()`、文件模式与稳定路径。
- JSON 序列化、反序列化、格式错误和数据结构验证。
- `while True` 菜单循环、功能分发和处理函数。
- 用 `main.py`、`prompt_service.py`、`storage.py` 分离交互、业务和存储职责。

项目结构：

```text
day02-python-foundation/
├── main.py
├── prompt_service.py
├── storage.py
├── prompts.json
├── requirements.txt
└── .gitignore
```

详细总结：`notes/day02-python.md`

## Day 03：HTTP / API

状态：⏭️ 下一步

### 学习目标

理解客户端如何通过 HTTP 调用服务端 API，并独立完成一个具备超时和异常处理的 Python API Client。

### 学习顺序

```text
客户端 / 服务端
↓
URL 与 HTTP 请求 / 响应
↓
方法、状态码、Headers、Body
↓
本地 HTTP 最小实验
↓
requests 发起 GET / POST
↓
查询参数与 JSON 请求体
↓
超时、网络异常、HTTP 错误、JSON 错误
↓
Post API Client 项目
```

### 阶段一：建立 HTTP 整体认知

- 理解客户端、服务端、请求、响应的关系。
- 拆解 URL：scheme、host、port、path、query。
- 理解 GET、POST、PUT/PATCH、DELETE 的用途，重点实践 GET 和 POST。
- 理解状态码分类与常见状态码：200、201、400、401、403、404、429、500。
- 理解 Headers、`Content-Type`、JSON Body 和查询参数。

### 阶段二：最小实验与观察

- 使用 Python 本地 HTTP 服务和浏览器观察一次完整请求。
- 在中文版浏览器开发者工具“网络”面板查看 URL、方法、状态码、响应头和响应体。
- 使用 `requests` 调用 JSONPlaceholder 测试 API；网络不可用时使用本地 JSON HTTP 服务完成核心实验。
- 对照浏览器访问、命令行客户端和 Python 代码三种调用方式。

### 阶段三：Python API 调用

- 使用 `requests.get()`、`requests.post()`。
- 使用 `params` 发送查询参数，使用 `json` 发送 JSON 请求体。
- 读取 `status_code`、`headers`、`text` 和 `response.json()`。
- 始终设置 `timeout`，并使用 `raise_for_status()` 检查 HTTP 错误。
- 处理 `Timeout`、`ConnectionError`、`HTTPError` 和 JSON 解析错误。

### 阶段四：Post API Client

项目结构：

```text
day03-http-api/
├── main.py
├── api_client.py
├── requirements.txt
└── .gitignore
```

功能：

```text
1. 按 ID 查看 Post
2. 按 userId 查询 Posts
3. 发送创建 Post 请求
0. 退出
```

模块职责：

- `main.py`：菜单、输入、输出和程序流程。
- `api_client.py`：构造请求、设置超时、检查响应并返回数据。

### 故障实验

- 请求不存在的资源，观察 404。
- 使用错误地址，观察连接异常。
- 设置极短超时，观察超时异常。
- 尝试解析非 JSON 响应，区分 HTTP 成功与数据格式正确。
- 故意漏掉 `raise_for_status()`，观察错误响应如何被误当成正常数据。

### 完成标准

- 能用自己的话解释一次 HTTP 请求从客户端到服务端再返回的过程。
- 能拆解 URL，并区分查询参数、请求头和请求体。
- 能根据状态码判断请求结果，而不是只看是否打印出内容。
- 能使用 `requests` 完成 GET、POST 和 JSON 解析。
- 能为网络请求设置超时，并处理常见异常。
- 能独立解释 `main.py` 与 `api_client.py` 的职责。
- Post API Client 的三项功能和无效输入处理均可正常运行。

### Day 03 范围边界

- 不调用 OpenAI API；大模型 API 放在下一阶段。
- 不实现 HTTP 服务端；FastAPI 放在后续阶段。
- 不引入异步请求、数据库、认证系统或前端界面。
- 身份认证本日只理解 Header 概念，不保存真实密钥。

## 当前下一步

创建 `day03-http-api`，从“客户端—服务端—请求—响应”的最小实验开始。
