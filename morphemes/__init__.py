from .utilities.morpheme_database import MorphemeDatabase
from appdata import AppDataPaths
from morphemes.config import Config, Settings
from enum import Enum


class MorphoLEXSeperatorType(Enum):
    PREFIX = "<"
    BOUND = ">"
    ROOT_OPEN = "("
    ROOT_CLOSE = ")"
    SEGMENT_OPEN = "{"
    SEGMENT_CLOSE = "}"

    @classmethod
    def contains(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def token_name(cls, value):
        if value == cls.PREFIX.value:
            return "prefix"
        elif value == cls.BOUND.value:
            return "bound"
        elif value == cls.ROOT_CLOSE.value:
            return "root"
        elif value == cls.ROOT_OPEN.value:
            return "root"
        elif value == cls.SEGMENT_CLOSE.value:
            return "segment"
        elif value == cls.SEGMENT_OPEN.value:
            return "segment"
        return "undefined"

class Morphemes:

    def __init__(self, data_path=None):
        if data_path is not None:
            Config.set(Settings.data_path, data_path)
        self.db = MorphemeDatabase(Config.get(Settings.data_path))

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
                if c == MorphoLEXSeperatorType.SEGMENT_OPEN.value:
                    cur = {
                        "children": [],
                        "type": "free"
                    }
                    in_segment = True
                if c == MorphoLEXSeperatorType.ROOT_OPEN.value:
                    in_root = True
                if (c == MorphoLEXSeperatorType.PREFIX.value or c == MorphoLEXSeperatorType.BOUND.value) and in_add_on is False:
                    in_add_on = True
                elif c == MorphoLEXSeperatorType.PREFIX.value or c == MorphoLEXSeperatorType.BOUND.value:
                    if cur is not None:
                        cur["children"].append({
                            "text": current,
                            "type": MorphoLEXSeperatorType.token_name(c)
                        })
                    else:
                        fragments.append({
                            "text": current,
                            "type": MorphoLEXSeperatorType.token_name(c)
                        })
                    current = ""
                    in_add_on = False
                if c == MorphoLEXSeperatorType.SEGMENT_CLOSE.value:
                    current = ""
                    fragments.append(cur)
                    cur = None
                    in_segment = False
                if c == MorphoLEXSeperatorType.ROOT_CLOSE.value:
                    if cur is not None:
                        cur["children"].append({
                            "text": current,
                            "type": "root"
                        })
                    current = ""
                    in_root = False
                if not MorphoLEXSeperatorType.contains(c):
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
