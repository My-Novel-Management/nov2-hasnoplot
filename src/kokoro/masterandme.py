# -*- coding: utf-8 -*-
"""Episode: 7-1.先生と私／こころ
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
def sc_newyeargreeting(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("新年の挨拶",
            sana.come("レンタルだが着物でやってくる"),
            sana.do("会社にやってくる"),
            sana.do("出社している人たちに挨拶"),
            sana.do("パソコンでチェック"),
            sana.do("電話やメールで挨拶や返信をして回る"),
            sana.do("一通り終わってから、先生のところに向かう"),
            sana.go(),
            camera=w.sana,
            stage=w.on_heroffice,
            day=w.in_visitgrave, time=w.at_midmorning,
            )

def sc_beout(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生は不在",
            sana.come("折角なので着物姿を見せようと思ってきたが"),
            sana.talk("あれ？　いない"),
            sana.do("電話してみるが出ない"),
            sana.do("合鍵で開けてみるが、寝ている訳でもない"),
            sana.do("と、書き置きを見つけた"),
            sana.talk("え？"),
            stage=w.on_hisapart,
            )

def sc_waiting(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("待ち合わせ",
            sana.come("先生の書き置きにあったので、いつもの喫茶店にやってくる"),
            noto.talk("やあ"),
            noto.do("モーニングを食べている"),
            sana.talk("よく$meが来るって分かりましたね"),
            noto.talk("もう二ヶ月以上の付き合いだからね。そろそろ寝癖まで分かるようになる"),
            sana.talk("え！"),
            noto.talk("あはは。冗談だよ"),
            noto.talk("それより、少し車を出してもらいたくてね"),
            sana.talk("いいですよ"),
            stage=w.on_mastercafe,
            )

def sc_inthecar(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("車の中で",
            sana.talk("もっと頼ってもらっていいんですよ"),
            noto.talk("以前のように担当が一人の作家だけ抱えていればいいという時代ではないからね"),
            noto.talk("時々眠そうにしているのを知っているよ"),
            sana.talk("すみません"),
            noto.talk("長編を書き上げる前にね、どうしても行っておきたかったんだ"),
            sana.talk("どこですか？"),
            noto.talk("大切な人の墓参りだ"),
            stage=w.on_car,
            )

def sc_visit_grave(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("墓参り",
            w.comment("沙奈は先生につきそい、知らない誰かの墓参りにやってくる"),
            sana.do("先生に連れられてやってくる"),
            sana.do("何も言わない先生について歩く"),
            noto.do("ある墓の前で立ち止まる"),
            sana.do("墓には「$tsuru」とあった"),
            noto.talk("あけましておめでとう"),
            sana.do("先生を一人にして、少し離れておく"),
            noto.do("何か小声で話している"),
            sana.think("確か学生時代の友人で、自殺したんだったかしら、と思い出す"),
            noto.talk("ありがとう。行こうか"),
            camera=w.sana,
            stage=w.on_hiscemetery,
            )

## episode
def ep_master_and_me(w: World):
    return w.episode("1.先生と私",
            ## NOTE
            sc_newyeargreeting(w),
            sc_beout(w),
            sc_waiting(w),
            sc_inthecar(w),
            sc_visit_grave(w),
            )
