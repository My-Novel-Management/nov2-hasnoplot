# -*- coding: utf-8 -*-
"""Chapter: こころ
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from kokoro.confess import ep_hisletter


## define alias
W = Writer


## chapter
def ch_kokoro(w: World):
    return w.chapter("こころ",
            ## NOTE: キャラクター造形
            ##  - 台詞が固いことに思い悩む
            ##  - 人物造形について教わる
            ##  - 墓地に付きそう　（こころエピ）
            ##  - 大事なことを先生が話してくれない。また時が来たらと言われる
            ##  - 先生の秘密を書いた手紙を見つけてしまう
            ##  - 手紙には最初の作品が「盗作」であった罪の告白が書かれていたのだった
            ep_hisletter(w),
            )
