# -*- coding: utf-8 -*-
"""Episode: 下：先生と手紙
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
def ep_letter(w: World):
    return w.episode("下：先生と手紙",
            ## NOTE
            ##  - 先生から手紙が送られてくる
            ##  - そこには先日話せなかったかつての友人について書かれていた
            note="3.先生から元親友の原稿を見せられる。それは先生より遥かに才能があったと思えた",
            )
