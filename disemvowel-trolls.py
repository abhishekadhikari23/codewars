'''
    #2019-12-26

                            https://www.codewars.com/kata/disemvowel-trolls/

    Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
'''

def disemvowel(string):
    s = ''
    for i in range(0,len(string)):
        if(string[i] not in 'aeiouAEIOU'):
            s = s + string[i]
    return s

st = input()
print(disemvowel(st))