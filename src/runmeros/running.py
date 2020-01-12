# -*- coding: utf-8 -*-
"""Episode: 走れ主人公
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
def ep_go_hero(w: World):
    return w.episode("走れ主人公",
            ## NOTE
            ##  - 本日期限だという先生の原稿を貰いに急ぐことに
            note="1.沙奈は自慢のミニで走っていた。先輩の代役として先生の担当編集になり、本日締切の原稿を貰う為だった",
            )
