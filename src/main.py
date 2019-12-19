# -*- coding: utf-8 -*-
"""Main story.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.common.times import COMMON_TIMES
from config import PERSONS, CHARAS, STAGES, DAYS, TIMES, ITEMS, WORDS
from src.demo.main import ep_demo

## NOTE:
#   名作10本
#   1. 走れメロス（太宰治）
#   1. 吾輩は猫である（夏目漱石）
#   1. 雪国（川端康成）
#   1. 蜘蛛の糸（芥川龍之介）
#   1. 金閣寺（三島由紀夫）
#   1. 城の崎にて（志賀直哉）
#   1. こころ（夏目漱石）
#   1. 檸檬（梶井基次郎）
#   1. 人間失格（太宰治）
#   1. 銀河鉄道の夜（宮沢賢治）


## main
def ch_main(w: World):
    return w.chapter("main",
            ep_demo(w).omit(),
            # 1.走れ編集者
            # 1.我輩は編集者である
            # 1.出張先は雪国
            # 1.蜘蛛よりも細い糸
            # 1.金閣寺と矜持
            # 1.城の崎に行きたい
            # 1.作家のこころ
            # 1.檸檬は嫌いです
            # 1.編集失格
            # 1.銀河鉄道の長い夜
            )

def world():
    """Create a world.
    """
    w = World(2)
    w.set_times(COMMON_TIMES)
    w.set_db(PERSONS, CHARAS,
            STAGES, DAYS, TIMES,
            ITEMS,
            WORDS)
    return w

def story(w: World):
    return w.story("Sample",
            ch_main(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

