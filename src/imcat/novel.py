# -*- coding: utf-8 -*-
"""Episode: 猫と小説
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
def ep_cat_and_books(w: World):
    return w.episode("猫と小説",
            ## NOTE
            ##  - 小説について語りだす
            ##  - 大量のライトノベル
            note="2.先生は小説について語り出す。特に依頼を受けたライトノベルとは何か、沙奈に次々と質問をぶつけ、返答に窮する",
            )
