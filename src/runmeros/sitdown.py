# -*- coding: utf-8 -*-
"""Episode: 座れ小説家
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
def ep_sitdown_novelist(w: World):
    return w.episode("座れ編集者",
            ## NOTE
            ##  - 何とか先生を探し出し、家に連れて戻る
            ##  - だがそこで先生は彼女に無理難題を言い出す
            note="3.沙奈は先生に土下座をして、事情を説明し、何とか家に戻って原稿を貰おうとするが",
            )
