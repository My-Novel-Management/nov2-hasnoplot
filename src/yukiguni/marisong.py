# -*- coding: utf-8 -*-
"""Episode: 手鞠歌
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
def ep_oldsong(w: World):
    return w.episode("手鞠歌",
            ## NOTE
            ##  - 不思議な手鞠歌の話を聞かされる
            ##  - 先生に今でも恋をしていると語る女性
            note="2.先生の知人（女性）から昔の先生の話を聞く。その中で「先生は人殺しなのよ」と教えられる",
            )
