# -*- coding: utf-8 -*-
"""Episode: 7-3.先生と両親／こころ
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
    return w.scene("3.先生と両親",
            sana.do("先生に案内される"),
            sana.do("古本屋などを回る"),
            sana.do("先生の叔父は本屋をやっていた"),
            sana.do("けれど現在は廃業して、夢だったうどん喫茶をやっているらしい"),
            sana.explain("両親には金沢で世話になった",
                "立派な書斎を思い出すが、本が充実していた理由はそこにあったようだ"),
            noto.talk("そういう自由さは、$meも羨ましいところさ"),
            )

## episode
def ep_master_and_parents(w: World):
    return w.episode("3.先生と両親",
            ## NOTE
            sc_main3(w),
            )
