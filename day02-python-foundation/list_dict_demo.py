prompts = [
    {
        "id": 1,
        "title": "解释代码",
        "content": "请解释下面的 Python 代码"
    },
    {
        "id": 2,
        "title": "总结文章",
        "content": "请总结下面的文章"
    }
]
keyword = input("请输入搜索关键词：")
results = []
for prompt in prompts:
    searchable_text = prompt["title"] + " " + prompt["content"]

    if keyword.lower() in searchable_text.lower():
        results.append(prompt)
        
print("搜索结果：")
print(searchable_text)
if len(results) == 0:
    print("没有找到匹配的 Prompt")
else:
    for prompt in results:
        print(f'{prompt["id"]}. {prompt["title"]}')