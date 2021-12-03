"""
Very Basic Passphrase Generator - Python Version
"""
import random

with open('list.txt', 'r') as file:
    phrase_list=file.read().replace('\n',',')

numerics='0123456789'

elements=phrase_list.split(',')

passphrase=""

def gen_phrase(word_num):
    count=0
    phrases=""
    while count < word_num:
        selector=random.randint(0, len(elements)-1)
        #print(elements[selector])
        count+=1
        phrases=phrases+elements[selector]+"-"
    return print(f"{phrases[:-1]}")

while True:
    try:
        words=int(input("Wie viele Wörter möchtest du benutzen? "))
        break
    except:
        print("Keine Zahl. Bitte gib eine Zahl ein: ")
gen_phrase(words)


