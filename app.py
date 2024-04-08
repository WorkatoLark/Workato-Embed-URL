import json
import os
import webbrowser
from time import sleep

import gradio as gr
import requests

from jwt_token import generate_jwt, generate_token

# Install
# 1. create customer account: tenant id
# 2. create a folder: user id
# 3. Import manifest to user folder
# Connect:
# 1. Iframe auth button ()
# 2. (optional) List all connections by account id (tenant id)
# 3. Update receipt
# Start flow
# 1. Call trigger flow api
HTML_STRING = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <script>
      window.addEventListener('message', receiveMessage);
      function receiveMessage(event) {
        var data = JSON.parse(event.data);

        switch (data.type) {
          case 'heightChange':
            document.getElementById('workatoId').style.height = data.payload.height + 'px';
            break;
          case 'connectionStatusChange':
            var message = data.error || (data.payload.connected ? 'Connected' : 'Disconnected');
            document.getElementById('statusId').innerText = message;
            break;
          case 'error':
            console.log(data.payload.message);
        }
      }
    </script>
  </head>
  <body>
    <h4>Status: <span id="statusId"></span></h4>
    <iframe id="workatoId" src="WORKATO_URL" style="width: 1000px; height: 1500px; border: 0"></iframe>
  </body>
</html>
"""
ORIGINAL_TOKEN = 'Bearer wrkaus-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjYjJhNzgzZi1lNzU3LTRhZTctODQ4Zi1kNmYwYmQzMzIzZDYiLCJqdGkiOiI1M2QyNWMwMC0zNDRjLTQyOTEtODM0Zi1iM2IxY2I3Y2RkNmQifQ.Zg734qAQ-31zn1pssyRMJHDf8npOmo1N-VLMv-Exx7HIDDn2z-jCnSVHbHyftsE_tAc8uFi4vzd6FGo5uB-CAwNxtz5ePRdGgF2addTi5GwqAjyi0vQgz9AjxuKUw1wQvLCwVTGsBQnE-M48qrQ-fdODx0GV7rzXUMrrSGn9xdWXsY5inaKd4ETPhLPYr2H5s05ouIt6Tw4AZxl7ERj3u5_pNyJQ34OPFALzZNETCsTsalzI_qMhZj9wnRv8_iEqQylnUFlwkQIwtWpXHq_LAOeHWEdyr3_kHQK6FZFTgkSSlP1q75uyN6y4RU0oKJw3JiyL0vjJMQra_8N96yKyBldRSsrcbH_OhTd-0sYbyUf8WRM-iJD7_yVdGiYDJvP-Mhqi-FnRGUsUkCfH3fDW5I_u-4MSB7AoI9b9A_9gvIC3_JcUqhO_9QRI2uiGkztdoUxCunRJ-Tx8dgWSa7wKKRQdrf2gYziqwXoqvMlD7wveEFrXq6cqnxLzukoWjsMcCv9GA-SIHN9Xw8p9k75AeF6Nc3zB0A1ZHxm11l2jCyM-puBncb3DadKMbNbJWXDBsNSNSB9Ct_h3n7PLYrumWeNnMXeTj6McJtWf7rogjBRZfJznYrovAT8joELzkmyNBC-JrVuMZ60tv4b0OHF8H3OSFPqoYq2y9wqk9VJxXfc'
API_TOKEN = 'Bearer wrkaus-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiYWUxODJmZC1lOTNiLTQyNjQtYmRmNC0wYzU3ZTFjNWI5NTgiLCJqdGkiOiJlODZjNGZkZS1jMmNjLTQ1MGQtOTg5ZS0wMzc1YjY5NTMxNDUifQ.QTlNuv8mv5vFuuIKT0us7ZvuAxm_3bv8Ph22yZfS-rFFlJ_XG40ky0MZXQNomqU5P9yZKuyBekozRGx7GnnpyTONHDRpGQ-G44Cl9A2d9CgDFr0VZQmyRk-1ba6EUON1DmP--s6pUMc0pqsK9drO01AgqHjOgkHbN3KDFj8cZ5iN_l1yaB4sJABfU7nFpBP5v-ljOPx0rG_EX6a6U8w90In3dQVJjzsIbamlLVQL-ECX2DAOAYPYxDHdrkLH7K44OEQoPFUElQYLtFVqsImI_q5T3d01Tt1aGJxuyc90rt9xNGR1Ext2yvydIQBaTWTCniFQmNLXJSWfFlTT1DkBn5nsiPRw62G7qn8Z0xgRLONuewr3GkSolu53W2gRCUpqWgaEEmXCjhwtwiSJyY39wa3ClrPZrb40zbGxbmoHwVUN7bYB2CNRQLzsWXpxyQzlNN85tr0k9SkeXVL2gDwWRmjc00j41Bc91qrxiPNP0lSONPdeDrMYUbsPoT6G9Rk0Kd024oeVJYaUrKuifkFD0HTeR5TuKEpgQEZM1dP5dj0BPUZiZ_fbt9zRgS6g4_8nzQm955NMNf9oBmGzs0Ucujg96WLN3EPFmNF1x4lmGscUe_liGckfeXckMr0IdB6O6BUSyXM70FmlVcX-V297eWi3tjdVONcq01v74on_c0s'


def create_user(tenant_id):
    url = 'https://www.workato.com/api/managed_users'
    headers = {
        'Authorization': ORIGINAL_TOKEN,
        'Content-Type': 'application/json'
    }

    data = {
        "name": tenant_id,
        "notification_email": "jiajun.wang@bytedance.com",
        "external_id": tenant_id,
        "whitelisted_apps": ["gmail", "github"]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = json.loads(response.text)
    print(response_json)
    if 'message' in response_json:
        print(response_json['message'])
        raise Exception(response_json['message'])
    elif 'id' in response_json:
        return response_json['id']
    else:
        raise Exception("Unknown error")


def list_all_folders(parent_id=None):
    url = 'https://www.workato.com/api/folders'
    headers = {
        'Authorization': ORIGINAL_TOKEN,
        'Content-Type': 'application/json'
    }
    params = {'parent_id': parent_id} if parent_id else {}
    response = requests.get(url, headers=headers, params=params)
    print(response.text)


def create_folder(parent_id, folder_name):
    url = f'https://www.workato.com/api/managed_users/{parent_id}/folders'
    headers = {
        'Authorization': ORIGINAL_TOKEN,
        'Content-Type': 'application/json'
    }

    data = {
        "name": folder_name
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = json.loads(response.text)
    print(response_json)
    if 'message' in response_json:
        print(response_json['message'])
        raise Exception(response_json['message'])
    elif 'id' in response_json:
        return response_json['id']
    else:
        raise Exception("Unknown error")


def import_manifest(user_id, folder_id):
    url = f'https://www.workato.com/api/managed_users/{user_id}/imports?folder_id={folder_id}?restart_recipes=true'
    headers = {
        'Authorization': ORIGINAL_TOKEN,
        'Content-Type': 'application/octet-stream'
    }

    file_path = 'Junyu V5.zip'
    with open(file_path, 'rb') as file:
        response = requests.post(url, headers=headers, data=file)
    response_json = json.loads(response.text)
    print(response_json)
    if 'message' in response_json:
        print(response_json['message'])
        raise Exception(response_json['message'])
    elif 'id' in response_json:
        return response_json['id']
    else:
        raise Exception("Unknown error")


def list_recipe_by_user_folder(user_id, folder_id):
    url = f'https://www.workato.com/api/managed_users/{user_id}/recipes'
    headers = {
        'Authorization': ORIGINAL_TOKEN,
        'Content-Type': 'application/json'
    }
    data = {
        "folder_id": folder_id,
    }
    response = requests.get(url, headers=headers, data=json.dumps(data))
    response_json = json.loads(response.text)
    print(response_json)
    connectors = response_json['result'][0]['config']
    recipe_id = response_json['result'][0]['id']
    print(f'list_recipe_by_user_folder user_id:{user_id}, folder_id: {folder_id} connectors: {connectors}')
    return create_connections_by_recipe(user_id, recipe_id, connectors, folder_id)


def create_connections_by_recipe(user_id, recipe_id, connectors, folder_id):
    provider = "provider"
    name = "name"
    connection_ids = []
    for connector in connectors:
        if connector['keyword'] == 'application':
            name = connector['name']
            provider = connector['provider']
        url = f'https://www.workato.com/api/managed_users/{user_id}/connections'
        headers = {
            'Authorization': ORIGINAL_TOKEN,
            'Content-Type': 'application/json'
        }
        data = {
            "name": f"{folder_id}_{provider}",
            "provider": provider,
            "folder_id": folder_id
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_json = json.loads(response.text)
        print(response_json)
        connection_ids.append(response_json['id'])
    print(f'create_connections_by_recipe user_id:{user_id}, folder_id: {folder_id} connection_ids: {connection_ids}')
    return recipe_id, connection_ids


def install_app(tenant_id, user_id):
    try:
        userid = create_user(tenant_id)
        folder_id = create_folder(userid, user_id)
        import_manifest(userid, folder_id)
        sleep(5)
        recipe_id, connection_ids = list_recipe_by_user_folder(userid, folder_id)
    except Exception as e:
        return f'install failed: {e}'

    return json.dumps({'user_id': userid,
                       'folder_id': folder_id,
                       'recipe_id': recipe_id,
                       'connection_id_1': connection_ids[0],
                       'connection_id_2': connection_ids[1]
                       })


def open_link_1(basic_info):
    basic_info = json.loads(basic_info)
    print(f'open_link_1 basic_info: {basic_info}')
    try:
        url = generate_jwt(basic_info['user_id'], basic_info['connection_id_1'])
        html_str = HTML_STRING.replace("WORKATO_URL", url)

        Html_file = open(r"integrations/workato_iframe.html", "w")
        Html_file.write(html_str)
        Html_file.close()
        # file_url = 'file://' + os.path.realpath("workato_iframe.html")
        # webbrowser.open(file_url, new=2)
        webbrowser.open('http://127.0.0.1:8000/integrations/workato_iframe.html', new=2)
    except Exception as e:
        print(e)
    return "Opened the webpage!"


def open_link_2(basic_info):
    basic_info = json.loads(basic_info)
    try:
        url = generate_jwt(basic_info['user_id'], basic_info['connection_id_2'])
        # html_str = HTML_STRING.replace("WORKATO_URL", url)
        #
        # Html_file = open(r"integrations/workato_iframe.html", "w")
        # Html_file.write(html_str)
        # Html_file.close()
        # file_url = 'file://' + os.path.realpath("workato_iframe.html")
        # webbrowser.open(file_url, new=2)
        # webbrowser.open('http://127.0.0.1:8000/integrations/workato_iframe.html', new=2)
        webbrowser.open(url, new=2)
    except Exception as e:
        print(e)
    return "Opened the webpage!"


def open_recipe(basic_info):
    try:
        basic_info = json.loads(basic_info)
        update_receipt(basic_info['user_id'], basic_info['recipe_id'], str(basic_info['connection_id_1']),
                       str(basic_info['connection_id_2']))
        token = generate_token(basic_info['user_id'])
        webbrowser.open(
            f"https://app.workato.com/direct_link?workato_dl_path=/recipes/{basic_info['recipe_id']}-test-junyu-v5/edit?step=80726d21-4e96-43a9-8e47-46d0522c894a&workato_dl_token={token}",
            new=2)
    except Exception as e:
        print(e)


def list_all_connections(user_id):
    url = f'https://www.workato.com/api/managed_users/{user_id}/connections'
    headers = {
        'Authorization': ORIGINAL_TOKEN,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    print(response_json)

def update_recipe_code (user_id, recipe_id, code):
    url = f'https://www.workato.com/api/managed_users/{user_id}/recipes/{recipe_id}'
    headers = {
        'Authorization': ORIGINAL_TOKEN,
        'Content-Type': 'application/json'
    }
    data = {
        "recipe": {
            "code": code
        }
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))
    response_json = json.loads(response.text)
    print(response_json)


def list_all_receipts(user_id):
    url = f'https://www.workato.com/api/managed_users/{user_id}/recipes'
    headers = {
        'Authorization': ORIGINAL_TOKEN,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    print(response_json)
    return response_json['result'][0]['id']


def update_receipt(user_id, recipe_id, account_id_1, account_id_2):
    url = f'https://www.workato.com/api/managed_users/{user_id}/recipes/{recipe_id}'
    headers = {
        'Authorization': ORIGINAL_TOKEN,
        'Content-Type': 'application/json'
    }
    data = {
        "recipe": {
            "config": "[{\"keyword\":\"application\",\"name\":\"github\",\"provider\":\"github\", \"account_id\": \"" + account_id_1 + "\"}, {\"keyword\":\"application\",\"name\":\"gmail\",\"provider\":\"gmail\", \"account_id\": \"" + account_id_2 + "\"}]"
        }
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))
    response_json = json.loads(response.text)
    print(response_json)


def start_recipe(user_id, recipe_id):
    url = f'https://www.workato.com/api/managed_users/{user_id}/recipes/{recipe_id}/start'
    headers = {
        'Authorization': ORIGINAL_TOKEN,
        'Content-Type': 'application/json'
    }
    response = requests.put(url, headers=headers)
    response_json = json.loads(response.text)
    print(response_json)




def start_flow(basic_info):
    basic_info = json.loads(basic_info)
    start_recipe(basic_info['user_id'], basic_info['recipe_id'])

def get_recipe_auth(account_id, recipe_id):
    print(f'account_id: {account_id}, recipe_id: {recipe_id}')



with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Column():
        gr.Markdown("<h2><center>Workato Demo</center></h2>")

        with gr.Row():
            account_id = gr.Textbox(label="account id")
            recipe_id = gr.Textbox(label="recipe id")

        install_app_button = gr.Button("Get Auth")
        install_output = gr.Textbox()
        install_app_button.click(fn=get_recipe_auth, inputs=[account_id, recipe_id], outputs=[install_output])



demo.launch()
