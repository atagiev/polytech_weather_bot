from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import phrases
import config

class Bot:

    def location(self, update, context):
        self.message_archive.append(("location", update))
        with self.cv:
            self.cv.notify_all()

    def get_weather(self, update, context):
        self.message_archive.append(("get_weather", update))
        with self.cv:
            self.cv.notify_all()

    def hello(self, update, context):
        update.message.reply_text(phrases.hello)
    
    def set_home_location(self,update,context):
        self.message_archive.append(("set_home_location", update))
        with self.cv:
            self.cv.notify_all()


    def __init__(self, message_archive, cv):
        self.message_archive = message_archive
        self.cv = cv

        self.updater = Updater(config.token, use_context=True)

        self.updater.dispatcher.add_handler(CommandHandler(['start', 'help'], self.hello))
        self.updater.dispatcher.add_handler(CommandHandler('set_home_location', self.set_home_location))

        self.updater.dispatcher.add_handler(MessageHandler(Filters.location, self.location))
        self.updater.dispatcher.add_handler(CommandHandler('get_weather', self.get_weather))

        self.updater.start_polling()

if __name__ == '__main__':
    message_archive =  []
    b = Bot(message_archive, None)