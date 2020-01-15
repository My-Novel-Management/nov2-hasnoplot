# -*- coding: utf-8 -*-
"""Block: 短編ラノベ掲載枠の動向
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer
_ = W.getWho()


## blocks
def bk_shortnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return (
            w.block("shortnovel1",
                sana.explain("#先生から短編の原稿を貰ってくるように言われた"),
            ),
            w.block("shortnovel2",
                sana.explain("#短編のプロットすらないと先生に言われる"),
            ),
            w.block("shortnovel3",
                sana.explain("#沙奈が枠埋め用の短編を書くことになった"),
            ),
            w.block("shortnovel4",
                sana.explain("#シェアハウスしていた友人作家見習いに短編掲載枠を取られる"),
            ),
            )

