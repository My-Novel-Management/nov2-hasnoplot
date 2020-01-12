# -*- coding: utf-8 -*-
"""Episode: 原稿焼失
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
def ep_lost(w: World):
    return w.episode("原稿焼失",
            ## NOTE
            ##  - 彼の家が火事になり（放火）、同業者から恨みを相当買っていたことが判明
            ##  - 更に脱税など、色々と問題が湧き上がる
            ##  - だが後で他の人間から聞くと、どうやら既に作品が書けなくなっていたとか
            ##  - 行方不明になり、連絡が途絶えた
            note="3.前担当の深谷を恨んでいた作家が放火し、先生の住処は燃えてしまい、折角の原稿もその大半が焼失してしまった",
            )
