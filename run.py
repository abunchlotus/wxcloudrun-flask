# 创建应用实例
import sys

from wxcloudrun import socketio
from wxcloudrun import app

# 启动Flask Web服务
if __name__ == '__main__':
    #socketio.run(app, host=sys.argv[1], port=sys.argv[2], allow_unsafe_werkzeug=True)
    socketio.run(app, host="127.0.0.1", port=8886, allow_unsafe_werkzeug=True)