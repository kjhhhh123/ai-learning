# Day 03：HTTP / API 学习笔记（进行中）

> 当前进度：模块 1～5 已学完；模块 6 正在学习。等模块 6 完成后，再补充运行验证结果并将 Day 03 标记为完成。

## 一、先建立整体画面

HTTP 学习的核心不是背函数，而是理解下面这条通信链路：

```text
客户端准备请求
    ↓
通过 HTTP 发送给服务端
    ↓
服务端读取请求并处理
    ↓
服务端返回 HTTP 响应
    ↓
客户端读取状态码和响应数据
```

在当前项目中：

- Python 程序是客户端。
- JSONPlaceholder 是服务端。
- `requests` 帮助 Python 程序发送 HTTP 请求。
- JSON 是客户端和服务端传递数据时常用的文本格式。

## 二、客户端与服务端

### 1. 客户端是什么

客户端是主动发起请求的一方。例如：

- 浏览器访问网页时，浏览器是客户端。
- 手机 App 请求数据时，App 是客户端。
- `requests.get(...)` 发起请求时，Python 程序是客户端。

### 2. 服务端是什么

服务端是接收请求、执行处理并返回结果的一方。它可能负责：

- 查询数据。
- 保存数据。
- 调用其他服务。
- 执行业务规则。
- 返回 HTML、JSON、图片等内容。

“客户端”和“服务端”描述的是一次通信中的角色，并不简单等同于两台固定的电脑。

## 三、HTTP、API、JSON 和 requests

| 概念 | 它是什么 | 在当前项目中的作用 |
|---|---|---|
| HTTP | 客户端与服务端通信的一套规则 | 规定请求和响应如何传输 |
| API | 服务端提供给其他程序使用的功能入口 | `/posts/1`、`/posts?userId=1` 等 |
| JSON | 一种常用的数据表示格式 | 表示文章、用户 ID、标题和正文 |
| requests | Python 第三方 HTTP 客户端库 | 帮助代码发送 GET、POST 请求 |

它们的关系可以理解为：

```text
Python 程序
  └─ 使用 requests
       └─ 按照 HTTP 规则调用 API
            └─ 请求和响应中经常使用 JSON 数据
```

## 四、URL 是什么

URL 是网络资源的地址。以这个地址为例：

```text
https://jsonplaceholder.typicode.com/posts?userId=1
```

可以拆成：

| 部分 | 示例 | 含义 |
|---|---|---|
| scheme | `https` | 使用的通信协议 |
| host | `jsonplaceholder.typicode.com` | 服务端主机地址 |
| port | 此处省略 | 服务监听的端口，HTTPS 默认常用 443 |
| path | `/posts` | 要访问的资源 |
| query | `userId=1` | 附加的查询条件 |

### Path 参数与 Query 参数

```text
/posts/1
```

这里的 `1` 位于路径中，表示访问 ID 为 1 的某一篇文章。

```text
/posts?userId=1
```

这里的 `userId=1` 是查询参数，表示从文章集合中筛选用户 1 的文章。

在 Requests 中，应使用 `params` 传递查询参数：

```python
query = {"userId": user_id}
response = requests.get(url, params=query, timeout=10)
```

`params=query` 会把字典编码到 URL 的查询部分，最终形成类似：

```text
https://jsonplaceholder.typicode.com/posts?userId=1
```

这样比手动拼接 `?` 和 `&` 更清晰，也能自动处理 URL 编码。

## 五、HTTP 请求由什么组成

一次 HTTP 请求主要包含：

```text
请求方法 + URL
请求头 Headers
请求体 Body（不一定存在）
```

### 1. 请求方法

| 方法 | 常见用途 |
|---|---|
| GET | 获取数据 |
| POST | 提交或创建数据 |
| PUT | 整体更新数据 |
| PATCH | 部分更新数据 |
| DELETE | 删除数据 |

方法表达客户端希望服务端执行什么操作，但真正的行为仍由服务端代码决定。例如，发送 POST 并不保证数据一定会永久保存。

### 2. 请求头 Headers

请求头携带对请求的补充说明，例如：

- 客户端能接收什么格式。
- 请求体使用什么格式。
- 身份认证信息。
- Cookie 等会话信息。

容易混淆的两个请求头：

- `Accept`：客户端希望收到什么格式的响应。
- `Content-Type`：当前发送的请求体是什么格式。

### 3. 请求体 Body

请求体用于携带要提交的数据，POST、PUT、PATCH 请求经常使用它。GET 请求通常把筛选条件放在 URL 查询参数中，而不是请求体中。

## 六、接口参数可以放在哪里

“接口传参”就是客户端把服务端所需的数据放到约定的位置。具体放在哪里必须看 API 文档，不能只凭参数名字猜测。

| 参数位置 | Requests 写法 | 常见用途 |
|---|---|---|
| URL 路径 | `f"/posts/{post_id}"` | 指定某个资源 |
| URL 查询参数 | `params={...}` | 筛选、搜索、分页 |
| 请求头 | `headers={...}` | 认证信息、内容类型等 |
| Cookie | `cookies={...}` | 会话标识 |
| 表单请求体 | `data={...}` | HTML 表单、传统接口 |
| JSON 请求体 | `json={...}` | 现代 Web API 提交结构化数据 |
| 文件请求体 | `files={...}` | 上传文件 |

当前阶段重点掌握：URL 参数、查询参数、请求头和 JSON 请求体。Cookie、表单和文件上传先建立认识即可。

## 七、HTTP 响应由什么组成

服务端返回的 HTTP 响应主要包含：

```text
状态码
响应头 Headers
响应体 Body
```

### 1. 状态码

状态码先告诉客户端请求的大致结果：

| 范围 | 含义 | 常见状态码 |
|---|---|---|
| 2xx | 请求成功 | 200、201、204 |
| 3xx | 重定向 | 301、302 |
| 4xx | 客户端请求存在问题 | 400、401、403、404、429 |
| 5xx | 服务端处理失败 | 500 |

常见状态码：

- `200 OK`：请求成功，通常用于成功获取数据。
- `201 Created`：服务端表示创建请求成功。
- `204 No Content`：请求成功，但没有响应体。
- `400 Bad Request`：请求格式或参数有问题。
- `401 Unauthorized`：尚未通过身份认证。
- `403 Forbidden`：身份可能已确认，但没有访问权限。
- `404 Not Found`：服务器能访问，但指定资源不存在。
- `429 Too Many Requests`：请求过于频繁。
- `500 Internal Server Error`：服务端内部错误。

`404` 和连接失败不是一回事：

- 收到 `404`，说明已经联系到服务器，服务器返回了响应。
- `ConnectionError`，说明客户端通常连服务器都没有成功连接。

### 2. 响应体

响应体是真正返回的内容，可能是：

- HTML 网页。
- JSON 数据。
- 图片或文件。
- 普通文本。

HTTP 请求成功不等于响应体一定是 JSON。解析前要根据接口约定或响应头判断数据格式。

## 八、使用 requests 发送 GET 请求

获取一篇文章：

```python
def get_post(post_id: int) -> dict:
    """根据文章 ID 获取一篇文章。"""
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url, timeout=10)

    # 遇到 4xx 或 5xx 状态码时抛出 HTTPError。
    response.raise_for_status()

    # 将响应体中的 JSON 转换成 Python 数据。
    return response.json()
```

按用户查询多篇文章：

```python
def get_posts_by_user(user_id: int) -> list:
    """获取指定用户的文章。"""
    url = f"{BASE_URL}/posts"
    query = {"userId": user_id}

    # params 会把 query 字典编码为 URL 查询参数。
    response = requests.get(url, params=query, timeout=10)
    response.raise_for_status()

    # JSON 数组会被转换成 Python 列表。
    return response.json()
```

### Response 对象

`requests.get()` 返回的不是文章本身，而是一个 `Response` 响应对象。常用内容包括：

- `response.status_code`：状态码。
- `response.headers`：响应头。
- `response.text`：按文本读取响应体。
- `response.json()`：把 JSON 响应体转换成 Python 数据。
- `response.raise_for_status()`：遇到 4xx、5xx 时抛出异常。

`response.text` 和 `response.json()` 的区别：

- `.text` 得到字符串，适合观察原始文本。
- `.json()` 解析 JSON，得到 Python 的字典、列表等数据，方便继续编程处理。

## 九、使用 POST 发送 JSON 数据

```python
def create_post(title: str, content: str, user_id: int) -> dict:
    """向练习 API 发送创建文章请求，返回模拟创建结果。"""
    post_data = {
        "title": title,
        "body": content,
        "userId": user_id,
    }

    # json= 会把字典转换成 JSON 请求体。
    response = requests.post(
        f"{BASE_URL}/posts",
        json=post_data,
        timeout=10,
    )

    response.raise_for_status()
    return response.json()
```

这里有三个不同的东西：

1. `post_data` 是 Python 程序内存中的字典。
2. `json=post_data` 把字典作为 JSON 请求体发送给服务器。
3. `response.json()` 解析服务器返回的 JSON 响应体。

### 为什么在网站中看不到新文章

JSONPlaceholder 是练习用的模拟 API。它会接收 POST 请求，并返回一个看起来创建成功的结果和模拟 ID，但不会把数据永久写入数据库。

因此：

```text
发送 POST
  ↓
收到 201 和模拟创建结果
  ↓
再次 GET 网站数据
  ↓
找不到刚才的文章
```

这不是 HTTP 的限制，而是这个练习服务器特意设计的行为。真实项目如果实现了数据库保存逻辑，创建后再次查询就可以看到数据。

## 十、前端、后端与问答系统

### 前端

前端是用户直接看到和操作的部分，例如：

- 提问输入框。
- “发送”按钮。
- 答案显示区域。
- 加载状态和错误提示。

### 后端

后端运行在服务器上，负责：

- 接收前端问题。
- 检查输入是否合法。
- 调用大模型 API。
- 保存问题和答案。
- 把结果返回给前端。
- 保护 API Key 等敏感配置。

### HTTP 在问答系统中做什么

```text
用户在前端输入问题
        ↓ HTTP 请求
自己的后端收到问题
        ↓ HTTP 请求
大模型服务收到 Prompt 并生成答案
        ↓ HTTP 响应
自己的后端整理答案
        ↓ HTTP 响应
前端显示答案
```

HTTP 负责在不同程序之间传输请求和响应；它本身不会理解问题，也不会生成答案。真正生成答案的是大模型，业务流程由后端控制，前端负责交互与展示。

当前 `api_client.py` 是一个调用别人 API 的客户端模块，还不是我们自己的 Web 后端。后续学习 FastAPI 时，才会开始编写能接收外部 HTTP 请求的服务端。

一个完整问答应用通常需要前端，但学习后端和大模型调用的早期阶段，可以先使用命令行充当前端，把注意力集中在核心数据流上。

## 十一、超时和异常处理

网络请求可能在不同阶段失败：

```text
建立连接失败
    ↓
等待时间过长
    ↓
服务器返回 4xx / 5xx
    ↓
响应体不是预期的 JSON
```

对应的常见异常：

| 异常 | 表示什么 |
|---|---|
| `Timeout` | 请求等待时间超过限制 |
| `ConnectionError` | 无法连接服务器 |
| `HTTPError` | `raise_for_status()` 检查到 4xx 或 5xx |
| `JSONDecodeError` | 响应体不是有效 JSON |
| `RequestException` | Requests 网络异常的父类，用作最后兜底 |

### 为什么设置 timeout

```python
response = requests.get(url, timeout=10)
```

如果不设置超时，程序可能长时间卡在网络请求上。`timeout=10` 是给网络等待设置边界，不表示整个服务器业务一定能在精确 10 秒内完成。

### 为什么调用 raise_for_status

Requests 收到 `404` 或 `500` 时仍会返回 `Response` 对象，不会自动把所有错误状态当作 Python 异常。

```python
response.raise_for_status()
```

这行代码把 4xx、5xx 响应转换成 `HTTPError`，使成功流程与失败流程更容易分开处理。

### except 为什么从具体到宽泛排列

```python
try:
    ...
except requests.exceptions.Timeout:
    ...
except requests.exceptions.ConnectionError:
    ...
except requests.exceptions.HTTPError:
    ...
except requests.exceptions.JSONDecodeError:
    ...
except requests.exceptions.RequestException:
    ...
```

`RequestException` 是多个 Requests 异常的父类。如果把它放在前面，前面的宽泛分支会先捕获异常，后面更具体的提示就没有机会执行。

## 十二、本地 HTTP 实验观察

在 `day03-http-api/lab/` 中运行：

```powershell
python -m http.server 8000
```

这条命令的整体含义是：让 Python 运行标准库中的 `http.server` 模块，在当前目录启动一个监听 8000 端口的简单 HTTP 文件服务器。

浏览器访问：

```text
http://localhost:8000
```

可以观察到：

- 正常文件存在时，服务器通常返回 `200` 和 HTML 内容。
- 请求不存在的路径时，服务器返回 `404`。
- 停止服务器后再次访问，会发生连接失败，而不是 `404`。
- HTML 响应可以正常显示，但对它调用 `.json()` 会发生 JSON 解析错误。

这个实验说明：状态码是否成功、服务器是否连接、响应数据是什么格式，是三个需要分别判断的问题。

