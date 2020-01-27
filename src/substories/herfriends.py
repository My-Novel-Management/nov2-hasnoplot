# -*- coding: utf-8 -*-
"""Block: 友人たち
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer
_ = W.getWho()


## blocks
def bk_herfriends(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return (
            w.block("友人１：絵師",
                sana.explain("$full_geroはイラストレーターをしている"),
                gero.talk("いや、最近なかなかビッとくるのが描けんでね"),
                sana.explain("名古屋出身ということで、割と気が合う"),
            ),
            )

