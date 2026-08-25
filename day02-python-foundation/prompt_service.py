# 负责 Prompt 的显示、添加和搜索等业务逻辑。
def show_prompts(prompts: list) -> None:
    # 空列表是正常状态，给用户明确提示后结束显示。
    if len(prompts) == 0:
        print("No prompts")
        return

    # 使用统一格式显示每个 Prompt 的编号、标题和正文。
    for prompt in prompts:
        print(f'{prompt["id"]}. {prompt["title"]}')
        print(f'   {prompt["content"]}')


def add_prompt(
    prompts: list,
    title: str,
    content: str
) -> dict:
    # 清理首尾空格，避免只包含空格的标题或正文通过验证。
    cleaned_title = title.strip()
    cleaned_content = content.strip()

    # 输入无效时抛出异常，由 main.py 决定如何提示用户。
    if cleaned_title == "":
        raise ValueError("title cannot be empty")

    if cleaned_content == "":
        raise ValueError("content cannot be empty")

    next_id = 1

    # 使用当前最大 ID 加一，避免删除中间数据后产生重复 ID。
    for prompt in prompts:
        if prompt["id"] >= next_id:
            next_id = prompt["id"] + 1

    # 每次创建新的字典，避免多个列表元素共享同一个可变对象。
    new_prompt = {
        "id": next_id,
        "title": cleaned_title,
        "content": cleaned_content
    }

    prompts.append(new_prompt)

    return new_prompt


def search_prompts(
    prompts: list,
    keyword: str
) -> list:
    # 统一清理关键词并转成小写，实现忽略英文大小写的搜索。
    normalized_keyword = keyword.strip().lower()

    if normalized_keyword == "":
        raise ValueError("keyword cannot be empty")

    results = []

    # 同时搜索标题和正文，匹配的 Prompt 保存到结果列表。
    for prompt in prompts:
        searchable_text = (
            prompt["title"]
            + " "
            + prompt["content"]
        ).lower()

        if normalized_keyword in searchable_text:
            results.append(prompt)

    return results


# 直接运行本模块时执行最小自测；被 main.py 导入时不会执行。
if __name__ == "__main__":
    sample_prompts = [
        {
            "id": 1,
            "title": "code",
            "content": "explain code"
        }
    ]

    show_prompts(sample_prompts)
