# -*- coding: utf-8 -*-
"""Episode: はしがき
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
def ep_firstpart(w: World):
    return w.episode("はしがき：小説の序文",
            ## NOTE
            ##  - 沙奈が書いている長編小説の最初の方
            ##  - うまく書けていない様子、悩みが書き連ねられ、やがて日記になる
            note="0.沙奈の小説の序文。学生時代に掛けなかったある少女の物語",
            )
