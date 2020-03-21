import requests

def main():
    base = input("First Currency: ")
    other = input("Second Currency: ")
    res = requests.get("http://data.fixer.io/api/latest?access_key=c8e5f40142eb52c284c8ca05b4f2531b&format=1",
                       params={"base": base, "symbols": other})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()
