#import codecs to deal with utf8 (what text in mac uses)
#This is using a Generator expressions
#The goal of this was to import a tweet, count capital/lowercase, repetition of words and letters
import codecs
import re
import collections 
from collections import Counter
totalcap = 0
totallow = 0
totalwords = 0

with codecs.open('finishedEnglishUTF8.txt','r',encoding='utf8') as f:
    for line in f:
        text = line[9:]
        textls = text.split()
        reslst= [word for word in text.split() if word.startswith('@')]
        new_list = [word for word in textls if word not in reslst]
        str1 = ' '.join(new_list)
        capcount = sum(1 for x in str1 if x.isupper())
        lowcount = sum(1 for c in str1 if c.islower())
        totalcap = totalcap+capcount
        totallow = totallow+lowcount
        c = collections.Counter(new_list)

        print("Entire Tweet:")
        print(new_list)
        print("Repeated Letters:")
        print([match[0] for match in re.findall(r'((\w)\2)', str1)])
        
        for letter, count in c.most_common(5):
            if count > 1:
                print('Most common:')
                print((letter, count))
                totalwords = totalwords +1
        str1=str1.replace(' ','')
        print("----")
        
    print("Total Capitals:", totalcap)
    print("Total Lowercase:", totallow)
    print("Repeated Words:", totalwords)
