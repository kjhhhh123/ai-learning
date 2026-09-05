"""提供 Post API Client 的命令行菜单和错误提示。"""

import requests

from api_client import create_post, get_post, get_posts_by_user


def show_menu() -> None:
    """显示程序功能菜单。"""
    print()
    print("=== Post API Client ===")
    print("1. 按 ID 查看 Post")
    print("2. 按 userId 查询 Posts")
    print("3. 发送创建 Post 请求")
    print("0. 退出")


def read_positive_int(prompt: str) -> int | None:
    """读取正整数；输入无效时返回 None。"""
    raw_value = input(prompt).strip()

    try:
        value = int(raw_value)
    except ValueError:
        print("请输入整数。")
        return None

    if value <= 0:
        print("请输入大于 0 的整数。")
        return None

    return value


def print_post(post: dict) -> None:
    """格式化显示一篇文章。"""
    print()
    print("文章 ID：", post["id"])
    print("用户 ID：", post["userId"])
    print("标题：", post["title"])
    print("正文：", post["body"])


def handle_get_post() -> None:
    """处理按 ID 查看文章的用户操作。"""
    post_id = read_positive_int("请输入 Post ID：")

    if post_id is None:
        return

    post = get_post(post_id)
    print_post(post)


def handle_get_posts_by_user() -> None:
    """处理按用户 ID 查询文章的操作。"""
    user_id = read_positive_int("请输入 userId：")

    if user_id is None:
        return

    posts = get_posts_by_user(user_id)

    if not posts:
        print("没有找到该用户的文章。")
        return

    print(f"共找到 {len(posts)} 篇文章：")

    for post in posts:
        print(f'{post["id"]}. {post["title"]}')


def handle_create_post() -> None:
    """处理创建文章的用户操作。"""
    title = input("请输入标题：").strip()
    content = input("请输入正文：").strip()

    if not title or not content:
        print("标题和正文不能为空。")
        return

    user_id = read_positive_int("请输入 userId：")

    if user_id is None:
        return

    created_post = create_post(
        title=title,
        content=content,
        user_id=user_id,
    )

    print("创建请求已成功完成。")
    print_post(created_post)
    print("说明：JSONPlaceholder 只模拟创建，不会永久保存数据。")


def main() -> None:
    """运行命令行菜单。"""
    while True:
        show_menu()
        choice = input("请选择功能：").strip()

        if choice == "0":
            print("程序已退出。")
            break

        # 异常处理放在循环内，单次请求失败后菜单仍能继续使用。
        try:
            if choice == "1":
                handle_get_post()

            elif choice == "2":
                handle_get_posts_by_user()

            elif choice == "3":
                handle_create_post()

            else:
                print("无效选项，请输入 0～3。")

        # 具体异常放在前面，父异常 RequestException 放在最后。
        except requests.exceptions.Timeout:
            print("请求超时，请稍后重试。")

        except requests.exceptions.ConnectionError:
            print("无法连接服务器，请检查网络或服务地址。")

        except requests.exceptions.HTTPError as error:
            print("HTTP 请求失败：", error)

        except requests.exceptions.JSONDecodeError:
            print("服务端返回的内容不是有效 JSON。")

        except requests.exceptions.RequestException as error:
            print("网络请求发生其他错误：", error)


if __name__ == "__main__":
    main()