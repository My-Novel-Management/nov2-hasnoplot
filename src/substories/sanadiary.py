# -*- coding: utf-8 -*-
"""Block: 沙奈の日記
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
def bk_sanadiary(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return (
            w.block("沙奈の日記１",
                sana.explain("こうして$meは先生と出逢った。",
                    "正直この出逢いは偶然がもたらした小さな悲劇だったけれど、",
                    "それが$meにとっても先生にとっても人生を大きく揺り動かすものになるとは、",
                    "文芸の神様ですら分からなかっただろう"),
                _.explain("ちなみに$meは文芸の神様の名を知らない。太宰治とか夏目漱石だろうか。それともシェークスピアやアリストテレスか。",
                    "できれば脱げとは言い出さない優しい神様であることを願った"),
                ),
            )

