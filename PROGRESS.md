# AI Engineering Learning Progress

更新时间：

2026-08-15

---

# 总体目标

目标：

补齐软件工程实践能力，沿大模型应用开发 / AI Agent 方向学习。

长期路线：

```
Git
↓
Python工程基础
↓
HTTP/API
↓
LLM API
↓
FastAPI
↓
RAG
↓
Agent
↓
部署
```

---

# Day01 Git / GitHub

状态：

✅ 已完成

---

## 已掌握内容

Git 基础：

- Git 是什么
- Git 与 GitHub 区别
- 本地仓库与远程仓库

常用命令：

- git init
- git status
- git add
- git commit
- git log
- git diff
- git clone
- git pull
- git push

项目管理：

- .gitignore
- remote
- origin
- main/master

分支：

- branch
- merge
- 冲突解决

---

## 已理解的重要概念

Git 工作流程：

```
工作区
↓
暂存区
↓
本地仓库
↓
远程仓库
```

reset：

```
--soft

回退 commit
保留代码和暂存


--mixed

回退 commit
保留代码
取消暂存


--hard

commit
暂存区
工作区

全部回退
```

---

# Day02 Python 工程基础

状态：

🚧 进行中

目标：

完成第一个工程项目：

Prompt Manager

---

# 已完成

## Python 环境基础

已经理解：

venv：

> 每个项目独立的 Python 运行环境。

作用：

避免不同项目之间依赖冲突。

---

## Python 内容分类

已理解：

### 标准库

例如：

```
json
os
sys
```

特点：

Python 自带。

不需要：

```
pip install
```

---

### 用户代码

例如：

```
main.py
storage.py
prompt_utils.py
```

放在项目目录。

不放：

```
.venv
```

---

### 第三方库

例如：

```
requests
openai
fastapi
python-dotenv
```

通过 pip 安装。

安装位置：

```
.venv/Lib/site-packages
```

---

# 当前学习位置

正在学习：

Python 数据结构基础：

```
list
↓
dict
↓
函数
↓
模块
↓
异常
↓
文件
↓
JSON
↓
Prompt Manager
```

---

# 待完成

## Python 工程基础

- 完整掌握 list
- 完整掌握 dict
- 理解可变对象与引用
- 函数设计
- import 与模块组织
- 异常处理
- 文件读写
- JSON 数据持久化

---

## Prompt Manager 项目目标

功能：

```
1. 查看 Prompt

2. 添加 Prompt

3. 搜索 Prompt

4. 保存数据

5. 程序重新启动后恢复数据
```

技术：

```
Python
+
JSON
+
文件操作
+
Git
```

---

# 当前下一步

按照顺序：

```
1. 完善 list 基础

2. 完善 dict 基础

3. 学习可变对象和引用

4. 进入函数

5. 完成 Prompt Manager
```