# -*- coding: utf-8 -*-
"""Episode: 蜘蛛の糸
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
def ep_spider_thread(w: World):
    return w.episode("蜘蛛の糸",
            ## NOTE
            ##  - 蜘蛛の糸の話
            ##  - 因果と縁を大切にしようという話
            note="3.結局プロットすらもらえず、原稿を書くには信頼を得ないといけないと言われ、その日は引き下がる沙奈",
            )
