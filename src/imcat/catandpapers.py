# -*- coding: utf-8 -*-
"""Episode: 2-4.猫と原稿／吾輩は猫である
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
    return w.scene("4.猫と原稿",
            sana.talk("今、なんて？"),
            noto.talk("だからないと言ったんだ", "プロットすらないよ"),
            sana.talk("嘘ですよね？"),
            noto.talk("$meは小説の中以外での嘘が嫌いでね"),
            sana.talk("プロットもないんですか？　ほんとに？"),
            sana.think("激しく混乱する"),
            sana.explain("今日原稿（初稿）をもらう手はずになっていると先輩からは聞いていた"),
            sana.talk("ちょっと確認します"),
            sana.do("電話する"),
            sana.talk("あの、先輩、今先生の家なんですけど"),
            sana.explain("そういうところがあるから気をつけて、がんばって原稿むしり取ってきてね、と笑われる"),
            sana.talk("探します"),
            noto.talk("だからないんだって"),
            sana.think("$Sは絶対に原稿を探し出すと決意した"),
            )

## episode
def ep_cat_and_manupapers(w: World):
    return w.episode("4.猫と原稿",
            ## NOTE
            sc_main4(w),
            )
