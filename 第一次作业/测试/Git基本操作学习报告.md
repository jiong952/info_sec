---
typora-copy-images-to: ./
---

# Git基本操作学习报告

创建git本地仓库：`git init`

git总共分为三个区域

- 工作区（working directory）
- 暂缓区（stage index）
- 历史记录区（history）

![image-20220904112850771](imgs\image-20220904112850771-16627270019882.png)

working directory --> stage index

- 对文件进行改动后，文件处于Unstaged Changes状态，需要通过`git add <fileName>`操作才能放到暂存区，也可以通过git gui的Stage Changed按钮进行操作。

stage index --> history

- 使用 `git commit -m [message]`可以将暂存区提交到本地仓库

版本回退 `git reset`

HEAD指针指向当前分支当前版本的游标

- soft：只重置HEAD到指定的版本，不修改暂存区以及工作目录
  - 应用场景：上一次的commit存在错误文件，则可以使用*git reset --soft 版本号*进行回滚
- mixed【默认】：修改HEAD以及暂存区
- hard：彻底回退版本，本地代码也会回退
  - 应用场景：代码修改出错，回退到上一个历史版本

图形化界面的快捷键

- CTRL + I 从unstaged 变为Staged

- F5刷新

- CTRL + 回车 commit

  ![first commit_visual](imgs\first commit_visual-16627270078744.png)