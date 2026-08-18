def show_prompts(prompts: list) -> None:
    if len(prompts) == 0:
        print("No prompts")
        return

    for prompt in prompts:
        print(f'{prompt["id"]}. {prompt["title"]}')
        print(f'   {prompt["content"]}')


def add_prompt(
    prompts: list,
    title: str,
    content: str
) -> dict:
    cleaned_title = title.strip()
    cleaned_content = content.strip()

    if cleaned_title == "":
        raise ValueError("title cannot be empty")

    if cleaned_content == "":
        raise ValueError("content cannot be empty")

    next_id = 1

    for prompt in prompts:
        if prompt["id"] >= next_id:
            next_id = prompt["id"] + 1

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
    normalized_keyword = keyword.strip().lower()

    if normalized_keyword == "":
        raise ValueError("keyword cannot be empty")

    results = []

    for prompt in prompts:
        searchable_text = (
            prompt["title"]
            + " "
            + prompt["content"]
        ).lower()

        if normalized_keyword in searchable_text:
            results.append(prompt)

    return results


if __name__ == "__main__":
    sample_prompts = [
        {
            "id": 1,
            "title": "code",
            "content": "explain code"
        }
    ]

    show_prompts(sample_prompts)