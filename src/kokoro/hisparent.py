# -*- coding: utf-8 -*-
"""Episode: 中：先生の親
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
def ep_parent(w: World):
    return w.episode("中：先生と両親",
            ## NOTE
            ##  - 先生がどんな親と暮らしていたのかを聞かされる
            ##  - 唯一自由だったのが本の中だった。本だけは自由に読むことを許された
            ##  - それから隠れて自分でも書くようになった
            ##  - しかしそんな自分とは全然レベルの違う、本物の小説をある人物に見せられた
            note="2.先生とその師匠、自殺した親友の関係について知った沙奈。先生はずっと親友に嫉妬していたことを知る",
            )
