# -*- coding: utf-8 -*-
"""Episode: 書き終えたら
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
def sc_finish(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("やっと終わった",
            sana.do("先生を見張っていたバイトの子から連絡があり、先生が消えたと"),
            sana.talk("もう。どういうことなの……"),
            _.do("立ち上がろうとして、倒れる$S"),
            )


## episode
def ep_finished(w: World):
    return w.episode("執筆の終わり",
            ## NOTE
            ##  - 作品を書き終えて
            ##  - 先生が病院から消えたと一報が
            sc_finish(w),
            )
