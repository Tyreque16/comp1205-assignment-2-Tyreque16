import random

def englishToSpongecase(text):
    #
    spongecase_list = []``
    
    
    for char in text:

        if random.choice([True, False]):
            spongecase_list.append(char.upper())
        else:
            spongecase_list.append(char.lower())

    spongecase_text = ''.join(spongecase_list)
    return spongecase_text
