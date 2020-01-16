# -*- coding: utf-8 -*-
"""Episode: 5-3.雪国抄／雪国
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
def sc_main3(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("3.雪国抄",
            sana.come("妙なことを聞かされて、帰ってくる"),
            sana.do("先生の家族と食事"),
            sana.do("夜は晩酌に付き合う"),
            noto.talk("意外と飲むんだね？"),
            sana.talk("父親は全然なんですけど、母親が酒豪で。福岡出身だから？"),
            noto.talk("あちらはすごいとは聞くけどねえ"),
            noto.talk("そういえば$asahiさんと会ったんだってね", "彼女、よく嘘をつくから気をつけて"),
            sana.talk("なんか先生が人殺しだって言われましたよ"),
            sana.do("空気が固まる"),
            noto.talk("まあ、違うともいえないんだけど"),
            noto.talk("時がきたら話すよ"),
            )

## episode
def ep_snowtale(w: World):
    return w.episode("3.雪国抄",
            ## NOTE
            sc_main3(w),
            )
