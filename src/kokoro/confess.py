# -*- coding: utf-8 -*-
"""Episode: 手紙の告白
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
def sc_hisconfess(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("罪の告白",
            sana.do("そこに書かれていたことを読んで驚いた"),
            _.think("これ、本当のことなの？"),
            _.do("$Sは注意深く手紙を読み返す"),
            _.do("紙が黄ばみ、古くなっていたが、そこに書かれた癖のある文字は先生のものに思えた"),
            _.talk("これが本当だとしたら"),
            _.do("そこには自分のデビュー作は、亡くなった友人が応募する予定だった原稿を盗作したものだと書かれていたのだった"),
            )


## episode
def ep_hisletter(w: World):
    return w.episode("先生の手紙",
            ## NOTE
            sc_hisconfess(w),
            )
