from pathlib import Path

import prompt_service
import storage


# 正式数据文件固定放在 main.py 所在目录，
# 不受终端当前工作目录影响。
DATA_FILE = (
    Path(__file__).resolve().parent
    / "prompts.json"
)


def show_menu() -> str:
    # 显示所有可用操作，并返回清理后的用户选择。
    print()
    print("Prompt Manager")
    print("==============")
    print("1. View prompts")
    print("2. Add prompt")
    print("3. Search prompts")
    print("0. Exit")

    return input("Select: ").strip()


def handle_view(prompts: list) -> None:
    # 查看操作只负责显示当前全部 Prompt。
    print()
    print("Current prompts:")
    prompt_service.show_prompts(prompts)


def handle_add(prompts: list) -> None:
    # 收集创建 Prompt 所需的数据。
    title = input("New title: ")
    content = input("New content: ")

    try:
        # 业务模块负责清理、验证并添加 Prompt。
        created_prompt = prompt_service.add_prompt(
            prompts,
            title,
            content
        )
    except ValueError as error:
        print("Cannot create prompt:", error)
        return

    try:
        # 添加成功后立即保存，避免程序退出时丢失数据。
        storage.save_prompts(
            DATA_FILE,
            prompts
        )
    except (OSError, ValueError) as error:
        print(
            "Created in memory, "
            "but could not save:",
            error
        )
        return

    print(
        "Created and saved:",
        created_prompt["title"]
    )


def handle_search(prompts: list) -> None:
    # 搜索只读取数据，不会修改 prompts 或 JSON 文件。
    keyword = input("Search: ")

    try:
        results = prompt_service.search_prompts(
            prompts,
            keyword
        )
    except ValueError as error:
        print("Cannot search:", error)
        return

    print()
    print("Search results:")
    prompt_service.show_prompts(results)


def main() -> None:
    # 程序启动时只加载一次数据。
    try:
        prompts = storage.load_prompts(
            DATA_FILE
        )
    except (OSError, ValueError) as error:
        # 加载失败后停止，避免覆盖可能仍可恢复的数据。
        print("Cannot load data:", error)
        return

    # 持续显示菜单，直到用户主动选择退出。
    while True:
        choice = show_menu()

        if choice == "1":
            handle_view(prompts)
        elif choice == "2":
            handle_add(prompts)
        elif choice == "3":
            handle_search(prompts)
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


# 只有直接运行 main.py 时才启动程序；
# 被其他模块导入时不会自动进入菜单循环。
if __name__ == "__main__":
    main()