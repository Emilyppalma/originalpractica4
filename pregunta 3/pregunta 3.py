import requests
url='https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGVycml0b3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60'
response=requests.get(url)

with open('perrito.jpg','wb') as f:
    f.write(response.content)
    pass