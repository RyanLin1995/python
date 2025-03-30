"""
实现额外的方法
"""
import re

def tokenize(text):
    # filters = '!"#$%&()*+,-./:; ?@[\\]^_`{|}~\t\n'
    filters = [
        "!", '"', "#", "$", "%", "&", "\(", "\)", "\*", "\+", ",", "-", "\.", "/", ":", ";", "<", "=", ">", "\?", "@", "\[", "\\", "\]", "^", "_", "`", "\{", "\|", "\}", "~", "\t", "\n", "\x97", "\x96", "”", "“",
    ]
    text = re.sub("<.*?>", " ", text, flags=re.S)
    text = re.sub("|".join(filters), " ", text, flags=re.S)
    return [i.strip().lower() for i in text.split()]

