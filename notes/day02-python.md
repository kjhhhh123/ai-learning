# Day 02：Python 工程基础学习速查

目标：掌握 Python 项目的基本组织方式，并完成能够保存数据的命令行 Prompt Manager。

## 今天最重要的两张图

```text
List / Dict 表达数据
        ↓
函数封装操作
        ↓
模块划分职责
        ↓
异常处理失败
        ↓
文件 / JSON 保存数据
        ↓
组成完整项目
```

```text
用户输入
   ↓
main.py（交互与流程）
   ↓
prompt_service.py（业务逻辑）
   ↓
storage.py（加载与保存）
   ↓
prompts.json（持久化数据）
```

## 01 虚拟环境与依赖

虚拟环境让每个项目拥有独立的 Python 包安装位置，避免不同项目的依赖版本互相影响。

`.venv` 中最需要记住的三个部分：

| 位置 | 作用 |
|---|---|
| `Scripts\python.exe` | 项目使用的 Python |
| `Scripts\pip.exe` | 项目使用的包管理工具 |
| `Lib\site-packages` | 第三方库的安装位置 |

常用命令：

| 命令 | 作用 |
|---|---|
| `python -m venv .venv` | 创建虚拟环境 |
| `.\.venv\Scripts\Activate.ps1` | 在 PowerShell 中激活 |
| `.\.venv\Scripts\python.exe main.py` | 不激活，直接使用项目 Python |
| `python -m pip install <package>` | 给当前 Python 安装第三方库 |
| `python -m pip install -r requirements.txt` | 按依赖清单安装 |

依赖分为三类：

| 类型 | 来源 | 示例 |
|---|---|---|
| 标准库 | Python 自带 | `json`、`pathlib` |
| 第三方库 | pip 安装 | `requests` |
| 用户模块 | 项目中自己编写 | `storage.py` |

`.venv` 是本机环境，不提交 Git；`requirements.txt` 记录项目依赖，应提交 Git。VS Code 还要通过“Python: 选择解释器”选择项目的 `.venv`。

## 02 List：管理一批有顺序的数据

List 有顺序、可修改、允许重复，下标从 `0` 开始。

```python
titles = ["code", "summary", "test"]
empty_titles = []
```

常用操作：

| 代码 | 作用 |
|---|---|
| `titles[0]` | 读取第一项 |
| `titles[-1]` | 读取最后一项 |
| `titles[1] = "review"` | 修改元素 |
| `titles.append("translate")` | 末尾添加一个元素 |
| `titles.extend(["a", "b"])` | 逐个添加一批元素 |
| `titles.remove("code")` | 按值删除 |
| `titles.pop(0)` | 按下标删除并返回该元素 |
| `del titles[0]` | 按下标删除 |
| `"test" in titles` | 成员判断 |
| `len(titles)` | 获取元素数量 |
| `type(titles)` | 检查对象类型 |
| `titles[1:3]` | 切片，取下标 1 到 3 之前 |

`append(["a", "b"])` 会把整个 List 当成一个元素；`extend(["a", "b"])` 会加入两个元素。

遍历：

```python
for title in titles:
    print(title)

for index, title in enumerate(titles, start=1):
    print(index, title)
```

`start=1` 只改变显示编号，不改变真实下标。访问不存在的下标会产生 `IndexError`。

## 03 Dict：描述一个结构化对象

Dict 使用键值关系保存数据，键不能重复。

```python
prompt = {
    "id": 1,
    "title": "code",
    "content": "explain code"
}

empty_prompt = {}
```

常用操作：

| 代码 | 作用 |
|---|---|
| `prompt["title"]` | 读取必须存在的字段 |
| `prompt.get("category", "unknown")` | 安全读取并提供默认值 |
| `prompt["title"] = "test"` | 修改字段 |
| `prompt["enabled"] = True` | 添加字段 |
| `prompt.pop("enabled")` | 删除并返回字段值 |
| `del prompt["content"]` | 删除字段 |
| `"title" in prompt` | 判断键是否存在 |
| `prompt.keys()` | 获取所有键 |
| `prompt.values()` | 获取所有值 |
| `prompt.items()` | 获取所有键值对 |
| `type(prompt)` | 检查对象类型 |

遍历：

```python
for key, value in prompt.items():
    print(key, value)
```

`prompt["key"]` 缺少键时产生 `KeyError`；只有字段确实允许缺失时才使用 `get()`，避免隐藏拼写错误。

一个 Prompt 使用 Dict，多个 Prompt 使用 List 中嵌套 Dict：

```python
prompts = [
    {"id": 1, "title": "code"},
    {"id": 2, "title": "test"}
]

print(prompts[0]["title"])
```

## 04 可变对象、引用与复制

List 和 Dict 都是可变对象。变量赋值复制的是引用，不会自动创建新对象。

```python
first = {"title": "code"}
second = first
second["title"] = "test"
```

此时 `first["title"]` 也会变成 `"test"`，因为两个变量指向同一个 Dict。

```text
first  ──┐
         ├──> 同一个 Dict
second ──┘
```

`second = first.copy()` 会浅复制外层容器，但内部嵌套的可变对象仍可能共享。函数接收到 List 后直接 `append()`，也会修改调用者原来的 List。

**容易踩坑：**循环添加数据时，如果反复把同一个 Dict 放入 List，修改其中一个元素可能导致多个元素一起变化。每次添加都应创建新的 Dict。

## 05 函数：封装一项明确工作

```python
def make_label(prompt_id: int, title: str) -> str:
    label = f"{prompt_id}. {title}"
    return label


result = make_label(1, "code")
```

| 概念 | 一句话理解 |
|---|---|
| 参数 | 函数定义中接收数据的变量 |
| 实参 | 调用函数时实际传入的数据 |
| `return` | 把结果交给调用者 |
| 局部变量 | 只在当前函数内部使用的变量 |
| 类型提示 | 说明预期类型，帮助阅读和检查 |

`print()` 是把内容显示给人看，`return` 是把结果交给其他代码继续使用。函数没有显式 `return` 时会返回 `None`；类型提示不会自动转换或强制检查类型。

工程中的函数应保持单一职责，例如把“添加”“显示”“搜索”“保存”拆成不同函数，减少重复代码。

## 06 模块、import 与程序入口

一个 `.py` 文件就是一个模块。

```python
import prompt_service
prompt_service.search_prompts(...)

from prompt_service import search_prompts
search_prompts(...)
```

使用模块前缀更容易看出函数来源；应避免 `from module import *`。

导入模块时，Python 会执行模块的顶层代码。入口和模块自测应放在：

```python
if __name__ == "__main__":
    main()
```

```text
直接运行当前文件：__name__ 等于 "__main__"，执行入口
被其他文件导入：__name__ 是模块名，不执行入口
```

- `ModuleNotFoundError`：Python 找不到要导入的模块，检查文件名、位置和解释器。
- 循环导入：两个模块互相依赖，可能出现名称尚未创建的问题；应重新划分职责，让依赖方向保持清晰。
- `__pycache__`：Python 自动生成的字节码缓存，可以删除并应忽略。

## 07 异常处理

异常表示程序运行时无法正常完成当前操作。

```python
try:
    number = int(text)
except ValueError as error:
    print(error)
else:
    print(number)
finally:
    print("finished")
```

| 部分 | 作用 |
|---|---|
| `try` | 放置可能产生异常的代码 |
| `except` | 捕获并处理指定异常 |
| `else` | 没有异常时执行 |
| `finally` | 无论成功失败都执行 |
| `raise` | 主动抛出异常 |

项目中的推荐关系：

```text
业务函数发现无效数据并 raise
              ↓
main.py 捕获具体异常并提示用户
```

只捕获自己知道如何处理的具体异常。不要用宽泛的 `except Exception` 把所有错误一口吞掉；搜索无结果等正常状态应返回空 List，不需要抛异常。

常见异常：

| 异常 | 常见原因 |
|---|---|
| `IndexError` | List 下标越界 |
| `KeyError` | Dict 缺少指定键 |
| `ValueError` | 值的内容不符合要求 |
| `TypeError` | 数据类型或操作不符合要求 |
| `FileNotFoundError` | 文件不存在 |
| `OSError` | 文件读写等系统操作失败 |
| `JSONDecodeError` | JSON 文本格式损坏 |

## 08 文件读写与 UTF-8

文件让数据离开内存并保存在磁盘中，实现程序重启后的数据恢复。

```python
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
```

`with` 会自动关闭文件，即使读写过程中发生异常。

| 模式 | 作用 |
|---|---|
| `r` | 读取；文件不存在时报错 |
| `w` | 覆盖写入；文件不存在时创建 |
| `a` | 在末尾追加；文件不存在时创建 |

```python
file.read()          # 读取文本
file.write("text")  # 写入文本
```

文本写入不会自动换行，需要显式写入 `\n`。中文文本明确使用 `encoding="utf-8"`，避免不同系统默认编码造成乱码。

## 09 路径与当前工作目录

相对路径根据程序启动时的当前工作目录解释，不是固定根据 Python 文件所在目录解释。

```python
from pathlib import Path

DATA_FILE = (
    Path(__file__).resolve().parent
    / "prompts.json"
)
```

这能让数据文件始终定位在 `main.py` 旁边，不受从哪个目录启动程序的影响。项目中不要硬编码只适用于自己电脑的绝对路径。

## 10 JSON：保存结构化数据

JSON 是文本格式；Python 的 List 和 Dict 是内存中的对象。二者需要经过序列化和反序列化才能转换。

| Python | JSON |
|---|---|
| Dict | object |
| List | array |
| `str` | string |
| `int` / `float` | number |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

四个核心函数：

| 函数 | 方向 |
|---|---|
| `json.dumps()` | Python 数据 -> JSON 字符串 |
| `json.loads()` | JSON 字符串 -> Python 数据 |
| `json.dump()` | Python 数据 -> JSON 文件 |
| `json.load()` | JSON 文件 -> Python 数据 |

```python
json.dump(
    prompts,
    file,
    ensure_ascii=False,
    indent=2
)
```

- `ensure_ascii=False`：中文直接保存，不转换成 Unicode 转义。
- `indent=2`：格式化缩进，方便人工查看。
- 尾部多逗号、空文件和损坏内容会导致 `JSONDecodeError`。
- Python 函数、集合等不支持的对象会导致序列化 `TypeError`。
- JSON 语法正确不等于数据结构正确，读取后仍要用 `isinstance()` 检查顶层类型、字段和字段类型。

## 11 Prompt Manager 是什么

Prompt Manager 用来保存和查找可重复使用的 Prompt 模板，避免每次重新编写相同指令。

菜单：

```text
1. 查看 Prompt
2. 添加 Prompt
3. 搜索 Prompt
0. 退出
```

统一数据结构：

```json
{
  "id": 1,
  "title": "code",
  "content": "explain code"
}
```

模块职责：

| 文件 | 职责 |
|---|---|
| `main.py` | 菜单、输入输出、功能分发和程序入口 |
| `prompt_service.py` | 显示、添加、搜索和业务验证 |
| `storage.py` | JSON 加载、保存和数据结构验证 |
| `prompts.json` | 保存实际 Prompt 数据 |

核心接口：

```python
load_prompts(file_path) -> list
save_prompts(file_path, prompts) -> None
add_prompt(prompts, title, content) -> dict
search_prompts(prompts, keyword) -> list
```

## 12 Prompt Manager 的关键规则

- 第一次运行没有 `prompts.json` 时，从空 List 开始。
- 空文件或损坏的 JSON 给出明确错误，不使用宽泛异常掩盖原因。
- 加载和保存时检查顶层 List、内部 Dict、必要字段及字段类型。
- 标题、正文和搜索词先用 `strip()` 清理，不能只包含空格。
- 新 ID 使用当前最大 ID 加一，而不是简单使用 List 长度。
- 搜索同时匹配标题和正文，使用 `lower()` 忽略英文大小写。
- 添加成功后立即保存，减少程序意外退出造成的数据丢失。
- 搜索只读取数据，不修改 List，也不需要保存文件。
- 加载失败后停止程序，避免错误数据被空 List 覆盖。
- 未知菜单选项只提示重新选择，不让程序崩溃。

程序循环：

```python
while True:
    choice = show_menu()

    if choice == "0":
        break
```

菜单编号是操作标识，不参与计算，因此保留为字符串，输入 `abc` 时也不会触发整数转换错误。

## 13 工程习惯与常见排查

| 现象 | 优先检查 |
|---|---|
| 安装了库却无法导入 | VS Code 和终端是否使用项目 `.venv` |
| 修改一个 Dict，其他数据也变化 | 是否共享了同一个可变对象 |
| 函数结果是 `None` | 是否漏写 `return` |
| 导入模块时程序自动启动 | 入口是否放在 `if __name__ == "__main__"` 中 |
| 数据文件出现在错误目录 | 是否错误依赖当前工作目录 |
| 中文读取乱码 | 读写时是否统一使用 UTF-8 |
| JSON 能读取但项目报错 | 数据类型和必要字段是否正确 |
| 添加后重启数据消失 | 添加成功后是否调用保存函数 |

代码注释用于说明模块职责、关键流程、设计原因和边界情况，不逐行翻译显而易见的语法。临时 demo、测试数据、`.venv` 和 `__pycache__` 不进入最终项目；完成阶段功能后使用 `git status`、`git diff` 检查并创建有意义的提交。

## 14 Day 02 最终自测

能用自己的话解释并完成即可，不要求背定义：

- 虚拟环境中的 Python、pip、`site-packages` 分别做什么。
- List 与 Dict 的用途，以及常用的增删改查和遍历方法。
- 赋值、共享引用和浅复制有什么区别。
- 参数、实参、`print()`、`return` 和局部变量的关系。
- `import` 为什么可能执行模块代码，`__name__` 判断解决什么问题。
- `try`、`except`、`else`、`finally` 和 `raise` 分别做什么。
- 相对路径为什么会随启动目录变化，`__file__` 如何解决。
- Python 对象、JSON 字符串和 JSON 文件之间如何转换。
- `main.py`、`prompt_service.py`、`storage.py` 各自负责什么。
- Prompt 从输入、添加、保存，到重启后恢复的完整数据流。

## Day 02 核心结论

Python 工程不只是会写语法，而是用数据结构表达数据、用函数封装行为、用模块划分职责、用异常处理失败，再用文件和 JSON 保存程序状态。

```text
输入 -> 处理 -> 保存 -> 退出 -> 重启 -> 恢复
```
