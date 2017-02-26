import shutil

import requests

url = 'https://media.guim.co.uk/43b232940616ef539e80483d5e3cfbfdea0ab29c/0_346_5407_3244/500.jpg'
response = requests.get(url, stream=True)
with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
print('Success')
del response