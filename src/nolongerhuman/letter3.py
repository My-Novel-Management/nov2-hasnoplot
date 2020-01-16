# -*- coding: utf-8 -*-
"""Episode: 9-4.第三の手記／人間失格
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
def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("4.第三の手記",
            ## 女と酒に溺れる日々
            sana.do("先生が病院から消えた、とバイト君から連絡が入った"),
            sana.talk("なんで！？"),
            _.do("時刻を見れば十二時を回っている",
                "もう今日が締め切り日だった"),
            sana.do("編集長からのメールに気づく"),
            _.do("そこには既に別の作家で長編枠は埋まったと書かれていた"),
            )

## episode
def ep_letter3(w: World):
    return w.episode("4.第三の手記",
            ## NOTE
            sc_main4(w),
            )
