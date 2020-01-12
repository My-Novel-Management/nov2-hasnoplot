# -*- coding: utf-8 -*-
"""Episode: 第一の手記：子供時代
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
def ep_childhood(w: World):
    return w.episode("第一の手記：子供時代",
            ## NOTE
            ##  - 先生に言われた通り、主人公である少女の幼少期から振り返って書いてみる
            ##  - すぐにわからなくなり、託されたアルバムから先生の小さい頃を掘り返す
            note="1.執筆が進まず、先生の助言メモを開いて、自分の人生を振り返ってヒントを探す沙奈",
            )
