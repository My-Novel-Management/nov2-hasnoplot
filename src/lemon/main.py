# -*- coding: utf-8 -*-
"""Chapter: 檸檬
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
from lemon.episode import ep_main


## define alias
W = Writer


## chapter
def ch_lemon(w: World):
    return w.chapter("檸檬",
            ## NOTE: 短編と長編
            ##  - 短編と長編の違いについて教わる
            ##  - 久しぶりに書いた自信作の短編を読みもせずに突き返され、書き直せと言われた
            ##  - どこが問題なのかが分からず、そこに別の仕事がやってくる
            ##  - いっぱいいっぱいになり、逃げ出す
            ##  - 大好きだった本屋に、檸檬が置かれていた。それは先生の仕業だった
            ##  - 昔のただの本好きだった頃を思い出して、ライトノベルという枠を外して作品を書き上げた
            ##  - 短編を書き上げたが、掲載されたのは別の作家の作品だった
            ##  - その報告をしたら先生の短編を読ませてもらい、自分が小さい頃に読んだ話を思い出した
            ## NOTE:
            ##  - 洋梨：
            ##  - 蜜柑：
            ##  - 檸檬：
            ep_main(w),
            note="何とか依頼された短編を書き終えた沙奈だったが、既にその枠は他の作家により埋められていたのだった",
            )
