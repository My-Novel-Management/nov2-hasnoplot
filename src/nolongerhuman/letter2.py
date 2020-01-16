# -*- coding: utf-8 -*-
"""Episode: 9-3.第二の手記／人間失格
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
    return w.scene("3.第二の手記",
            ## 中学時代、高校時代
            ## 親友の原稿
            sana.do("知人から$tsuruの持ち込み原稿を手に入れる"),
            _.do("それに目を通す"),
            sana.talk("これって……"),
            _.explain("そこに書かれていたものは確かに先生のものとそっくりだった",
                "しかし決定的だったのは裏写りする文字が明らかにトレースしたそれだということだ"),
            )

## episode
def ep_letter2(w: World):
    return w.episode("3.第二の手記",
            ## NOTE
            sc_main3(w),
            )
