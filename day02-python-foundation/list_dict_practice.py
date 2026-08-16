# 完成下面的功能：
# 创建一个 List，里面预先保存两个 Prompt。
# 每个 Prompt 都是 Dict，包含 id、title 和 content。
# 让用户输入第三个 Prompt 的标题和正文。
# 创建新的 Dict，并添加到 List。
# 使用编号显示所有 Prompt。
# 让用户输入搜索关键词。
# 同时搜索标题和正文。
# 搜索英文时忽略大小写。
# 没有匹配结果时显示提示。
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
title=input("请输入标题：")
content=input("请输入内容：")
new_dict={"id":len(prompts)+1,
            "title":title,
            "content":content
        }
prompts.append(new_dict)
for prompt in prompts:
    print(f'{prompt["id"]}.{prompt["title"]}')
    print(prompt["content"])