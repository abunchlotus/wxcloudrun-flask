import requests
import json
import logging
import base64


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
    key = "c2staE5GcUZCRkw5dGFUdkp4SEF6OHVUM0JsYmtGSm5XYXdXazVIRkRUbEJBQVQxSmhX"
    headers = {"Content-Type": "application/json",
               "Authorization": "Bearer {}".format(base64.b64decode(key.encode('utf-8')).decode('utf-8'))}
    print(headers)

    temperature = 0.1
    role = "user"
    msg_dict = {
        "temperature": temperature,
        "model": "gpt-3.5-turbo",
        "messages": [{"role": role, "content": msg}]
    }
    logger.error("i am here")
    resp = requests.post(url=url, headers=headers, json=msg_dict, verify=False)
    if resp.status_code != 200:
        msg = "return 200!"
        logger.error("error,{}".format(resp.text))
        logger.error("error,{}".format(resp))
        return msg

    resp_content = resp.content
    resp_content_dict = json.loads(resp_content)
    choices_dict = resp_content_dict["choices"]
    message_dict = choices_dict[0].get("message")
    real_content = message_dict["content"]
    return real_content


if __name__ == "__main__":
    a = send_requests("你知道特斯拉吗")
    print(a)

