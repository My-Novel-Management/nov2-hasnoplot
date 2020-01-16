# -*- coding: utf-8 -*-
"""Episode: 1-1.走れ編集者／走れメロス
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
def sc_main1(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("1.走れ編集者",
            sana.do("電車を降りて、小さな体で必死に駅構内を走っていく"),
            sana.do("大きなカバンを二つも下げた小柄な女が走るのを、周囲はどう見ているだろう"),
            sana.do("それでも必死だ"),
            sana.do("そして転ぶ。ストッキングが破れる"),
            sana.talk("ああ、もうつらーい"),
            sana.think("トラックが迫ってきて、引かれたら異世界に行けるんだろうか、なんて考えたり"),
            sana.think("王、と呼ばれる新編集長の顔を思い出す"),
            )


## episode
def ep_runeditor(w: World):
    return w.episode("1.走れ編集者",
            ## NOTE
            sc_main1(w),
            )
