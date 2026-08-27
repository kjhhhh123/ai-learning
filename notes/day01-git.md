# Day 01：Git / GitHub 学习速查

目标：会用 Git 管理本地代码版本，并把项目同步到 GitHub。

## 今天最重要的一张图

```text
工作区
  ↓ git add
暂存区
  ↓ git commit
本地仓库
  ↓ git push
GitHub 远程仓库
```

## 01 Git 和 GitHub 的区别

| 概念 | 一句话理解 | 主要操作 |
|---|---|---|
| Git | 本地版本控制工具 | `init`、`add`、`commit`、`log`、`reset` |
| GitHub | 远程代码托管与协作平台 | 创建仓库、`push`、`clone`、`pull` |

Git 没有网络也能保存和查看本地版本；执行 `git push` 后，本地提交才会同步到 GitHub。

## 02 Git 仓库与四个区域

普通文件夹执行：

```powershell
git init
```

会生成隐藏的 `.git` 目录，使当前文件夹成为 Git 仓库。`.git` 保存提交历史、分支、暂存区和仓库配置，不应手动修改或删除。

| 区域 | 保存什么 |
|---|---|
| 工作区 Working Directory | 当前正在编辑的真实文件 |
| 暂存区 Staging Area | 准备放入下一次提交的变化 |
| 本地仓库 Local Repository | 已经提交的版本历史 |
| 远程仓库 Remote Repository | GitHub 上用于备份和协作的仓库 |

**容易混淆：**`commit` 只保存到本地仓库，不等于已经上传 GitHub；`push` 才负责同步到远程仓库。

## 03 文件的四种状态

```text
Untracked
  ↓ git add
Staged
  ↓ git commit
Unmodified
  ↓ 修改文件
Modified
  ↓ git add
Staged
```

| 状态 | 含义 |
|---|---|
| Untracked | 新文件存在，但 Git 还没有跟踪 |
| Staged | 变化已进入暂存区，准备提交 |
| Unmodified | 相对于最近一次提交没有新修改 |
| Modified | 已跟踪文件发生修改，但还没有重新暂存 |

遇到不确定的状态，先运行：

```powershell
git status
```

## 04 必须掌握的本地 Git 命令

| 命令 | 作用 | 记忆方式 |
|---|---|---|
| `git init` | 初始化当前仓库 | 开始让 Git 管理项目 |
| `git status` | 查看分支和文件状态 | 不清楚时先看它 |
| `git diff` | 查看尚未暂存的修改 | 工作区改了什么 |
| `git diff --staged` | 查看已经暂存的修改 | 下次准备提交什么 |
| `git add hello.py` | 暂存指定文件 | 精确加入本次提交 |
| `git add .` | 暂存当前目录中应跟踪的变化 | 批量加入 |
| `git commit -m "message"` | 把暂存区保存成一个版本 | 创建本地版本 |
| `git log --oneline` | 单行查看提交历史 | 查看版本记录 |

一次提交应尽量只完成一个明确目的，提交说明要能概括“这次完成了什么”，避免只写 `update`。

## 05 `git reset`：soft / mixed / hard

`HEAD` 表示当前提交，`HEAD~1` 表示上一个提交。

| 命令 | 提交 | 暂存区 | 工作区 | 适用情况 |
|---|---|---|---|---|
| `git reset --soft HEAD~1` | 回退 | 保留 | 保留 | 重新组织或修改刚才的提交 |
| `git reset --mixed HEAD~1` | 回退 | 重置 | 保留 | 重新选择哪些变化需要暂存 |
| `git reset --hard HEAD~1` | 回退 | 重置 | 重置 | 确定放弃提交及工作区变化 |

```text
soft：只动版本
mixed：版本 + 暂存区
hard：版本 + 暂存区 + 工作区代码
```

`--mixed` 是默认模式。单独执行 `git reset` 通常相当于 `git reset --mixed HEAD`：不移动当前提交，只把已暂存的变化撤回工作区。

**危险操作：**`--hard` 可能直接丢失尚未提交的代码，执行前必须确认目标提交和影响范围。

## 06 `.gitignore`：哪些文件不要跟踪

Python 项目常见内容：

```gitignore
.venv/
__pycache__/
*.pyc
.env
.vscode/
```

| 内容 | 忽略原因 |
|---|---|
| `.env` | 常保存 API Key、Token 等敏感信息 |
| `.venv/` | 本机虚拟环境体积大，可以重新创建 |
| `__pycache__/`、`*.pyc` | Python 自动生成的缓存 |
| `.vscode/` | 常包含本机编辑器配置 |

`.gitignore` 本身通常需要提交，让协作者共享忽略规则。

**容易踩坑：**文件已经被 Git 跟踪后，再把它写进 `.gitignore`，不会自动停止跟踪。

## 07 本地仓库连接 GitHub

```powershell
git remote add origin https://github.com/用户名/仓库名.git
git remote -v
git branch -M main
git push -u origin main
```

| 命令 | 作用 |
|---|---|
| `git remote add origin <URL>` | 保存远程地址，并将其命名为 `origin` |
| `git remote -v` | 检查远程名称和地址 |
| `git branch -M main` | 把当前分支重命名为 `main` |
| `git push -u origin main` | 首次推送并建立跟踪关系 |

`origin` 是远程仓库的常用别名，不是特殊服务器。`main` 是本地分支，`origin/main` 表示本地记录的远程 `main` 状态；建立跟踪关系后，通常可以直接使用 `git push`。

## 08 clone / push / pull

| 命令 | 方向 | 什么时候使用 |
|---|---|---|
| `git clone <URL>` | GitHub → 新本地仓库 | 第一次把远程项目完整复制到电脑 |
| `git push` | 本地仓库 → GitHub | 把新的本地提交推送到远程 |
| `git pull` | GitHub → 当前本地仓库 | 获取并合并远程的新提交 |

`clone` 不只是下载当前文件，还会复制提交历史并配置远程仓库。

## 09 分支、合并与冲突

分支让不同任务拥有独立的开发路线，完成后再合并回目标分支。

```powershell
git branch
git switch -c feature-name
git switch main
git merge feature-name
```

| 命令 | 作用 |
|---|---|
| `git branch` | 查看本地分支 |
| `git switch -c feature-name` | 创建并切换到功能分支 |
| `git switch main` | 切换回主分支 |
| `git merge feature-name` | 把功能分支合并到当前分支 |

两个分支修改同一文件的同一位置时，Git 可能无法自动合并，并在文件中加入冲突标记：

```text
 <<<<<<< HEAD
当前分支内容
 =======
另一分支内容
 >>>>>>> feature-name
```

解决流程：理解双方修改 → 保留正确的最终内容 → 删除冲突标记 → 检查和运行代码 → `git add` → 完成提交。

## 10 VS Code 源代码管理

中文版 VS Code 左侧“源代码管理”可以完成：

- 查看已修改和未跟踪文件；
- 打开文件差异；
- 点击 `+` 暂存变化；
- 输入提交说明并提交；
- 创建、切换和合并分支；
- 拉取、推送与同步；
- 使用合并编辑器处理冲突。

图形界面和命令行操作的是同一个 Git 仓库。命令行适合理解原理，图形界面适合提高日常效率。

## 11 日常 Git 工作流

```powershell
git status
git diff
git add .
git diff --staged
git commit -m "描述本次修改"
git push
```

- 提交前先检查状态和差异，避免带入无关文件。
- 一次提交尽量只包含一个目的。
- 拉取或合并后检查并运行项目。
- 不提交虚拟环境、缓存、密钥和临时文件。

## 12 Day 01 最终自测

能用自己的话解释即可，不要求背定义：

- Git 与 GitHub 有什么区别。
- 工作区、暂存区、本地仓库、远程仓库如何流动。
- Untracked、Staged、Unmodified、Modified 分别表示什么。
- `add` 与 `commit`、`commit` 与 `push` 有什么区别。
- `clone`、`push`、`pull` 的数据方向。
- `soft`、`mixed`、`hard` 分别影响哪些区域。
- 为什么 `.env`、`.venv` 和缓存文件需要忽略。
- `origin`、本地 `main` 和 `origin/main` 分别是什么。
- 分支解决什么问题，冲突出现后如何处理。
- VS Code 源代码管理与 Git 命令是什么关系。

## Day 01 核心结论

Git 的核心不是“上传代码”，而是管理本地版本历史；GitHub 是远程托管与协作平台。先 `commit` 到本地仓库，再 `push` 到 GitHub。
