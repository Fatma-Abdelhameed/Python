import sys
from collections import Counter
def find_common_words(file):
    file_text = open(file, 'r').read() 
    common_words = Counter(file_text.split()).most_common(20)
    return list(map(lambda w: w[0], common_words))

def write_common_words_in_file(common_words):
    file = open('common_words.txt', 'w')
    for word in common_words:
        file.write(word)

write_common_words_in_file(find_common_words(sys.argv[1]))