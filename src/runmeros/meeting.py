# -*- coding: utf-8 -*-
"""Episode: 先生に会う
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
def sc_hisorder(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生の命令",
            noto.talk("じゃあまずは服を脱いでくれるかな"),
            sana.talk("え……"),
            _.do("絶句した"),
            _.think("何を言われたのか分からず考え直し、再度尋ねてみる"),
            _.talk("聞き間違えだと思うんですが、今何と？"),
            noto.talk("だから服を脱いでくれと言った",
                "コートだけじゃない", "そのブラウスにスカートも",
                "当然その後は下着もだ"),
            sana.talk("脱げません"),
            _.do("即答する"),
            noto.talk("君はその覚悟もなくここにやってきたというんだね？"),
            sana.talk("編集者としての矜持とか言うつもりはありません",
                "もし$meが女でなかったとしても、そう言われましたか？"),
            noto.talk("何が楽しくて男に服を脱がせようとするんだ？",
                "そもそも$meは男性はよこさないように言っているから、それでもここに来るというなら、男性ではないだろう",
                "だから同じだよ", "脱いでくれないか、と言う"),
            sana.talk("それは、服を脱ぐことが原稿を受け取ることの条件になっている、と考えてよろしいんでしょうか？"),
            _.think("昔のすごい作家列伝で夢物語的に語られることはあったが、まさか本当に女性編集に向かって脱げという作家がいるなんて"),
            noto.talk("原稿？　なんのことだろう",
                "今日は産休に入る$fukayaさんの代役がいくからよろしくと彼女に言われただけだ"),
            sana.talk("じゃあ$fukaya先輩もここで？"),
            noto.do("笑っている"),
            sana.think("先輩に騙された",
                "とんでもない作家についてしまった、と後悔を始めていた"),
            )


## episode
def ep_firstmeet(w: World):
    return w.episode("はじめての先生",
            ## NOTE
            ##  - 先生と出会ったのだが
            ##  - いきなり「脱げ」と言われた
            sc_hisorder(w),
            note="4.やっと探し当てた先生を家に連れ戻すと、そこで沙奈は先生に「脱げ」と命令されたのだった",
            )
