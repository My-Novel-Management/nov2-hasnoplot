# -*- coding: utf-8 -*-
"""Episode: 檸檬
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
    return w.scene("1.洋梨",
            sana.think("どうして自分も小説を書いているのだろうか、と疑問に"),
            sana.talk("意味ないのに"),
            sana.think("でも学生時代に作家を目指していた頃の気持ちを思い出す"),
            sana.talk("意外と楽しいかも"),
            sana.do("同僚から連絡がきて、短編掲載枠に先生以外の作家を打ち込むことになったらしい、と言われる"),
            sana.do("先生に連絡を取ろうとするが、繋がらない"),
            sana.talk("なんでこの時代にスマホも持ってないんですか！"),
            sana.go("出かける"),
            )

def sc_main2(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("2.蜜柑",
            sana.do("何とか先生の原稿を待ってもらう話をつけてくる"),
            sana.do("せめてプロットくらいないのかと言われるが、大丈夫です、と答えるしかなかった"),
            sana.do("編集の仕事をしつつ、小説を書く"),
            sana.do("スマホで執筆"),
            sana.do("寝ながら電車も多々あった"),
            sana.do("シェアハウスの友人に相談したり、読んでもらったり"),
            sana.do("何とかして完成させた"),
            sana.talk("先生、書き上がりました"),
            sana.do("先生のところに原稿を持っていく"),
            )

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
def ep_main(w: World):
    return w.episode("檸檬",
            ## NOTE
            sc_main1(w),
            sc_main2(w),
            sc_main3(w),
            sc_main4(w),
            )
