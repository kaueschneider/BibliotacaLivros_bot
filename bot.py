from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Updater
from telegram import ReplyKeyboardMarkup

STATE1 = 1
STATE2 = 2

def feedback(update, context):
    try:
        message = 'Por favor, digite um feedback para este bot:'
        update.message.reply_text(
            message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))
        return STATE1
    except Exception as e:
        print(str(e))


def inputFeedback(update, context):
    feedback = update.message.text
    print(feedback)
    if len(feedback) < 10:
        message = """Seu feedback foi muito curtinho... 
                        \nInforma mais pra gente, por favor?"""
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)
        return STATE1
    else:
        message = "Muito obrigado pelo seu feedback!"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END


def inputFeedback2(update, context):
    feedback = update.message.text
    message = "Muito obrigado pelo seu feedback!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END

def welcome(update, context):
    firstname = update.message.from_user.first_name
    message = ('Olá ' + firstname + '!')
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text = message)

def main(): 
    token = '1303726410:AAHRI84bmBQepDh32ymo5OJQp-woMakBnPQ'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('feedback', feedback)],
        states={
            STATE1: [MessageHandler(Filters.text, inputFeedback)],
            STATE2: [MessageHandler(Filters.text, inputFeedback2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)

    updater.start_polling()
    print('Eu sou o updater' + str(updater))
    updater.idle()  

 

if __name__ == '__main__':
    main()
