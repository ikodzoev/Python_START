import view
from logger import log
import model
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes


@log
def start():
    """Стартовая функция"""

    # while True:
    #     match view.menu():
    #         case 0:
    #             break
    #         case 1:
    #             view.print_book(model.get_data())
    #         case 2:
    #             model.add_data(view.add_record())
    #         case 3:
    #             model.add_data(view.editor(model.get_data_id(view.request_id())))
    #         case 4:
    #             view.print_book(model.get_data_last_name(view.request_last_name()))
    bot_token = "5850359754:AAEU52LCv-L0XuvLX50QcDrI-hOPX5eTBJc"
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", view.greetings))
    app.add_handler(CommandHandler("load", view.phone_book))
    app.add_handler(CommandHandler("add", view.add))
    app.add_handler(CommandHandler("edit", view.edit))
    app.add_handler(CommandHandler("find", view.find))
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), view.echo)
    start_handler = CommandHandler('start', start)

    app.add_handler(start_handler)
    app.add_handler(echo_handler)
    # app.add_handler(CommandHandler("add", view.greatings))
    # app.add_handler(CommandHandler("edit", view.greatings))
    # app.add_handler(CommandHandler("find", view.greatings))
    # app.add_handler(CommandHandler("start", hello))
    app.run_polling()
