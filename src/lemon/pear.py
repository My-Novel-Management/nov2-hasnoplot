# -*- coding: utf-8 -*-
"""Episode: 4-1.洋梨／檸檬
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
def sc_main1(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("1.洋梨",
            sana.think("どうして自分も小説を書いているのだろうか、と疑問に"),
            sana.talk("意味ないのに"),
            sana.think("でも学生時代に作家を目指していた頃の気持ちを思い出す"),
            sana.talk("意外と楽しいかも"),
            sana.do("同僚から連絡がきて、短編掲載枠に先生以外の作家を打ち込むことになったらしい、と言われる"),
            sana.do("先生に連絡を取ろうとするが、繋がらない"),
            sana.talk("なんでこの時代にスマホも持ってないんですか！"),
            sana.go("出かける"),
            )

## episode
def ep_pear(w: World):
    return w.episode("1.洋梨",
            ## NOTE
            sc_main1(w),
            )
