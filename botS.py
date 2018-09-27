from qqbot import QQBotSlot as qqbotslot, RunBot
import random

@qqbotslot
def onQQMessage(bot, contact, member, content):
    if content == "help":
        bot.SendTo(contact, '输入.help查找帮助，使用.r空格后输入骰子，再空格后输入判定名称~\n'
                            '加减法的运算为.add空格后接加法，.sub空格后接减法\n'
                            '这个bot写得时间很短而且bot本人是个弱智，如果卡bug了不是露娜的错\n'
                            ' 都怪我弱智，蟹蟹 ')

    elif '@ME' in content:
        bot.SendTo(contact, '你就算艾特也不会给你加成功率的啊煞笔')

    elif '.r' in content:
        dontuse, use, string = content.split()
        time, limit = use.split("d")
        result = 0
        for x in range(int(time)):
            result = random.randint(1, int(limit)) + result

        bot.SendTo(contact, member.name + '进行判定:' + string + ' 骰出结果: ' + str(result))

    elif '.add' in content:
        dontuse,use = content.split()
        one, two = use.split("+")
        result = int(one) + int(two)
        bot.SendTo(contact, '不会算算数的弱智：' + member.name + ' 计算结果: ' + str(result))

    elif '.sub' in content:
        dontuse, use = content.split()
        one, two = use.split("-")
        result = int(one) - int(two)
        bot.SendTo(contact, '不会算算数的弱智：' + member.name + ' 计算结果: ' + str(result))


if __name__ == "__main__":
    RunBot()

