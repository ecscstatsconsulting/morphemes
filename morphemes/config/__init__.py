import os.path
from enum import Enum
import json
from appdata import AppDataPaths
from tabulate import tabulate

class Settings(str, Enum):
    data_path = "data_path"


class Config:
    __default_conf = {
        "data_path": None
    }

    __conf = __default_conf

    __setters = [
        "data_path"
    ]

    @staticmethod
    def list():
        Config.load()
        my_list = [["Key", "Value"]]
        for key in Config.__conf:
            my_list.append([key, Config.__conf[key]])
        print(tabulate(my_list, tablefmt="grid"))

    @staticmethod
    def save():
        data_path = Config.get(Settings.data_path) + '/config.json'
        with open(data_path, "w") as f:
            json.dump(Config.__conf, f, indent=2)

    @staticmethod
    def load():
        data_path = Config.get(Settings.data_path) + "/config.json"
        if os.path.exists(data_path):
            with open(data_path, "r") as f:
                Config.__conf = json.load(f)

    @staticmethod
    def clear():
        data_path = Config.get(Settings.data_path) + "/config.json"
        if os.path.exists(data_path):
            os.remove(data_path)
        Config.__conf = Config.__default_conf

    @staticmethod
    def get(name: Settings):
        if name == Settings.data_path and Config.__conf[name] is None:
            app_paths = AppDataPaths('morphemes')
            Config.__conf[name] = app_paths.app_data_path
            Config.save()
        return Config.__conf[name]

    @staticmethod
    def set(name: Settings, value):
        if name in Config.__setters:
            Config.__conf[name] = value
            Config.save()
        else:
            raise NameError("Name not accepted in set() method")