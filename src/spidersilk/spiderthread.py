# -*- coding: utf-8 -*-
"""Episode: 3-3.蜘蛛のスレッド／蜘蛛の糸
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
def sc_noplot(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("プロットはない",
            noto.talk("なら君が書けばいい。誰だって三十枚くらい書けるだろう？"),
            _.talk("それに一番読者のことを理解しているというなら、その君らが書いた方がよっぽど読者の欲しいものが書けるんじゃないのか？"),
            sana.talk("それができるならやってます。みんな書きますよ"),
            _.talk("でも現実は違う"),
            _.talk("村上春樹や宮部みゆき、東野圭吾を読んで自分でもあんなものは書ける。そう言う人もいます"),
            _.talk("けど彼らが実際に書いたものはとても小説と呼べるものじゃありません"),
            _.talk("難解なものならいくらでも書けるかも知れませんが、広く様々な人に手にとって読まれる作品というのは違います"),
            _.talk("誰でもできることなら、もっと沢山の人が村上春樹になってますよ！"),
            _.talk("みんなできないから、ううん、それぞれ違うものが出来上がるからこそ、いいんです"),
            sana.think("いつの間にか熱く語っていた"),
            noto.do("腕組みをしながら満足げ"),
            sana.talk("何も言い返すことはないんですか？"),
            noto.talk("いや。$fukaya君と初めてあった日のことを思い出していたんだよ"),
            sana.explain("先生は$fukaya先輩のことを懐かしそうに語る"),
            sana.explain("良い作品は作家だけでなく編集者も大切と聞いている"),
            sana.think("先生の一番新しい本を読んだことを思い出す。あれも担当は$fukayaだった"),
            sana.talk("どうして今更ライトノベルなんですか？"),
            noto.talk("それは$meにとっての蜘蛛の糸だからだ"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_firstmeet, time=w.at_afternoon,
            )

def sc_novelvalue(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("小説の価値",
            sana.think("蜘蛛の糸、といった意味を考える"),
            sana.think("作家の言葉には本質が眠っているという$fukayaの助言を思い出す"),
            sana.talk("それは最後にお釈迦様がたらしてくれた希望だってことですか？"),
            noto.talk("君は作家の価値は何で決まると思う？"),
            sana.talk("価値、ですか？"),
            _.talk("出した作品でしょうか"),
            noto.talk("そう考える人が多いかな"),
            _.talk("何を書いたのか。つまり結果だね"),
            _.talk("結果だけを追い求めた、その結果が現在の出版業界だ"),
            _.talk("出版だけじゃない。結果、つまり売上しか見てこなかったから、こんなになってしまった"),
            _.talk("作家の価値とはね"),
            _.talk("結果じゃない。つまり何を書いたかじゃない"),
            _.talk("何を書くか。未来にこそあるんだよ"),
            sana.talk("未来？"),
            _.talk("でもそれじゃあ価値なんて分からない"),
            noto.talk("だから君たちがいるんだろう？　編集は作家から未来を買っているんだよ"),
            sana.do("言葉を失う"),
            )

## episode
def ep_spiderthread(w: World):
    return w.episode("3.蜘蛛のスレッド",
            ## NOTE
            sc_noplot(w),
            sc_novelvalue(w),
            )
