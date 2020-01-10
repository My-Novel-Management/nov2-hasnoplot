# -*- coding: utf-8 -*-
"""Episode: 何故か短編を書くことに
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
def sc_mywiriting(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("短編小説を書く",
            sana.talk("なんでそうなるんですか！"),
            _.do("君も書いてくれ、と言われて憤る"),
            noto.talk("君に教えていると小説のことを、まだこんなに考えることができるのだな、と気づいた",
                "それないっそ君に書かせてみればまた$meも小説を書けるような気がするんだ"),
            sana.talk("だからって"),
            noto.talk("君は約束してくれただろう？", "脱ぐ以外だったら何でもしますって"),
            sana.talk("それは言葉の綾というもので"),
            noto.talk("書かない、と言ってる訳じゃない",
                "君は$meに小説を書かせたいし、原稿が欲しい",
                "$meもできることなら書きたいと思っている",
                "そのお手伝いを頼んでいるんだ",
                "それにもし駄目だったら君の小説で穴埋めすればいいし"),
            sana.talk("そんなゴーストライターみたいな真似できません！"),
            noto.talk("最終的に$meが直せば誰が書いたかなんて分からないよ",
                "そもそも最近の読者でそこまで読み込むことができる人がどれくらいいるだろう"),
            _.do("大量のラノベを見やる"),
            sana.talk("いますよ", "$meは読者さんのこと信じてますし、",
                "何より$me自身が先生の作品を読みたいんです", "待ってるんです"),
            noto.talk("つまり、書いてくれるってことだね、君も短編を"),
            sana.talk("え？"),
            noto.talk("$meに書かせるには君が書く必要がある",
                "考える余地などないだろう？", "時間もないことだし、早速"),
            sana.talk("先生！"),
            noto.do("お茶を立てる準備を始める"),
            _.talk("これがないとね"),
            sana.talk("ほんと、勘弁してください……"),
            _.do("そんな彼女の前にはノートパソコンがあり、画面が真っ白なワープロソフトが起動されていた"),
            )


## episode
def ep_writenovel(w: World):
    return w.episode("短編小説を書くことに",
            ## NOTE
            ##  - 何故か沙奈も短編小説を書くことになった
            sc_mywiriting(w),
            )
