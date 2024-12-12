from openai import OpenAI
API_KEY = open("ApiKey.txt", "r",encoding="utf-8").read().strip()
prompts = open("prompt.txt", "r", encoding="utf-8").read()
# prompts = open("Alice.yml", "r", encoding="utf-8").read()
def get_response(chat):
    client = OpenAI(
        api_key=API_KEY,
        base_url="https://api.moonshot.cn/v1",
    )
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system",
             "content": f"{prompts}"},
            {"role": "user", "content": f"{chat}"}
        ],
        temperature=0.3,
    )
    return completion.choices[0].message.content
if __name__ == '__main__':
    content = "你好，爱丽丝，你喜欢什么游戏？"
    response=get_response(content)

    print(response)
