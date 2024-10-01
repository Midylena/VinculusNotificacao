from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Util.Padding import unpad
import API
import json

FIXED_KEY = "12345678901234567890123456789012"

def decrypt(encrypted_data):
    key_bytes = FIXED_KEY.encode('utf-8')
    
    cipher = AES.new(key_bytes, AES.MODE_ECB)

    encrypted_bytes = b64decode(encrypted_data)

    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    
    try:
        decrypted_data = unpad(decrypted_bytes, AES.block_size, style='pkcs7')
    except ValueError:
        raise ValueError("Invalid padding")
    
    return decrypted_data.decode('utf-8')

if __name__ == '__main__':
    token = json.loads(API.login())
    bearer_token = token["token"]

    get = json.loads(API.get(bearer_token))
    encryptedData = get["encryptedData"]
    encrypted_data_base64 = encryptedData
    
    decrypted_data = decrypt(encrypted_data_base64)
    print(decrypted_data)
