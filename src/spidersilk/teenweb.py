# -*- coding: utf-8 -*-
"""Episode: 3-1.若者のネット／蜘蛛の糸
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
def sc_beangry(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("激怒",
            sana.come("帰ってくる"),
            gero.be(),
            azu.be("二人は食事中"),
            gero.talk("あら、どうしたん？"),
            azu.talk("大丈夫？"),
            sana.look("額に冷えピタ"),
            sana.talk("大丈夫くないです。Ｓランクに遭遇しました"),
            sana.do("とりあえずスーツを脱いで、戻ってくる"),
            sana.talk("とにかくご飯"),
            azu.talk("はいはい"),
            azu.do("$sanaの分を入れてきてあげる"),
            sana.talk("もうほんと最悪の作家の担当になったのよ"),
            sana.explain("今日あった出来事を二人にぶちまけた"),
            gero.talk("脱げって何そらパワハラセクハラ酷いがな"),
            azu.talk("でも$noto先生って『$masternovel1』の作家さんでしょ？"),
            _.talk("あれ書いてる人がそんなこと言うなんて"),
            sana.talk("作品と人間性は関係ないわよ。酷い作家でも人気作や才能の塊みたいな人いるし、それは何も小説に限った話じゃない"),
            _.talk("ただ裏方は大変だってだけ"),
            _.talk("大昔から変わらないけど、でもそもそも今みたいな職人気質の作家なんて少数だっただろうし、小説書いて発表してそれで食べていこうなんて変人だからね"),
            azu.talk("酷い"),
            sana.talk("だから昔の話。今はどんな芸能だってそれなりに技術を高めれば誰にでもチャンスがあるというのが実態だし"),
            _.talk("$azuminoだって今書いてる作品がデビュー作になるかも知れないでしょ？"),
            azu.talk("どうだろ"),
            sana.talk("$geroだっていつ絵がバズるかわかんないじゃん。そういうもんだよ"),
            gero.talk("バズってもＢＬだからどんな顔したらいいか分からんがね"),
            sana.talk("でも好きなことで人気になるんだからいいじゃない。どうだ！　ってやってやればいいのよ"),
            _.talk("変に恥じらったり恐縮するから漬け込まれるだけで、断るものは断固として断る、受け入れるものは受け入れる。この姿勢が大事なのよ"),
            sana.talk("だからこそあの先生許すまじ！"),
            sana.do("ご飯をもりもり食べて"),
            camera=w.sana,
            stage=w.on_herhouse_int,
            day=w.in_firstmeet, time=w.at_night,
            )

## episode
def ep_teenweb(w: World):
    return w.episode("1.若者のネット",
            ## NOTE
            sc_beangry(w),
            )
