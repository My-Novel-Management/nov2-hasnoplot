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
## local files
from kokoro.e1_masterandme import ep_master_and_me
from kokoro.e2_parentsandme import ep_parents_and_me
from kokoro.e3_masterandparents import ep_master_and_parents
from kokoro.e4_masterandletter import ep_master_and_letter


## define alias
W = Writer


## chapter
def ch_kokoro(w: World):
    return w.chapter("先生のこころ",
            ## NOTE: episodes
            ##  1.先生と私
            ##  2.私と両親
            ##  3.先生と両親
            ##  4.先生と手紙
            ## NOTE: キャラクター造形
            ##  - 台詞が固いことに思い悩む
            ##  - 人物造形について教わる
            ##  - 墓地に付きそう　（こころエピ）
            ##  - 大事なことを先生が話してくれない。また時が来たらと言われる
            ##  - 先生の秘密を書いた手紙を見つけてしまう
            ##  - 手紙には最初の作品が「盗作」であった罪の告白が書かれていたのだった
            ## NOTE
            ##  - 上：先生と私：外で偶然出会う（実は先生がストーカーしていただけ）／謎の墓参り（盗作した友人の
            ##  - 中：先生と親：父親が腎臓の病気／先生から手紙を貰う
            ##  - 下：先生と手紙：先生の友人についての告白
            ep_master_and_me(w),
            ep_parents_and_me(w),
            ep_master_and_parents(w),
            ep_master_and_letter(w),
            note="先生に送られた、自殺した親友の手紙を見つけ、先生のトラウマの正体を知る沙奈",
            )
