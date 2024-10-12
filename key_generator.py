import secrets

def generate_secret_key():
    return secrets.token_hex(32)

print("Secret Key:", generate_secret_key())