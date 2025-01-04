from __future__ import print_function

import plac
from spacy.attrs import ORTH
from spacy.en import English
import io

def main(text_loc):
    with io.open(text_loc, 'r', encoding='utf8') as file_:
       text = file_.read()
    nlp = English()
    doc = nlp(text)

    counts = doc.count_by(ORTH)
    print(len(counts))
    for word_id, count in sorted(counts.items(), reverse=True, key=lambda item: item[1]):
        print(count, nlp.vocab.strings[word_id])

if __name__ == '__main__':
    plac.call(main)

