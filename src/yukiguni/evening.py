# -*- coding: utf-8 -*-
"""Episode: 夕景色
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
def ep_eveningsight(w: World):
    return w.episode("夕景色",
            ## NOTE
            ##  - 先生に誘われ、先生の実家の雪国にやってくる
            ##  - そこで先生の母親や旧知の女性たちと出会う
            note="1.先生に誘われて先生の実家にやってきた沙奈。そこで先生の昔を知る女性と出会う",
            )
