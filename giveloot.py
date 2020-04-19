#!/usr/bin/env
import random
import string

f = open('loot.txt', 'r')
loot = f.readlines()
f.close()

print("You have found " + random.choice(loot).rstrip('\n'))