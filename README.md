# Kean University 课程位置追踪应用

本应用允许Kean University学生监控课程剩余位置，并打包为Android APK文件。

## 功能

- 用户登录界面（支持Kean University的Okta单点登录系统）
- 课程数据自动抓取
- 可视化显示课程名称和剩余位置
- 刷新按钮获取最新数据
- 错误处理和用户反馈

## 技术栈

- **前端**: Kivy (Python GUI框架)
- **后端**: Python requests, BeautifulSoup4
- **认证**: Okta SSO处理
- **打包**: Buildozer (用于Android APK)

## 使用说明

### 本地运行

1. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

2. 运行应用：
   ```
   python main.py
   ```

### Android APK打包

在Linux环境下执行以下命令：

1. 安装Buildozer：
   ```
   pip install buildozer
   ```

2. 初始化Buildozer：
   ```
   buildozer init
   ```

3. 构建APK：
   ```
   buildozer android debug
   ```

生成的APK文件将位于 `bin/` 目录下。

## Okta认证说明

本应用已更新以支持Kean University的Okta单点登录系统。应用会：

1. 访问课程规划页面，自动重定向到Okta登录
2. 在Okta页面提交用户凭据
3. 处理SAML认证流程
4. 返回课程规划页面获取数据

## 注意事项

- 请确保遵守Kean University的使用条款
- 应用使用网络请求抓取数据，请合理使用避免对服务器造成过大负载
- 如遇到多因素认证(MFA)，可能需要手动处理

## 文件结构

```
/workspace/
├── main.py              # 主应用文件（包含UI和应用逻辑）
├── course_scraper.py    # 课程数据抓取模块（支持Okta认证）
├── requirements.txt     # 项目依赖
├── buildozer.spec       # Android打包配置
└── README.md            # 本说明文件
```

## 故障排除

- 如果登录失败，检查用户名和密码是否正确
- 确保网络连接正常
- 如果遇到MFA，当前版本可能无法自动处理，需要手动登录