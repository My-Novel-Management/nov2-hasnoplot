# -*- coding: utf-8 -*-
"""Episode: 2-2.猫と小説／吾輩は猫である
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
def sc_aboutmaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生について",
            noto.talk("で、用件は理解した。もう挨拶は済んだろう。帰り給え。$meは忙しいんだ"),
            sana.do("どう考えても本を読みながら猫とたわむれていたとしか思えない"),
            sana.think("先生の取扱説明書を思い出す"),
            sana.think("一度へそを曲げたらその日は何もできない"),
            _.think("気分が乗らないと執筆しない"),
            _.think("ただし小説の話を始めると長い。話は大好きである"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_firstmeet, time=w.at_afternoon,
            )

def sc_introduction(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("自己紹介",
            sana.talk("えっと、オーディションなんですね？　$me一人ですが"),
            noto.talk("$fukayaさんも最初にやったよ。彼女はなんでも応えてくれて、実に素晴らしい編集だった"),
            _.talk("作家と編集はお互いのことをよく知る必要がある、そうは思わないかね？"),
            sana.talk("そういわれれば、そうですけど"),
            noto.talk("では始めてくれ"),
            sana.talk("は、はい"),
            sana.talk("$full_sanaです。歳は二十五になりました"),
            noto.talk("なぜ編集の仕事を？"),
            sana.talk("本が、好きだったから"),
            _.talk("中学の頃はただの本好きな少女でした。高校になってから作家を目指したこともあります"),
            _.talk("でもそれは挫折しました"),
            _.talk("大学時代は文芸部に所属こそしましたが、それでも書くよりは読んだり、作ったりするのを手伝う方が楽しいと感じて"),
            _.think("話しているうちに自分が編集に感じた魅力を思い出す"),
            noto.talk("ありがとう。素直な人なんだ、$sana君は。うん。悪くない"),
            sana.talk("ありがとうございます"),
            )

def sc_aboutnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("小説とは",
            noto.talk("では、そんな君にとって小説とは何かね？"),
            sana.think("どう答えようと迷う"),
            noto.talk("おそらく人間の数だけその解釈というのはある。で、君はなんと考えている？"),
            sana.talk("作家の人生です"),
            noto.talk("ふーん。その心は？"),
            sana.talk("小説は基本的に文字、文章だけで物語を紡ぐものです。そこには必然、その作者が何を考え、普段何を見て、どう感じているかが書かれます"),
            _.talk("それはその作家の人生といってもいい"),
            _.talk("物語はフィクションですが、そこに描かれたものは作者にとって真実なんです"),
            _.talk("だからこそ$meは小説を読むと同時に作者の人生を、その哲学を感じます"),
            noto.do("じっと腕組みをして聞いている"),
            sana.talk("じゃあ先生にとっての小説って何なんですか？"),
            noto.talk("何だろうね"),
            _.talk("それこそ十歳の頃からの付き合いだからもう四十年ほどになる。空気や水、そういってもいい"),
            _.talk("身の回りにあって、普段摂取しているのに、その実、何なのかはよく分からない"),
            _.talk("小説とは何か？　と問い続けることが、$meにとっての小説かも知れない"),
            )

## episode
def ep_cat_and_novel(w: World):
    return w.episode("2.猫と小説",
            ## NOTE
            sc_aboutmaster(w),
            sc_introduction(w),
            sc_aboutnovel(w),
            )
