from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    """Аргумент не может быть бошльше 5"""
    joke_list = []
    include_jokes = []
    if num <= 5:
        while num > 0:
            choose_nouns = choice(list(filter((lambda x: x not in include_jokes), nouns)))
            choose_adverbs = choice(list(filter((lambda x: x not in include_jokes), adverbs)))
            choose_adjectives = choice(list(filter((lambda x: x not in include_jokes), adjectives)))
            include_jokes.append(choose_nouns)
            include_jokes.append(choose_adverbs)
            include_jokes.append(choose_adjectives)
            j = str(' '.join((choose_nouns,  choose_adverbs,  choose_adjectives)))
            joke_list.append(j)
            num -= 1
        return joke_list
    return None


print(get_jokes(5))
