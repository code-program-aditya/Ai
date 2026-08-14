vowal={'a','e','i','o','u'}
word=input("enter the word")
vowelinword=set(word).intersection(vowal)
print("vowels in the word are:",vowelinword)