import json
from pathlib import Path


# 验证从 JSON 中读取的数据是否符合 Prompt Manager 的结构。
def _validate_prompts(data: object) -> list:
    # 顶层数据必须是 List。
    if not isinstance(data, list):
        raise ValueError(
            "prompt data must be a list"
        )

    for prompt in data:
        # List 中的每个元素都必须是 Dict。
        if not isinstance(prompt, dict):
            raise ValueError(
                "each prompt must be a dict"
            )

        # 验证核心字段是否存在。
        if "id" not in prompt:
            raise ValueError(
                "prompt is missing id"
            )

        if "title" not in prompt:
            raise ValueError(
                "prompt is missing title"
            )

        if "content" not in prompt:
            raise ValueError(
                "prompt is missing content"
            )

        # 验证核心字段的类型。
        if not isinstance(prompt["id"], int):
            raise ValueError(
                "prompt id must be an integer"
            )

        if not isinstance(prompt["title"], str):
            raise ValueError(
                "prompt title must be a string"
            )

        if not isinstance(prompt["content"], str):
            raise ValueError(
                "prompt content must be a string"
            )

    return data


# 把完整 Prompt List 序列化并保存为 JSON。
def save_prompts(
    file_path: Path,
    prompts: list
) -> None:
    # 保存前先验证，避免主动写入错误结构。
    _validate_prompts(prompts)

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            prompts,
            file,
            ensure_ascii=False,
            indent=2
        )

        # 让文本文件以换行结束，方便终端和编辑器显示。
        file.write("\n")


# 从 JSON 文件读取并恢复 Prompt List。
def load_prompts(file_path: Path) -> list:
    try:
        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)
    except FileNotFoundError:
        # 第一次启动没有数据文件时，从空列表开始。
        return []
    except json.JSONDecodeError as error:
        # 把底层 JSON 错误转换成项目更容易理解的错误。
        raise ValueError(
            "invalid JSON at "
            f"line {error.lineno}, "
            f"column {error.colno}"
        ) from error

    return _validate_prompts(data)


# 直接运行 storage.py 时执行保存、加载闭环测试。
if __name__ == "__main__":
    test_path = (
        Path(__file__).resolve().parent
        / "test_prompts.json"
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