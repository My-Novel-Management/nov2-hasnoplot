# -*- coding: utf-8 -*-
"""Episode: 第二の手記：学生時代
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
def ep_schooldays(w: World):
    return w.episode("第二の手記：学生時代",
            ## NOTE
            ##  - 自分の学生時代を振り返る
            ##  - あまり良い思い出がなく、本ばかりが友達だった
            ##  - 本棚から先生の作品を借りる
            ##  - そこに日記を見つける
            ##  - 日記には小説の断片に隠れて、本音が書かれていた
            note="2.沙奈は自分の学生時代を振り返っていた。そんな時入院中の先生から電話が入る",
            )
