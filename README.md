# simple_remote_view
- 手机浏览器同局域网内查看电脑屏幕
- 支持多显示器
- 支持左键点击操作
- 免安装
- 控制ppt
## 使用方式

1. 手机电脑处于同一局域网
2. 打开simple_remote_view.exe
3. 允许通过防火墙
4. 手机扫描连接不同的显示器
![image](https://github.com/user-attachments/assets/756eff1a-8571-45cb-bff8-678e44f5129c)
5. 在手机上查看电脑屏幕或者单击控制电脑
![265740741dfa6eb1baf0aa9c8a4d456](https://github.com/user-attachments/assets/ce939a3f-b584-4f5e-8795-5e5f2f9ddd14)

## 开发指南
### 安装依赖
```
requirements.txt
```
### 运行
```
python app.py
```
### 打包
```
pip install pyinstaller

pyinstaller app.spec
```
