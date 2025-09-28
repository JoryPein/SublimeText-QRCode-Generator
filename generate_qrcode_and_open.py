# 导入必要的系统库
import sys
import os
import tempfile
import time
import subprocess

# 将插件自带的 'lib' 目录添加到 Python 的模块搜索路径中
# 确保插件可以正确导入其依赖的库
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)

# 导入依赖库
import qrcode
from PIL import Image
import six

# 导入 Sublime Text 相关的 API
import sublime
import sublime_plugin

# 定义一个 Sublime Text 命令，用于生成二维码并打开
class GenerateQrcodeAndOpenCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # 获取当前选中的第一个区域
        region = self.view.sel()[0]

        # 判断选中区域是否为空
        if not region.empty():
            # 获取选中区域的文本内容
            text = self.view.substr(region)

            try:
                # 使用 qrcode 库生成二维码图像
                img = qrcode.make(text)
                
                # 获取系统临时目录
                temp_dir = tempfile.gettempdir()
                # 使用当前时间戳生成唯一的文件名
                timestamp = str(int(time.time()))
                file_name = 'qrcode_{}.png'.format(timestamp)
                # 拼接文件的完整路径
                file_path = os.path.join(temp_dir, file_name)
                # 保存二维码图像到文件
                img.save(file_path)

                # 在 Sublime Text 状态栏显示提示信息
                status_message = '二维码已生成: {}，正在打开...'.format(file_path)
                sublime.status_message(status_message)

                # 根据不同操作系统使用对应的方式打开文件
                if sys.platform == "win32":
                    os.startfile(file_path)
                elif sys.platform == "darwin": # macOS
                    subprocess.call(["open", file_path])
                else: # Linux
                    subprocess.call(["xdg-open", file_path])

            except Exception as e:
                # 如果发生异常，则在错误弹窗中显示详细信息
                error_message = '生成或打开二维码失败: {}: {}'.format(type(e).__name__, e)
                sublime.error_message(error_message)
        else:
            # 如果没有选择文本，则在状态栏提示用户
            sublime.status_message("请先选择文本内容")