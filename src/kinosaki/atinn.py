# -*- coding: utf-8 -*-
"""Episode: 6-1.旅の宿にて／城の崎にて
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
def sc_main1(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("1.旅の宿にて",
            sana.do("先生に連れてこられ、城の崎にやってくる"),
            sana.talk("こっち初めてきました"),
            noto.talk("この雰囲気が好きで、たまにくるんだ"),
            noto.do("楽しそうに見て歩く"),
            )

## episode
def ep_atinn(w: World):
    return w.episode("旅の宿にて",
            ## NOTE
            sc_main1(w),
            )
