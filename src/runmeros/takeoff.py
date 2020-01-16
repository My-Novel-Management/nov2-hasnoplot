# -*- coding: utf-8 -*-
"""Episode: 1-4.脱げ編集者／走れメロス
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
def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("4.脱げ編集者",
            sana.talk("な、何を……"),
            noto.talk("だから脱げと言っているんだ",
                "その上着だけじゃない", "まずは全部脱いで裸になってもらおう"),
            sana.think("最悪だ、と思った"),
            sana.think("先輩はちょっと癖があると言っていたけれど、ちょっとどころじゃない",
                "これはＳランクだ", "最悪のＳだった"),
            )

## episode
def ep_takeoffeditor(w: World):
    return w.episode("4.脱げ編集者",
            ## NOTE
            sc_main4(w),
            )
