from pykis import *
import json

def open_json(path):
    with open(path) as f:
        config = json.load(f)
        TOKEN_id = config['id']
        AppKey = config['secretkey']
        Account = config['account']
        virtual = config['virtual'] # False

def save_json(your_id, your_appkey, your_secretkey, your_account, your_virtual, path_name):
    auth = KisAuth(
        id=your_id,
        appkey=your_appkey,
        secretkey=your_secretkey,
        account=your_account,
        virtual=your_virtual,
    )
    auth.save(path_name)