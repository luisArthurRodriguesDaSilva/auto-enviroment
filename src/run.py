from botcity.core import DesktopBot
import tags as tg
import ambient.tolls.clicks as cl


def run():
    class Bot(DesktopBot):
        def action(self, execution=None):
            cl.click(self, tg.guiPy_png)

    Bot.main()

run('C:\\Users\\user\\Desktop\\guiPy.exe')
