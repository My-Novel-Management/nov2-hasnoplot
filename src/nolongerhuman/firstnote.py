# -*- coding: utf-8 -*-
"""Episode: 9-1.はしがき／人間失格
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
    return w.scene("1.はしがき",
            sana.talk("はぁ"),
            _.explain("先生が無事に入院したことで、原稿が締め切りに間に合わないことは確実となった"),
            sana.talk("とにかく、今度こそは穴埋めを"),
            _.explain("何とか$Sがダミーの原稿を出すことで誤魔化す。これしかなかった"),
            sana.do("必死に原稿に向かう"),
            _.think("学生時代に作家を目指して書いていた頃を思い出す"),
            _.think("執筆は孤独な作業だし、見返すと、駄作を書いている実感しかない"),
            _.think("先生に言われたことを思い出す"),
            noto.voice("駄作でも最後まで書き切ることだ",
                "作品は一度書いて終わりじゃない。何度も書き直して、どんどん質を上げることができる",
                "しかし書き終えていない作品、特に頭の中にあるだけで無様でも言葉にまったくなっていない作品は、それだけで書き上がった駄作よりも価値は低い",
                "頭の中の傑作は咲かない花と同じだ"),
            sana.do("パソコンに向かう"),
            _.do("そこに連絡が来る",
                "監視しているバイト君", "先生に付き合いきれないと愚痴"),
            )

## episode
def ep_firstnote(w: World):
    return w.episode("1.はしがき",
            ## NOTE
            sc_main1(w),
            )
