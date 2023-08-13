from ambient.tolls.utils import Nf, watch
import tags as tg  # noqa: E261, F401


def firsth_block(self, nf: Nf) -> None:
    watch(self, nf, tg.githubFollow, turns=10)
