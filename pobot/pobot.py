import random
from nltk.tokenize import SyllableTokenizer


def run(words):
    # parts = [decompose(x, stub=4) for x in words]
    SSP = SyllableTokenizer()
    parts = [SSP.tokenize(x) for x in words]
    portmanteau = stitch("", parts)
    return portmanteau


def decompose(word, stub=3):
    if len(word) < stub:
        return [word]
    else:
        return [word[x:x+stub] for x in range(len(word) - stub + 1)]


def stitch(word, parts):
    if word == "":
        part, parts = get_part(parts)
        word += part[0]
    while parts:
        part, parts = get_part(parts)
        # TODO: put in some effort and don't lazily just select a random word
        word += random.choice(part)
    return word


def get_part(parts):
    length = len(parts)
    random_index = random.randrange(length)
    part = parts[random_index]
    less_parts = [x for x in parts if x is not part]
    return part, less_parts
