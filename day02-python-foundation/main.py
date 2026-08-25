from pathlib import Path

import prompt_service
import storage


# 数据文件固定放在 main.py 所在目录，
# 避免受到终端当前工作目录的影响。
DATA_FILE = (
    Path(__file__).resolve().parent
    / "prompts.json"
)


def main():
    # 程序启动时，从磁盘恢复之前保存的 Prompt。
    try:
        prompts = storage.load_prompts(
            DATA_FILE
        )
    except (OSError, ValueError) as error:
        # 加载失败后停止程序，避免覆盖可能仍可恢复的数据。
        print("Cannot load data:", error)
        return

    # 显示程序启动时已经存在的数据。
    print("Current prompts:")
    prompt_service.show_prompts(prompts)

    # 获取用户准备添加的新 Prompt。
    title = input("New title: ")
    content = input("New content: ")

    try:
        # add_prompt 会验证输入，并修改 prompts 列表。
        created_prompt = prompt_service.add_prompt(
            prompts,
            title,
            content
        )
    except ValueError as error:
        # 标题或正文无效时，不执行文件保存。
        print("Cannot create prompt:", error)
    else:
        try:
            # 只有添加成功后，才把完整数据保存到磁盘。
            storage.save_prompts(
                DATA_FILE,
                prompts
            )
        except OSError as error:
            # 内存中的数据已经改变，但磁盘写入失败。
            print(
                "Created in memory, "
                "but could not save:",
                error
            )
        else:
            print(
                "Created and saved:",
                created_prompt["title"]
            )

    # 搜索只读取当前数据，不会修改或保存文件。
    keyword = input("Search: ")

    try:
        results = prompt_service.search_prompts(
            prompts,
            keyword
        )
    except ValueError as error:
        print("Cannot search:", error)
    else:
        print("Search results:")
        prompt_service.show_prompts(results)


# 只有直接运行 main.py 时才启动程序；
# 其他文件导入 main.py 时不会自动执行。
if __name__ == "__main__":
    main()