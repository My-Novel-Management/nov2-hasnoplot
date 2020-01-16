# -*- coding: utf-8 -*-
"""Episode: 8-1.第一章／金閣寺
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
    return w.scene("第一章",
            noto.talk("ああ、そうだ", "$meは彼の作品を盗んだ",
                "それがデビュー作になったんだよ"),
            sana.do("先生はそう告白した", "密告の手紙は事実だった",
                "そしてそれを当時編集者だった編集長は知っていたのだ"),
            )

## episode
def ep_chapter1(w: World):
    return w.episode("1.第一章",
            ## NOTE
            sc_main1(w),
            )
