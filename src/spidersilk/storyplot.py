# -*- coding: utf-8 -*-
"""Episode: 物語のプロット
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
def ep_story_plot(w: World):
    return w.episode("物語のプロット",
            ## NOTE
            ##  - せめてプロットだけでもと言う沙奈に先生はプロットの説明を始める
            note="2.何とかプロットだけでももらおうとする沙奈に、先生はプロットとは何なのかについて解説を始める",
            )
