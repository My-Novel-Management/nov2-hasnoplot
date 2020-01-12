# -*- coding: utf-8 -*-
"""Episode: ほんとうのものがたり
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
def ep_trunovel(w: World):
    return w.episode("ほんとうのものがたり",
            ## NOTE
            ##  - 沙奈は先生に言われた本当の物語を探す為に、改めて編集の仕事に戻った
            note="3.自分の物語とは何だろうか。沙奈は書き上がった先生の原稿のゲラ刷りを見つめながら考え込んでいた",
            )
