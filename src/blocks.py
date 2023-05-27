from ambient.tolls.utils import Nf
import tags as tg


def firsth_block(self, nf: Nf) -> None:
    nf.click(tg.thunderClient)
    nf.awaitItGoOut(tg.thunderClient)
