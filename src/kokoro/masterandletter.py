# -*- coding: utf-8 -*-
"""Episode: 7-4.先生と手紙／こころ
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
def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("4.先生と手紙",
            sana.come("先生のアパートにやってくる"),
            sana.do("留守でも掃除をしたりしている"),
            sana.think("世話女房だな、と苦笑"),
            sana.think("結婚相手はいないの？　と訊かれたことを思い出し"),
            sana.talk("先生？　ないない"),
            sana.do("と、本棚の後ろに隠されていたアルバムを見つける"),
            sana.do("更にその中に古くなった手紙が挟まれていた", "日記の破った欠片だ"),
            sana.think("最初にそれは隠しておきたかったものだと思った"),
            sana.do("その書き出しを読んで驚く"),
            sana.talk("本当のことなの？"),
            _.explain("そこには友人を殺したのは自分だと書かれていた"),
            )

## episode
def ep_master_and_letter(w: World):
    return w.episode("4.先生と手紙",
            ## NOTE
            sc_main4(w),
            )
