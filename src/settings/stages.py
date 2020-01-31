# -*- coding: utf-8 -*-
"""Setting: 舞台設定
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


## define alias
W = Writer
_ = W.getWho()


## setting stages
def set_stages(w: World):
    w.setTexture("on_hercampany_int", "事務机が整然と並び、パーテーションで区切られている")
    w.setTexture("on_hercampany_ext", "オフィス街のビルが並ぶ中にある")
    w.setTexture("on_herhouse", "３LDKで洋間をそれぞれの居室にしている。家賃10万。三階建ての三階")
    w.setTexture("on_hisapart", "１LDKで和室を寝室にしている。家賃10万。二階建ての一階")
