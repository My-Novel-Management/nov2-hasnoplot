# -*- coding: utf-8 -*-
"""Setting: 安曇野
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
    azu = W(w.azumino)
    ## lifenote
    w.entryLifeNote(
        w.lifenote("日常", w.azumino,
            )
    )

    ## history
    w.entryHistory(w.azumino,
    *w.createHistories(
        (6, "小学校入学"),
        (25, "沙奈たちとシェアハウス。バイトしつつ作家を目指す"),
            ),
    )
    ## texture
    w.setTexture("azumino", "ロングヘアに眼鏡")

