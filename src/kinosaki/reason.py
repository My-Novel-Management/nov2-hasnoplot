# -*- coding: utf-8 -*-
"""Episode: 書けなくなった理由
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
def sc_truth(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生から理由を聞く",
            noto.talk("$meはね、才能なんかこれっぽちもないんだよ"),
            sana.talk("何言ってるんですか？", "$meは先生の作品に感動して作家を、この業界を目指したんですよ？"),
            noto.talk("$meはずっとその彼の幻影を追いかけてきたんだ",
                "ただもうこの世に彼はいない",
                "死んだら勝ちなんだよ。勝ち逃げなんだよ",
                "人間の想像の中に逃げ込めば、もう勝ち目はない",
                "想像は無限だからね"),
            sana.talk("先生……"),
            _.think("いつになく弱気な先生が心配になる"),
            noto.talk("君に読んでもらった、$meが見ている作家見習いの作",
                "あれね……本当は$meなんだよ"),
            sana.talk("え？"),
            noto.talk("もう君の方がずっとよく書ける",
                "もともとだましだまし書いてきたものが、遂に無理になった",
                "才能はね、いつか枯れてしまうものなんだ"),
            sana.do("そう言った先生は寂しそうにおちょこを口に持っていった"),
            )


## episode
def ep_reason(w: World):
    return w.episode("書けなくなった本当の理由",
            ## NOTE
            sc_truth(w),
            note="4.先生の親友でライバルだった男性の自殺を聞かされ、それが先生の人生および小説のトラウマになっていると知る",
            )
