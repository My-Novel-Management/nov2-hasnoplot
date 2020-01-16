# -*- coding: utf-8 -*-
"""Episode: 5-2.手鞠歌／雪国
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
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("2.手鞠歌",
            asahi.talk("ちょっといいかしら"),
            sana.talk("何ですか？"),
            sana.do("彼女に古い喫茶店に連れて行かれる"),
            asahi.talk("ここでよく彼ら三人が集まって話してたのよ"),
            asahi.talk("知ってるかしら"),
            asahi.talk("$full_notoはね、人殺しなのよ"),
            )

## episode
def ep_temarisong(w: World):
    return w.episode("2.手鞠歌",
            ## NOTE
            sc_main2(w),
            )
