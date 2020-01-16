# -*- coding: utf-8 -*-
"""Episode: 2-3.猫とビール／吾輩は猫である
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
def sc_main3(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("3.猫とビール",
            noto.talk("小説にお酒はつきものでね"),
            noto.talk("ちょっとビールを買ってきてもらえるかね"),
            sana.go("仕方なく買い物に"),
            sana.explain("近所のコンビニで、気の良さそうなおばさん",
                "一緒に買ったおつまみで、また先生？　担当変わったのね、と言われる始末"),
            sana.come("両手いっぱいにして戻ってくる"),
            sana.do("先生が消えている"),
            sana.talk("どこですか！"),
            sana.do("探し回る"),
            sana.do("近所を歩き回ってやっと見つけた"),
            noto.talk("いや、こいつがね"),
            noto.do("猫を抱き上げて"),
            noto.talk("この自由さは見習いたい"),
            sana.think("充分自由人だがな、と思ったり"),
            )


## episode
def ep_cat_and_beer(w: World):
    return w.episode("3.猫とビール",
            ## NOTE
            sc_main3(w),
            )
