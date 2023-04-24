from botcity.core import DesktopBot
import tags as tg  # noqa: E261, F401
import ambient.tolls.clicks as cl

cl_functions = [cl.find, cl.click, cl.clickIfPossible]


def run():
    class Bot(DesktopBot):
        def action(self, execution=None):
            find = cl.remove_self_necessity(self, cl.find)
            click = cl.remove_self_necessity(self, cl.click)
            clickIfPossible = cl.remove_self_necessity(self, cl.clickIfPossible)
            nf = [find, click, clickIfPossible]  # noqa: F841

    Bot.main()
