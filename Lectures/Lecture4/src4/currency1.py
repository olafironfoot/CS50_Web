import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=c8e5f40142eb52c284c8ca05b4f2531b&format=1")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"]["USD"]
    print(f"1 EUR is equal to {rate} USD")

if __name__ == "__main__":
    main()
