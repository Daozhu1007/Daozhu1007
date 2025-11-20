[app]
# 应用的基本信息
title = Kean Course Tracker
package.name = keancoursetracker
package.domain = org.example

# 源代码目录
source.dir = .

# 应用版本
version = 0.1

# 应用描述
description = Kean University 课程位置追踪器

# 主入口文件
requirements = python3,kivy,requests,beautifulsoup4

# 应用入口
source.include_exts = py,png,jpg,kv,atlas

# 编译选项
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30

# 应用图标和启动画面
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# 服务配置（如果需要后台运行）
# services = http:main.py

[buildozer]
# 构建目录
log_level = 2

# 针对Android平台的配置
[app] 
android.add_compile_options = --target 21