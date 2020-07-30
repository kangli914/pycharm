import base64
import requests


class User():
    """User class to have exchange the token"""

    # constants
    DOMAIN_URL = "bolt.vena.io"

    def __init__(self, name, password, token=""):
        self.name = name
        self.password = password
        self.token = token

    def __str__(self):
        return f"name: {self.name}, password: {self.password}, token: {self.token}"

    def login(self):
        result = requests.post(f"https://{User.DOMAIN_URL}/login", auth=(self.name, self.password))
        result.raise_for_status()
        payload = result.json()
        return payload["apiUser"], payload["apiKey"]

    def get_token(self):
        api_user, api_key = self.login()
        self.token = User.encode_string(f"{api_user}:{api_key}")
        return self.token

    @staticmethod
    def encode_string(auth_str):
        return base64.b64encode((auth_str).encode()).decode()


def token_generator(file):
    with open(file) as f:
        for line in f:
            name, password = line.strip().split(",")
            user = User(name, password)
            yield f"{user.name},{user.password},{user.get_token()}" + "\n"


if __name__ == "__main__":
    with open("token.csv", "a") as f:
        line = token_generator("users.csv")
        f.writelines(line)
