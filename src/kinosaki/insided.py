# -*- coding: utf-8 -*-
"""Episode: 4.心の内にて／城の崎にて
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
    return w.scene("4.心の内にて",
            noto.do("見せようと思ったはずの原稿を、$Sはゴミ箱に捨てた"),
            sana.talk("どうして"),
            noto.talk("こんなものはね、何にもならない",
                "ただ手なりで書いただけの、文章の羅列だ",
                "それを偉そうに君に見せて、これが小説だ、なんて語れはしない", "昔から$meはそんなつまらなくて卑屈な人間だと思い出した"),
            sana.do("悲しそうに見えた"),
            sana.think("けれど作家が一度破り捨てたものを拾ってまで本にしようとは思ってはいけない",
                "作家とはプライドの塊なのだ", "それを担当編集は何よりも理解してあげなくてはならない",
                "たとえ会社を敵に回しても", "そう言われたことを思い出す"),
            sana.talk("わかりました", "でも、そうですね、$meも書きます",
                "その代わり先生ももう一度挑戦して下さい", "納得がいくものができるまで待ちますから",
                "それまでの穴埋めは$meが何とかします", "何とかしてみせます"),
            sana.think("つい勢いで言ってしまったことを、後悔していた"),
            sana.do("長編小説を書きながら唸る"),
            sana.talk("$meには無理だ……"),
            )


## episode
def ep_insided(w: World):
    return w.episode("4.心の内にて",
            ## NOTE
            sc_main4(w),
            )
