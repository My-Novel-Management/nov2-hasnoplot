# -*- coding: utf-8 -*-
"""Episode: カムパネルラはどこに消えた
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
def ep_campanella(w: World):
    return w.episode("カムパネルラはどこに消えた",
            ## NOTE
            ##  - 大好きな作品として銀河鉄道の夜を紹介する
            ##  - 多くの作家の作品が見つけられずに亡くなる
            ##  - 親友の作品をこの世に送り出したかった、と盗作の真実を話す
            ##  - だが沙奈は手に入れていた原稿との大きな違いを指摘する（編集の仕事
            note="1.何とか先生を見つけ出した沙奈。先生は盗作がバレたことで作家生命を断とうとしていたが、沙奈は盗作ではなかったと証言する",
            )
