# -*- coding: utf-8 -*-
"""Setting: 香美
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
    komi = W(w.komi)
    ## lifenote
    w.entryLifeNote(
        w.lifenote("日常", w.komi,
            )
    )

    ## history
    w.entryHistory(w.komi,
    *w.createHistories(
        (6, "小学校入学"),
        (19, "病気で死亡"),
            ),
    )
    ## texture
    w.setTexture("komi",
            [
                "髪", "痛みやすく猫みたいな細い癖毛",
                "体格", "小柄で痩せ気味",
                ])

