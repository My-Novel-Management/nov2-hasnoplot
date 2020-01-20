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
    return w.scene("ごねる先生",
            noto.talk("$fukaya君に担当を戻してもらえないか？"),
            sana.talk("$meでは原稿は出せないというんですか？"),
            noto.talk("彼女から何も聞いてないし、引き継ぎに来るのが筋ってものじゃないか？"),
            _.talk("だいたい急にやってきて原稿をよこせなんて、まるで借金取りみたいじゃないか"),
            sana.talk("借金取りじゃなくても編集は原稿を取りに来ます"),
            _.talk("書かない作家に書かせるのも編集の仕事ですから"),
            _.talk("もう一度確認しますけど、ないんですね？　プロットも？"),
            noto.talk("ああ。何もない"),
            sana.do("頭をおさえる"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_firstmeet, time=w.at_afternoon,
            )

def sc_writingterm(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("何故か沙奈も書くことに",
            sana.talk("分かりました。そこまで言うなら$meも短編小説を書きます"),
            _.talk("その代わり、先生もちゃんと書いて下さい"),
            _.talk("書いて、$meに小説とは何なのか教えて下さい"),
            noto.do("驚いている"),
            sana.talk("それじゃあ、ここにちゃんと記名と捺印お願いします"),
            sana.do("持っていたノートを切り取り、そこに即席で契約書を作成する"),
            noto.talk("代書屋さんでもないのによくささっと作成できるね"),
            sana.talk("色々と修羅場を踏んでいるんですよ、これでも"),
            sana.think("大学時代のことを思い出して"),
            sana.talk("とにかく、簡易ですけど、効力はあります。もし不履行になった場合は、賠償として木の屋のパンケーキおごってもらいますから"),
            noto.talk("ああ、最近話題になってるやつね"),
            sana.talk("友達と食べにいく約束したままになってるんです！"),
            noto.talk("じゃあ食べに行けばいいじゃない"),
            sana.talk("高いんです！　おまけにみんな忙しいんです！"),
            noto.talk("たまには休むのも大事だよ？"),
            sana.talk("先生はたっぷり休まれてましたよね？"),
            noto.talk("どこで聞いたのそれ"),
            sana.talk("敏腕編集ですから"),
            sana.talk("とにかくいいですね？", "ちゃんと原稿やってくださいよ！"),
            sana.talk("作家は小説を書く、編集はそれを本にする。それが仕事ってものです"),
            sana.go(),
            sana.explain("こうして何故か$Sまで小説を書くことになってしまった"),
            )

## episode
def ep_mastermind(w: World):
    return w.episode("4.先生のマインド",
            ## NOTE
            sc_makedifficult(w),
            sc_writingterm(w),
            )
