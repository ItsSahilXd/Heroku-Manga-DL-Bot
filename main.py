from config import bot
from Plugins.manga import Manga
from Plugins.starter import start

try:
    start()
    Manga()
    

except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()
