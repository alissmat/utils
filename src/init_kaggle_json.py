
import os, json


def init_on_kaggle(username, api_key):
    """ Adapted from https://www.kaggle.com/code/donkeys/kaggle-python-api"""
    KAGGLE_CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.kaggle')
    os.makedirs(KAGGLE_CONFIG_DIR, exist_ok = True)
    api_dict = {"username":username, "key":api_key}
    with open(fr"{KAGGLE_CONFIG_DIR}\kaggle.json", "w", encoding='utf-8') as f: #
        json.dump(api_dict, f)
