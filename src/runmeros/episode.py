# -*- coding: utf-8 -*-
"""Episode: 走れメロス
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
    return w.scene("1.走れ編集者",
            sana.do("電車を降りて、小さな体で必死に駅構内を走っていく"),
            sana.do("大きなカバンを二つも下げた小柄な女が走るのを、周囲はどう見ているだろう"),
            sana.do("それでも必死だ"),
            sana.do("そして転ぶ。ストッキングが破れる"),
            sana.talk("ああ、もうつらーい"),
            sana.think("トラックが迫ってきて、引かれたら異世界に行けるんだろうか、なんて考えたり"),
            sana.think("王、と呼ばれる新編集長の顔を思い出す"),
            )

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

def sc_main3(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("3.座れ編集者",
            noto.talk("新しい編集か？　座れ"),
            noto.do("笑みもなくすごむ"),
            sana.do("ただただおそれ、どうしようと"),
            sana.think("作家の言葉を尊重する",
                "それが教えだった"),
            sana.do("言われた通りに座る", "ストッキングの足で正座", "スカートで来なければよかったと"),
            )

def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("4.脱げ編集者",
            sana.talk("な、何を……"),
            noto.talk("だから脱げと言っているんだ",
                "その上着だけじゃない", "まずは全部脱いで裸になってもらおう"),
            sana.think("最悪だ、と思った"),
            sana.think("先輩はちょっと癖があると言っていたけれど、ちょっとどころじゃない",
                "これはＳランクだ", "最悪のＳだった"),
            )

## episode
def ep_main(w: World):
    return w.episode("走れメロス",
            ## NOTE
            sc_main1(w),
            sc_main2(w),
            sc_main3(w),
            sc_main4(w),
            )
