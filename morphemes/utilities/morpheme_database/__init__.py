import json
import os
import re
import pandas as pd
import requests
from tinydb import TinyDB, where

import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

default_morpholex_git_location = "https://github.com/hugomailhot/MorphoLex-en/raw/master/MorphoLEX_en.xlsx"


def process_df(df, db):
    table = db.table("WORDS")
    rows = json.loads(df.reset_index().to_json(orient='records'))
    table.insert_multiple(rows)


class MorphemeDatabase:
    def __init__(self, data_path):
        self.data_path = data_path

    def get_excel_dictionary_path(self):
        filename = self.data_path + "/MorphoLEX_en.xlsx"
        return filename

    def get_db_path(self):
        filename = self.data_path + "/db.json"
        return filename

    def create_db(self):
        path = self.get_db_path()
        if os.path.exists(path):
            os.remove(path)
        db = TinyDB(path)
        return db

    def load_db(self):
        path = self.get_db_path()
        if not os.path.exists(path):
            self.refresh()
        db = TinyDB(path)
        return db

    def get_excel(self):
        path = self.get_excel_dictionary_path()
        if os.path.exists(path):
            return pd.ExcelFile(self.get_excel_dictionary_path())
        else:
            self.download_morpholex_dictionary()
            return pd.ExcelFile(self.get_excel_dictionary_path())

    def download_morpholex_dictionary(self, url=default_morpholex_git_location):
        r = requests.get(url)
        f = open(self.get_excel_dictionary_path(), "wb")
        f.write(r.content)

    def refresh(self):
        print("---- Downloading Morpheme Database ----")
        db = self.create_db()
        xl = self.get_excel()
        sheet_names = xl.sheet_names
        for sheet_name in sheet_names:
            if re.match("^[0-9]-[0-9]-[0-9]$", sheet_name):
                df = xl.parse(sheet_name)
                process_df(df, db)

    def lookup(self, word):
        db = self.load_db()
        tbl = db.table("WORDS")
        result = tbl.search(where("Word").matches("^" + word + "$", flags=re.IGNORECASE))
        return result
