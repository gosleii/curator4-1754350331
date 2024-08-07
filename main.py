# token 7279771096:AAHWt0Awchpf59tnqqrC9I2cjneJ_evEXkM

import telebot

bot = telebot.TeleBot("7279771096:AAHWt0Awchpf59tnqqrC9I2cjneJ_evEXkM")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     "*Привет!* \n Тут ты можешь задать любой интересующий тебя вопрос, не стесняйся )",
                     parse_mode="Markdown")


@bot.message_handler(commands=['whale'])
def main(message):
    bot.send_message(message.chat.id, "У зубатых китов, таких как касатки и белые киты, могут быть от 20 до 50 зубов, "
                                      "хотя у некоторых видов их может быть значительно больше. \n У усатых китов, "
                                      "таких как голубой кит или финвал, зубы отсутствуют. Вместо них у них есть "
                                      "специальные усики (балеены), которые используются для фильтрации пищи из воды.")


@bot.message_handler(commands=['7_47_am'])
def main(message):
    bot.send_message(message.chat.id, 'Разница в терминологии между "завинчивать" и "забалтывать" связана с '
                                      'конструктивными особенностями винтов и болтов, а также с их предназначением. '
                                      '\n *Винты* — это крепежные элементы, которые имеют нарезанную резьбу и обычно '
                                      'используются для соединения деталей, когда требуется надежное зацепление с '
                                      'материалом. Когда мы говорим "завинчивать", мы имеем в виду процесс '
                                      'закручивания винта в материал (например, дерево или металл), что подразумевает '
                                      'его углубление в поверхность. \n *Болты*, с другой стороны, обычно используются '
                                      'вместе с гайками и имеют гладкую часть под головкой. Они не предназначены для '
                                      'ввинчивания в материал, а скорее для соединения деталей, которые сжимаются '
                                      'между гайкой и головкой болта. Поэтому мы не говорим "забалтывать", '
                                      'поскольку это не отражает реального процесса их использования.',
                     parse_mode="Markdown")


@bot.message_handler(commands=['bot_name'])
def main(message):
    bot_name = bot.send_message(message.chat.id, "Напиши свой вариант именим для бота")
    bot.register_next_step_handler(bot_name, main_step_2)


def main_step_2(message):
    if len(message.text) <= 20 and message.text[-3:] == "bot" and message.text[0] not in '1234567890':
        bot.send_message(message.chat.id, "Ник одобрен!")
    else:
        bot.send_message(message.chat.id, "*Ошибка!!!*", parse_mode="Markdown")


@bot.message_handler(commands=['information'])
def main(message):
    bot.send_message(message.chat.id,
                     "[Случайный интересный факт сможешь найти тут)](https://randstuff.ru/fact/)",
                     parse_mode="Markdown")

bot.infinity_polling()
