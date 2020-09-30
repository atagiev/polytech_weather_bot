from threading import Thread
import phrases
from yandex_parser import Yandex_parser
from owm_parser import Owm_parser

class Location_manager:

    def get_weather(self, lat, lon):
        weather = self.yandex_parser.parse(lat, lon) + self.owm_parser.parse(lat, lon)
        return weather

    def message_worker(self):
        while True:
            for req in self.request_archive:
                code, lat, lon = self.db.get_loc(req.message.chat_id)
                if code == 0:
                    req.message.reply_text(phrases.no_location)
                else:
                    weather = self.get_weather(lat, lon)
                    req.message.reply_text(weather)
                self.request_archive.remove(req)   

            for loc in self.location_archive:
                self.db.update_loc(loc.message.chat_id, loc.message.location.latitude, loc.message.location.longitude)
                self.location_archive.remove(loc)         

    def __init__(self, request_archive, location_archive, db):
        self.request_archive = request_archive
        self.location_archive = location_archive
        self.db = db
        self.yandex_parser = Yandex_parser()
        self.owm_parser = Owm_parser()


if __name__ == '__main__':
    request_archive, location_archive, db = [], [],[]