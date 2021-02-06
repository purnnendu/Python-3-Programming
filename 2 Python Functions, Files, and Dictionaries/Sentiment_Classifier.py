#!/usr/bin/env python3

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    for i in punctuation_chars:
        if i in s:
            s = s.replace(i, "")
    return s

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(s):
    count = 0
    for i in s.split():
        i = strip_punctuation(i)
        if i.lower() in positive_words:
            count += 1
    return count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(s):
    count = 0
    for i in s.split():
        i = strip_punctuation(i)
        if i.lower() in negative_words:
            count += 1
    return count

f = open("project_twitter_data.csv", "r")
content = f.readlines()
result = [["Number of Retweets, ", "Number of Replies, ", "Positive Score, ", "Negative Score, ", "Net Score\n"]]
for i in content[1:]:
    for j in i.split(","):
        t, rt, r = j
        res = ["{}, ".format(rt), "{}, ".format(r.strip()), "{}, ".format(get_pos(t)), "{}, ".format(get_neg(t)), "{}\n".format(get_pos(t) - get_neg(t))]
        result.append(res)
f.close()

g = open("resulting_data.csv", "w")
count = 1
for i in result:
    for j in i:
        g.write(j)
g.close()
