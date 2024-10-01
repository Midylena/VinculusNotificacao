import requests
import json

ip = "https://vinculusserver-ehbvfkakgyf4cjhs.eastus2-01.azurewebsites.net"

def login():
    url = ip+"/auth/login"

    headers = {}
    json = {
        "login": "milenaAlves",
	    "password":"123456789"
    }

    response = requests.post(url=url, json=json, headers=headers)
    response_data = str(response.json())
    string_response = response_data.replace("'","\"").replace("]","").replace("[","").replace("None", "null")   
    return string_response

def get(bearer_token):
    url = ip+"/historicoVinculus/milenaAlves/get"

    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    json = {}

    response = requests.get(url=url, json=json, headers=headers)
    response_data = str(response.json())
    string_response = response_data.replace("'","\"").replace("]","").replace("[","").replace("None", "null")   

    return string_response

def post(notificacao, dataHoraAtual, bearer_token):
    url = ip+"/historicoVinculus/milenaAlves/notificacaoPost"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    historico_data = {
        "notificacao" : notificacao,
        "dataHoraAtual": dataHoraAtual
    }

    response = requests.post(url=url, json=historico_data, headers=headers)

if __name__ == '__main__':
    token = json.loads(login())
    bearer_token = token["token"]
    get(bearer_token)
    post(1, bearer_token)