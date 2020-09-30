from bot import Bot
from database import Database
from location_manager import Location_manager

request_archive, location_archive = [], []
bot = Bot(request_archive, location_archive)
db = Database()
lm = Location_manager(request_archive, location_archive, db)
lm.message_worker()