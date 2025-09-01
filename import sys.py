import sys

import time

def printlyrics():
    lines = [
        ("chanthamode ennum neeyo entethalle sundari",0.08),#1
        ("anthivettamaarum neram swantham neeye kanmanee",0.09),#2
        ('chadapada thulumpedee karalinte kudathilu',0.06),#3
        ('aniyaay udane nirayan varane',0.05),#4
        ('hurry-burry enikkilla',0.04),#5
        ('athukkenne mathi mathi',0.05),#6
        ('nurapadarum',0.01),#7
        ('thiramadhuram nukaran',0.04),#8
        ('kadukittu varuthoru kadakkannumadichenne',0.06),#9
        ('kudukittu valikkalle midukkipenne',0.05),#10
        ('thirichittum marichittum gunichittum harichittum',0.06),#11
        ('kulippichu kedathalle kudukkapenne',0.04),#12
        
           
    ]
    delays_after_line = [0.5] * len(lines)
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)
        print()  # Move to the next line after each lyric line
        time.sleep(delays_after_line[i])

if __name__ == '__main__':
    printlyrics()