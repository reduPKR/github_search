import requests
import json

def get_data(item):
    data = {
        "proprietário": item['repository']['owner']['login'],
        "repositório": item['repository']['name'],
        "repositório completo": item['repository']['full_name'],
        "url do código": item['html_url'],
        "nome do arquivo": item['name'],
        "privado": item['repository']['private'],
        "descrição": item['repository']['description']
    }

    return json.dumps(data)


def send_to_webhook(item):
    print(
        f"proprietário: {item['repository']['owner']['login']}\n"
        f"repositório : {item['repository']['name']}\n"
        f"repositório completo: {item['repository']['full_name']}\n"
        f"url do código: {item['html_url']}\n"
        f"nome do arquivo: {item['name']}\n"
        f"privado: {item['repository']['private']}\n"
        f"descrição: {item['repository']['description']}"
    )
    print("-" * 80)

    webhook_url = "https://webhook.site/9cbac4c0-92bb-4647-aebe-c0c223e35c0e"
    header = {
        'Content-Type': 'application/json'
    }

    requests.post(webhook_url, data=get_data(item), headers=header)


if __name__ == "__main__":
    url = "https://api.github.com/search/code?q={}-user:MMMMM&in:file&sort=created&order=desc"
    token = ""

    header = {
        'authorization': 'Bearer {}'.format(token)
    }

    with open("lista.txt") as file:
        for line in file:
            url = url.format(line)
            response = requests.request("GET", url, headers=header)
            response_json = response.json()
            #print(response_json["items"])

            for item in response_json["items"]:
                send_to_webhook(item)
