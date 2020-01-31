# -*- coding: utf-8 -*-
"""Setting: 深谷
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
    fukaya = W(w.fukaya)
    ## lifenote
    w.entryLifeNote(
        w.lifenote("日常", w.fukaya,
            )
    )

    ## history
    w.entryHistory(w.fukaya,
    *w.createHistories(
        (6, "小学校入学"),
        (23, "アリス出版入社"),
        (35, "産休に入る"),
            ),
    )
    ## texture
    w.setTexture("fukaya", "ショートヘア、僅かに赤み。体格は160cm中肉。意外と筋肉質")

