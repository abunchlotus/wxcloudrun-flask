import requests
import json
import logging

from requests.packages import urllib3
# 关闭警告
urllib3.disable_warnings()

logger = logging.getLogger('log')

def send_requests(msg: str) -> str:
    if not msg:
        print("no msg inside")
        return ""
    #api_key = "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"
    #url = "https://api.openai.com/v1/chat/completions"
    url = "https://www.dqszlishuqiang.com:8081/v1/chat/completions"
    headers = {"Content-Type": "application/json",
               "Authorization": "Bearer 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"}

    temperature = 0.1
    role = "user"
    msg_dict = {
        "temperature": temperature,
        "model": "gpt-3.5-turbo",
        "messages": [{"role": role, "content": msg}]
    }
    logger.info("i am here")
    resp = requests.post(url=url, headers=headers, json=msg_dict, verify=False)
    if resp.status_code != 200:
        msg = "return 200!"
        logger.info("error,{}".format(resp.text))
        logger.info("error,{}".format(resp))
        return msg

    # {
    #     "id": "chatcmpl-123",
    #     "object": "chat.completion",
    #     "created": 1677652288,
    #     "choices": [{
    #         "index": 0,
    #         "message": {
    #             "role": "assistant",
    #             "content": "\n\nHello there, how may I assist you today?",
    #         },
    #         "finish_reason": "stop"
    #     }],
    #     "usage": {
    #         "prompt_tokens": 9,
    #         "completion_tokens": 12,
    #         "total_tokens": 21
    #     }
    # }

    resp_content = resp.content
    resp_content_dict = json.loads(resp_content)
    choices_dict = resp_content_dict["choices"]
    message_dict = choices_dict[0].get("message")
    real_content = message_dict["content"]
    return real_content


if __name__ == "__main__":
    a = send_requests("长沙市今天的天气怎么样")
    print(a)

