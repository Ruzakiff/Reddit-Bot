import praw
import config
import time
import os
import random
active="showerthoughts+test"

def bot_login():
	print "Loggin in..."
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "SAB V1.7")
	print "Logged in!"
	return r
def run_bot(r,commentsused):
	for comment in r.subreddit(active).stream.comments():
		print comment.author
		if comment.id not in commentsused:
    			print "Processing comment: " + comment.id
    			with open ("/Users/ryan/Desktop/test/commentsused.txt", "a") as f:
					f.write(comment.id+"\n")
			toexplain=[]
			message=""
			usedwords=""
			temptemp=comment.body.replace("\n\n"," ")
			tempstring=temptemp.split(" ")
			for compare in tempstring:
				for target in data:
					if target.upper()==compare.upper():
						toexplain.append(target.upper())
			if len(toexplain)>=1 and comment.author!="Shitty_acronym_bot":
				for search in data:
						while toexplain.count(search.upper())>1:
							toexplain.remove(search.upper())
				for x in range(0,len(toexplain)):
					long=False
					avan=nouns[:]
					avav=verbs[:]
					avaa=adjs[:]
					avay=advs[:]
					random.shuffle(avan)
					random.shuffle(avav)
					random.shuffle(avaa)
					random.shuffle(avay)
					temp=""
					usedwords+=toexplain[x]+","
					if len(toexplain[x])==2:
						for j in range(0,(len(avav))):
							if(avav[j][0].upper()==toexplain[x][0]):
								temp+=avav[j][0].upper()+avav[j][1:]+" "
								avav.remove(avav[j])
								break
						for j in range(0,(len(avan))):
							if(avan[j][0].upper()==toexplain[x][1]):
								temp+=avan[j][0].upper()+avan[j][1:]+" "
								avan.remove(avan[j])
								break
						print temp
					elif len(toexplain[x])==3:
						for j in range(0,(len(avav))):
							if(avav[j][0].upper()==toexplain[x][0]):
								temp+=avav[j][0].upper()+avav[j][1:]+" "
								avav.remove(avav[j])
								break
						for j in range(0,(len(avaa))):
							if(avaa[j][0].upper()==toexplain[x][1]):
								temp+=avaa[j][0].upper()+avaa[j][1:]+" "
								avaa.remove(avaa[j])
								break
						for j in range(0,(len(avan))):
							if(avan[j][0].upper()==toexplain[x][2]):
								temp+=avan[j][0].upper()+avan[j][1:]+" "
								avan.remove(avan[j])
								break
						print "got"
					elif len(toexplain[x])==4:
						for j in range(0,(len(avan))):
							if(avan[j][0].upper()==toexplain[x][0]):
								temp+=avan[j][0].upper()+avan[j][1:]+" "
								avan.remove(avan[j])
								break
						for j in range(0,(len(avav))):
							if(avav[j][0].upper()==toexplain[x][1]):
								temp+=avav[j][0].upper()+avav[j][1:]+" "
								avav.remove(avav[j])
								break
						for j in range(0,(len(avaa))):
							if(avaa[j][0].upper()==toexplain[x][2]):
								temp+=avaa[j][0].upper()+avaa[j][1:]+" "
								avaa.remove(avaa[j])
								break
						for j in range(0,(len(avan))):
							if(avan[j][0].upper()==toexplain[x][3]):
								temp+=avan[j][0].upper()+avan[j][1:]+" "
								avan.remove(avan[j])
								break
					elif len(toexplain[x])==5:
						for j in range(0,(len(avan))):
							if(avan[j][0].upper()==toexplain[x][0]):
								temp+=avan[j][0].upper()+avan[j][1:]+" "
								avan.remove(avan[j])
								break
						for j in range(0,(len(avav))):
							if(avav[j][0].upper()==toexplain[x][1]):
								temp+=avav[j][0].upper()+avav[j][1:]+" "
								avav.remove(avav[j])
								break
						for j in range(0,(len(advs))):
							if(advs[j][0].upper()==toexplain[x][2]):
								temp+=advs[j][0].upper()+advs[j][1:]+" "
								advs.remove(advs[j])
								break		
						for j in range(0,(len(avaa))):
							if(avaa[j][0].upper()==toexplain[x][3]):
								temp+=avaa[j][0].upper()+avaa[j][1:]+" "
								avaa.remove(avaa[j])
								break
						for j in range(0,(len(avan))):
							if(avan[j][0].upper()==toexplain[x][4]):
								temp+=avan[j][0].upper()+avan[j][1:]+" "
								avan.remove(avan[j])
								break
					else:
						long=True
					temp=temp.strip(" ")
					if long==True:
						message+="Acroynm Too Long,"
					else:
						message+=temp+","
				message=message.strip(",")
				usedwords=usedwords.strip(",")
				plural="You've used an acronym!!!" if len(toexplain)<=1 else "You've used multiple acronynms!!!"
				print usedwords
				print message
				print temp
				comment.reply(plural+"\n\nYou said: "+usedwords+"\n\nMeaning: "+message+"\n\nBeep Boop I'm Shitty Acronym Bot! Made By /u/Ruzakiff")
			else:
				print "No acronym"
		else:
		 	print "processed already"
def get_saved_comments():
	with open('/Users/ryan/Desktop/test/commentsused.txt', "r") as f:
			commentsused = f.read()
			commentsused = commentsused.split("\n")
			commentsused = filter(None, commentsused)
	return commentsused
def get_data():
	with open('/Users/ryan/Desktop/test/data.txt', "r") as f:
			data = f.read()
			data = data.split("\n")
			data = filter(None, data)
	return data
def get_nouns():
	with open('/Users/ryan/Desktop/test/Nouns.txt', "r") as f:
			nouns = f.read()
			nouns = nouns.split("\n")
			nouns = filter(None, nouns)
	return nouns
def get_verbs():
	with open('/Users/ryan/Desktop/test/Verbs.txt', "r") as f:
			verbs = f.read()
			verbs = verbs.split("\n")
			verbs = filter(None, verbs)
	return verbs
def get_adjs():
	with open('/Users/ryan/Desktop/test/Adjectives.txt', "r") as f:
			adjs = f.read()
			adjs = adjs.split("\n")
			adjs = filter(None, adjs)
	return adjs
def get_advs():
	with open('/Users/ryan/Desktop/test/Adverbs.txt', "r") as f:
			advs = f.read()
			advs = advs.split("\n")
			advs = filter(None, advs)
	return advs

r = bot_login()
commentsused = get_saved_comments()
data=get_data()
nouns=get_nouns()
adjs=get_adjs()
advs=get_advs()
verbs=get_verbs()
print nouns
print verbs
print data
while True:
	run_bot(r, commentsused)
