import json
from collections import OrderedDict

def json_to_text(file_path):
    with open (file_path) as f:
        json_data = json.load(f)
    news_list = json_data["rss"]["channel"]["items"]
    all_words_list = []
    for item in news_list:
        for k, v in item.items():
            if k == "description":
                for word in v.lower().split():
                    if len(word) > 6:
                        all_words_list.append(word)
    return all_words_list

def word_counter(file_to_text_foo):
    all_words_list = file_to_text_foo
    uniques = []
    for word in all_words_list:
        if word not in uniques:
            uniques.append(word)

    counts = []
    for unique in uniques:
        count = 0
        for word in all_words_list:
            if word == unique:
                count += 1
        counts.append((count, unique))
    counts.sort()
    counts.reverse()

    for i in range(10):
        count, word = counts[i]
        print(f'Cлово "{word}" встречается {count} раз')


word_counter(json_to_text("newsafr.json"))
        




  

    
