from botcity.core import DesktopBot
import tags as tg
import ambient.tolls.clicks as cl

cl_functions = [cl.find, cl.click, cl.clickIfPossible]


def run():
    class Bot(DesktopBot):
        def action(self, execution=None):
            [
                find,
                click,
                clickIfPossible,
            ] = list(map(lambda x: cl.remove_self_nescessity(self, x), cl_functions))

    Bot.main()
