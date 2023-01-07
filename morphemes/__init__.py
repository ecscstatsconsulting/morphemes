from .utilities.morpheme_database import MorphemeDatabase
from appdata import AppDataPaths

class Morphemes:

    def __init__(self, data_path=None):
        if data_path is None:
            app_paths = AppDataPaths('morphemes')
            data_path = app_paths.app_data_path
        self.db = MorphemeDatabase(data_path)

    def count(self, word):
        morph_db_results = self.db.lookup(word)
        output = 0
        if morph_db_results is not None and len(morph_db_results) > 0:
            morph_db_result = morph_db_results[0]
            output = morph_db_result["Nmorph"]
        return output

    def __parse_segmentation(self, segmentation):
        output = None
        if segmentation is not None:
            in_segment = False
            in_root = False
            in_add_on = False
            current = ''
            fragments = []
            cur = None
            for c in segmentation:
                if c == "{":
                    cur = {
                        "children": [],
                        "type": "free"
                    }
                    in_segment = True
                if c == "(":
                    in_root = True
                if c == ">" and in_add_on is False:
                    in_add_on = True
                elif c == ">":
                    if cur is not None:
                        cur["children"].append({
                            "text": current,
                            "type": "bound"
                        })
                    else:
                        fragments.append({
                            "text": current,
                            "type": "bound"
                        })
                    current = ""
                    in_add_on = False
                if c == "}":
                    current = ""
                    fragments.append(cur)
                    cur = None
                    in_segment = False
                if c == ")":
                    if cur is not None:
                        cur["children"].append({
                            "text": current,
                            "type": "root"
                        })
                    current = ""
                    in_root = False
                if c != "(" and c != ")" and c != "{" and c != "}" and c != ">":
                    current = current + c

            output = fragments
        return output

    def parse(self, word):
        morph_db_results = self.db.lookup(word)
        output = {}
        if morph_db_results is not None and len(morph_db_results) > 0:
            morph_db_result = morph_db_results[0]
            output["status"] = "FOUND_IN_DATABASE"
            output["word"] = word
            output["morpheme_count"] = morph_db_result["Nmorph"]
            segmentation = morph_db_result["MorphoLexSegm"]
            fragments = self.__parse_segmentation(segmentation)
            if fragments is not None:
                output["tree"] = fragments
        else:
            output["status"] = "NOT_FOUND"
            output["word"] = word
            #not found words, ie names of people/places should be counted as 1 morpheme
            output["morpheme_count"] = 1
        return output
