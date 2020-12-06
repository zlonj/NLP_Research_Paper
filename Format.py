# Stanford
def stanford_format(list_of_taggings):
    out_str = '\n'   
    length = len(list_of_taggings)
    for i in range(length):
        tag_tuple = list_of_taggings[i]
        if tag_tuple[1] == 'PERSON':
            out_str = out_str + tag_tuple[0] + '\tPER\n'
        elif tag_tuple[1] == 'ORGANIZATION':
            out_str = out_str + tag_tuple[0] + '\tORG\n'
        elif tag_tuple[1] == 'LOCATION':
            out_str = out_str + tag_tuple[0] + '\tLOC\n'
        else:
            out_str = out_str + tag_tuple[0] + '\tO\n'
    out_str = out_str + '\n'
    return out_str


# spaCy
def spaCy_format(list_of_taggings):
    out_str = '\n'
    length = len(list_of_taggings)
    for i in range(length):
        tag_tuple = list_of_taggings[i]
        if tag_tuple[1] == 'PERSON':
            out_str = out_str + tag_tuple[0] + '\tPER\n'
        elif tag_tuple[1] == 'ORG':
            out_str = out_str + tag_tuple[0] + '\tORG\n'
        elif tag_tuple[1] == 'LOC':
            out_str = out_str + tag_tuple[0] + '\tLOC\n'
        elif tag_tuple[1] == 'GPE':
            out_str = out_str + tag_tuple[0] + '\tLOC\n'
        else:
            out_str = out_str + tag_tuple[0] + '\tO\n'
    out_str = out_str + '\n'
    return out_str

# Flair
def flair_format(list_of_taggings):
    out_str = '\n'   
    length = len(list_of_taggings)
    for i in range(length):
        tag_tuple = list_of_taggings[i]
        if tag_tuple[1][2:]== 'PER':
            out_str = out_str + tag_tuple[0] + '\tPER\n'
        elif tag_tuple[1][2:] == 'ORG':
            out_str = out_str + tag_tuple[0] + '\tORG\n'
        elif tag_tuple[1][2:] == 'LOC':
            out_str = out_str + tag_tuple[0] + '\tLOC\n'
        else:
            out_str = out_str + tag_tuple[0] + '\tO\n'
    out_str = out_str + '\n'
    return out_str

# NLTK