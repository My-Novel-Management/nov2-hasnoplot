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
def sc_thinkingnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("長編小説を考える",
            w.comment("先生と約束をしたので長編の構想を練ってみる"),
            sana.be("テーブルにノートパソコンを広げている"),
            gero.come("やってきて"),
            gero.talk("また残業？　たまには息抜きせんと頭爆発してまうで？"),
            sana.talk("先生と約束したのよ。$meも長編小説を書きますって"),
            gero.talk("あんたそうやっていつも安請け合いするから余計な残業増えるんちゃう？"),
            sana.think("$geroの言うことに一理あった"),
            azu.come("バイトから戻ってきて"),
            azu.talk("ただいまー。疲れちゃった、さすがに"),
            sana.talk("おつかれー"),
            gero.talk("あ、何かお土産？"),
            azu.have("手にはケーキ"),
            sana.talk("長編って言われても、普段から考えてないと何も出てこない"),
            _.talk("ねえ。$azuminoはいつもどうしてるの？"),
            azu.talk("え……考えたこと、ない"),
            _.talk("何か書きたい映像が浮かんで、それが徐々に話になっていく……みたいな感じです"),
            _.talk("今応募中の長編だって、結局細かく決めたりせずに書き始めたから、最後の方はぐだっちゃったし"),
            _.talk("たぶん駄目なんだろうな"),
            sana.talk("ちゃんと小説の体はなしてたんだから、心配しなくても一次は通るわよ。そこから先なんだから"),
            azu.talk("$sanaにそう言ってもらえると、なんだか嬉しい"),
            sana.talk("けど、やっぱりそういう風に黙っててもなんか湧いてくるくらいなのが作家なのかな。$meは向いてないな"),
            azu.talk("人それぞれだよ。何かテーマを決めて書かないと駄目って人もいるし"),
            sana.talk("テーマか"),
            gero.talk("普段から飢えてないといけないんだがね"),
            _.talk("$meは男に飢えている。だからＢＬを描く"),
            sana.talk("それつながりが変だよ"),
            gero.talk("変で結構！　変態で結構！"),
            _.talk("世界を変えるのは一般人でなく変態なのである"),
            sana.do("その元気さに笑う"),
            camera=w.sana,
            stage=w.on_herhouse_int,
            day=w.in_thinknovel, time=w.at_night,
            )

def sc_beout(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生は不在",
            sana.come("外回りのついでに先生のアパートに立ち寄ってみる"),
            sana.talk("先生？　おはようございます？"),
            sana.do("インタフォンを押すが返答がない"),
            sana.think("まだ寝てるのかな"),
            sana.do("電話を鳴らしてみるが、出る様子もない"),
            sana.think("じゃあ失礼して"),
            sana.do("合鍵を使ってドアを開ける"),
            _.do("中を確認するが先生はいない"),
            sana.talk("あれ？　いない"),
            sana.do("と、テーブルの上に書き置きを見つけた"),
            sana.talk("え？"),
            stage=w.on_hisapart,
            day=w.in_visitgrave, time=w.at_afternoon,
            )

def sc_waiting(w: World):
    sana, noto = W(w.sana), W(w.noto)
    chiyo = W(w.chiyoda)
    return w.scene("待ち合わせ",
            sana.come("先生の書き置きにあったので、いつもの喫茶店にやってくる"),
            noto.be("ご飯を食べ終えて、まったりと座っている"),
            chiyo.be("$notoに食後のコーヒーを出している"),
            chiyo.talk("あら、$sanaちゃん。いらっしゃい"),
            noto.talk("やあ"),
            noto.do("モーニングを食べ終えてお腹を擦っている"),
            sana.talk("よく$meが来るって分かりましたね"),
            noto.talk("もう二ヶ月以上の付き合いだからね。そろそろ寝癖まで分かるようになる"),
            sana.talk("え！"),
            noto.talk("あはは。冗談だよ"),
            noto.talk("それより、少し車を出してもらいたくてね"),
            sana.talk("はい。いいですよ"),
            noto.do("ゆっくりとコーヒーを飲む"),
            sana.talk("じゃあ、一旦会社に戻って取ってきます"),
            sana.go("出ていく"),
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

## episode
def ep_master_and_me(w: World):
    return w.episode("1.上　先生と私",
            ## NOTE
            sc_thinkingnovel(w),
            sc_beout(w),
            sc_waiting(w),
            sc_inthecar(w),
            )
