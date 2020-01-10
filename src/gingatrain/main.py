# -*- coding: utf-8 -*-
"""Chapter: 銀河鉄道の夜
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from gingatrain.epilogue import ep_epilogue


## define alias
W = Writer


## chapter
def ch_gingatrain(w: World):
    return w.chapter("銀河鉄道の夜",
            ## NOTE: 修正作業やら後始末
            ##  - 死んだらどうなるのかと考えて怖くなって眠れなくなった学生時代のことを不意に思い出す
            ##  - 夢の中で銀河鉄道に乗っている　（銀河鉄道の夜
            ##  - 銀河鉄道の中で先生と自分が書いた小説についてダメ出しなど語り合う　（銀河鉄道の夜
            ##  - 先生に原稿を見せる
            ##  - 先生から鬼のようなダメ出しと、それでも一点だけ、ほめられる
            ##  - 編集長に見せたら翌朝直々にゲラを渡される、まっかっか
            ##  - まだまだゲラ作業は続く、けれど、これにて一旦編集日記は終わろうと思います、で締める
            ep_epilogue(w),
            )
