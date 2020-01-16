# -*- coding: utf-8 -*-
"""Episode: 7-2.私と両親／こころ
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
    return w.scene("2.私と両親",
            sana.do("$notoに連れられて、彼が懇意にしている洋食屋に"),
            sana.do("近代文学がずらりと並ぶ本棚に囲まれている。文学亭"),
            sana.talk("こんな場所があったんですね"),
            noto.talk("今月で閉店だそうだ"),
            sana.think("時代の厳しさを教わる"),
            sana.do("先生に自分の家庭環境のことを話す"),
            sana.do("小さい頃から本に触れて育った"),
            sana.do("作家の夢は諦めたけれど、本に関わる仕事がしたいと思った"),
            noto.talk("君も書けばいいんだ", "あの短編は良かった"),
            sana.talk("流石に編集をやりながらは無理ですよ", "もうあんな大変な真似はできません"),
            sana.think("そう答えつつも、本当にそうなんだろうか？", "と自問していた"),
            )

## episode
def ep_parents_and_me(w: World):
    return w.episode("2.私と両親",
            ## NOTE
            sc_main2(w),
            )
