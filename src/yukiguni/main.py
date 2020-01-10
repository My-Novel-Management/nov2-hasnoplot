# -*- coding: utf-8 -*-
"""Chapter: 雪国
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from yukiguni.barganingpoint import ep_bargaining


## define alias
W = Writer


## chapter
def ch_yukiguni(w: World):
    return w.chapter("雪国",
            ## NOTE: 文章について
            ##  - 文章は基本を押さえているのがまず大事、などの説明
            ##  - 先生がいきなり実家に帰っていて、そこは雪国だった（北陸
            ##  - 先生の学生時代の話
            ##  - 先生の初恋エピソード
            ##  - 友情を感じた女性と、その彼女が許嫁と語った病床の男性＝盗作作品を書いた男性（雪国エピソード
            ##  - 自分の仕事が一段落する
            ##  - 長編の執筆にようやく取り掛かる
            ep_bargaining(w),
            )
