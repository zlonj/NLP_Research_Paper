import spacy
import corpus_transform
import output_format
import sys

from spacy.tokens import Doc


corpus = sys.argv[1]
source = corpus_transform.transform(corpus)
tagger = spacy.load("en_core_web_sm")

def custom_tokenizer(text):
    return Doc(tagger.vocab, text.split(' '))

tagger.tokenizer = custom_tokenizer

# target file for write
f = open("spacy-output.txt", "w")
buf = '\n'

for sentence in source:
    doc = tagger(sentence)
    lst = []
    for word in doc:
        lst.append([word.text, word.ent_type_])
    model_result = output_format.spacy_format(lst)
    buf += model_result

f.write(buf)
f.close()

    
