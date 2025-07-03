import requests
URL = "http://127.0.0.1:8000/predict"
payload = {"features": [5.1, 3.5, 1.4, 0.2]}
if __name__ == "__main__":
    r = requests.post(URL, json=payload, timeout=10)
    r.raise_for_status()
    print("Response:", r.json())
if __name__ == "__main__":
    r = requests.post(URL, json=payload, timeout=10)
    r.raise_for_status()
    print("Response:", r.json())
