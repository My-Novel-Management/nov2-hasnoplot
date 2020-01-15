# -*- coding: utf-8 -*-
"""Chapter: 城の崎にて
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
from kinosaki.episode import ep_main


## define alias
W = Writer


## chapter
def ch_kinosaki(w: World):
    return w.chapter("城の崎にて",
            ## NOTE: シーン
            ##  - シーンについての解説
            ##  - 事故エピソード（城の崎にて
            ##  - 様々な生き物が語りかけてくる（城の崎にて
            ##  - イモリエピソード（城の崎にて
            ep_main(w),
            note="先生に連れられ城之崎に慰安旅行にやってくる。そこで先生が小説を書けなくなったトラウマを知る",
            )
