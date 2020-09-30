from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import config, phrases

class Bot:

    def location(self, update, context):
        self.location_archive.append(update)
        update.message.reply_text(phrases.add_location)

    def get_weather(self, update, context):
        self.request_archive.append(update)

    def hello(self, update, context):
        update.message.reply_text(phrases.hello)

    def __init__(self, request_archive, location_archive):
        self.request_archive = request_archive
        self.location_archive = location_archive

        self.updater = Updater(config.token, use_context=True)

        self.updater.dispatcher.add_handler(CommandHandler(['start', 'help'], self.hello))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.location, self.location))
        self.updater.dispatcher.add_handler(CommandHandler('get_weather', self.get_weather))

        self.updater.start_polling()

if __name__ == '__main__':
    request_archive, location_archive = [], []
    b = Bot(request_archive, location_archive)





