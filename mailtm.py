import json
import time

import requests
from random_strings import random_string


headers = {
    'authority': 'api.mail.tm',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'tr-TR,tr;q=0.7',
    'origin': 'https://mail.tm',
    'referer': 'https://mail.tm/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}


def get_domain():

    r = requests.get('https://api.mail.tm/domains', headers=headers)
    if r.status_code == 200:
        return {"status":"OK","domain":r.json()["hydra:member"][0]["domain"]}
    if r.status_code != 200:
        return {"status":"ERROR","response":r.text}


def create_account(domain):
    mail = random_string(15)
    passw = random_string(10)
    json_data = {
        'address': f'{mail}@{domain}',
        'password': f'{passw}',
    }

    r = requests.post('https://api.mail.tm/accounts', headers=headers, json=json_data)


    if r.status_code == 201:
        return {"status":"OK","mail":f'{mail}@{domain}',"password":passw}
    if r.status_code != 201:
        return {"status":"ERROR","response":r.text}

def get_token_of_account(mail,password):
    json_data = {
        "address": mail.lower(),
        "password": password,
    }

    r = requests.post('https://api.mail.tm/token', headers=headers, json=json_data)
    data = r.json()
    data = {"status": "OK", **data}
    return data




