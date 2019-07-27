import pandas as pd
import matplotlib.pyplot as plt

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of positive words to use
positive_words = []
with open("C:\\Users\\User\\Desktop\\positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("C:\\Users\\User\\Desktop\\negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(st):
    ll = list(st)
    for c in ll:
        if c in punctuation_chars:
            ll.remove(c)
    return "".join(ll)

def get_pos(k):
    pos=0
    words_list = k.split(" ")
    for word in words_list:
        if strip_punctuation(word) in positive_words:
            pos+=1
    return pos

def get_neg(k):
    neg=0
    words_list = k.split(" ")
    for word in words_list:
        if strip_punctuation(word) in positive_words:
            neg+= 1
    return neg

with open("C:\\Users\\User\\Desktop\\project_twitter_data.csv","r") as read_f:
    with open("C:\\Users\\User\\Desktop\\resulting_data.csv","w") as write_f:

        # write header
        row_string = '{},{},{},{},{}'.format("Number of Retweets", " Number of Replies"," Positive Score"," Negative Score"," Net Score")
        write_f.write(row_string)
        write_f.write('\n')

        lines = read_f.readlines()
        for line in lines[1:]:
            line_list= line.split(',')
            ll = line_list[2].split('\n')
            p = get_pos(line_list[0])
            n = get_neg(line_list[0])
            s = p - n
            #print(line_list[1], ll[0], p, n, s)
            row_string = '{},{},{},{},{}'.format(line_list[1], ll[0], p, n, s)
            write_f.write(row_string)
            write_f.write('\n')

df  = pd.read_csv("C:\\Users\\User\\Desktop\\resulting_data.csv")
print(df)
