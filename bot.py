from telegram.ext import CommandHandler, Updater


def welcome(update, context):
    message = ('Olá ' + update.message.from_user.first_name + '!')
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text = message)

def main(): 
    token = '1303726410:AAHRI84bmBQepDh32ymo5OJQp-woMakBnPQ'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    updater.start_polling()
    print('Eu sou o updater' + str(updater))
    updater.idle()  

 

if __name__ == '__main__':
    main()
