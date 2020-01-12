# -*- coding: utf-8 -*-
"""Episode: 先生の銀河鉄道
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

## episode
def ep_galaxytrain(w: World):
    return w.episode("先生の銀河鉄道",
            ## NOTE
            ##  - 先生は自分の為ではなくずっと誰かの為に書きたかったと語る
            ##  - 先生は無事に手術を終えて経過良好
            ##  - なのに無茶をして小説を仕上げてくれた
            note="2.先生を説得して病院に連れ戻し、自分の作品の修正作業をする沙奈。しかしそこに編集長から電話が入る",
            )
