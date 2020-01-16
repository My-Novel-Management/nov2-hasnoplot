# -*- coding: utf-8 -*-
"""Episode: 5-4.続雪国／雪国
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
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("4.続雪国",
            noto.talk("ああ、心配ない", "ちゃんと長編は考えているよ"),
            sana.do("そう言われて安堵する"),
            sana.think("しかし、$asahiに言われたことが気になっていた"),
            )


## episode
def ep_nextstory(w: World):
    return w.episode("4.続雪国",
            ## NOTE
            sc_main4(w),
            )
