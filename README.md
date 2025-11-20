# Kean University 课程位置追踪器

这是一个用于自动抓取 Kean University 选课系统中课程剩余位置的移动应用程序，可以打包成 APK 文件在安卓手机上安装使用。

## 功能特性

- 登录 Kean University 选课系统
- 自动抓取课程剩余位置信息
- 可视化界面显示课程数据
- 一键刷新获取最新数据
- 适配移动设备界面

## 技术架构

- **前端界面**: Kivy (Python GUI 框架)
- **网络请求**: requests 库
- **HTML 解析**: BeautifulSoup4
- **移动端打包**: Buildozer

## 项目结构

```
/workspace/
├── main.py              # 主应用文件
├── course_scraper.py    # 课程数据抓取模块
├── requirements.txt     # 项目依赖
├── buildozer.spec       # Android 打包配置
└── README.md            # 项目说明
```

## 使用说明

### 本地运行 (开发测试)

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行应用：
```bash
python main.py
```

### 打包成 APK (Android)

1. 在 Linux 环境下安装 Buildozer：
```bash
pip install buildozer
```

2. 初始化 Buildozer：
```bash
buildozer init
```

3. 构建 APK：
```bash
buildozer android debug
```

生成的 APK 文件将在 `bin/` 目录中。

## 重要提醒

⚠️ **法律和道德注意事项**:
- 使用此应用时请遵守 Kean University 的使用条款
- 不要对选课系统造成过大负载，建议合理设置刷新频率
- 仅用于个人学习和便利目的，不要用于恶意刷课等行为
- 网站结构可能随时变化，需要相应更新解析代码

## 代码说明

`course_scraper.py` 文件中的解析逻辑需要根据实际的网页结构进行调整，因为不同学校和系统的页面结构可能不同。当前代码使用了通用的解析方法，但可能需要针对具体页面进行调整。

## 自定义配置

- 在 `buildozer.spec` 中可以修改应用名称、版本、权限等信息
- 在 `course_scraper.py` 中可以调整登录和数据抓取逻辑
- 在 `main.py` 中可以修改用户界面布局和交互方式

## 故障排除

如果无法抓取数据，请检查：
1. 网站登录流程是否发生变化
2. 是否需要处理额外的验证机制（如验证码、双因素认证）
3. 网络请求头是否需要更新
4. 页面元素选择器是否需要调整