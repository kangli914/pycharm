import requests

DOMAIN_URL = "bolt.vena.io"

def generate_tokens(file, max=-1):
    count = 0

    try:
        with open(file, "r") as f:
            for line in f:
                name, password = line.strip().split(",")
                result = requests.post(f"https://{DOMAIN_URL}/login", auth=(name, password))
                
                result.raise_for_status()
                payload = result.json()

                count += 1
                # yield result
                yield payload["apiUser"] + "," + payload["apiKey"] + "\n" 
                
                if max != -1 and count >= max:
                    break

    except FileNotFoundError as e:
        print(f"File Error: {e}")
    except:
        print(f"Unexpected Error")

if __name__ == "__main__":
    tokens = generate_tokens("users.csv", 2)
    
    with open("response.txt", "w") as f:

        # https://stackoverflow.com/questions/12377473/python-write-versus-writelines-and-concatenated-strings
        # write() expects a single string.
        # writelines() expects an iterable. You can use a list, a tuple, or a generator.
        # for item in tokens:
        #     print(item)
        #     f.write(f"{item}")

        f.writelines(tokens)