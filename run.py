# 创建应用实例
import sys

from wxcloudrun import socketio

# 启动Flask Web服务
if __name__ == '__main__':
    socketio.run(host=sys.argv[1], port=sys.argv[2])
