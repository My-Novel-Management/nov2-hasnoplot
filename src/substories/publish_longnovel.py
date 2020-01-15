# -*- coding: utf-8 -*-
"""Block: 長編出版枠の動向
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
def bk_longnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return (
            w.block("longnovel1",
                sana.explain("#ある有名作家の長編を準備していると聞かされる"),
            ),
            w.block("longnovel2",
                sana.explain("#長編の準備はしていると先生に言われる"),
            ),
            w.block("longnovel3",
                sana.explain("#長編出版枠に他の作家も競合していると知る"),
            ),
            w.block("longnovel4",
                sana.explain("#長編出版枠は先生の方向で進めると言われる"),
            ),
            w.block("longnovel5",
                sana.explain("#長編の構想はずっとあると先生から聞く"),
            ),
            w.block("longnovel6",
                sana.explain("#捨てられた長編原稿を見つける"),
            ),
            w.block("longnovel7",
                sana.explain("#無事に先生が長編執筆を始める"),
            ),
            w.block("longnovel8",
                sana.explain("#長編原稿が消失する"),
            ),
            w.block("longnovel9",
                sana.explain("#別の作家がその出版枠に収まりそうと連絡を受ける"),
            ),
            w.block("longnovel10",
                sana.explain("#先生の初めてのライトノベルレーベルでの出版が正式に決まる"),
            ),
            )

