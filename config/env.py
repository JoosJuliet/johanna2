import json
import os
import sys

config_path = '.'
if sys.path[0]:
    config_path = sys.path[0]

# Load Config.json
env = json.load(open('./config.json' % config_path))
with open('./config.json') as config:
    env = json.load(config.read())

def get_env(setting, env=env):
    try:
        return env[setting]
    except KeyError:
        error_msg = f'Set the {setting} environment variable'


SECRET_KEY = get_env("SECRET_KEY")