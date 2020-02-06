# -*- coding: utf-8 -*-
"""Chapter: 金閣寺
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
from kinkaku.e1_chapter1 import ep_chapter1
from kinkaku.e2_chapter2 import ep_chapter2
from kinkaku.e3_chapter3 import ep_chapter3
from kinkaku.e4_chapter4 import ep_chapter4


## define alias
W = Writer


## chapter
def ch_kinkakuji(w: World):
    return w.chapter("金閣寺の美意識",
            ## NOTE: episodes
            ##  1.第一章
            ##  2.第二章
            ##  3.第三章
            ##  4.第四章
            ## NOTE: サブストーリー
            ##  - 執筆が難航している
            ##  - サブストーリーについて教わる
            ##  - コンプレックスが邪魔をする　（金閣寺
            ##  - 作家として活躍する、障害もちの同級生と再会　（金閣寺
            ##  - 原稿を燃やそうとする　（金閣寺
            ##  - 編集長から先生の企画をやめると通告がある
            ##  - 大事な原稿の入稿締め切りが迫る
            ##  - 先生が入院する
            ##  - 実際にあった事件を小説にしていた　（金閣寺
            ##  - 過去を振り返って告白する構造　（金閣寺
            ep_chapter1(w),
            ep_chapter2(w),
            ep_chapter3(w),
            ep_chapter4(w),
            note="執筆が難航する中、仕事で小説家として活躍する同級生と再会する沙奈。一方先生は体調を崩し、遂には入院してしまう",
            )
