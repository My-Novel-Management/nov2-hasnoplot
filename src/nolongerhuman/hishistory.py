# -*- coding: utf-8 -*-
"""Episode: 第三の手記：先生の秘密
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## define alias
W = Writer
_ = W.getWho()


## scenes

## episode
def ep_hissecret(w: World):
    return w.episode("第三の手記：彼の秘密",
            ## NOTE
            ##  - 発見した告白日記
            ##  - そこには盗作でデビューしてから、必死に彼になろうとしていた苦悩が書かれていた
            ##  - ずっとその幻影につきまとわれ、それを紛らわせる為に酒に走った
            ##  - 編集長から既に他の作家に穴埋めのあてがついたと
            ##  - それでも先生の言葉を思い出して、最後まで書く
            ##  - 夜は更けていく
            ##  - 先生から謎の電話
            note="3.本棚の奥に先生の秘密の日記を見つけてしまい、沙奈はそこで先生のデビュー作が盗作であったことを知る",
            )
