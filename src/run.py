from botcity.core import DesktopBot
import tags as tg  # noqa: E261, F401
import blocks as bls
from ambient.tolls.utils import getClickFunctions


def run():
    class Bot(DesktopBot):
        def action(self, execution=None):
            nf = getClickFunctions(self)
            find, click, clickIfPossible, awaitItGoOut = nf
            bls.firsth_block(self, nf)

    Bot.main()
