import telepot
import json

def handler(pd: "pipedream"):

  bot = telepot.Bot('Your bot Token')
  chat = ('Your chat ID')

  fresh_server = pd.steps["trigger"]["event"]["body"]["check_url"]
  fresh_status = pd.steps["trigger"]["event"]["body"]["response_summary"]
  fresh_text = pd.steps["trigger"]["event"]["body"]["text"]
  fresh_name = pd.steps["trigger"]["event"]["body"]["check_name"]

  response = ("Status: " + fresh_status + "\n" + "Name: " + fresh_name + "\n" + "URL: " + fresh_server + "\n \n" + "Server message: \n" + fresh_text)

  bot.sendMessage(chat, response)

  return ('Ok!')