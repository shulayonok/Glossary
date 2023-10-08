glossary = {}


def read():
    with open("glossary.txt", "r", encoding="utf8") as file:
        for line in file:
            if line != "\n":
                splitting = line.split(" - ")
                splitting[1] = splitting[1].replace("\n", "")
                glossary[splitting[0].lower()] = splitting[1]


def search(key):
    if key in glossary:
        return glossary[key]
    else:
        return "Такого элемента нет в глоссарии"
