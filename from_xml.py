import xml.etree.cElementTree as ET

def xml_to_text(file_path):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_path, parser)
    root = tree.getroot()

    description_list = root.findall("channel/item/description")
    all_words_list = []
    for description in description_list:
        for word in description.text.lower().split():
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



word_counter(xml_to_text("newsafr.xml"))



