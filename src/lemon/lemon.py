# -*- coding: utf-8 -*-
"""Episode: 檸檬
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
def ep_bomb(w: World):
    return w.episode("檸檬",
            ## NOTE
            ##  - 書店を爆破したらどうなるか、と言い出す
            ##  - 人間の感情や気持ちはもっと自由なんだと、黒い感情もいっぱいある
            ##  - 今活躍中の、自分の同級生
            note="3.何とか短編を書き終えた沙奈だったが、先生の枠は既に他の作家の作品によって埋められていた",
            )
