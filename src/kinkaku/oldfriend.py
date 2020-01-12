# -*- coding: utf-8 -*-
"""Episode: かつての同級生
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
def ep_oldfriend(w: World):
    return w.episode("かつての同級生",
            ## NOTE
            ##  - 作家として華々しい活躍をする同級生と再会
            ##  - 彼から作家としての苦労とか色々教わる
            ##  - 編集者として下手に出て聞いていたが
            ##  - 抱かせてくれたら一本書いてやる、と笑われた
            note="1.沙奈は出版社で同じ学校出身の天才と呼ばれている作家と再会する",
            )
