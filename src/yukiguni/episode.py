# -*- coding: utf-8 -*-
"""Episode: 雪国
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
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("1.夕景色",
            sana.do("先生のデビュー作をやっと手に入れて読んでいる"),
            sana.explain("作品はライトノベルとは全然違う、純文学よりの文芸作品で、地元の金沢の情景がよく滲んでいた",
                "切ない三角関係だった"),
            sana.come("駅を降りて"),
            noto.talk("やあ、遅かったね"),
            sana.talk("雪なんて聞いてません"),
            sana.do("足元はスニーカーだが、滑ってしまう"),
            noto.talk("あら？　君は雪国の人間じゃあなかったんだな"),
            sana.talk("知らない訳じゃないですけど、こんなには降ったことないです"),
            noto.talk("じゃあ行こうか"),
            sana.do("先生が自分で運転していた", "まだ昨年免許を取ったところだという"),
            sana.talk("$meが運転します"),
            noto.talk("いやいやここは$meの庭みたいなものだよ"),
            sana.do("早速道を間違えていた"),
            sana.come("先生の生家にやってくる"),
            )

def sc_main2(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("2.手鞠歌",
            asahi.talk("ちょっといいかしら"),
            sana.talk("何ですか？"),
            sana.do("彼女に古い喫茶店に連れて行かれる"),
            asahi.talk("ここでよく彼ら三人が集まって話してたのよ"),
            asahi.talk("知ってるかしら"),
            asahi.talk("$full_notoはね、人殺しなのよ"),
            )

def sc_main3(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("3.雪国抄",
            sana.come("妙なことを聞かされて、帰ってくる"),
            sana.do("先生の家族と食事"),
            sana.do("夜は晩酌に付き合う"),
            noto.talk("意外と飲むんだね？"),
            sana.talk("父親は全然なんですけど、母親が酒豪で。福岡出身だから？"),
            noto.talk("あちらはすごいとは聞くけどねえ"),
            noto.talk("そういえば$asahiさんと会ったんだってね", "彼女、よく嘘をつくから気をつけて"),
            sana.talk("なんか先生が人殺しだって言われましたよ"),
            sana.do("空気が固まる"),
            noto.talk("まあ、違うともいえないんだけど"),
            noto.talk("時がきたら話すよ"),
            )

def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("4.続雪国",
            noto.talk("ああ、心配ない", "ちゃんと長編は考えているよ"),
            sana.do("そう言われて安堵する"),
            sana.think("しかし、$asahiに言われたことが気になっていた"),
            )


## episode
def ep_main(w: World):
    return w.episode("雪国",
            ## NOTE
            sc_main1(w),
            sc_main2(w),
            sc_main3(w),
            sc_main4(w),
            )
