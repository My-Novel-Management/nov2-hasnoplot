# -*- coding: utf-8 -*-
"""Episode: 3-4.先生のマインド／蜘蛛の糸
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
def sc_makedifficult(w: World):
    sana, noto = W(w.sana), W(w.noto)
    manupaper = W(w.manupaper)
    return w.scene("ごねる先生",
            w.comment("ここまでに締切日の提示をしておくこと"),
            sana.come("約束通り、原稿を確認にやってくる$S"),
            sana.talk("先生おはようございます！", "本日は原稿受け取り日になっておりますが進捗どうでしょうか？"),
            noto.be("何か縫い物をしようとしている"),
            sana.talk("何してるんですか？"),
            noto.talk("糸が通らなくてね"),
            sana.talk("これでいいですか？"),
            noto.talk("おお、ありがとう。ボタンが外れてしまって"),
            _.talk("どうにもボタンというのが苦手なんだが、取れていると気になるだろう？"),
            sana.do("シャツのボタンが取れている"),
            sana.talk("$meがやりますから、原稿をお願いします"),
            manupaper.be("机の上にある"),
            manupaper.look("真っ白なまま"),
            sana.talk("今度は何してるんですか？"),
            noto.talk("ちょっと小腹が空いたので何か作ろうかと思って"),
            sana.do("コンロに薬缶を掛けたまま待っている先生を見て"),
            sana.talk("$meが何か作ります！　先生は原稿をしてください！"),
            _.talk("そもそもどこまで書けたんですか？　進捗どうなんですか？"),
            noto.talk("慌てる乞食は貰いが少ないよ"),
            sana.talk("貰えるなら少なくても構いません。さあ原稿を！"),
            noto.do("溜息"),
            noto.talk("ねえ。$fukaya君はいつ戻ってくるんだろうか？"),
            sana.talk("$meでは原稿は出せないというんですか？"),
            noto.talk("彼女から何も聞いてないし、引き継ぎに来るのが筋ってものじゃないかな？"),
            _.talk("だいたい急にやってきて原稿をよこせなんて、まるで借金取りみたいじゃないか"),
            sana.talk("借金取りじゃなくても編集は原稿を取りに来ます"),
            _.talk("そもそも本日は原稿の第一次締切が延期されたものですからね？"),
            _.talk("もう一度確認しますけど、ないんですね？　プロットも？"),
            noto.talk("ああ。何もない"),
            sana.do("頭をおさえる"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_nogetpaper3, time=w.at_afternoon,
            )

def sc_writingterm(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("何故か沙奈も書くことに",
            sana.be("正座している"),
            noto.be("机の前で腕組みしている"),
            sana.talk("先生はどうしたら原稿を書いてくれますか？"),
            noto.talk("書く時は書く。作家の仕事だからね"),
            sana.talk("じゃあ何で書いてくれないんですか！？"),
            noto.talk("さあ、どうしてだろうね"),
            sana.do("先生を睨みつける"),
            noto.do("溜息"),
            noto.talk("$fukayaさんからは何も聞いていない？"),
            _.talk("実はここ十年、まともに小説を書いたことはないんだよ"),
            sana.talk("え？"),
            noto.talk("書けなくなってしまった"),
            _.talk("そんな$meを何とかしようとエッセイや批評、紀行文等の仕事を$fukayaさんが取ってきてくれた"),
            _.talk("去年彼女がライトノベルレーベルに異動したことで、そっちなら書けるかも知れないと挑戦する機会をくれたんだ"),
            _.talk("かなり無理をして企画をねじ込んでくれたらしい"),
            sana.think("それで編集長は嫌がっていたのか、と思い出す"),
            sana.talk("書けない。そう仰る作家さんもいますよ"),
            _.talk("でも本当に書くのが嫌なら、既に辞めちゃってるんですよね"),
            _.talk("$meも昔は作家を目指して書いてました。でもそれらは今や黒歴史です"),
            _.talk("それでも何か本を作る仕事に関わりたい、手伝いたい、そんな思いで今この編集って仕事をやってます"),
            _.talk("本は小説は、作家一人で作るものじゃありません"),
            _.talk("先生。$meも手伝います。だから、今一度、挑戦してみませんか？　小説に"),
            noto.talk("そうか。君も小説を書いてくれるのか"),
            _.talk("それなら、あの頃みたいに誰かと共に目指すなら、書けるかも知れない"),
            sana.talk("え？"),
            noto.talk("君も同じように短編小説を書いてくれ。$meも書く。きっとそれなら書けると思うんだ"),
            noto.do("手を握って"),
            noto.talk("ありがとう。なんだか書ける気がしてきたよ"),
            sana.talk("え、ええ。けど"),
            noto.talk("楽しみだなあ。まさか担当さんも一緒に小説書いてくれるなんて。流石に$fukayaさんはそこまでしてくれなかったからね"),
            sana.talk("え？　ちょっと先生？"),
            noto.talk("まあ分からなくなったら何でも聞いてくれ。これでも三十年ばかり、いや学生時代からなら四十年近くも小説を書いてきたんだからな"),
            noto.do("楽しげ"),
            sana.explain("こうして何故か$Sまで小説を書くことになってしまったのだった"),
            )

## episode
def ep_mastermind(w: World):
    return w.episode("4.先生のマインド",
            ## NOTE
            sc_makedifficult(w),
            sc_writingterm(w),
            )
