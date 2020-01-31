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
            sana.come("今日こそはと意気込んでやってくる"),
            sana.talk("先生、原稿を取りに伺いました！"),
            sana.do("しかし反応がない"),
            sana.talk("先生？"),
            sana.do("鍵が開いている"),
            sana.do("こっそり中に入る"),
            sana.talk("お邪魔しまーす"),
            noto.be("寝ている"),
            sana.do("先生が横になったまま動かないのを見て"),
            sana.talk("先生？　……寝てる？"),
            sana.do("机の上の原稿用紙には文字が這っている"),
            sana.talk("読めない……"),
            sana.do("部屋の片付けを始める"),
            sana.explain("部屋を片付け終え、食事を作っておく"),
            noto.do("目覚めて"),
            noto.talk("あれ？　$fukayaさん？"),
            sana.talk("違いますよ。$meです"),
            noto.talk("なんだ君か。どうしたの？"),
            sana.talk("原稿を取りに伺ったんですが、まだみたいでしたので"),
            _.talk("でも真面目に書こうとされているみたいなので"),
            noto.do("くしゃくしゃにしてゴミ箱に投げる。落ちる"),
            sana.talk("あ……"),
            noto.talk("寝ながらだから何書いてたのか分からんな"),
            sana.talk("字が汚いんじゃなかったんですか！"),
            noto.talk("流石に自分で読めない文字はどうしようもないさ"),
            sana.do("頭を抱える"),
            ## NOTE
            ##  理不尽さを際立たせるように
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_secondmeet, time=w.at_afternoon,
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
            ## NOTE: プロットについての説明
            w.load("プロットとは"),
            sana.talk("プロットについては、理解しました"),
            noto.talk("またそうやって気軽に分かった風なことを言う"),
            sana.talk("とにかくですね、もうプロットはいいです。それよりも原稿を下さい"),
            noto.talk("ない"),
            sana.talk("一枚も書いていないなんてことはないですよね？"),
            noto.talk("ない"),
            sana.talk("じゃあプロットでも企画書でもメモ書きでも何でもいいです。見せて下さい"),
            noto.talk("ないよ"),
            sana.talk("先生！？"),
            noto.talk("ないものはない。正直に言っている。なに、締切まではまだ日にちがあるじゃないか"),
            sana.do("溜息"),
            ## NOTE
            ##  プロットの話で少し見直しつつも、やはりSランクだと断定
            )

## episode
def ep_storyplot(w: World):
    return w.episode("2.物語のプロット",
            ## NOTE
            sc_badwriter(w),
            sc_aboutplot(w),
            )
