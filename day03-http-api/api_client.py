"""封装文章 API 的 GET、POST 请求和响应解析。"""

import requests


# 集中保存 API 基础地址，各函数只需追加具体资源路径。
BASE_URL = "https://jsonplaceholder.typicode.com"

# 网络请求统一使用这个超时时间，避免配置散落在多个函数中。
REQUEST_TIMEOUT = 10


def get_post(post_id: int) -> dict:
    """根据文章 ID 获取一篇文章。"""

    url = f"{BASE_URL}/posts/{post_id}"

    response = requests.get(
        url,
        timeout=REQUEST_TIMEOUT,
    )

    # 遇到 4xx 或 5xx 状态码时抛出 HTTPError。
    response.raise_for_status()

    # 将响应体中的 JSON 转换成 Python 数据。
    return response.json()


def get_posts_by_user(user_id: int) -> list:
    """获取指定用户的文章。"""
    url = f"{BASE_URL}/posts"
    query = {"userId": user_id}

    # params 会把 query 字典编码为 URL 查询参数。
    response = requests.get(
        url,
        params=query,
        timeout=REQUEST_TIMEOUT,
    )

    # 先检查 HTTP 状态，避免把错误响应当成文章列表。
    response.raise_for_status()

    # 该接口返回 JSON 数组，解析后得到 Python List。
    return response.json()


def create_post(title: str, content: str, user_id: int) -> dict:
    """发送创建文章请求，返回练习 API 的模拟结果。"""

    # JSON 字段名由 API 规定，右侧是函数接收的 Python 参数。
    post_data = {
        "title": title,
        "body": content,
        "userId": user_id,
    }

    # json= 会把 Python 字典转换成 JSON 请求体。
    response = requests.post(
        f"{BASE_URL}/posts",
        json=post_data,
        timeout=REQUEST_TIMEOUT,
    )

    # 状态检查通过后才解析服务端返回的 JSON。
    response.raise_for_status()
    return response.json()