import requests, bs4
import src.phrases as phrases

thunderstorm = u'\U0001F4A8'
drizzle = u'\U0001F4A7'
rain = u'\U00002614'
snowflake = u'\U00002744'
snowman = u'\U000026C4'
atmosphere = u'\U0001F301'
clearSky = u'\U00002600'
fewClouds = u'\U000026C5'
clouds = u'\U00002601'
hot = u'\U0001F525'
defaultEmoji = u'\U0001F300'


class Yr_parser:
    def __init__(self):
        self.website = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}"

    def parse(self, lat, lon):
        try:
            link = self.website.format(lat, lon)

            r = requests.get(link)
            data = r.json()
            description = get_weather_description(data['properties']['timeseries'][0]['data']['next_1_hours']['summary']['symbol_code'])
            weather = phrases.yr.format(data['properties']['timeseries'][0]['data']['instant']['details']['air_temperature'],
                                        description,
                                        data['properties']['timeseries'][0]['data']['next_1_hours']['details']['precipitation_amount'],
                                        data['properties']['timeseries'][0]['data']['instant']['details']['wind_speed'])

            return weather
        except:
            return phrases.yr_error

def get_weather_description(data):
    if 'clearsky' in data:
        return 'Ясно ' + clearSky
    elif 'cloudy' in data:
        return 'Облачно ' + clouds
    else:
        return ' '

if __name__ == "__main__":
    yp = Yr_parser()
    print(yp.parse("50", "30"))