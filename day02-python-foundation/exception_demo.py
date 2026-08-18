# 编写 validate_tag(tag)：先用 strip() 清理空格，
# 内容为空时主动抛出 ValueError，然后在调用处使用 try/except 捕获并打印异常。
def validate_tag(tag):
    clean_tag=tag.strip()
    if(clean_tag==""):
        raise ValueError
    return clean_tag

tag=input("请输入：")

try:
    tag1=validate_tag(tag)
except ValueError:
    print("invalid")
else:
    print(tag1)
    