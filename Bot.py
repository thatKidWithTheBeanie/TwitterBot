import schedule
import time
import tweepy
import random

### the messy stuff
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
### singular nouns, plural nouns, singular verbs, plural verbs and infinitives..
s_nouns = ["um cara", "minha mae humana", "o rei dos gatos", "algum cara", "um gato com raiva", "uma preguiça", "seu parça", "esse cara legal que meu jardineiro conheceu ontem", "Superman", "algum cara que estava de boas perto da minha caixinha de areia"]
p_nouns = ["esses caras", "ambas as minhas mães", "todos os reis do mundo", "alguns caras", "todos os gatos do gatil", "a multidão de preguiças vivendo embaixo da sua cama", "seus parças", "tipo, todas essas pessoas"]
s_verbs = ["como", "chuto", "trato", "me encontro com", "crio", "hacks", "configuro", "espiono", "mio em", "fujo de", "tento automatizar", "explodo", "beija"]
p_verbs = ["come", "chuta", "trata", "se encontra com", "cria", "hack", "configura", "espiona", "mia em", "escapa de", "tenta automatizar", "explode", "beijo"]
infinitives = ["para fazer uma torta.", " sem razão aparente.", "porque o céu é verde.", "for uma doença.", "para poder fazer torrada explodir.", "para saber mais sobre arqueologia.", "porque eu mandei.", "para me fazer rei para sempre.", "então eu o executei."]
#### select word from each list
s1 = random.choice(s_nouns)
s2 = random.choice(s_verbs)
s3 = random.choice(p_nouns).lower()
s4 = random.choice(infinitives)

def job(t):
#### append words into sentance
s1 = random.choice(s_nouns)
s2 = random.choice(s_verbs)
s3 = random.choice(p_nouns).lower()
s4 = random.choice(infinitives)
tweet = (s1 + " " + s2 + " " + s3 + " " + s4)
#### authenticate
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
### post!
api.update_status(tweet)
### did it work?
print ("yayyy!!")
return

### at X time complete the task
schedule.every().day.at("23:59").do(job,'It is nearly midnight')

while True:
schedule.run_pending()
time.sleep(60) # wait one minute
