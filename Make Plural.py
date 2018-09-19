import praw
import config
import time
import os
import random
def get_verbs():
	with open('/Users/ryan/Desktop/test/Nouns.txt', "r") as f:
			verbs = f.read()
			verbs = verbs.split("\n")
			verbs = filter(None, verbs)
	return verbs

verbs=get_verbs()
for x in range(0,len(verbs)):
		verbs[x]=verbs[x]+"s"
		print verbs[x]
with open ("/Users/ryan/Desktop/test/test.txt", "a") as f:
	for x in range(0,len(verbs)):
		f.write(verbs[x]+"\n")
