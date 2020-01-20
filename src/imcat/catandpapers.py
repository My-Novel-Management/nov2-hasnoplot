# -*- coding: utf-8 -*-
"""Episode: 2-4.猫と原稿／吾輩は猫である
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
def sc_havenoplot(w: World):
    sana, noto = W(w.sana), W(w.noto)
    fukaya = W(w.fukaya)
    return w.scene("プロットはない",
            noto.talk("ああ、だからないよ", "原稿どころかプロットもない"),
            sana.talk("え"),
            sana.do("慌てて自分の手帳を確かめる"),
            sana.talk("あの先生、$meは今日先輩から原稿をもらってくるように頼まれているんです。わかりますか？"),
            noto.talk("先輩というのは$fukayaさんのこと？"),
            sana.talk("そうです"),
            noto.talk("ないよ。それにそんな約束したかなあ"),
            sana.talk("いやいや、ここに書いてありますよ！"),
            sana.do("引き継ぎ資料を見せて"),
            noto.talk("ああ、確かにこの可愛らしい書き込みは彼女だね"),
            _.talk("しかし困ったなあ。ほんとに何もないよ。とにかくまだ資料を読んでいる段階でね"),
            _.do("手にしているのは猫の写真集だ"),
            sana.talk("ほんとに？"),
            sana.talk("あの、確認します"),
            sana.do("$fukayaに連絡する"),
            fukaya.voice("ああ、そうきたか。先生あれこれ理由つけてなかなか書かないから、がんばって！"),
            sana.talk("がんばってじゃないです！"),
            sana.talk("本当にないんですか？　メモくらいは"),
            noto.talk("探してみる？"),
            noto.do("部屋を見ると、すごく散らかっていた。寝室も、キッチンも"),
            noto.talk("最近$fukayaさん忙しくてなかなか顔出してくれなかったからねえ"),
            sana.think("編集は家政婦じゃないし"),
            sana.think("最悪中の最悪だと認定した"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_firstmeet, time=w.at_afternoon,
            )

## episode
def ep_cat_and_manupapers(w: World):
    return w.episode("4.猫と原稿",
            ## NOTE
            sc_havenoplot(w),
            )
