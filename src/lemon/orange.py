# -*- coding: utf-8 -*-
"""Episode: 蜜柑
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
def ep_various_books(w: World):
    return w.episode("蜜柑：いろいろな作品種類がある",
            ## NOTE
            ##  - 先生から小説にも一定の形があると教わる
            ##  - 短編と長編の違いについて教わる
            ##  - 小説の自由さを教わる
            note="2.短編について教わる沙奈。先生も書くという条件で沙奈ももう一度短編小説執筆に挑戦する",
            )
