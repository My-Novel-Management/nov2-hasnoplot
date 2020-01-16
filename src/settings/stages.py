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
    w.setTexture("on_hercampany_int",
            [
                "内装", "事務机が整然と並ぶ",
                "壁", "クリーム色",
                ])
    w.setTexture("on_hercampany_ext",
            [
                "立地", "オフィス街のビルが並ぶ中",
                ])
    w.setTexture("on_herhouse_int",
            [
                "間取り", "３ＬＤＫ、３人で洋間をそれぞれの寝室に",
                "家賃", "10万／月",
                "階数", "三階／三階建て（エレベータなし）",
                ])
    w.setTexture("on_hisapart_int",
            [
                "間取り", "１ＬＤＫ、和室を寝室に、Ｌは仕事場",
                "家賃", "10万／月",
                "階数", "一階／二階建て",
                ])
