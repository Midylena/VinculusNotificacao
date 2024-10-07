import time
import API
import json
import Decryption
import math
from datetime import datetime

def update_token():
    token = json.loads(API.login())
    return token["token"]

def process_data(bearer_token):
    crip = json.loads(API.get(bearer_token))
    encryptedData = crip["encryptedData"]
    decrypted_data = Decryption.decrypt(encryptedData)

    data = json.loads(decrypted_data)
    x = data["acelX"]
    y = data["acelY"]
    z = data["acelZ"]

    x2 = x * x
    y2 = y * y
    z2 = z * z

    xyz2 = x2 + y2 + z2
    raiz = math.sqrt(xyz2)
    mod = abs(raiz)


    if mod >= 5:
        dataHora = datetime.now()
        dataHoraAtual = dataHora.strftime("%d-%m-%Y %H:%M:%S")
        API.post(1, dataHoraAtual, bearer_token)
        print(mod)
        time.sleep(2)
        API.post(0, dataHoraAtual, bearer_token)
        print("Queda Detectada!", dataHoraAtual)

def main():
    bearer_token = update_token() 
    intervalo_token = 90 * 60 

    proxima_atualizacao = time.time() + intervalo_token 

    while True:  # Loop infinito
        if time.time() >= proxima_atualizacao:
            print("Atualizando o token...")
            bearer_token = update_token()
            proxima_atualizacao = time.time() + intervalo_token 

        process_data(bearer_token)
        time.sleep(0.1) 

if __name__ == "__main__":
    main()
