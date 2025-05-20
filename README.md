在终端上演示《传送门》片尾曲效果的 Python 脚本程序。

## 使用条件

`still_alive_credit.py` 脚本使用 Python 3，以下提到的 `pip` 多数情况下对应 `pip3` 命令
以调用 Python 3 的 `pip` 组件。

Windows 下需要使用 Windows terminal，MinTTY 等支持 ANSI 终端转义序列的终端模拟器。

为了播放音乐，需要用 `pip` 安装 `playsound`。`playground` 在 Linux 下依赖 
`python-gobject` 软件包（Ubuntu 已默认安装）。在 MacOS 下还需要用 `pip` 安装 `PyObjC`。

## 使用方法

在当前目录下执行：

```
python3 still_alive_credit.py
```

可以使用`--stay`参数使得播放完音乐后不退出，停留在播放完的界面。默认是自动退出。你也可以按`Ctrl+C`退出。

```
python3 still_alive_credit.py --stay
```

可以使用 `--no-sound` 参数不带音乐进行演示，此时脚本只依赖 Python 标准库：

```
python3 still_alive_credit.py --no-sound
```
