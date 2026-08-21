from pathlib import Path


# 负责把 Prompt 数据保存到文本文件，并从文本文件恢复数据。
def save_prompts(
    file_path: Path,
    prompts: list
) -> None:
    # 使用 w 模式保存当前完整数据，旧文件内容会被覆盖。
    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:
        for prompt in prompts:
            # 每个 Prompt 保存为一行，字段之间使用制表符分隔。
            line = (
                f'{prompt["id"]}\t'
                f'{prompt["title"]}\t'
                f'{prompt["content"]}\n'
            )

            file.write(line)


def load_prompts(file_path: Path) -> list:
    # 逐行读取文件，并把每一行恢复成一个 Prompt 字典。
    prompts = []

    try:
        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:
            for line in file:
                # 去掉行末换行符，空行不作为 Prompt 处理。
                cleaned_line = line.rstrip("\n")

                if cleaned_line == "":
                    continue

                # 最多切分两次，期望得到 id、title、content 三部分。
                parts = cleaned_line.split("\t", 2)

                if len(parts) != 3:
                    raise ValueError(
                        "invalid prompt data"
                    )

                # 文本文件读取到的 ID 是字符串，需要恢复成整数。
                prompt_id = int(parts[0])
                title = parts[1]
                content = parts[2]

                prompt = {
                    "id": prompt_id,
                    "title": title,
                    "content": content
                }

                prompts.append(prompt)
    except FileNotFoundError:
        # 第一次运行时数据文件可能还不存在，此时从空列表开始。
        return []

    return prompts


# 直接运行 storage.py 时执行最小的保存、加载自测；
# 被 main.py 导入时不会执行。
if __name__ == "__main__":
    test_path = (
        Path(__file__).parent
        / "test_prompts.txt"
    )

    test_prompts = [
        {
            "id": 1,
            "title": "code",
            "content": "explain code"
        }
    ]

    save_prompts(
        test_path,
        test_prompts
    )

    loaded_prompts = load_prompts(test_path)

    print(loaded_prompts)
