# -*- coding: utf-8 -*-
"""Episode: 洋梨
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
def ep_noneed_novel(w: World):
    return w.episode("洋梨：それはもう必要ない",
            ## NOTE
            ##  - せっかく書いた短編を先生は「駄目だ」と見ることもなく捨てる
            ##  - 挫折を思い出す
            note="1.適当に書き上げた短編小説を先生は読むこともなく駄目だと捨ててしまう",
            )
