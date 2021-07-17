import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, bot
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, CallbackContext


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

FIRST = range(1)
UNO, DOS, TRES = range(3)


def start(update: Update, context: CallbackContext) -> int:
    
    user = update.message.from_user
    logger.info("Usuario %s Ha iniciado conversacion", user.first_name)
    keyboard = [
        [

            InlineKeyboardButton("Formula del area del círculo",
            callback_data=str(UNO)),
        ],
        [

            InlineKeyboardButton("Formula para calcular area del cuadrado ",
            callback_data=str(DOS)),
        ],
         [

            InlineKeyboardButton("Formula para calcular el area del Triángulo",
            callback_data=str(TRES)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    user = update.effective_user
    update.message.reply_markdown_v2(
    fr'¡Hola {user.mention_markdown_v2()}\!, Por favor, Selecciona una opción',
    reply_markup=reply_markup)
    return FIRST

def uno(update: Update, context: CallbackContext) -> int:
    update.callback_query.answer()
    text = 'Usted ha seleccionado: \n\nLa formula para calcular el area del círculo.\n\n\nLa formula para calcular el area del círculo es: d = 2 • r \n\n\nFormula: \nhttps://cutt.ly/hmZDTqn'
    update.callback_query.edit_message_text(text=text)
    return ConversationHandler.END
    

def dos(update: Update, context: CallbackContext) -> int:
    update.callback_query.answer()
    text = 'Usted ha seleccionado: \n\nLa formula para calcular el area del cuadrado.\n\n\nLa formula para calcular el area del uadrado es: A = a² \n\n\nFormula: \nhttps://cutt.ly/BmZFKHs'
    update.callback_query.edit_message_text(text=text)
    return ConversationHandler.END


def tres(update: Update, context: CallbackContext) -> int:
    update.callback_query.answer()
    text = 'Usted ha seleccionado: \n\nLa formula para calcular el area del Triángulo.\n\n\nLa formula para calcular el area del triángulo es:A = b • h / 2 \n\n\nFormula: \nhttps://cutt.ly/HmZF2vM'
    update.callback_query.edit_message_text(text=text)
    return ConversationHandler.END

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Use /start para realizar otra consulta")
    
    

def main() -> None:
       
    updater = Updater("1907672648:AAFOlaaT5H6Dlv3J96B9n40zh4LZxmNm5AQ")
    
    dispatcher = updater.dispatcher
    updater.dispatcher.add_handler(CommandHandler('help', help))
   
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(uno, pattern='^' + str(UNO) + '$'),
                CallbackQueryHandler(dos, pattern='^' + str(DOS) + '$'),
                CallbackQueryHandler(tres, pattern='^' + str(TRES) + '$'),

            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    
    dispatcher.add_handler(conv_handler)

    
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()