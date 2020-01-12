# -*- coding: utf-8 -*-
"""Episode: 私の思い出
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
def sc_hisnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生の短編小説",
            sana.do("渡されたその原稿に目を通す"),
            _.do("おじいさんと孫娘の話だ"),
            _.do("亡くなる前に、彼女に読み書きを教える",
                "ただそれだけの話なのに温かくて寂しくて、小さい頃に祖父母が亡くなった時のことを思い出す"),
            _.do("その話を読み終えて、自分の中に湧き上がった気持ちが、かつて味わったものだと気づく"),
            _.talk("これ、読んだことある", "でもあれってもっと概要だけだった"),
            noto.talk("昔書いたものだ",
                "その時は長すぎるし難しいということで、おじいさんが教えるところと、亡くなって娘さんが何を感じたか、",
                "というだけに短くしたからね"),
            sana.think("それは$Sが小さい頃に触れた、初めてといっていい「小説」だった",
                "本は好きだったけれどそれまでは物語ばかりで、どんなお話なんだろうという楽しみ方しかしていなかったところが、",
                "小さなパンフレットに載っていたその断片に書かれた文章が、美しかったのだ",
                "またそれで表現された物語が、少し悲しくて、けれど美しかった"),
            _.talk("先生、$meは"),
            _.do("言葉にならず、ただ涙が滲んだ"),
            )


## episode
def ep_mymemory(w: World):
    return w.episode("懐かしい気持ち",
            ## NOTE
            ##  - 先生の書いた短編を読んで、自分の大事な作品が先生のものだったと気づく
            sc_hisnovel(w),
            note="4.折角書いた短編が無意味だったと知り落ち込む沙奈に、先生は自分の書いた短編を読ませる。それは小さい頃に感動した話だった",
            )
