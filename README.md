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
![1bf251ed0d26d29b06650e7c75922ea](https://github.com/user-attachments/assets/f3c46cd2-d02d-41ec-997b-4debfaa3e4b3)

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
