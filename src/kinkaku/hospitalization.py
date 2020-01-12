# -*- coding: utf-8 -*-
"""Episode: 先生の入院
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## define alias
W = Writer
_ = W.getWho()


## scenes
def sc_sensei_badnews(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生の凶報",
            sana.talk("え？", "何だって？"),
            _.do("もう一度バイト君に聞き返す"),
            _.do("何度確認しても同じだった"),
            _.do("先生は入院したのだ"),
            _.think("ずっと診てもらった方がいいと言っていたのに、倒れるまで守らなかった"),
            _.do("原稿に手がつかず、とにかくと立ち上がり、入院先を聞いて、外に出た"),
            _.do("車に乗り込むが、手が震えている"),
            )


## episode
def ep_hospitalization(w: World):
    return w.episode("先生、入院する",
            ## NOTE
            ##  - 書けずに行き詰まった
            ##  - 先生の助けを借りようとする
            ##  - 編集長から最後通告がある
            ##  - 先生が入院した、と連絡を受けた
            sc_sensei_badnews(w),
            note="4.火事で焼け出され、そのまま体調を崩した先生は一旦入院することになり、残った荷物は沙奈が引き受けることになった"
            )
