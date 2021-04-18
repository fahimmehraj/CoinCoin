import giphy_client
from giphy_client.rest import ApiException
import time
import random

def gif(q):
    api_key = ""
    api_instance = giphy_client.DefaultApi()
    api_response = api_instance.gifs_search_get(api_key, q, limit=100, rating="g")
    lst = list(api_response.data)
    o=[]
    for i in lst:
        o.append(i.embed_url)
    return o

t=[]

items=["among us", "star wars", "matrix", "lord of the rings"]
for i in items:
    for item in gif(i):
        t.append(item)
while True:
    time.sleep(60)
    print(random.choice(t))
