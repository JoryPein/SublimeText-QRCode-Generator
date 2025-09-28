# ------------------------------------------------------------------
# ST3 Plugin Dependency Loader
#
# This code block must be at the absolute top of the file. It
# manually and forcefully injects the 'lib' directory into the path
# BEFORE any other plugin code or imports are processed.
# ------------------------------------------------------------------
import sys
import os

# Define the path to our bundled 'lib' directory
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')

# Forcefully add the 'lib' directory to the front of the Python path
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)

# --- Dependency imports ---
# Now that the path is guaranteed to be correct, we can import
# our bundled libraries.
import qrcode
from PIL import Image  # We can even import from PIL directly now
import six

# --- Sublime Text imports ---
# These should always come after the dependency loading.
import sublime
import sublime_plugin

# --- Standard library imports ---
import tempfile
import time
import subprocess
# ------------------------------------------------------------------


#
# The actual plugin command class
#
class GenerateQrcodeAndOpenCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.sel()[0]

        if not region.empty():
            text = self.view.substr(region)

            try:
                # This call will now finally succeed
                img = qrcode.make(text)
                
                temp_dir = tempfile.gettempdir()
                timestamp = str(int(time.time()))
                file_name = 'qrcode_{}.png'.format(timestamp)
                file_path = os.path.join(temp_dir, file_name)
                img.save(file_path)

                status_message = '二维码已生成: {}，正在打开...'.format(file_path)
                sublime.status_message(status_message)

                if sys.platform == "win32":
                    os.startfile(file_path)
                elif sys.platform == "darwin":
                    subprocess.call(["open", file_path])
                else:
                    subprocess.call(["xdg-open", file_path])

            except Exception as e:
                # We add the type of exception for better debugging
                error_message = '生成或打开二维码失败: {}: {}'.format(type(e).__name__, e)
                sublime.error_message(error_message)
        else:
            sublime.status_message("请先选择文本内容")