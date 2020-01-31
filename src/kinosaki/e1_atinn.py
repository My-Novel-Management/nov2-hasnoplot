# -*- coding: utf-8 -*-
"""Episode: 6-1.旅の宿にて／城の崎にて
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
def sc_station(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("新幹線のホームにて",
            sana.come("大きなキャリーバッグと共にやってくる"),
            noto.talk("そんなに沢山の荷物が必要なのかね？"),
            sana.talk("先生が長編執筆に取り掛かるというから、その準備もあるんです"),
            noto.talk("のんびりいこうよ。まだ先は長いよ"),
            sana.talk("締切は来月ですからね。絶対に書いて下さいよ？"),
            noto.talk("分かってるよ"),
            sana.explain("何故か先生の福利厚生も兼ねて、城之崎旅行に一泊二日で行くことになりました"),
            w.eventStart("城之崎旅行"),
            ## NOTE
            ##  いきなり旅行に出かけるところから。事情は簡単に道中で解説。取材旅行をしたい、と言われたので
            ##  また少しだけ「恋愛」を匂わせると共に、ストーカーされているのを感じさせておく
            camera=w.sana,
            area=w.Tokyo,
            stage=w.on_station,
            day=w.in_trip_kinosaki, time=w.at_midmorning,
            )

def sc_enjoymaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("楽しそうな先生",
            sana.do("先生と横並びで座っている"),
            sana.do("新幹線は右手に富士山が、とかアナウンス"),
            noto.talk("そういえば名古屋だっけ？"),
            sana.talk("名古屋は叔母の家です。$meは隣の方です"),
            sana.think("たまには帰ってきて、と言っていたことを思い出す"),
            sana.think("でも帰ると結婚とかの話になるので、嫌だった"),
            ## NOTE
            ##  車内でLINEで下呂とやり取りをすること。今回はサブで下呂のWeb絵師の問題について、ちょっと触れます
            ##  またそれが「城の崎にて」の死を考える部分の引用ともなります
            stage=w.on_train_int,
            )

def sc_kinosaki(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("城之崎",
            sana.talk("これ、素敵ですね！"),
            noto.talk("出たよ", "それ以外に言うことがないのか", "語彙が貧弱だよ"),
            sana.talk("いいんですよ"),
            sana.do("初めて見る温泉街の雰囲気に感動している"),
            noto.talk("雑誌時代にどこか取材旅行とかしなかったの？"),
            sana.talk("$meのやっていたのは傾倒が違って、子ども向けのものだったり、半分くらいは食べ物でした"),
            sana.talk("農業体験とか、その手のはいっぱいやりましたよ"),
            sana.do("二人で歩く"),
            sana.do("浴衣で歩く温泉客とすれ違い、声をあげる"),
            noto.do("楽しそうな先生"),
            noto.talk("ああ、ここだ。ずっと世話になっていたんだけれど、最近経営者が変わってね"),
            noto.talk("予約は取っておいてくれたんだよね？"),
            sana.talk("ばっちりですよ"),
            ## NOTE
            ##  城之崎の街の空気感を
            area=w.Kinosaki,
            stage=w.on_street,
            time=w.at_afternoon,
            )

def sc_atinn(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("宿に二人",
            sana.do("案内された部屋は二人部屋だった"),
            sana.talk("あの、頼んでおいたのは別々の部屋のはずだったんですが"),
            sana.explain("勘違いして夫婦と思って二人部屋にしちゃったと言われて"),
            noto.talk("まあいいじゃないか", "間違いも起こらないだろう、君と$meじゃ"),
            sana.talk("それはそうかも知れませんけど……"),
            _.think("流石にまずい、という認識はある"),
            noto.talk("スキャンダルになるような人間でもないし、一泊のことだ。いいじゃないか"),
            sana.talk("まあ、先生がそう言われるなら……"),
            sana.explain("こうして一つの部屋で一晩を明かすことになった"),
            ## NOTE
            ##  テンポよくここまで進み、同室で、とお決まりの流れを
            stage=w.on_oldinn,
            )

## episode
def ep_atinn(w: World):
    return w.episode("旅の宿にて",
            ## NOTE
            sc_station(w),
            sc_enjoymaster(w),
            sc_kinosaki(w),
            sc_atinn(w),
            )
