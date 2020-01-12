# -*- coding: utf-8 -*-
"""Episode: 上：墓参り
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
def ep_visitgraves(w: World):
    return w.episode("上：先生と私",
            ## NOTE
            ##  - 偶然出先で出会う
            ##  - 先生の墓参りに付き合う（誰か言ってくれない
            ##  - 先生から小説、特に人物造形のことを教わる
            note="1.出先で偶然先生に出会い、誰のものとも分からない墓参りに付き合った",
            )
