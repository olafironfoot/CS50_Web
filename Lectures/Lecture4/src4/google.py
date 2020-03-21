import requests

def main():
    # res = requests.get("https://www.google.com/")
    res = requests.get("https://plan.toggl.com/#timeline/204958/teams/191023?zoom=month")
    print(res.text)

if __name__ == "__main__":
    main()
