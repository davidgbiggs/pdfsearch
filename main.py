import os
import sys
from tika import parser

def find_text(term, filename):
    raw = parser.from_file("./pdfs/" + filename)

    text = raw['content']
    return term in text

terms = sys.argv[1:]
search_term = " ".join(terms)

for filename in os.listdir('pdfs'):
    f = os.path.join('pdfs', filename)
    if os.path.isfile(f):
        if find_text(search_term, filename):
            print(filename)