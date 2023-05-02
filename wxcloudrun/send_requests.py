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
    resp = requests.post(url=url, headers=headers, json=msg_dict, verify=False, timeout=60)
    if resp.status_code != 200:
        msg = "return 200!"
        logger.error("error,{}".format(resp.text))
        logger.error("error,{}".format(resp))
        return msg
    logger.error("i am here1")
    resp_content = resp.content
    logger.error("i am here2")
    resp_content_dict = json.loads(resp_content)
    logger.error("i am here3")
    choices_dict = resp_content_dict["choices"]
    logger.error("i am here4")
    message_dict = choices_dict[0].get("message")
    logger.error("i am here5")
    real_content = message_dict["content"]
    logger.error("i am here6")
    logger.error(resp.text)
    return real_content

def send_json(json_dict: dict):
    print("json_dict in send_json is {}".format(json_dict))
    # url = "https://api.openai.com/v1/chat/completions"
    url = "https://www.dqszlishuqiang.com:8081/v1/chat/completions"
    # url = "http://43.157.28.126:8082/v1/chat/completions"

    raw_k = "#USn4cJ96YGe1K4uYf9m4T3Bl#bkFJd3TNoEBiLnwGvDRapPPL#"
    new_k_0 = raw_k.replace("#", "")
    new_k_1 = "sk-{}".format(new_k_0)
    headers = {"Content-Type": "application/json",
               "Authorization": "Bearer {}".format(new_k_1)}

    # msg_dict = {"prompt": "如何评价霍利菲尔德", "options": {"parentMessageId": "chatcmpl-7B2flR1e0MUZVdwECG0bYDry3GY4J"}, "temperature": 0.1, "top_p": 1}

    resp = requests.post(url=url, headers=headers, json=json_dict, verify=False, timeout=60)
    print(resp.text)
    if resp.status_code != 200:
        msg = "return not 200"
        print(resp.text)
        return {"error": msg}
    return resp.text
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
    #
    # resp_content = resp.content
    # resp_content_dict = json.loads(resp_content)
    # choices_dict = resp_content_dict["choices"]
    # message_dict = choices_dict[0].get("message")
    # real_content = message_dict["content"]
    # return real_content


if __name__ == "__main__":
    a = send_requests("你知道特斯拉吗")
    print(len(a))

