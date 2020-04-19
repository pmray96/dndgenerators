#!/usr/bin/env
import random
import string

f = open('names.txt', 'r')
names = f.readlines()
f.close()

f = open('taverns.txt', 'r')
taverns = f.readlines()
f.close()

f = open('adjectives.txt', 'r')
adjectives = f.readlines()
f.close()

print(random.choice(adjectives).rstrip('\n') + " " + random.choice(names).rstrip('\n') + " " + random.choice(taverns).rstrip('\n'))