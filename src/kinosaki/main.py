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
from kinosaki.e1_atinn import ep_atinn
from kinosaki.e2_oldtalk import ep_oldtalk
from kinosaki.e3_edgeindead import ep_edgeindead
from kinosaki.e4_insided import ep_insided


## define alias
W = Writer


## chapter
def ch_kinosaki(w: World):
    return w.chapter("城の崎にて先生と",
            ## NOTE: episodes
            ##  1.旅の宿にて
            ##  2.昔の話にて
            ##  3.死の淵にて
            ##  4.心の内にて
            ## NOTE: シーン
            ##  - シーンについての解説
            ##  - 事故エピソード（城の崎にて
            ##  - 様々な生き物が語りかけてくる（城の崎にて
            ##  - イモリエピソード（城の崎にて
            ep_atinn(w),
            ep_oldtalk(w),
            ep_edgeindead(w),
            ep_insided(w),
            note="先生に連れられ城之崎に慰安旅行にやってくる。そこで先生が小説を書けなくなったトラウマを知る",
            )
