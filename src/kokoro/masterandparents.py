# -*- coding: utf-8 -*-
"""Episode: 7-3.先生と友人／こころ
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
def sc_riverside(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("川沿いを",
            sana.do("先生に連れ出され、歩いていた"),
            sana.explain("玉川上水は太宰治が心中したので有名な場所だ"),
            sana.explain("駅から井の頭公園までの散策路は今でも多くの人に愛されている"),
            noto.talk("少しだけ話しておこう"),
            noto.talk("これは作家としての資質"),
            camera=w.sana,
            stage=w.on_tamagawariver,
            day=w.in_visitgrave, time=w.at_afternoon,
            )

def sc_treasure_friend(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("友を大切に",
            sana.come("先生と井の頭公園まで歩く"),
            noto.talk("ここをよく歩くんだ。文豪たちも同じ気持ちだったのかな、なんて考える訳じゃないが、それでも同じような空気を吸っていれば偉くなれる気がする"),
            noto.do("表情が柔らかい"),
            noto.think("昔のことを思い出している"),
            noto.talk("デビューが決まり、こっちに出てきた頃に、右も左も分からなくてね。迷いながら歩いてたら、写真で見たことがある場所に出て"),
            noto.talk("それ以来、何かあるとここにくる"),
            noto.talk("君には友人はいるかね？"),
            sana.talk("今、シェアハウスしているんです。それぞれイラストレーターだったり、作家だったりを目指している、大切な友達です"),
            noto.talk("ああ、そうか。それは良いな"),
            noto.talk("昔は長屋といってね、ずっと繋がった沢山の狭い部屋を詰め込んだ大きな家があって、そこで同じような夢を抱く人間が暮らしたものだ"),
            noto.talk("友達は大切にしなさい。誰もがそう言う。その意味を、本当に理解できるのは、その友達を失った時だ"),
            noto.talk("人は失わなければ分からない。愚かな生き物でもある"),
            sana.explain("先生はやたらと友人に対して大切にしなさいと言った"),
            sana.think("何かあったのだろうが、それを聞いていいものかどうか、判断がつかなかった"),
            stage=w.on_tamagawariver,
            day=w.in_visitgrave, time=w.at_midmorning,
            )

## episode
def ep_master_and_parents(w: World):
    return w.episode("3.先生と友人",
            ## NOTE
            sc_riverside(w),
            sc_treasure_friend(w),
            )
