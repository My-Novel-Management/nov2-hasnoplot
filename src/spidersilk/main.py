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
from spidersilk.e1_teenweb import ep_teenweb
from spidersilk.e2_storyplot import ep_storyplot
from spidersilk.e3_spiderthread import ep_spiderthread
from spidersilk.e4_mastermind import ep_mastermind


## define alias
W = Writer


## chapter
def ch_spidersilk(w: World):
    return w.chapter("蜘蛛の糸は切れたか？",
            ## NOTE:
            ##  1.若者のネット
            ##  2.物語のプロット
            ##  3.蜘蛛のスレッド
            ##  4.先生のマインド
            ## NOTE: プロット
            ##  - プロットについて、簡単な話
            ##  - 先生の「書けない現状」を聞かされる
            ##  - 沢山のプロットもどきを見せられる
            ##  - 最終締切までに原稿がなければ先生は金輪際頼まないだろうと宣告された
            ##  - 何故か自分が短編を書くことになる
            ##  - 因果
            ep_teenweb(w),
            ep_storyplot(w),
            ep_spiderthread(w),
            ep_mastermind(w),
            note="プロットすらないと笑う先生の代わりに、何故か沙奈が短編小説を書いてその枠を埋めることになった",
            )
