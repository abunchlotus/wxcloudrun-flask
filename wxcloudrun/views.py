from datetime import datetime
from flask import render_template, request
from wxcloudrun import app, socketio
from wxcloudrun import send_requests
from flask_socketio import emit
import logging

logger = logging.getLogger('log')


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('aaa.html')

@app.route("/api/gpt-3", methods=["POST"])
def generate_text():
    logger.info("entry")
    data = request.get_json()
    msg = data["msg"]
    return send_requests.send_requests(msg)


@app.route("/api/gpt20230502", methods=["POST"])
def generate_text_new():
    data = request.json
    print("data is {}".format(data))
    print("data_type is {}".format(type(data)))
    return send_requests.send_json(data)


@socketio.on('connect')
def handle_connect():
    logger.error('Client connected')
    emit('on_open', '成功连接到服务器')


@socketio.on('message')
def handle_message(message):
    logger.error(f"Received message: {message}")
    emit('message', message)


@socketio.on('disconnect')
def handle_disconnect():
    logger.error('Client disconnected')
