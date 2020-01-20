# -*- coding: utf-8 -*-
"""Episode: 6-3.死の淵にて／城の崎にて
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
def sc_confession(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生の告白",
            noto.talk("大切な友人だった"),
            _.talk("将来、ともに作家になろうと誓った"),
            _.talk("しかし$meだけが作家になり、彼は屍になった"),
            _.talk("$meは作家になったことを時々後悔している"),
            _.talk("彼が作家になっていれば、こんなことにはならなかったんじゃないかって"),
            camera=w.sana,
            stage=w.on_oldinn,
            day=w.in_trip_kinosaki, time=w.at_night,
            )

def sc_inmydream(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("夢の中",
            sana.do("夢を見ていた"),
            sana.do("小さい頃の夢だ"),
            sana.do("迷子になって怖くて泣いていたら、そこに父親が来てくれた"),
            sana.do("病気で父親を失っているからか、$Sにとって父のイメージはいつもあの日の父親だった"),
            sana.do("目覚めると、先生が側にいてくれて、父親を思い出して、また安眠に戻った"),
            stage=w.on_dream,
            )

## episode
def ep_edgeindead(w: World):
    return w.episode("3.死の淵にて",
            ## NOTE
            sc_confession(w),
            sc_inmydream(w),
            )
