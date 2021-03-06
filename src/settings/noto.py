# -*- coding: utf-8 -*-
"""Setting: 先生
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
    noto = W(w.noto)
    ## lifenote
    w.entryLifeNote(
        w.lifenote("先生の日常", w.noto,
            noto.do("朝はゆっくり起きるので、酷い場合は十二時を過ぎる"),
            noto.do(""),
            ),
        w.lifenote("先生の嗜好", w.noto,
            noto.think("健全な精神は健康な身体に宿るとし、鍛錬を欠かさない"),
            noto.go("ジム通い"),
            )
    )

    ## history
    w.entryHistory(w.noto,
    *w.createHistories(
        (6, "小学校入学"),
        (13, "中学校入学"),
        (16, "高校入学"),
        (19, "大学入学"),
        (21, "デビュー作を応募し受賞"),
        (22, "作家デビュー"),
        (32, "告白の手紙を書く"),
            ),
    )
    ## texture
    w.setTexture("noto", "髪は白髪まじりで短く借り揃えている、180cm近くあり割とがっしり")

