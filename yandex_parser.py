import requests, bs4
import phrases

class Yandex_parser:
    def __init__(self):
        self.website = "https://yandex.ru/pogoda/?lat={}&lon={}"
    
    def parse(self, lat, lon):
        try:
            link = self.website.format(lat, lon)
            
            r=requests.get(link)
            b=bs4.BeautifulSoup(r.content,"html.parser")
            temp = b.find(class_="temp__value").getText()
            looks_like = b.find(class_="link__feelings fact__feelings").div.getText()
            weather = phrases.yandex.format(temp,looks_like)

            return weather
        except:
            return phrases.yandex_error


if __name__ == "__main__":
    yp = Yandex_parser()
    print(yp.parse("1","1"))