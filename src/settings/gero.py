# -*- coding: utf-8 -*-
"""Setting: 下呂
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


## setting person
def set_person(w: World):
    gero = W(w.gero)
    ## lifenote
    w.entryLifeNote(
        w.lifenote("日常", w.gero,
            )
    )

    ## history
    w.entryHistory(w.gero,
    *w.createHistories(
        (6, "小学校入学"),
        (10, "絵かきを目指す"),
        (19, "上京し、沙奈たちとシェアハウス"),
            ),
    )
    ## texture
    w.setTexture("gero", "長髪で後ろにまとめている")

