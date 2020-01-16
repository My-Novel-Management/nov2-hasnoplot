# -*- coding: utf-8 -*-
"""Episode: 2-1.猫と先生／吾輩は猫である
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
    return w.scene("1.猫と先生",
            sana.talk("嫌です"),
            sana.explain("突然脱げと言われたが、$Sはそれをすぐに断った"),
            noto.talk("君の仕事は何？"),
            sana.talk("先生の担当編集です", "先生が良い作品を書いて本にできるようにお手伝いと橋渡しをする仕事です"),
            noto.talk("じゃあ脱ぐべきだな",
                "君が脱ぐことで$meは作品を書くことができる", "もし脱がなければ原稿は永遠に完成しない"),
            sana.think("面倒な作家が現れた"),
            sana.explain("なんとかいいすくめて、脱がなくて済ませる"),
            sana.do("足元に猫がやってきて、いつく"),
            noto.talk("へえ。そいつは人にあまり興味を示さないので有名なんだが、なるほどね"),
            )


## episode
def ep_cat_and_master(w: World):
    return w.episode("1.猫と先生",
            ## NOTE
            sc_main1(w),
            )
