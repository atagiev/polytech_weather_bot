from src.bot import Bot
from src.database import Database
from src.weather_manager import Weather_manager
from threading import Condition

cv = Condition()
request_archive, location_archive = [], []
bot = Bot(request_archive, location_archive, cv)
db = Database()
lm = Weather_manager(request_archive, location_archive, db, cv)
lm.message_worker()