from src.bot import Bot
from src.database import Database
from src.weather_manager import Weather_manager
from threading import Condition

cv = Condition()
message_archive = []
bot = Bot(message_archive, cv)
db = Database()
Wm = Weather_manager(message_archive, db, cv)
Wm.message_worker()