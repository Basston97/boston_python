# Импортируем необходимые библиотеки
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Определяем состояния разговора
START, GET_FIN_TIPS = range(2)

# Функция для команды /start
def start(update: Update, _: CallbackContext) -> int:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Привет, {user.mention_markdown_v2()}! 👋'
        fr'Я бот по финансовой грамотности. '
        fr'Отправьте /get_tips, чтобы получить советы по финансам.'
    )

    return START

# Функция для команды /get_tips
def get_tips(update: Update, _: CallbackContext) -> int:
    update.message.reply_text("Здесь будут советы по улучшению финансового положения.")
    return GET_FIN_TIPS

# Функция для обработки текстовых сообщений от пользователя
def handle_text(update: Update, _: CallbackContext) -> int:
    text = update.message.text.lower()
    if text == 'пока':
        update.message.reply_text("До свидания! Если у вас будут вопросы по финансам, пишите.")
        return ConversationHandler.END
    else:
        update.message.reply_text("Извините, я пока не могу обрабатывать такие запросы.")
        return GET_FIN_TIPS

# Основная функция для запуска бота
def main():
    # Здесь нужно указать ваш токен, который вы получили от BotFather
    token = "YOUR_BOT_TOKEN"
    updater = Updater(token)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            START: [CommandHandler('get_tips', get_tips)],
            GET_FIN_TIPS: [MessageHandler(Filters.text & ~Filters.command, handle_text)],
        },
        fallbacks=[],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

