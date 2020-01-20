# -*- coding: utf-8 -*-
"""Episode: 3-2.物語のプロット／蜘蛛の糸
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
def sc_badwriter(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("悪い作家",
            sana.talk("ない……"),
            noto.talk("だから言っただろう？", "何故編集の癖に作家のいったことを信じない"),
            sana.talk("小説家は嘘をつく仕事ですから"),
            noto.talk("それは小説の中だけの話だ。何も現実を嘘だらけにするつもりはない"),
            sana.talk("じゃあせめて頭の中にはプロットくらいはあるんですよね？"),
            _.talk("内容の確認もなしに原稿をもらうまで分からないんじゃ、$me、流石に困ります"),
            _.talk("締切も迫ってますし"),
            _.talk("そもそも今日は一次締め切りだったはずですよね？"),
            noto.talk("さあな。君とは約束をしていないからね"),
            sana.think("最悪な作家だ、という思いが強くなる"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_firstmeet, time=w.at_afternoon,
            )

def sc_aboutplot(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("プロットとは",
            noto.talk("そもそも君はプロットが何なのかも知らないだろう？"),
            sana.talk("それくらい分かりますよ"),
            noto.talk("じゃあ、ここに何か書いてみなさい。そうだ。シンデレラでいい"),
            sana.do("考えて、書いてみる"),
            sana.talk("これでいいでしょうか"),
            sana.do("見せる"),
            noto.talk("これが君にとってのプロット、ということでいいかな？"),
            noto.talk("これは一体誰に見せるものなんだ？"),
            sana.talk("目の前の先生ですよ"),
            noto.talk("なのにタイトルもない。署名もない。一体何を目的としたものかも分からない"),
            noto.talk("プロットというのは、物語の構造を簡単に記したものだ"),
            _.talk("誰かに見せる為のものと自分用のものではその意味合いも異なる"),
            _.talk("君たち編集が言うのは主に企画書のことだね"),
            _.talk("どんなジャンルのどんな作品なのか。誰が主人公で、何が起こるのか"),
            _.talk("あらすじに、扱うテーマやモチーフ、主要な登場人物について"),
            _.talk("だが今君がここに書いたのは、単なるシンデレラのあらすじにすぎない"),
            _.talk("それもこのあらすじには、テーマも何もない。君が書きたいことも表現されてはいない"),
            _.talk("何より、どこがポイントになるのか、つまり、一番の見せ場なのかが書いてない"),
            _.talk("これでは合格点は与えられないな"),
            sana.do("開いた口が塞がらない"),
            )

## episode
def ep_storyplot(w: World):
    return w.episode("2.物語のプロット",
            ## NOTE
            sc_badwriter(w),
            sc_aboutplot(w),
            )
