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
            ## NOTE:
            ##  冒頭文：ではみなさんは、そういうふうに川だと言われたり、乳の流れたあとだと言われたりしていた
            sana.be("スマホを手に固まっている"),
            sana.voice("ジョバンニさん。あなたはわかっているのでしょう"),
            sana.hear("そんな声が頭の中に降ってきた"),
            _.think("酷く混乱していた"),
            tsuchi.voice("あの、聞いてます？"),
            sana.talk("え？　ちょっとどういうことなの？", "どうして先生が病院から消えるの？", "何かのミステリ？"),
            tsuchi.voice("$meだって分かりませんよ",
                "朝来たら看護師さんが騒いでて", "とてもあんな火傷で出歩いていいもんじゃないって"),
            sana.talk("とにかく今からそっち行くから近所探しててて！"),
            tsuchi.voice("ててて、って。落ち着いて下さいよ"),
            sana.talk("落ち着ける訳ないでしょ！"),
            _.think("正気を保てる気がしない"),
            _.do("そもそも原稿を書き上げたまま寝ていて、気づくともう十時を回っている"),
            _.do("慌てて顔だけ洗った"),
            ## NOTE
            ##  慌てた心境と、最終回の騒動を想像させる
            camera=w.sana,
            stage=w.on_heroffice_int,
            day=w.in_vanishmaster, time=w.at_midmorning,
            )

def sc_investigation(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("先生の捜索",
            sana.come("病院にやってくる"),
            sana.talk("あ、いた。ね、見つかった？"),
            tsuchi.be("ロビィでうろうろしている"),
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
            ## NOTE
            ##  改めて状況説明
            area=w.Mitaka,
            stage=w.on_hospital_int,
            time=w.at_beforenoon,
            )

def sc_writervisit(w: World):
    sana, noto = W(w.sana), W(w.noto)
    yuza = W(w.yuzawa)
    return w.scene("記者さんお願い",
            sana.come("病院から出てくる"),
            yuza.be("待ち構えていて"),
            yuza.talk("どうです、先生の具合は"),
            sana.talk("あー！"),
            yuza.talk("相変わらずうるさいな、あんた。それより送りつけたアレ見たか？　もっと仔細をあげつらって全部指摘してやってもいいんだぞ？"),
            w.eventPoint("先生の盗作騒動", "$yuzawaは原稿オリジナルを持っている"),
            sana.talk("その件について相談があるんですけど、その前に"),
            yuza.talk("は？　病院から消えた？　なんだいそりゃミステリか？"),
            sana.think("同じ感想に苦笑"),
            sana.talk("何でここまで来たんですか？"),
            yuza.talk("何って先生の取材に"),
            sana.talk("足です！"),
            yuza.talk("バイクだよ。取材は足が命だからな。都内じゃ車よりバイクの方が"),
            sana.talk("お願い。乗せて。先生を探さないといけないの。先生見つけたら好きなだけ取材してくれて構わないから！"),
            yuza.talk("ああ、そういうことなら"),
            ## NOTE
            ##  誰でも味方につけてしまう沙奈の能力発動
            ##  湯沢はあまり活躍シーンないので、この道中で多少彼の人となりを見せておく。それがどこか親心みたいなものに繋がっているように
            ##  沙奈はファザコンであること
            stage=w.on_parking,
            )

def sc_anywhere(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    yuza = W(w.yuzawa)
    chiyo = W(w.chiyoda)
    return w.scene("どこにもいない",
            sana.come("行きつけの喫茶店にやってくる"),
            yuza.come("一緒にやってきて"),
            chiyo.be("掃除をしている"),
            sana.talk("あの、先生来てませんか？"),
            chiyo.talk("最近見てないわ。入院したって聞いたけどぉ？"),
            sana.explain("簡単に説明して、何か手がかりがないか訊いてみるが、分からないとのことだった"),
            sana.talk("ほんと、もう！"),
            ## NOTE
            ##  千代田さんもここくらいしか出番がないので、印象づけておく（あるいは後でちょろっと出す）
            stage=w.on_mastercafe,
            time=w.at_noon,
            )

def sc_accident(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi, fukaya = W(w.tsuchiura), W(w.fukaya)
    yuza = W(w.yuzawa)
    utsu = W(w.utsu)
    return w.scene("人身事故報道",
            sana.come("やや苦手なバーにやってくる"),
            yuza.come("一緒にやってくる"),
            utsu.be("グラスを磨いている"),
            sana.talk("すみません、先生探してるんですが"),
            utsu.talk("また逃げられたんでしょうか"),
            sana.talk("そうじゃないんですけど、そうでもあるんです"),
            utsu.look("苦笑している"),
            sana.explain("だが何も分からないまま"),
            sana.explain("そこにテレビでちょうど中央線の人身事故報道"),
            sana.talk("え？"),
            sana.explain("ちょうど年齢や背格好が同じに"),
            sana.do("そこに$fukayaから連絡"),
            fukaya.voice("先生見つかった？"),
            sana.talk("いえ、まだです"),
            fukaya.voice("そっか。今日、なのよね"),
            sana.talk("何がですか？"),
            fukaya.voice("ちょっと気になることがあって"),
            sana.talk("はい","え？", "玉川上水？"),
            fukaya.voice("$meが行ってあげられたらいいんだけど、もしもの時は$sana、お願いね"),
            sana.think("先生にまさかはないと思いたい。でも自殺しないとは断言できなかった"),
            ## NOTE
            ##  バーもここくらいなので、印象づけておく
            stage=w.on_masterbar,
            )

def sc_river(w: World):
    sana, noto = W(w.sana), W(w.noto)
    yuza = W(w.yuzawa)
    tsuchi = W(w.tsuchiura)
    return w.scene("玉川上水",
            sana.come("先生と歩いた玉川上水に"),
            yuza.come("一緒に歩いている"),
            sana.talk("来てない、やっぱり"),
            yuza.talk("まさか太宰治よろしく誰かと心中、いや、誰もいなけりゃ単なる自殺か"),
            sana.talk("妙なこと言わないで下さいよ"),
            yuza.talk("だがな、盗作した作家の末路ってのは本当に悲惨なもんだぜ",
                "それが一度有名になった作家なら尚の事",
                "世間は忘れても自分は一生忘れねえ。そういう業の深い行いが盗作なんだぜ"),
            sana.think("盗作について、考え込む"),
            sana.do("何か違う、と感じている"),
            sana.talk("そもそも何故先生は病院を出たんだろう"),
            sana.think("締切のため？"),
            yuza.talk("あるいは証拠隠滅か"),
            sana.talk("あの、$yuzawaさん。お願いがあるんですが"),
            yuza.talk("な、何だよ？"),
            sana.talk("あなたが持っている$tsuruさんの原稿、見せてくれませんか？　確かめたいことがあるんです"),
            w.eventPoint("先生の盗作騒動", "敦賀の原稿を見せてもらうよう頼む"),
            ## NOTE
            ##  ここで沙奈は気づく
            stage=w.on_tamagawariver,
            )

def sc_hurry(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("急げ",
            w.comment("沙奈はある場所に急いだ"),
            sana.be("運転席で慌てた様子でいる"),
            sana.do("車である場所に急いだ"),
            sana.think("お願い、間に合って"),
            sana.do("やがて見えてくる"),
            sana.do("太宰の墓がある場所。そこに彼の親友の墓もある"),
            stage=w.on_car_int,
            ).omit()

## episode
def ep_campanella(w: World):
    return w.episode("1.カムパネルラはどこに消えた？",
            ## NOTE
            sc_whereishe(w),
            sc_investigation(w),
            sc_writervisit(w),
            sc_anywhere(w),
            sc_accident(w),
            sc_river(w),
            sc_hurry(w),
            )
