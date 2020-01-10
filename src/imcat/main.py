# -*- coding: utf-8 -*-
"""Chapter: 吾輩は猫である
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from imcat.noplot import ep_noplot


## define alias
W = Writer


## chapter
def ch_Imacat(w: World):
    return w.chapter("吾輩は猫である",
            ## NOTE: 起承転結
            ##  - 起承転結についての説明を受ける
            ##  - 物語（小説）について講義が始まる
            ##  - 猫が先生だという話をされた
            ##  - 小説界に捨てられた作家　（吾輩は猫である
            ##  - 作家の「名前」の話
            ##  - ラノベ界についての苦言（軽視　（吾輩は猫である
            ##  - だが資料として大量のラノベを、ビールを飲みながら読んでいた
            ##  - 最終的に「プロット」もないと言われた
            ep_noplot(w),
            )
