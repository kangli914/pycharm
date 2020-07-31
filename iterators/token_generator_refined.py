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


class TokenFileGenerator():
    """Generator the tokens"""

    # constants
    READER_NAME = "users.csv"
    WRITEER_NAME = "token.csv"

    # class variables
    count = 0
    max_count = 0

    def __init__(self):
        pass

    def __str__(self):
        return f"Token file generator"

    @classmethod
    def generate_tokens(cls):
        with open(cls.READER_NAME) as f_reader:
            for line in f_reader:
                name, password = line.strip().split(",")
                user = User(name, password)
                cls.count += 1
                yield f"{user.name},{user.password},{user.get_token()}" + "\n"
                if cls.max_count and cls.get_token_count() >= cls.max_count:
                    break

    @classmethod
    def write_tokens(cls):
        with open(cls.WRITEER_NAME, "w") as f_writer:
            user_token = cls.generate_tokens()
            f_writer.writelines(user_token)

    @classmethod
    def get_token_count(cls):
        return cls.count

    @classmethod
    def set_max_token(cls, max):
        cls.max_count = max

if __name__ == "__main__":
    TokenFileGenerator.set_max_token(4)
    TokenFileGenerator.write_tokens()