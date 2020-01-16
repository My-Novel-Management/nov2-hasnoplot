# -*- coding: utf-8 -*-
"""Episode: 4-2.蜜柑／檸檬
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
    return w.scene("2.蜜柑",
            sana.do("何とか先生の原稿を待ってもらう話をつけてくる"),
            sana.do("せめてプロットくらいないのかと言われるが、大丈夫です、と答えるしかなかった"),
            sana.do("編集の仕事をしつつ、小説を書く"),
            sana.do("スマホで執筆"),
            sana.do("寝ながら電車も多々あった"),
            sana.do("シェアハウスの友人に相談したり、読んでもらったり"),
            sana.do("何とかして完成させた"),
            sana.talk("先生、書き上がりました"),
            sana.do("先生のところに原稿を持っていく"),
            )

## episode
def ep_orange(w: World):
    return w.episode("2.蜜柑",
            ## NOTE
            sc_main2(w),
            )
