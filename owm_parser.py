import config, phrases
import requests

class Owm_parser:
    def __init__(self):
        self.website = "http://api.openweathermap.org/data/2.5/weather"
    def parse(self, lat, lon):
        try:
            r = requests.get(self.website, params={'lat': lat, 'lon': lon, 'units': 'metric', 'lang': 'ru', 'APPID': config.owm_api_key})
            data = r.json()
            weather = phrases.owm.format(data['main']['temp'],data['weather'][0]['description'])
            return weather
        except:
            return phrases.owm_error


if __name__ == "__main__":
    op = Owm_parser()
    print(op.parse("1", "1"))