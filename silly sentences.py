
#silly stuff
#this is made by geat
#one sentence for one run

name = ["David", "Andrew", "James",  "Robert", "Jhon", "William"]
verb = ["works", "buys", "rides", "kicks", "fires", "destroys",]
noun = ["lion", "bicycle", "plane", "car", "worker", "helicopter"]
from random import randint
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked


        
     
    

print(pick(name), pick(verb), "a", pick(noun), end=".")
