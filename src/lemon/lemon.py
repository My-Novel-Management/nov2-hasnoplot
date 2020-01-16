# -*- coding: utf-8 -*-
"""Episode: 4-3.檸檬／檸檬
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
    return w.scene("3.檸檬",
            sana.do("書き上げた短編を先生は読まずに捨てた"),
            sana.talk("どうしてですか？"),
            noto.talk("納得して書いたものなのか？", "とてもそうは思えない",
                "とりあえず書けば$meも書くだろう、約束だから間に合わせでもいいだろう、そんな空気を感じたから捨てた"),
            noto.talk("作家の前に魂の入っていない原稿を持ってくるな！"),
            sana.think("考え違いをしていた", "こんな風に真剣に怒鳴ることができる人とは思ってなかった"),
            sana.think("初めて自分で雑誌のコーナーを担当した時のことを思い出す",
                "あまり気乗りしなくて、適当でいいかとやっつけ仕事になったものを、当時の編集長は何も言わずにコーナーから外した"),
            sana.think("何故かと尋ねたら今の先生と同じことを言われた"),
            sana.talk("確かに先生の言われた通りです", "間に合わせで書いた作品です",
                "小説のていなどなしていないでしょう",
                "けど、$meは$meなりにがんばって書いたものです", "魂が入ってないとは思ってません"),
            noto.talk("それならこれを雑誌に掲載して、楽しみに待っている読者の目にさらしても大丈夫かね？"),
            sana.talk("え、それは"),
            noto.talk("確かに$meは言ったよ", "君が書くなら$meも書こうと",
                "掲載する保険にもなるじゃないかと", "でもそれが実際に掲載されると君は思わなかった",
                "なぜならそんなものは編集会議で落とされるに決まっているからだ",
                "そのつもりで書いたんだろう？"),
            sana.think("その通りだった"),
            sana.talk("$meのはいいんですよ、それよりも先生の原稿を"),
            noto.talk("ないよ"),
            sana.talk("え？"),
            noto.talk("$meは書いていない"),
            sana.talk("それは約束が違います！"),
            noto.talk("約束は正式な担当編集としかしない。君は$meの正式な担当になったのかね？"),
            noto.explain("#実は後でゴミ箱から拾って原稿を読んでいる"),
            )

## episode
def ep_lemon(w: World):
    return w.episode("3.檸檬",
            ## NOTE
            sc_main3(w),
            )
