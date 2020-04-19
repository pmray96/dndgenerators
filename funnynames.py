#!/usr/bin/env
import random
import string

f = open('characternames.txt', 'r')
names = f.readlines()
f.close()


f = open('characteradjectives.txt', 'r')
adjectives = f.readlines()
f.close()

print(random.choice(names).rstrip('\n') + " the " + random.choice(adjectives).rstrip('\n'))