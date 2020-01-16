# -*- coding: utf-8 -*-
"""Episode: 1-2.憤れ編集者／走れメロス
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
    fuka = W(w.fukaya)
    return w.scene("2.憤れ編集者",
            sana.explain("呼びつけられ、怒鳴られると思ったら、産休になった先輩の代わりに新しく作家の担当になってもらうという話だった"),
            sana.do("ほっとしたところに、$fukayaから大量の引き継ぎ"),
            sana.talk("先輩、出産直前まで仕事するつもりだったんですか？"),
            fuka.talk("だって先生、$meじゃないと書かないって言うだもん",
                "ちょっとねえ、一癖ある先生なのよ"),
            sana.do("資料に目を通す"),
            sana.explain("純文学の地方文学賞を受賞し、そこからここの元編集長で今の社長が声をかけて売り出した作家だった"),
            sana.do("$Sも名前は聞いたことがある"),
            sana.talk("それで何故第二文芸部の方に？"),
            sana.explain("一文が一般書籍、二文が主に漫画やアニメ、ライトノベルを扱う部署になっていた"),
            fuka.talk("まあ、色々あってね。それもおいおい説明するけど、とにかく今日は顔通しと、頼んでおいた短編原稿をもらってこないと"),
            sana.talk("いきなりハードですね"),
            fuka.do("急に苦しみだして、救急車を"),
            fuka.talk("大丈夫大丈夫。けど、ごめんね。誰か手のあいてる人についてきてもらって"),
            fuka.go("いってしまう"),
            sana.talk("あーあ、前途多難だわ"),
            )


## episode
def ep_angryeditor(w: World):
    return w.episode("2.憤れ編集者",
            ## NOTE
            sc_main2(w),
            )
