import requests

response=requests.get("https://www.facebook.com")
print(response.text)


# import requests

# query=input("enter news type:")
# url=f"https://newsapi.org/v2/everything?q={query}&from=2024-04-06&sortBy=publishedAt&apiKey=68ffc52d8d914dba93880a80f68601d3"
# r=requests.get(url)
# print(r.text)