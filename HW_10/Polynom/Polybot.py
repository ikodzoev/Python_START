"""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.
Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.
Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE
                ):
    """Вывод приветствия."""

    await update.message.reply_text(
        f'Здравствуйте, {update.effective_user.first_name}! '
        f'Введите /poly и нажмите enter для вычисления суммы многочленов: '
        f'13*x^2 + 72*x + 66 = 0 и 82*x^2 + 58*x + 49 = 0 ')


async def poly(update: Update, context: ContextTypes.DEFAULT_TYPE
               ):
    """Вывод приветствия."""
    await update.message.reply_text(f'Сумма многочленов: {polynom_res_sum}')


def poly_genium():
    global polynom_res_sum
    with open('polynom_res1.txt', 'r') as data:
        polynom_res1 = data.read()
    with open('polynom_res2.txt', 'r') as data:
        polynom_res2 = data.read()
    file_1 = open('polynom_res1.txt', 'r')
    file_2 = open('polynom_res2.txt', 'r')
    sum_poly = open('polynom_res_sum.txt', 'w')
    file1 = file_1.readline()
    file2 = file_2.readline()
    for i in range(len(file1)):
        if file1[i - 1] != '^':
            if file1[i].isnumeric():
                sum_poly.write(str(int(file1[i]) + int(file2[i])))
            else:
                sum_poly.write(str(file1[i]))
        else:
            sum_poly.write(str(file1[i]))
    sum_poly = open('polynom_res_sum.txt', 'r')
    with open('polynom_res_sum.txt', 'r') as data:
        polynom_res_sum = data.read()


poly_genium()
bot_token = "PLACE YOUR TOKEN HERE"
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("poly", poly))
# print(poly_genium())
app.run_polling()
