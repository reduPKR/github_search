import requests
import json

url = "https://api.github.com/search/code?q={}-user:reduPKR&in:file&sort=created&order=desc"
token = ""

headers = {
    'authorization': 'Bearer {}'.format(token)
}

with open("lista.txt") as file:
    for line in file:
        url = url.format(line)
        response = requests.request("GET", url, headers=headers)
        response_json = response.json()
        #print(response_json["items"])

        for item in response_json["items"]:
            print(
                f"proprietário: {item['repository']['owner']['login']}\n"
                f"repositório : {item['repository']['name']}\n"
                f"repositório completo: {item['repository']['full_name']}\n"
                f"privado: {item['repository']['private']}\n"
                f"nome do arquivo: {item['name']}\n"
                f"url do código: {item['html_url']}"
            )
            print("-"*80)
