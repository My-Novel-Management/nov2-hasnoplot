# -*- coding: utf-8 -*-
"""Episode: 4-4.柘榴／檸檬
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
def sc_gladreport(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king = W(w.nirasaki), W(w.king)
    return w.scene("嬉しい報告",
            sana.do("急遽呼び出しを受けて編集会議を開いている"),
            king.do("渋い顔"),
            king.talk("前回号で予告しておいた作家陣に関しては全てゴーがもらえてるな？"),
            nira.talk("それは大丈夫です"),
            king.talk("$ln_sanaの方も間に合ったを聞いた"),
            sana.talk("はい"),
            king.talk("$meとしては残り一枠を、どちらで埋めれば売上が出るかということにしか興味がない"),
            sana.think("競合相手はこのラノベが読みたいにもランクインした実力ある若手作家だった"),
            king.talk("分かるな？"),
            sana.talk("分かりません"),
            king.talk("何だと？"),
            sana.talk("$meたちは売上という数字に顔を突き合わせて仕事をしているんじゃなくて、読者の声と向き合いたいんです"),
            sana.do("ネットで集めた読者の声を見せる"),
            sana.talk("これです"),
            king.talk("無断で何をしているんだ、君は？"),
            sana.talk("$meは教わったんです。前の編プロで"),
            _.talk("ただやりたい、こうしたいと夢を語るのは作家の仕事で、編集はそれを助ける為に情報をかき集めて補助するんだって"),
            _.talk("これだけの人が先生を待っているんです！"),
            king.talk("$nirasakiはどう思うんだ？"),
            nira.talk("待っている人がいる。それがすなわち売上に繋がる訳ではありません"),
            _.talk("実際にSNSでの人気はごく局所的なもので、反響があるのに売上がない、数字が出ないといったことはよくあります"),
            _.talk("ですが、ミクロな観点ではなくマクロな視点でもって考えると、執筆歴の長い$noto先生のような作家に参加してもらえるのは、"),
            _.talk("この会社にとってもですが、業界そのものにもメリットが大きいんじゃないでしょうかね"),
            sana.do("内心でフォローを感謝する"),
            king.talk("わかった。だが、これは$meの責任じゃないからな。お前ら二人で何とか売れ。いいな？"),
            sana.talk("は、はい！"),
            sana.explain("こうして正式に先生の初ライトノベル短編小説の雑誌掲載が決まった"),
            camera=w.sana,
            stage=w.on_heroffice,
            day=w.in_meetingshortnovel, time=w.at_afternoon,
            )

def sc_formallyeditor(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("正式に担当に",
            sana.come("その足で急いでやってくる"),
            sana.talk("先生！"),
            noto.talk("騒がしいね"),
            sana.talk("決まったんですよ！"),
            noto.talk("そうか"),
            sana.talk("嬉しそうじゃないですね。どうしてですか？"),
            noto.talk("いや、嬉しいよ。けど、その陰で誰かは割を食ったのだろう？"),
            _.talk("作家は常に誰かの犠牲の上に立って作品を発表している。そういう自覚は持っておくものだ"),
            _.talk("だからこそハンパなものは出せない"),
            sana.think("自分の書いたものがどうだったのか、と問われているよう"),
            noto.talk("ああ、それから、君の小説ね、赤いれておいたから、あとで読み返してみて"),
            sana.talk("え？"),
            sana.do("ゲラになって帰ってきて、苦笑"),
            sana.talk("分かりました"),
            stage=w.on_hisapart,
            time=w.at_evening,
            )

## episode
def ep_pomegranate(w: World):
    return w.episode("4.柘榴",
            ## NOTE
            sc_gladreport(w),
            sc_formallyeditor(w),
            )
