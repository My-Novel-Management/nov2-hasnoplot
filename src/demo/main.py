# -*- coding: utf-8 -*-
"""Demo: story no1
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes


## episode
def ep_demo(w: World):
    return w.episode("Demo", "__description__",
            )
