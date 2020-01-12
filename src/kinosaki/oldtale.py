# -*- coding: utf-8 -*-
"""Episode: 昔語り
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
def ep_oldtale(w: World):
    return w.episode("先生の昔語り",
            ## NOTE
            ##  - 気を許してきたのか、昔のことを話してくれる
            ##  - 先生と小説の関係について
            note="2.先生が何故作家を目指したのか。その昔話を聞かせてくれた。それは親友と初恋の女性との三人の思い出だった",
            )
