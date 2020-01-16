# -*- coding: utf-8 -*-
"""Episode: 8-4.第四章／金閣寺
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
    return w.scene("第四章",
            sana.do("その日は久々の休日で、午前中は睡眠にかまけて、午後から執筆作業に入った"),
            sana.do("先生のメモを見返す"),
            _.do("サブストーリーについて"),
            _.think("先生の告白について思い返す"),
            _.think("まだ信じられないでいた"),
            _.do("執筆に集中できずに飛び出す"),
            sana.talk("先生？"),
            _.do("街を探して歩く"),
            _.hear("と、消防車と救急車のサイレン"),
            _.go("急いで追いかける"),
            _.come("先生のアパート近く"),
            sana.talk("そんな……"),
            sana.do("火事で先生のアパートが燃えている"),
            sana.explain("古い木造で趣があるとか言っていたが火事に対してはこの有様だった"),
            noto.come("燃え盛るアパートから救出される"),
            noto.have("その手には原稿を持っている"),
            sana.talk("先生！"),
            sana.do("だがその原稿はほとんど焼けてしまっていた"),
            noto.talk("すまない。折角の原稿が"),
            sana.talk("そんなものより先生が"),
            noto.talk("原稿は作家の命だよ、$sana君"),
            noto.go("救急車で運ばれていく"),
            sana.think("今の言葉の意味をよく噛みしめる"),
            )

## episode
def ep_chapter4(w: World):
    return w.episode("4.第四章",
            ## NOTE
            sc_main4(w),
            )
