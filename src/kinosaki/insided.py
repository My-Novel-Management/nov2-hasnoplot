# -*- coding: utf-8 -*-
"""Episode: 6-4.心の内にて／城の崎にて
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
def sc_exchange_condition(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("交換条件",
            w.comment("長編原稿を捨てた先生に対して、沙奈も書くからもう一度チャレンジしてと頼む"),
            sana.do("何かを破る音で目覚める"),
            sana.talk("先生何してるんですか！"),
            noto.talk("ああ、おはよう。朝起きて読んでみたら、こんな作品は$meのものじゃないと分かった"),
            sana.talk("けど"),
            noto.talk("やはり無理だったよ。もう小説は書けない。こんなものしか書けないようでは……"),
            sana.talk("先生言ったじゃないですか。最初から完成している小説なんかないって"),
            sana.talk("書き上げてからがスタートなんだって"),
            sana.talk("一緒に作り上げていきませんか？", "駄作かどうかは作者が決めることじゃない。$meが決めることでもない"),
            sana.talk("読んだ誰かが面白かったかどうか、心を打ったかどうかです"),
            sana.talk("評価なんて百人いたら百通りなんです"),
            noto.talk("じゃあ君はあれを校正すれば売り物になったと思うのか？"),
            _.talk("$meの作品として楽しめたとでも？"),
            sana.do("答えられない"),
            noto.talk("残念ながら$meは、いや、作家というのは卑屈の塊なんだよ"),
            _.talk("いつだって、心のどこかでは誰かに褒めてもらいたい。すごいと言ってもらいたい。そういう気持ちが隠れている"),
            _.talk("でもおおっぴらには口にできないから、常に自信なさげか、逆に見栄っ張りで、自分の作品がどうして評価されないって思ってる"),
            _.talk("けどいざ書いている自作を読んでみると、これ本当に面白いのだろうかと悩む"),
            _.talk("そんなことの繰り返しなんだ"),
            _.talk("多くの作家が書けなくなる、続きを出せなくなるのは、何も売上が全てじゃない"),
            _.talk("やがて行き詰まるんだ"),
            _.talk("自分の全てを否定されたような気になる"),
            sana.talk("先生！"),
            sana.do("抱き締める"),
            sana.talk("分かってます"),
            sana.talk("でも、$meは待ってますから"),
            noto.talk("そうやって君たち編集はいつだって"),
            sana.talk("じゃあ、$meも書きます"),
            _.talk("長編小説を、書きます。それならいいでしょう？"),
            noto.talk("え？"),
            sana.talk("短編の時のように$meに教えながらなら、きっと素晴らしいものが書けますよ。先生は、そういう方がいいんです"),
            noto.talk("できるだろうか"),
            sana.talk("一人では無理でも、二人なら、可能性も大きくなります"),
            noto.talk("そうか。やってみようかな"),
            sana.talk("はい"),
            camera=w.sana,
            stage=w.on_oldinn,
            day=w.in_backhome, time=w.at_morning,
            )

def sc_intrain(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("電車の中にて",
            sana.be("帰りの新幹線車内"),
            sana.do("眠りこける先生を見て"),
            sana.do("写真を取る"),
            stage=w.on_train,
            )

def sc_unknown_sender(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("差出人不明の手紙",
            w.comment("旅から帰ると差出人不明の手紙が入っていた"),
            sana.do("キャリーバッグと共に帰ってくる"),
            sana.do("自分宛てのかわいらしい封筒を見つけて"),
            sana.talk("誰だろ？"),
            sana.do("何も書いてないが、開ける"),
            sana.do("写真が入っていた。それは先生とホテルに行った時のものだ"),
            sana.talk("何これ……"),
            sana.think("気持ち悪さが湧き上がる"),
            stage=w.on_herhouse,
            )

## episode
def ep_insided(w: World):
    return w.episode("4.心の内にて",
            ## NOTE
            sc_exchange_condition(w),
            sc_intrain(w),
            sc_unknown_sender(w),
            )
