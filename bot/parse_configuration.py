import os, configparser

class Parse:
    config = configparser.ConfigParser()
    config.read('bot/configuration.ini', encoding = 'utf_8_sig')

def get_value_by_key(key, value):
    return Parse.config.get(key, value).replace('"', '')

def get_values_by_section(key) -> dict:
    return dict(Parse.config.items(key)).values()