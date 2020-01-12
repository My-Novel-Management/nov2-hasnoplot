# -*- coding: utf-8 -*-
"""Episode: 温泉旅行
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
def ep_onsen(w: World):
    return w.episode("温泉旅行",
            ## NOTE
            ##  - 先生は温泉旅行に行きたいと言い出す
            ##  - 城之崎にやってくる
            ##  - 温泉を楽しむが
            note="1.先生が急に慰安旅行をしたいと言い出し、半ば無理やり、沙奈は温泉に連れ出される",
            )
