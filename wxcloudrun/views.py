from datetime import datetime
from flask import render_template, request
from wxcloudrun import app, socketio
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
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


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    if 'msg' in params:
        msg = params["msg"]
        res = send_requests.send_requests(msg)
        logger.error(res)
        return res

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)


@app.route("/api/gpt-3", methods=["POST"])
def generate_text():
    logger.info("entry")
    data = request.get_json()
    msg = data["msg"]
    return send_requests.send_requests(msg)

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
