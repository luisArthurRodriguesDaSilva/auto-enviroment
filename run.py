from botcity.core import DesktopBot


def run(path):
    class Bot(DesktopBot):
        def action(self, execution=None):
            pass

    Bot.main()
