import requests

URL_shortening_service="https://nvg.li/php/a/shorturl.php?url="
URL=input("What URL would you like to make shorten?")

query=r.post(URL_shortening_service+URL)

print(query.text)