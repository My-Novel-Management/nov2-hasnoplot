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
            ## NOTE
            ##  シェアハウスでの友人との会話が、一番沙奈の普段着を出すところ。言葉も荒っぽく、時に方言が出ること
            ##  またそれぞれが既に問題を抱えていることを示唆する
            camera=w.sana,
            area=w.Tokyo,
            stage=w.on_herhouse_int,
            day=w.in_firstmeet, time=w.at_night,
            )

def sc_atoffice(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, yone, king = W(w.nirasaki), W(w.yonezawa), W(w.king)
    return w.scene("会社にて",
            sana.come("やってくる"),
            sana.talk("おはようございます。あ……"),
            nira.be("自分の席に座ってパソコンを確認している"),
            nira.wear("黄色いパーカーにマスク、下は迷彩柄のカーゴパンツ"),
            nira.talk("よう"),
            sana.talk("インフル移さないで下さいよ"),
            nira.talk("もう大丈夫だよ。それよりあの$notoの担当なんだって？　ご愁傷さま"),
            sana.talk("ほんとは担当嫌だったから休んだとか、ないですよね？"),
            nira.talk("何言ってんだよ。これでもいっぱい作家抱えてて大変なんだよ"),
            nira.do("パソコンで校正作業。いっぱい赤を入れている"),
            sana.talk("うわぁ。誤字だらけ"),
            nira.talk("そうなんだよ。この先生いっつも同じ誤字ばかりでさ、参るわ"),
            sana.do("机の上には封筒。中には募集中の新人賞の応募原稿のプリントアウト"),
            sana.talk("ネット応募可にしてから大変ですよね。やたら同じの使いまわしてる人いるでしょ"),
            nira.talk("溺れるなんとかだからな。藁だって応募するさ"),
            sana.do("日程を確認する"),
            w.comment("ここで新人賞の日程も確認。安曇野も応募中"),
            sana.explain("この時の原稿の一つが$azuminoのものとは知らなかった"),
            stage=w.on_heroffice_int,
            day=w.in_secondmeet, time=w.at_midmorning,
            ## NOTE
            ##  インフル開けて出てくるのは一週間後だが、この日から出てくる予定にしておく
            ##  韮崎初登場なので、外見や雰囲気描写しておく
            )

## episode
def ep_teenweb(w: World):
    return w.episode("1.若者のネット",
            ## NOTE
            sc_beangry(w),
            sc_atoffice(w),
            )
