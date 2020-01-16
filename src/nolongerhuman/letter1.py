# -*- coding: utf-8 -*-
"""Episode: 9-2.第一の手記／人間失格
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
def sc_main2(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("2.第一の手記",
            ## 恥の多い生涯を送ってきました、の序文
            ## 少年時代
            sana.think("先生の日記を振り返る"),
            _.think("学生時代。当時から小説を書いていた先生。親友と競い合うようにして出版社に持ち込みをしていた"),
            _.think("今ならネットに投稿しているのだろうか", "ランキングを競い合っているのだろうか"),
            _.think("当時の読者は互いとその女性だけだった"),
            )

## episode
def ep_letter1(w: World):
    return w.episode("2.第一の手記",
            ## NOTE
            sc_main2(w),
            )
