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
def sc_main2(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("2.物語のプロット",
            noto.talk("蜘蛛の糸という作品を知っているかね？"),
            sana.talk("芥川龍之介ですよね？"),
            noto.talk("ああ、そうだ", "流石に読んでいるか"),
            noto.talk("あの作品の釈迦を見て、なんか冷たいなと感じると言われたことがあるんだが、",
                "君はどう思う？"),
            sana.explain("それは物語のラストの解釈という話だった"),
            sana.explain("プロットは骨子として重要だが、小説というのは書いているうちに色々と変わってしまう"),
            sana.explain("最終的にどんなオチをつけるかで全然違って見えてくるとも"),
            noto.talk("構造とはね、あくまで作品の理解を助けるものであり、また作品を演出するためのものでしかない",
                "だからさっき話したように必ずしも起承転結でなくともよい"),
            noto.talk("じゃあ、唯一書かなければいけないものとは何か？", "分かるかな？"),
            sana.explain("徐々に講義のようになってきた"),
            sana.talk("主人公の葛藤とか、そういったことですか？"),
            noto.talk("それも悪くはない", "ただ葛藤させるために書くというのならそれはまた違ってくる",
                "本来書く時に葛藤するのは作家であるべきなんだ",
                "苦労せずに、苦心せずに生み出されたものは、薄っぺらでしかない"),
            sana.do("徐々に先生の話に飲み込まれていた"),
            )


## episode
def ep_storyplot(w: World):
    return w.episode("2.物語のプロット",
            ## NOTE
            sc_main2(w),
            )
