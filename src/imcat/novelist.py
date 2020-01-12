# -*- coding: utf-8 -*-
"""Episode: 猫と先生
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
def ep_novelist(w: World):
    return w.episode("猫と先生",
            ## NOTE
            ##  - 黒猫を飼っている時代錯誤な作家先生
            note="1.脱がないと、答えた沙奈に次々と時代錯誤な要求をする先生",
            )
