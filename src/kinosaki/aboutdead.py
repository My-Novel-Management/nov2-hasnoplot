# -*- coding: utf-8 -*-
"""Episode: 死について
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
def ep_aboutdead(w: World):
    return w.episode("死について",
            ## NOTE
            ##  - 先生は生命について、特に死について語り始める
            ##  - 先生の大切な人間が二人も死んだ過去があった
            note="3.先生の親友と、その初恋の女性を巡って争いがあったが、初恋の女性は病気で亡くなってしまう",
            )
