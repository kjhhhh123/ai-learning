import prompt_service


def main():
    prompts = [
        {
            "id": 1,
            "title": "code",
            "content": "explain code"
        },
        {
            "id": 2,
            "title": "summary",
            "content": "summarize text"
        }
    ]

    print("Current prompts:")
    prompt_service.show_prompts(prompts)

    title = input("New title: ")
    content = input("New content: ")

    try:
        created_prompt = prompt_service.add_prompt(
        prompts,
        title,
        content
    )
    except ValueError as error:
        print("Cannot create prompt:", error)
    else:
        print("Created:", created_prompt["title"])

    keyword = input("Search: ")
    try:
        results = prompt_service.search_prompts(
            prompts,
            keyword
        )
    except ValueError as error:
        print(error)
    else:
        print("Search results:")
        prompt_service.show_prompts(results)


if __name__ == "__main__":
    main()