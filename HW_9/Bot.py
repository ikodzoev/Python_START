import logging
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import numexpr as calc

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!\nЭтот бот выполняет три задачи: '
                                    f'\nВведи /bin и любое число для конвертации в двоичную систему'
                                    f'\nВведи /fib и любое число для выведения списка негафибоначчи'
                                    f'\nВведи /cl и арифметическое выражение для вычисления: ')


async def dectobin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    number = update.message.text[5:]

    await update.message.reply_text("{0:b}".format(int(number)))


async def fibonarium(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    num = update.message.text[5:]
    number = int(num)
    fibo_list = list()
    fibo_list.append(0)
    fibo_list.append(1)

    for i in range(2, number + 1):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])

    fibo_list.insert(0, 1)
    fibo_list.insert(0, -1)

    for i in range(0, number - 2):
        fibo_list.insert(0, (fibo_list[1]) - (fibo_list[0]))
    await update.message.reply_text(f'Негафибоначчи: {fibo_list}')


async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    exp = update.message.text[4:]
    res = update.message.text

    await update.message.reply_text(f'{res[3:]} = {calc.evaluate(exp)}')


app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("bin", dectobin))
app.add_handler(CommandHandler("fib", fibonarium))
app.add_handler(CommandHandler("cl", calculate))

app.run_polling()
