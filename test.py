import requests
from config import *

res = requests.post(url_pre + '/train', json={"data":"no_train"})
if res.ok:
    print (res.json())
