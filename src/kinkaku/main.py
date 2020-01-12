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
from kinkaku.burnlost import ep_lost
from kinkaku.hospitalization import ep_hospitalization
from kinkaku.jealousy import ep_jealousy
from kinkaku.oldfriend import ep_oldfriend


## define alias
W = Writer


## chapter
def ch_kinkakuji(w: World):
    return w.chapter("金閣寺",
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
            ep_oldfriend(w),
            ep_jealousy(w),
            ep_lost(w),
            ep_hospitalization(w),
            note="執筆が難航する中、仕事で小説家として活躍する同級生と再会する沙奈。一方先生は体調を崩し、遂には入院してしまう",
            )
