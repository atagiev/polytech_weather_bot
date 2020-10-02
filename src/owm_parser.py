import config, phrases
import requests

thunderstorm = u'\U0001F4A8'    # Code: 200's, 900, 901, 902, 905
drizzle = u'\U0001F4A7'         # Code: 300's
rain = u'\U00002614'            # Code: 500's
snowflake = u'\U00002744'       # Code: 600's snowflake
snowman = u'\U000026C4'         # Code: 600's snowman, 903, 906
atmosphere = u'\U0001F301'      # Code: 700's foogy
clearSky = u'\U00002600'        # Code: 800 clear sky
fewClouds = u'\U000026C5'       # Code: 801 sun behind clouds
clouds = u'\U00002601'          # Code: 802-803-804 clouds general
hot = u'\U0001F525'             # Code: 904
defaultEmoji = u'\U0001F300'

class Owm_parser:
    def __init__(self):
        self.website = "http://api.openweathermap.org/data/2.5/weather"
    def parse(self, lat, lon):
        try:
            r = requests.get(self.website, params={'lat': lat, 'lon': lon, 'units': 'metric', 'lang': 'ru', 'APPID': config.owm_api_key})
            data = r.json()
            weatherId = data['weather'][0]['id']
            emoji = getEmoji(weatherId)
            weather = phrases.owm.format(data['main']['temp'], data['main']['feels_like'], data['weather'][0]['description'], emoji, data['wind']['speed'])
            return weather
        except:
            return phrases.owm_error


def getEmoji(weatherID):
    if weatherID:
        if str(weatherID)[0] == '2' or weatherID == 900 or weatherID==901 or weatherID==902 or weatherID==905:
            return thunderstorm
        elif str(weatherID)[0] == '3':
            return drizzle
        elif str(weatherID)[0] == '5':
            return rain
        elif str(weatherID)[0] == '6' or weatherID==903 or weatherID== 906:
            return snowflake + ' ' + snowman
        elif str(weatherID)[0] == '7':
            return atmosphere
        elif weatherID == 800:
            return clearSky
        elif weatherID == 801:
            return fewClouds
        elif weatherID==802 or weatherID==803 or weatherID==803:
            return clouds
        elif weatherID == 904:
            return hot
        else:
            return defaultEmoji    # Default emoji

    else:
        return defaultEmoji   # Default emoji

if __name__ == "__main__":
    op = Owm_parser()
    print(op.parse("60", "30"))