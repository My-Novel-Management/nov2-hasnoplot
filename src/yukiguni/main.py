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
## local files
from yukiguni.e1_sunset import ep_sunsetsight
from yukiguni.e2_temarisong import ep_temarisong
from yukiguni.e3_snowtale import ep_snowtale
from yukiguni.e4_nextstory import ep_nextstory


## define alias
W = Writer


## chapter
def ch_yukiguni(w: World):
    return w.chapter("雪国の思い出",
            ## NOTE: episodes
            ##  1.夕景色
            ##  2.手鞠歌
            ##  3.雪国抄
            ##  4.続雪国
            ## NOTE: 文章について
            ##  - 文章は基本を押さえているのがまず大事、などの説明
            ##  - 先生がいきなり実家に帰っていて、そこは雪国だった（北陸
            ##  - 先生の学生時代の話
            ##  - 先生の初恋エピソード
            ##  - 友情を感じた女性と、その彼女が許嫁と語った病床の男性＝盗作作品を書いた男性（雪国エピソード
            ##  - 自分の仕事が一段落する
            ##  - 長編の執筆にようやく取り掛かる
            ##  - 先生の断章たち（雪国ももとは複数の雑誌に構想的に断章が書かれていたもの
            ##  - 胎内くぐりの村
            ## NOTE:
            ##  - 雪国だった（先生の地元編
            ##  - 先生の旧知らしい大人の女性
            ep_sunsetsight(w),
            ep_temarisong(w),
            ep_snowtale(w),
            ep_nextstory(w),
            note="先生の実家（金沢）に連れてこられた沙奈。先生の旧知の人間から色々教わる。先生は長編を書く条件として沙奈も長編を書くことを約束させた",
            )
