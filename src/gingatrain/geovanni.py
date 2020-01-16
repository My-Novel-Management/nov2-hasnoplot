# -*- coding: utf-8 -*-
"""Episode: 10-2.ジョバンニの気持ち／銀河鉄道の夜
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
def sc_main2(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("2.ジョバンニの気持ち",
            sana.talk("違うんです。これを見て下さい"),
            _.do("先生に$tsuruの持ち込み原稿を見せる"),
            noto.do("驚き言葉を失う"),
            sana.explain("それを読めば先生の原稿から僅かに表現を変えただけの代物だとすぐに分かる"),
            noto.talk("どういうことなんだ？"),
            sana.talk("$tsuruさんの知人の編集から先生の原稿の写しをもらって、それを書き換えて別の出版社に持ち込んだそうです"),
            noto.do("混乱している"),
            noto.talk("何故そんな真似を？"),
            sana.talk("書けなかったからです。才能が枯れていたのは先生ではなく$tsuruさんの方だったんです"),
            _.explain("自殺の原因が盗作という禁断の手札を手にしてしまったことだった",
                "それについて彼の姉に出会って話を聞いてきた",
                "姉はこう言っていた",
                "小説を書くことよりも先に本を出すことの方が大切だったみたいですと"),
            noto.talk("だから、あんなに生き急いで見えたのか"),
            sana.talk("先生は言いましたね",
                "作家には本を出すことよりもっと大切な仕事があると",
                "でも$tsuruさんにとっては本を出すことの方が大事だった"),
            noto.talk("本を出すことが作家だと、彼は思っていたんだ",
                "けれどね、本を出すのは副次的なことで、一番大切なのは自分にしか書けない小説を書くということ",
                "上手くなくてもいい、まとまってなくてもいい",
                "自分の魂を削ってそこに何かしらを込めたものなら、それを読んだ人の心は動く",
                "そしてそう信じることが作家にとって何よりも大事なんだ"),
            sana.think("先生は本当の作家だ、と感じた"),
            noto.talk("君ともこういう話ができるようになったね"),
            _.do("微笑んで、先生は封筒を渡す"),
            sana.talk("いいんですか？"),
            noto.talk("だって君は$meの担当編集なんだろう？"),
            )

## episode
def ep_geovanni(w: World):
    return w.episode("2.ジョバンニの気持ち",
            ## NOTE
            sc_main2(w),
            )
