# -*- coding: utf-8 -*-
"""Setting: 敦賀
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
    tsuru = W(w.tsuru)
    ## lifenote
    w.entryLifeNote(
        w.lifenote("敦賀の学生当時", w.tsuru,
            tsuru.do("朝方だったので、五時くらいには目覚めて執筆"),
            )
    )

    ## history
    w.entryHistory(w.tsuru,
    *w.createHistories(
        (6, "小学校入学"),
        (13, "中学校入学"),
        (16, "高校入学"),
        (19, "上京して作家に弟子入り"),
        (22, "自殺"),
            ),
    )
    ## texture
    w.setTexture("tsuru", "長髪で後ろで括っていた")

