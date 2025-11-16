import requests

def fetch(url):
    r = requests.get(url)
    with open("api_output.json", "w") as f:
        f.write(r.text)
    print("Saved: api_output.json")
