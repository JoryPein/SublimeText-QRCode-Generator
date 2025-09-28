# QRCodeGenerator for Sublime Text

这是一个为 Sublime Text 4 开发的插件，能够将选中的文本内容快速生成二维码，并自动打开。

---

## ✨ 功能特性

- **快速生成**: 只需选中一段文本，即可通过命令一键生成对应的二维码。
- **自动打开**: 生成的二维码图片会自动通过系统默认的图片查看器打开，方便快捷。
- **跨平台支持**: 支持 Windows、macOS 和 Linux 主流操作系统。
- **临时存储**: 二维码图片保存在系统临时目录中，不会污染您的项目文件夹。

## ⚙️ 依赖

本插件依赖于以下 Python 库：

- `qrcode`
- `Pillow`
- `six`

这些依赖已经打包在插件的 `lib` 目录中，您无需手动安装。

## 🚀 安装

### 通过 Package Control (推荐)

这是安装此插件最简单的方法。

1.  打开 Sublime Text 4。
2.  按下 `Ctrl+Shift+P` (Windows/Linux) 或 `Cmd+Shift+P` (macOS) 打开命令面板。
3.  输入 `Package Control: Install Package` 并回车。
4.  搜索 `QRCodeGenerator` 并回车进行安装。

*(注意：此插件目前尚未提交到官方的 Package Control 仓库。提交后，上述方法才可用。在提交之前，请使用手动安装方法。)*

### 手动安装

1.  点击 `Preferences` > `Browse Packages...` 菜单，打开您的 `Packages` 目录。
2.  进入 `Packages` 目录后，通过以下任一方法操作：
    *   **方法一：Git Clone**
        在 `Packages` 目录下打开终端，并执行以下命令：
        ```bash
        git clone https://github.com/JoryPein/SublimeText-QRCode-Generator.git "QRCodeGenerator"
        ```

    *   **方法二：下载 ZIP**
        1.  在 GitHub 仓库页面点击 `Code` > `Download ZIP`。
        2.  解压下载的文件。
        3.  将解压后的文件夹重命名为 `QRCodeGenerator`。
        4.  将 `QRCodeGenerator` 文件夹移动到第一步打开的 `Packages` 目录下。

3.  重启 Sublime Text 4 使插件生效。

## 💡 如何使用

1.  在 Sublime Text 编辑器中，选中您想要生成二维码的文本内容（例如，一个网址、一段文字等）。
2.  按下 `Ctrl+Shift+P` (Windows/Linux) 或 `Cmd+Shift+P` (macOS) 打开命令面板。
3.  输入 `Generate QR Code` 并回车。
4.  插件会自动生成二维码图片，并调用系统默认程序打开它。

### 添加快捷键 (可选)

为了更高效地使用，您可以为该命令绑定一个自定义快捷键。

1.  打开 `Preferences` > `Key Bindings`。
2.  在右侧的用户自定义快捷键文件 (`Default (OS).sublime-keymap`) 中，添加以下内容：

    ```json
    [
        { "keys": ["ctrl+alt+q"], "command": "generate_qrcode_and_open" }
    ]
    ```
    您可以将 `"ctrl+alt+q"` 替换为您喜欢的任意快捷键组合。

3.  保存文件即可生效。现在，您只需选中文字后按下 `ctrl+alt+q` 就可以直接生成二维码了。

## 🤝 贡献

欢迎通过提交 Issue 或 Pull Request 来为本项目做出贡献。

## 📄 许可证

本项目基于 [MIT License](LICENSE) 发布。
