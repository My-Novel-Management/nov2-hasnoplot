# -*- coding: utf-8 -*-
"""Episode: 10-1.カムパネルラはどこに消えた？／銀河鉄道の夜
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
def sc_whereishe(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("先生はどこへ？",
            w.comment("バイト君から先生失踪の報を受けた沙奈"),
            sana.talk("え？　ちょっと分からない", "どうして先生が病院から消えるの？", "何かのミステリ？"),
            tsuchi.voice("$meだって分かりませんよ",
                "朝来たら看護師さんが騒いでて", "とてもあんな火傷で出歩いていいもんじゃないって"),
            sana.talk("とにかく今からそっち行くから近所探しててて！"),
            tsuchi.voice("ててて、って。落ち着いて下さいよ"),
            sana.talk("落ち着ける訳ないでしょ！"),
            _.think("酷く混乱していた"),
            _.do("そもそも原稿を書き上げたまま寝ていて、気づくともう十時を回っている"),
            _.do("慌てて顔だけ洗った"),
            camera=w.sana,
            stage=w.on_heroffice,
            day=w.in_vanishmaster, time=w.at_midmorning,
            )

def sc_investigation(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("先生の捜索",
            sana.come("病院にやってくる"),
            sana.talk("あ、いた。ね、見つかった？"),
            tsuchi.talk("それがあの先生、窓から出てったんですよ！"),
            sana.talk("は？"),
            sana.explain("説明を受けると、個室のカーテンを結んで三階から中庭に降りて、そこからタクシーで出て行ったというのだ"),
            sana.talk("なんてこと……"),
            sana.think("$fukaya先輩から聞いた缶詰伝説を思い出す",
                "それはホテルだったが、抜け出して、クラブに酒を飲みに行っていたという"),
            sana.talk("ほんと作家ってやつは！"),
            sana.talk("とにかく手分けして探すから"),
            tsuchi.talk("探すってどこを？"),
            sana.talk("バイクで近所回って、見かけた人いないか当たってみて",
                "$meは先輩にも連絡して、行きそうな場所当たってみる",
                "何かあったら連絡ちょうだいよ！"),
            stage=w.on_hospital,
            )

def sc_anywhere(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("どこにもいない",
            sana.come("行きつけの喫茶店にやってくる"),
            sana.talk("あの、先生来てませんか？"),
            sana.explain("簡単に説明して、何か手がかりがないか訊いてみるが、分からないとのことだった"),
            sana.talk("ほんと、もう！"),
            stage=w.on_mastercafe,
            )

def sc_accident(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("人身事故報道",
            sana.come("やや苦手なバーにやってくる"),
            sana.talk("すみません、先生探してるんですが"),
            sana.explain("だが何も分からないまま"),
            sana.explain("そこにテレビでちょうど中央線の人身事故報道"),
            sana.talk("え？"),
            sana.explain("ちょうど年齢や背格好が同じに"),
            sana.do("そこに$fukayaから連絡"),
            sana.talk("はい",
                "え？", "玉川上水？",
                "でも先生が自殺だなんて", "そもそもあそこってそんな水流れてましたっけ？"),
            stage=w.on_masterbar,
            )

def sc_river(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("玉川上水",
            sana.come("先生と歩いた玉川上水に"),
            sana.talk("来てない、やっぱり"),
            sana.do("呼びかけながら探しつつ、何か違う、と感じている"),
            sana.think("そもそも何故病院を出たんだろう"),
            sana.think("締切のため？"),
            stage=w.on_tamagawariver,
            )

def sc_hurry(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("急げ",
            w.comment("沙奈はある場所に急いだ"),
            sana.do("車である場所に急いだ"),
            sana.think("お願い、間に合って"),
            sana.do("やがて見えてくる"),
            sana.do("太宰の墓がある場所。そこに彼の親友の墓もある"),
            stage=w.on_car_int,
            )

## episode
def ep_campanella(w: World):
    return w.episode("1.カムパネルラはどこに消えた？",
            ## NOTE
            sc_whereishe(w),
            sc_investigation(w),
            sc_anywhere(w),
            sc_accident(w),
            sc_river(w),
            sc_hurry(w),
            )
