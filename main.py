import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    temp = get_close_matches(word, data, cutoff=0.8)

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(temp) > 0:
        yes_or_no = input(f"Did you mean {temp[0]}? Type Y for yes, N for no.")
        if yes_or_no == "Y":
            return data[temp[0]]
        elif yes_or_no == "N":
            return ["Word does not exist. Please double check it."]
        else:
            return ["Program did not understand your entry."]
    else:
        return ["Word does not exist. Please double check it."]


while True:
    word = input("Enter the word:")

    for item in translate(word.lower()):
        print(item)
