import requests
#no such isbns? 0441172717%2C0141439602?
# res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "sq1OpyVMNF4302OEUIu7CA", "isbns": "0441172717%2C0141439602"})
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "sq1OpyVMNF4302OEUIu7CA", "isbns": "9781632168146"})
print(res.json())
