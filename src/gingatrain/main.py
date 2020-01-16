# -*- coding: utf-8 -*-
"""Chapter: 10.銀河鉄道の夜
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
from gingatrain.campanella import ep_campanella
from gingatrain.epilogue import ep_epilogue
from gingatrain.geovanni import ep_geovanni
from gingatrain.truthstory import ep_truthstory


## define alias
W = Writer

## chapter
def ch_gingatrain(w: World):
    return w.chapter("銀河鉄道の夜",
            ## NOTE: episodes
            ##  1.カムパネルラはどこに消えた？
            ##  2.ジョバンニの気持ち
            ##  3.ほんとうのものがたり
            ##  4.エピローグ
            ## NOTE: 修正作業やら後始末
            ##  - 死んだらどうなるのかと考えて怖くなって眠れなくなった学生時代のことを不意に思い出す
            ##  - 夢の中で銀河鉄道に乗っている　（銀河鉄道の夜
            ##  - 銀河鉄道の中で先生と自分が書いた小説についてダメ出しなど語り合う　（銀河鉄道の夜
            ##  - 先生に原稿を見せる
            ##  - 先生から鬼のようなダメ出しと、それでも一点だけ、ほめられる
            ##  - 編集長に見せたら翌朝直々にゲラを渡される、まっかっか
            ##  - まだまだゲラ作業は続く、けれど、これにて一旦編集日記は終わろうと思います、で締める
            ## NOTE: main
            ##  - 先生の原稿が採用され、校正作業を経て、出版する為、製本される
            ## NOTE: sub
            ##  - 先生のデビュー作は盗作ではなかった（元親友の持ち込み原稿が見つかる）
            ep_campanella(w),
            ep_geovanni(w),
            ep_truthstory(w),
            ep_epilogue(w),
            note="先生を何とか病院に連れ戻し、長編のゲラ修正をする沙奈。自分の作品は無理だったが先生の作品の出版が決まり、何とか一段落するが",
            )
