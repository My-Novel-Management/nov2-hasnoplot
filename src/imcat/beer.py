# -*- coding: utf-8 -*-
"""Episode: 猫とビール
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
def ep_cat_and_beer(w: World):
    return w.episode("猫とビール",
            ## NOTE
            ##  - 酒を飲み始め、話を有耶無耶にされる
            note="3.先生はとりあえずビールが欲しいと沙奈をコンビニまで買い物に行かせるが、その間に逃げ出してしまう",
            )
