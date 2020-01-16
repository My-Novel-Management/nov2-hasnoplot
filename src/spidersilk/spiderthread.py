# -*- coding: utf-8 -*-
"""Episode: 3-3.蜘蛛のスレッド／蜘蛛の糸
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
    return w.scene("3.蜘蛛のスレッド",
            sana.talk("それで、その原稿はどこなんです？", "今話してくれましたよね？"),
            noto.talk("ない"),
            sana.talk("ない、んですか？", "全然？"),
            noto.talk("君が書けばいいじゃないか"),
            sana.do("突然そんなことを言い出す"),
            sana.talk("問題をすり替えないで下さい", "小説は特殊技能なんですよね？",
                "だから専門家である先生が書かないといけない", "$meはその原稿をちゃんと本にする義務がある"),
            noto.talk("なんだか最近は編集が書くとかいったことも聞くよ", "原稿三十枚程度なら君でも書けるだろう",
                "それにライトノベルには詳しいと豪語したじゃないか", "なら書いてみればいい"),
            sana.do("墓穴を掘った"),
            sana.talk("先生の作品でなければ掲載する価値がないんですよ",
                "$meの書いたものなんて誰が待っているっていうんですか"),
            )

## episode
def ep_spiderthread(w: World):
    return w.episode("3.蜘蛛のスレッド",
            ## NOTE
            sc_main3(w),
            )
