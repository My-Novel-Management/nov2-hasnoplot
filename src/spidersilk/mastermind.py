# -*- coding: utf-8 -*-
"""Episode: 3-4.先生のマインド／蜘蛛の糸
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
def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("4.先生のマインド",
            sana.talk("それじゃあ本当にプロットどころか、どんな話を書こうというアイデアもないんですね？"),
            noto.talk("たった原稿用紙三十枚だろう？", "一晩で書いてしまうよ"),
            sana.talk("じゃあどうして原稿がないんですか？", "先輩と約束した締切ですよね？"),
            noto.talk("そこらにでも隠れてるんじゃないかな？"),
            sana.think("この作家、Ｓランクだと直感する",
                "ちなみに作家はその実力とは別に正確別にラベリングされている",
                "Ｓは最悪のＳだ"),
            sana.do("何故か$Sが短編小説を書くことになってしまった"),
            )


## episode
def ep_mastermind(w: World):
    return w.episode("4.先生のマインド",
            ## NOTE
            sc_main4(w),
            )
