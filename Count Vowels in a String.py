def Vowels(Letter):
    vowel = 0
    aa = "a,e,i,o,u"
    for i in Letter:
        if i in aa:
            vowel += 1
    print(vowel)
Letter = "HellO Ah"
Vowels(Letter.lower())
