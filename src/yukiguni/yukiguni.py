# -*- coding: utf-8 -*-
"""Episode: 雪国抄
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
def ep_snow_story(w: World):
    return w.episode("雪国抄",
            ## NOTE
            ##  - 先生と小説のルーツについて教わる
            ##  - やる気になった先生と交換条件
            note="3.先生の知人から聞かされたことを確かめようとするがはぐらかされる。何故か急に長編を執筆してもいいと言い出す先生だったが",
            )
