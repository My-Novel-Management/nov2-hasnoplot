# -*- coding: utf-8 -*-
"""Chapter: 走れメロス
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from runmeros.meeting import ep_firstmeet


## define alias
W = Writer


## chapter
def ch_runmeros(w: World):
    return w.chapter("走れメロス",
            ## NOTE: アイデア出し
            ##  - 先輩が産休になり、急遽代役として編集部に異動してくる
            ##  - ゲラをチェックするところを入れる
            ##  - 新しい編集長（王と呼ばれている）の傍若無人ぶりに憤り　（走れメロス
            ##  - 元編集で世話になった人を助ける為に、作家先生から原稿を取ってくることに
            ##  - 先生に何とか出会うがいきなり「脱げ」と言われた
            ep_firstmeet(w),
            )
