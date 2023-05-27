from ambient.tolls.utils import take_click_types
import tags as tg


def firsth_block(self, nf) -> None:
    find, click, clickIfPossible, awaitItGoOut = take_click_types(nf)
    click(btnName=tg.thunderClient, waiting_time=5000)
    click(tg.host)
