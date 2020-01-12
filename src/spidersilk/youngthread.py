# -*- coding: utf-8 -*-
"""Episode: 若者のスレッド
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
def ep_young_thread(w: World):
    return w.episode("若者のスレッド",
            ## NOTE
            ##  - 若者文化、特に機械ものが苦手という先生
            note="1.プロットがないと言い張る先生に対して、何とか痕跡だけでも探そうと家探しする。しかし先生はパソコンすら持っていなかった",
            )
