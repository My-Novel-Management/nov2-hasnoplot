# -*- coding: utf-8 -*-
"""Chapter: 檸檬
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


## chapter
def ch_lemon(w: World):
    return w.chapter("檸檬",
            )
