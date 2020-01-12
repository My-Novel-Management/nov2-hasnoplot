# -*- coding: utf-8 -*-
"""Chapter: 蜘蛛の糸
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
from spidersilk.shortnovel import ep_writenovel
from spidersilk.spiderthread import ep_spider_thread
from spidersilk.storyplot import ep_story_plot
from spidersilk.youngthread import ep_young_thread


## define alias
W = Writer


## chapter
def ch_spidersilk(w: World):
    return w.chapter("蜘蛛の糸",
            ## NOTE: プロット
            ##  - プロットについて、簡単な話
            ##  - 先生の「書けない現状」を聞かされる
            ##  - 沢山のプロットもどきを見せられる
            ##  - 最終締切までに原稿がなければ先生は金輪際頼まないだろうと宣告された
            ##  - 何故か自分が短編を書くことになる
            ##  - 因果
            ## NOTE
            ##  - 若者のスレッド：小説の神様
            ##  - 物語のプロット
            ##  - 蜘蛛の糸：因果について
            ep_young_thread(w),
            ep_story_plot(w),
            ep_spider_thread(w),
            ep_writenovel(w),
            note="プロットすらないと笑う先生の代わりに、何故か沙奈が短編小説を書いてその枠を埋めることになった",
            )
