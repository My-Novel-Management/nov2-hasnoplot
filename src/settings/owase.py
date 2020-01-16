# -*- coding: utf-8 -*-
"""Setting: 尾鷲
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
    owase = W(w.owase)
    ## lifenote
    w.entryLifeNote(
        w.lifenote("日常", w.owase,
            )
    )

    ## history
    w.entryHistory(w.owase,
    *w.createHistories(
        (6, "小学校入学"),
        (26, "作家になるため公募や持ち込み"),
            ),
    )
    ## texture
    w.setTexture("owase",
            [
                "髪", "茶髪",
                ])

