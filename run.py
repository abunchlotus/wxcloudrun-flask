# 创建应用实例
import sys

from wxcloudrun import socketio
from wxcloudrun import app

# 启动Flask Web服务
if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1", port=8886)
