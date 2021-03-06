import requests


def get_def(word, index):
    """
    Returns the definitions of a given word using https://api.dictionaryapi.dev

    The index parameter is used to choose which definition to return
    """

    responce = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    print(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    meaningList = []

    for Homonym in range(len(responce.json())):
        for definition in responce.json()[Homonym]["meanings"][0]["definitions"]:
            meaningList += [definition["definition"]]

    return meaningList[index]


def get_def_num(word):
    """
    Returns the number of definitions a word has
    """
    
    responce = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    print(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    num = 0

    for Homonym in range(len(responce.json())):
        for definition in responce.json()[Homonym]["meanings"][0]["definitions"]:
            num += 1

    return num
