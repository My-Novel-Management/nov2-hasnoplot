# -*- coding: utf-8 -*-
"""Episode: 3-1.若者のネット／蜘蛛の糸
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
def sc_main1(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("1.若者のネット",
            sana.think("プロットすらないと言われたが、それくらいでは引き下がらない",
                "作家とは締切を伸ばすためなら何でもする生き物なのだ"),
            sana.talk("今どきパソコンもスマホもないなんて、どうやってやり取りしてたんですか！？"),
            sana.talk("ちょっと探します"),
            noto.talk("人の言うことは素直に聞いた方が良い"),
            sana.talk("締切を守らない作家に人権はありません"),
            sana.think("それは前の雑誌編集部での教えだった"),
            sana.do("$Sは家探しする"),
            sana.do("ついでに掃除もする"),
            noto.talk("そういえばお腹すいたなあ"),
            sana.talk("出前でも取りますか？", "最近は宅配サービスも充実してて"),
            noto.talk("料理できないの？", "$fukayaさんの味噌汁は絶品だったんだよなあ"),
            sana.talk("作れますよ、一応"),
            sana.do("何故か料理することに"),
            )


## episode
def ep_teenweb(w: World):
    return w.episode("1.若者のネット",
            ## NOTE
            sc_main1(w),
            )
