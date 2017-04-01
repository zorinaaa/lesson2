import re

with open('referat.txt', 'r', encoding = 'utf-8') as f:
    #content = f.read()
    #print(content)

    words = 0
    for line in f:
        line = line.replace('\n', '')
        
        count_filter = len(line.split(' '))
        print(count_filter)

        for count in count_filter:
            if count!=' ':
                words += 1
        print(words)