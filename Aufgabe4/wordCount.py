import re
from collections import Counter

# Tally occurrences of words in a list
cnt = Counter()
with open("Aufgabe4\E.T.txt", "r") as file:
    words = file.read()
    words = words.replace("\n", '')
    words = words.split(' ')
    for word in words:
        cnt[word] += 1
    with open("output.txt", "w+") as f:
        text = ""
        for key in cnt.keys():
            text += "%s,%s\n" % (key, cnt[key])
        print(text)
        f.write(text)