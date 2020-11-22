#counting the number of  repeated letter in a string of words
#import module :collections
#use of counter module

from collections import Counter
word=input("Please enter a sentence: ").strip().replace(" ", "") 
c=Counter(word).most_common(1)
print(c)



