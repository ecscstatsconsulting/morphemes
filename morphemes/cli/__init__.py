import click
import re
from morphemes.config import Config, Settings
from morphemes import Morphemes
import json

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """morphemes cli"""
    pass

@main.group("config")
def config():
    """config settings for the morphemes package"""

@config.command("list")
def config_list():
    """list all config settings for the morphemes package"""
    Config.list()


@main.command("word-tree")
@click.argument("input_word")
def word(input_word):
    m = Morphemes()
    d = m.parse(input_word)
    print(json.dumps(d, sort_keys=True, indent=4))


@main.command("word-count")
@click.argument("input_word")
def word_count(input_word):
    m = Morphemes()
    c = m.count(input_word)
    print(c)


@main.command("count")
@click.argument("filename", type=click.Path(exists=True))
def count(filename):
    print(filename)
    m = Morphemes()
    full_text = ""
    with open(filename) as f:
        lines = f.readlines()
        full_text = " ".join(lines)
    broken_text = full_text.split(" ")
    words = []
    count = 0
    for part in broken_text:
        parse = re.sub(r"[^\w']+", "", part, flags=re.UNICODE)
        if len(parse) > 0:
            words.append(parse.lower())
            count += m.count(parse.lower())
    print(count)
