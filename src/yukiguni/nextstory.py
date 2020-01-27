# -*- coding: utf-8 -*-
"""Episode: 5-4.続雪国／雪国
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
def sc_newyearparty(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, tsuchi = W(w.nirasaki), W(w.king), W(w.tsuchiura)
    return w.scene("新年会にて",
            sana.explain("一月の十三日、午後からはホテルで会社の新年会が行われた"),
            sana.be("珍しくスカート姿で会場にいる"),
            tsuchi.be("だが穴あきジーンズ姿の$S"),
            sana.talk("こういうところに来る時はせめてもう少しマシな格好をしてきて"),
            tsuchi.talk("何言ってんすか。このジーンズ十三万すよ！"),
            sana.do("顔を覆う"),
            sana.talk("やっぱり先生来てくれなかったな"),
            nira.come("シャンペン片手にやってきて"),
            nira.talk("何やってんだよ。さっさと作家に顔合わせしてこい"),
            sana.talk("$meの担当してる人ほとんど来てないし"),
            nira.talk("別に自分の担当じゃなくてもいい。作家はみんな不安なんだから"),
            _.talk("とにかく声と名刺くらいは配っとけって。編集は人脈が命だ"),
            sana.talk("そういうもんですか"),
            nira.go("手を振って行ってしまう"),
            king.come("やってきて"),
            king.talk("どうかね。うまくやってるか？"),
            sana.talk("はあ"),
            king.talk("うちで書いてもらえそうな先生いたらツバつけといてよ"),
            king.go(),
            tsuchi.talk("なんか大変すね"),
            sana.talk("まあ、ね"),
            _.think("$nirasakiが言うことも分かってはいた。だが沢山に声をかけても覚えていなかったら意味がないだろう"),
            _.think("$fukayaから人脈は確かに大事だけど、それが名刺集めになってたら意味がないと言われたことを思い出す"),
            sana.talk("名刺を貰っても五分で顔も名前も忘れる。でも情熱をもって話せばそのことだけは覚えてもらえる"),
            tsuchi.talk("人付き合いとかめんどいっす"),
            sana.talk("あんたは気楽でいいわね。人生楽しいでしょ？"),
            tsuchi.talk("最近格闘ゲームでプロもいいかなって思ってるんす。知ってます？　プロゲーマーって"),
            sana.talk("話には聞いてるけど、なかなか難しいんじゃない？"),
            tsuchi.talk("でも小説だってもとを正せばただの趣味みたいなもんなんだから、それが金にできる世の中になれば関係ないんじゃないすか？"),
            sana.talk("一理あるわね"),
            _.think("考え込む"),
            tsuchi.do("スマホで何かしている"),
            sana.talk("何してんの？"),
            tsuchi.talk("ＳＮＳで面白いつぶやき探してるだけ"),
            sana.talk("うちの先生は機械オンチだからそういうの全然駄目で助かってるけど"),
            _.talk("この前$nirasakiさんが文句言ってた。どうでもいいことで噛み付いて炎上した作家の新刊が半年延期になったって"),
            _.talk("ほんと、面倒ばかりじゃない、そんなの"),
            tsuchi.talk("変なこと書かなきゃいいだけっすよ"),
            _.do("スマホの画面を見せる"),
            sana.talk("え……"),
            tsuchi.voice("新年会なう。ご馳走と共に"),
            sana.talk("何勝手に個人情報垂れ流してんのよ！"),
            sana.do("慌てて削除させる"),
            sana.talk("先が思いやられるわ……"),
            camera=w.sana,
            stage=w.on_hotelhall,
            day=w.in_newyearparty, time=w.at_afternoon,
            )

def sc_ourparty(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("私たちの新年会",
            sana.explain("その翌日に$Sは$geroたちとささやかな新年会を開いた"),
            gero.be("座っている"),
            azu.come("鍋を運んできて"),
            sana.be("飲み物を入れている"),
            sana.explain("準備はみんなでした"),
            sana.explain("お肉は$Sが買ったけれど、料理や飲み物で他の二人は貢献してくれている"),
            sana.talk("じゃ、乾杯しますか"),
            gero.talk("おーし。飲んで食うぞー"),
            azu.talk("明日も仕事だからほどほどにね"),
            sana.talk("乾杯！"),
            gero.talk("はぁ。この一杯の為に絵を描いているといっても過言じゃない"),
            sana.talk("そういや$azuminoはあれだっけ。まもなく一次発表？"),
            azu.talk("それ言わないで。胃がきりきりする"),
            _.talk("それに他の公募用に必死に書いてるところだし"),
            _.talk("あ、それに、最近ちょっとね"),
            gero.talk("ネットの誹謗中傷なんてほっとけばいいのに"),
            sana.talk("何かあった？"),
            gero.talk("掲示板に書き込まれてたんだってさ。なんか作品の描写とかキャラクタがきもいって"),
            sana.talk("そんなの無視しちゃえ"),
            azu.talk("分かってるんだよ。単なるやっかみの類だって。でも見ちゃうとさ"),
            sana.talk("ＳＮＳならブロックする。掲示板なら削除依頼しておく。そういうのが基本"),
            _.talk("とにかくネットの批評には関わらないようにするのが一番なんだから"),
            gero.talk("ネットといえばさ、あんたの先生。なんか盗作って書いてたけど、あれほんと？"),
            sana.talk("何それ。雑誌の短編のこと？"),
            azu.talk("ううん。なんかね、二十年も前のネタらしいけど、デビュー作について色々言われたんだって"),
            _.talk("同級生が自殺してるんでしょ？　それが盗作らしいって"),
            sana.talk("そんな話知らない"),
            _.think("それは不穏の始まりだった"),
            stage=w.on_herhouse_int,
            time=w.at_night,
            )

## episode
def ep_nextstory(w: World):
    return w.episode("4.続雪国",
            ## NOTE
            sc_newyearparty(w),
            sc_ourparty(w),
            )
