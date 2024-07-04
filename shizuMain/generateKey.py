from cryptography.fernet import Fernet 
import os
import json

# -=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-

def generate_key():

    obj = {
        "backLog": []
    }

    key = Fernet.generate_key()
    script_dir = os.path.dirname(os.path.abspath(__file__))  
    key_path = os.path.join(script_dir, 'backupPass.json')

    print(key_path)
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
    print(key)

# -=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-


if __name__ == ('__main__'):
    generate_key()