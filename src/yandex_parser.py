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


class Yandex_parser:
    def __init__(self):
        self.website = "https://yandex.ru/pogoda/?lat={}&lon={}"
    
    def parse(self, lat, lon):
        try:
            link = self.website.format(lat, lon)
            
            r = requests.get(link)
            b = bs4.BeautifulSoup(r.content,"html.parser")
            temp = b.find(class_="temp__value").getText()
            feels_like = b.find(class_="term__value").getText()
            looks_like = b.find(class_="link__feelings fact__feelings").div.getText()
            emoji = getEmoji(looks_like)
            wind = b.find(class_="wind-speed").getText()
            rain_next_two_hours = b.find(class_="maps-widget-fact__title").getText()
            weather = phrases.yandex.format(temp, feels_like, looks_like, emoji, wind, rain_next_two_hours)

            return weather
        except:
            return phrases.yandex_error


def getEmoji(looks_like):
    if looks_like:
        if looks_like == 'Гроза':
            return thunderstorm
        elif looks_like == 'Небольшой дождь':
            return drizzle
        elif looks_like == 'Дождь':
            return rain + rain
        elif looks_like == 'Снег':
            return snowflake + ' ' + snowflake
        elif looks_like == 'Небольшой снег':
            return snowflake
        elif looks_like == 'Туман':
            return atmosphere
        elif looks_like == 'Ясно':
            return clearSky
        elif looks_like == 'Малооблачно':
            return fewClouds
        elif looks_like == 'Облачно с прояснениями':
            return fewClouds
        elif looks_like == 'Пасмурно':
            return clouds
        else:
            return defaultEmoji    # Default emoji

    else:
        return defaultEmoji   # Default emoji

if __name__ == "__main__":
    yp = Yandex_parser()
    print(yp.parse("60", "30"))