import requests
import time

lastfish = 0
lastdig = 0
lasthunt = 0
lastbeg = 0
lastdep = 0
lastsell = 0

def todiscord(msg):
    url = "https://discord.com/api/v9/channels/869824878595932182/messages"
    payload={'content': msg,
    'tts': 'false'}
    files=[

    ]
    headers = {
      'authorization': 'DISCORD_AUTH_TOKEN',
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

def sellall():
    todiscord("pls sell fish max")
    time.sleep(1.5)
    todiscord("pls sell worm max")
    time.sleep(1.5)
    todiscord("pls sell cookie max")
    time.sleep(1.5)
    todiscord("pls sell exoticfish max")
    time.sleep(1.5)
    todiscord("pls sell slunk max")
    time.sleep(1.5)
    todiscord("pls sell garbage max")
    time.sleep(1.5)
    todiscord("pls sell junk max")
    time.sleep(1.5)
    todiscord("pls sell boar max")
    time.sleep(1.5)
    todiscord("pls sell ant max")
    time.sleep(1.5)
    todiscord("pls sell bread max")
    time.sleep(1.5)
    todiscord("pls sell duck max")
    time.sleep(1.5)
    todiscord("pls sell deer max")
    time.sleep(1.5)
    todiscord("pls sell jellyfish max")
    time.sleep(1.5)
    todiscord("pls sell ladybug max")
    time.sleep(1.5)
    todiscord("pls sell rabbit max")
    time.sleep(1.5)
    todiscord("pls sell rarefish max")
    time.sleep(1.5)
    todiscord("pls sell seaweed max")
    time.sleep(1.5)
    todiscord("pls sell sticlbug max")
    time.sleep(1.5)
    todiscord("pls bal")

while (True):
    if (time.time() - lastfish > 40):
        todiscord("pls fish")
        lastfish = time.time()

    if (time.time() - lastdig > 40):
        todiscord("pls dig")
        lastdig = time.time()

    if (time.time() - lasthunt > 40):
        todiscord("pls hunt")
        lasthunt = time.time()

    if (time.time() - lastbeg > 45):
        todiscord("pls beg")
        lastbeg = time.time()

    if (time.time() - lastdep > 900):
        todiscord("pls dep max")
        lastdep = time.time()

    if (time.time() - lastsell > 900):
        sellall()
        lastsell = time.time()

    
