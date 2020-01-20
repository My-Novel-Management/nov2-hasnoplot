# -*- coding: utf-8 -*-
"""Episode: 8-3.第三章／金閣寺
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
def sc_stalker(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nose = W(w.nose)
    return w.scene("ストーカー被害",
            w.comment("最近何か妙なことが起こると思っていたら、ストーカーされていた"),
            sana.do("会社からの帰り道"),
            sana.do("駅を出て、歩く"),
            sana.think("最近身の回りで妙なことが起こる"),
            sana.think("つけられている風"),
            sana.do("コンビニに入って確かめる"),
            sana.do("気の所為と分かって、再びアパートに向かう"),
            camera=w.sana,
            stage=w.on_street,
            day=w.in_stalking, time=w.at_night,
            )

def sc_intimidation(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nose = W(w.nose)
    return w.scene("脅迫",
            sana.do("薄暗い路地"),
            sana.hear("パトカーのサイレン"),
            sana.do("スマホで友人に連絡。だが二人ともバイトだった"),
            sana.think("確かに自分をつける影が一つある"),
            sana.do("慌てる"),
            sana.do("メッセージが送られてくる"),
            sana.think("それはまるで自分が書いたような文面"),
            sana.think("これって"),
            sana.talk("ひょっとして$noseさんですか？"),
            sana.do("立ち止まって振り返ると、フードの男が笑った"),
            noto.talk("知ってたか。もうあんたの家そこだろ。お茶くらい出してくれよ"),
            )

def sc_manstalk(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira = W(w.nirasaki)
    nose = W(w.nose)
    return w.scene("男の話",
            nose.be("くつろいでいる"),
            sana.talk("一体何のつもりなんですか"),
            nose.talk("編集だろう？　だったら小説の話だ"),
            sana.talk("持ち込み、ということですか？　だったら明日出版社の方に"),
            nose.do("机を叩く"),
            nose.talk("先生の原稿もってんだろ？　見せてくれ"),
            sana.talk("何言ってるんですか？"),
            nose.talk("あの人には世話になった。$meはもう一度あの人を喰らう"),
            sana.talk("くう？"),
            nose.talk("ノベルイーター。$meはそう呼んでる。良い小説をパクるんだよ。それで$meの小説にする。そうすれば、また復活できる"),
            sana.talk("あなたは盗作で、もうこの業界じゃ"),
            nose.talk("名義も何も変えればいいだけさ。芸能人と同じだ。顔が出る商売じゃない。名前もいくらでも使える"),
            nose.talk("$meに、小説を書かせろ"),
            nose.do("せまる$S"),
            sana.talk("やめて"),
            nose.talk("少女趣味はないんだがな……あんた、意外といいもの持ってるな"),
            sana.talk("お願い……"),
            nira.talk("おーい"),
            sana.talk("$nirasakiさん！"),
            nira.talk("あ、わりぃ。お邪魔だったか"),
            nose.talk("さっさと出てけよ、このボンクラ編集"),
            nira.talk("あんた……そっか。$meさ、どうしても許せないことってのがあんだ"),
            nira.talk("一つは初対面の人間への暴言、もう一つは女への暴力だよ！"),
            nira.do("$noseを殴りつける"),
            nose.go("逃げていく"),
            nira.talk("おい待て！"),
            sana.talk("待って"),
            sana.do("裾を掴み"),
            sana.talk("ごめんなさい……"),
            stage=w.on_herhouse,
            )

def sc_cooldown(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira = W(w.nirasaki)
    nose = W(w.nose)
    return w.scene("落ち着いてから",
            sana.do("温かいものを飲んで落ち着いた$S"),
            nira.talk("もういいか？"),
            sana.talk("なんで、来てくれたんですか？"),
            nira.talk("ちょっと$notoのことで話があったんだが、まあいいよ、もう"),
            sana.talk("先生が何か？"),
            nira.talk("そんなことより、警察にいっといた方がいいぞ。あの手のは一度じゃすまない"),
            sana.talk("分かってる。けど"),
            nira.talk("しばらくホテルか何か、別の場所にいけ。それくらい何とかなるだろ？"),
            sana.talk("意外と気遣いなんだ"),
            nira.talk("バカかよ。事件は勘弁なんだよ"),
            nira.go(),
            sana.think("悪くないやつだ、と思った"),
            )

## episode
def ep_chapter3(w: World):
    return w.episode("3.第三章",
            ## NOTE
            sc_stalker(w),
            sc_intimidation(w),
            sc_manstalk(w),
            sc_cooldown(w),
            )
