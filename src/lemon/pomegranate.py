# -*- coding: utf-8 -*-
"""Episode: 4-4.柘榴／檸檬
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
    return w.scene("4.柘榴",
            sana.do("連絡を受けて、兄の知人の作家が雑誌掲載枠を勝ち取ったと聞いた"),
            sana.talk("すみません先生", "$meの力及ばずです"),
            noto.talk("君の知り合いなんだろう？", "もっと喜ぶべきじゃないのか？"),
            noto.talk("作家というのは常に評価にさらされる",
                "望んだ通りにいつも掲載される、出版されるというのは、ごく一部の限られた作家だけだ",
                "その表に出ている作家、作品の下には無数の誰にも読まれることのない作品が埋まっている"),
            noto.do("先生は何か小さな冊子を取り出す"),
            sana.talk("これは？"),
            noto.talk("読んでみるといい"),
            sana.explain("それはパンフレットに掲載された掌編だった"),
            sana.talk("これ……"),
            sana.think("小さい頃に読んだことのあるものだった"),
            noto.talk("君の作品は$meが読者になった", "荒削りだが、そこに描かれた素直な気持ちは素晴らしいものだったよ"),
            sana.talk("ありがとうございます"),
            noto.talk("さて、これで君は$meの担当合格だ", "新作を頼むよ"),
            sana.talk("え？"),
            noto.talk("言っただろう？", "この人に頼みたいと思ったらその時は正式に採用しようと"),
            noto.do("一筆書いて渡す"),
            sana.do("そこには「担当編集$full_sanaにお願いします」と"),
            )

## episode
def ep_pomegranate(w: World):
    return w.episode("4.柘榴",
            ## NOTE
            sc_main4(w),
            )
