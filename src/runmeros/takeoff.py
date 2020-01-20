# -*- coding: utf-8 -*-
"""Episode: 1-4.脱げ編集者／走れメロス
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
def sc_rejection(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("編集拒否",
            sana.talk("え"),
            sana.do("絶句する"),
            sana.talk("あの！　先生！", "$me、本日付で先生の担当編集になった$full_sanaです！"),
            _.talk("$fukayaさんは引き継ぎの際に体調を崩されたので、$me一人で来ました"),
            _.talk("あの、お願いします！", "とにかく中に入れて下さい！"),
            sana.do("反応がない"),
            _.think("中にいるのは分かっている"),
            _.think("居留守を使う作家に対しては騒ぐのが一番だが、関係を壊す可能性がある"),
            sana.do("先輩のメモを見る"),
            _.do("何か効果的なもの、食べ物とかで釣れないかと探る"),
            sana.talk("今日はいいお酒をお持ちしましたよ。どうですか？"),
            _.do("無反応"),
            sana.talk("○○屋のたい焼きです"),
            _.do("全く変わらない"),
            sana.talk("$fn_notoさん。別れたくないの！", "$me、どうしてももう一度あなたとやり直したいの"),
            _.talk("開けてくれないならここで朝まで座り込むから！"),
            _.talk("ずっと騒いでやるから！"),
            noto.talk("やめてくれ"),
            noto.do("顔を見せた"),
            camera=w.sana,
            stage=w.on_hisapart_ext,
            day=w.in_firstmeet, time=w.at_midmorning,
            )

def sc_takeoff(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("脱げ編集者",
            sana.come("何とか中に入れてもらえた$Sだったが"),
            noto.do("警戒して睨みつけている"),
            noto.look("着物姿で長身、無精髭"),
            sana.think("どうしよう、と困惑"),
            _.think("ここまで警戒されたのは初めてだった"),
            sana.talk("えっと、先程は玄関先で騒いでしまい申し訳ありませんでした"),
            noto.talk("そうだな"),
            sana.talk("でも先生が中に入れてくださらないから"),
            noto.talk("編集という人間はいつもそうやって作家のせいにする"),
            sana.talk("いえ。今のは言葉のあやで"),
            noto.talk("言葉を適当に使うな。編集だろう？"),
            sana.talk("すみません"),
            noto.talk("本当にすまないという気持ちがあるのなら、脱げ"),
            sana.talk("は？"),
            noto.talk("誠意を見せるには言葉ではなく、何かしら実行して見せる必要がある。だから脱げ"),
            sana.talk("言葉のつながりがおかしいです。どうして脱げになるんですか？"),
            noto.talk("裸の付き合いという言葉を知らぬか？"),
            sana.talk("いやいや。何言ってるか分かりません"),
            noto.talk("$meは君が脱ぐまで何も話さない"),
            sana.think("あ、これ駄目な作家だ。Ｓランクだわ"),
            _.explain("作家には密かにランクがつけられている"),
            _.explain("それは作品の人気などもあるが、それよりも編集の扱いやすさによる"),
            _.explain("Ｓとは最悪のＳだ。つまり編集から一番嫌われるタイプの作家であった"),
            stage=w.on_hisapart_int,
            )

## episode
def ep_takeoffeditor(w: World):
    return w.episode("4.脱げ編集者",
            ## NOTE
            sc_rejection(w),
            sc_takeoff(w),
            )
