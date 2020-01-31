# -*- coding: utf-8 -*-
"""Setting: 編集長
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
    king = W(w.king)
    ## lifenote
    w.entryLifeNote(
        w.lifenote("日常", w.king,
            )
    )

    ## history
    w.entryHistory(w.king,
    *w.createHistories(
        (6, "小学校入学"),
        (50, "新しく第二文芸部の編集長になる"),
            ),
    )
    ## texture
    w.setTexture("king", "短めの髪")

