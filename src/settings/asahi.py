# -*- coding: utf-8 -*-
"""Setting: 朝日
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
    asahi = W(w.asahi)
    ## lifenote
    w.entryLifeNote(
        w.lifenote("日常", w.asahi,
            )
    )

    ## history
    w.entryHistory(w.asahi,
    *w.createHistories(
        (6, "小学校入学"),
        (52, "飲み屋を経営"),
            ),
    )
    ## texture
    w.setTexture("asahi",
            [
                "髪", "背中までのロング、ストレートでよく手入れされている",
                ])

