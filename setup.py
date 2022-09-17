import requests,os

try:
  from config import *
  os.system('pm2 start bot.py --name {} --interpreter python3.8 --interpreter-args -u'.format(BOT_ID))
except Exception as e:
  API_ID = 12410826
  API_HASH = '563d5c8290807e93d9bd3976467ad251'

  out ="""
API_ID = 12410826
API_HASH = '563d5c8290807e93d9bd3976467ad251'
"""
  def Bot(TOKEN,method,data):
    url = "https://api.telegram.org/bot{}/{}".format(TOKEN,method)
    post = requests.post(url,data=data)
    return post.json()
  ID = ""
  go = True
  while go:
    token = input("input you're bot TOKEN:")
    get = Bot(token,"getme",{})
    if get["ok"]:
      out = out+"\n"+"TOKEN = '{}'\nBOT_ID = TOKEN.split(':')[0]".format(token)
      go = False
      ID = token.split(':')[0]

    else:
      print("TOKEN is invalid, Try again")

  sudo = input("input you're ID:")
  out = out+"\n"+"SUDO = {}".format(sudo)
  botate = input("input you're username Channel: @")
  out = out+"\n"+"BOTATE = '{}'".format(botate)

  f = open("config.py","w+") 
  f.write(out)
  f.close()

  os.system('pm2 start bot.py -f --name {} --interpreter python3.8 --interpreter-args -u'.format(ID))
