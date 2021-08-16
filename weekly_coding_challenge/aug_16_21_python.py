#!/usr/bin/env python3

# Write a function that divides a phrase into word buckets, with each bucket containing 
# n or fewer characters. Only include full words inside each bucket.

# Examples
# bucketize("she sells sea shells by the sea", 10)
#   -> ["she sells", "sea shells", "by the sea"]

# bucketize("the mouse jumped over the cheese", 7)
#   -> ["the", "mouse", "jumped", "over", "the", "cheese"]

# bucketize("fairy dust coated the air", 20)
#   -> ["fairy dust coated", "the air"]

# bucketize("a b c d e", 2)
#   -> ["a", "b", "c", "d", "e"]

# NOTES 
#=======#
# Spaces count as one character.

# Trim beginning and end spaces for each word bucket (see final example).

# If buckets are too small to hold a single word, return an empty array: []

# The final goal isn't to return just the words with a length equal (or lower) to the 
# given n, but to return the entire given phrase bucketized (if possible). So, for the 
# specific case of "by" the only word with a proper length, the phrase can't be 
# bucketized, and the returned array has to be empty.

def bucketize(phrase, n):

    if len(phrase) > n:
        phrase = phrase.strip().split(' ')
        result = []        
        i = 0
        next = ''

        while i < len(phrase):
            if not next and len(phrase[i]) <= n:
                next += phrase[i]
                i += 1
            elif len(next + ' ') + len(phrase[i]) <= n:
                next += ' ' + phrase[i]
                i += 1
            elif next:
                result.append(next)
                next = ''
            else:
                i += 1
        result.append(next)
        return result

    return []

a = "  the mouse jumped over the cheese  " #7
b = "fairy dust coated the air" # 20
c = "a b c d e" # 2
d = "she sells sea shells by the sea" #10

print(bucketize(a,7))
print(bucketize(b,20))
print(bucketize(c,2))
print(bucketize(d,10))
print(bucketize(c,15))      
     

