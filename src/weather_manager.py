import phrases
from yandex_parser import Yandex_parser
from owm_parser import Owm_parser
from yr_parser import Yr_parser

class Weather_manager:

    def get_weather(self, lat, lon):
        weather = phrases.before_weather + self.yandex_parser.parse(lat, lon) + self.owm_parser.parse(lat, lon) + self.yr_parser.parse(lat,lon)
        return weather

    def message_worker(self):
        while True:
            with self.cv:
                for msg in self.message_archive:
                    state = self.db.get_state(msg[1].message.chat_id)
                    if msg[0]=="location":
                        if state == "0" or state =="1":
                            self.db.update_loc(msg[1].message.chat_id, msg[1].message.location.latitude, msg[1].message.location.longitude)
                            self.db.update_state(msg[1].message.chat_id,"2")
                            msg[1].message.reply_text(phrases.home_location)
                        elif state == "2":
                            weather = self.get_weather(msg[1].message.location.latitude, msg[1].message.location.longitude)
                            msg[1].message.reply_text(weather)
                    elif msg[0]=="set_home_location":
                        if state =="0" or state =="2":
                            self.db.update_state(msg[1].message.chat_id,"1")
                            msg[1].message.reply_text(phrases.send_home_location)
                        elif state =="1":
                            msg[1].message.reply_text(phrases.send_home_location)
                    elif msg[0]=="get_weather":
                        if state =="0" or state =="1":
                            msg[1].message.reply_text(phrases.error)
                        elif state=="2":
                            lat,lon = self.db.get_loc(msg[1].message.chat_id)
                            weather = self.get_weather(lat, lon)
                            msg[1].message.reply_text(weather)

                    self.message_archive.remove(msg)
                self.cv.wait()

    def __init__(self, message_archive, db, cv):
        self.message_archive = message_archive
        self.db = db
        self.yandex_parser = Yandex_parser()
        self.owm_parser = Owm_parser()
        self.yr_parser = Yr_parser()
        self.cv = cv

if __name__ == '__main__':
    message_archive, db, cv = [], [], 1
    weather = Weather_manager(message_archive, db, cv)
    print(weather.get_weather("60", "30"))
