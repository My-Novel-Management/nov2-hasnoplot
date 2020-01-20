# -*- coding: utf-8 -*-
"""Episode: 9-1.はしがき／人間失格
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
def sc_notintime(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, tsuchi = W(w.nirasaki), W(w.tsuchiura)
    return w.scene("間に合わないことが決定",
            sana.do("先生の容態を聞いて、命に別状はないと知り、ほっとする"),
            sana.think("でもこれで完全に原稿は間に合わない。その上、書いたものが燃えてしまったのだ"),
            sana.think("せめてパソコン使っておいてくれたら"),
            sana.think("全部書き終えたと言っていたことを思い出す"),
            sana.think("冗談で言っていたけれど、本当に自分が書いたものを先生の作品として会議に持ち込もうかと思った"),
            nira.talk("おう。どうだ？"),
            nira.do("仕事終わりで来てくれた"),
            sana.talk("一応"),
            camera=w.sana,
            stage=w.on_hospital,
            day=w.in_firemaster, time=w.at_night,
            )

def sc_alternative(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, tsuchi = W(w.nirasaki), W(w.tsuchiura)
    king = W(w.king)
    return w.scene("代替案",
            w.comment("編集長から別の作家の作品をそこにぶちこむか、原稿を何とかするかと迫られ"),
            sana.do("緊急会議で、編集長から言われる"),
            king.talk("原稿は焼けた、そうなんだな？"),
            sana.talk("はい"),
            king.talk("おまけに先生は入院して治療中。全治三ヶ月？　いつ書けるようになるんだ？"),
            sana.talk("わかりません"),
            king.talk("とにかく可能な限り出版点数は減らしたくないので、何とか代替になる作品か作家を探せ。別に$ln_sanaじゃなくてもいい"),
            sana.do("これで完全に先生の出版は終わった"),
            sana.do("会議が終わり"),
            nira.talk("ま、良かったんじゃねえか。あの先生、ちょっとな"),
            sana.talk("何よ？"),
            nira.talk("これ"),
            nira.do("スマホでネットニュースを見せる。そこには盗作疑惑？と"),
            sana.think("前に接触してきた雑誌記者だと直感"),
            sana.talk("あのさ、その出版社に知り合いいる？"),
            nira.talk("まあ、ツテは多少"),
            sana.talk("お願い、紹介して"),
            stage=w.on_heroffice,
            day=w.in_nextfire, time=w.at_midmorning,
            )

def sc_impossible(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, tsuchi = W(w.nirasaki), W(w.tsuchiura)
    return w.scene("先生は無理です",
            sana.do("紹介してもらった別の出版社の編集に会った"),
            sana.explain("だがその人からは当然情報源は教えられないと言われた"),
            tsuchi.come("疲れた顔でやってくる"),
            sana.talk("どうしたの？"),
            tsuchi.talk("どうもこうもないっすよ"),
            sana.explain("彼が言うには、先生は元気で、あれが欲しいこれが欲しい、何かってこい、ああ原稿書くのに机が欲しいとか言い出して、面倒見てられないと"),
            sana.talk("先生らしいわ"),
            sana.talk("あとで行って、大人しく治療してくださいって言っとくから"),
            tsuchi.talk("ああ、$meも早く作家になりてえ"),
            sana.talk("何か書いてるの？"),
            tsuchi.talk("書こうとは思ってるんですけどねえ……"),
            sana.talk("何でもいいから書いてみなさい", "$meは全然裁量ないけど、目を通すくらいなら力になれるから"),
            tsuchi.talk("エタってばっかなんすよ"),
            sana.talk("エタる？"),
            tsuchi.talk("言わないすか？", "書きかけたまま永遠に終わらないからエタる"),
            sana.think("先生が言っていたことを思い出す。書き終えない傑作は、書き終えた駄作よりも遥かに駄作だと"),
            stage=w.on_famires,
            time=w.at_afternoon,
            )

## episode
def ep_firstnote(w: World):
    return w.episode("1.はしがき",
            ## NOTE
            sc_notintime(w),
            sc_alternative(w),
            sc_impossible(w),
            )
