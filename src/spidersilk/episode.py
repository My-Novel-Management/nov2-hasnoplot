# -*- coding: utf-8 -*-
"""Episode: 蜘蛛の糸
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
def sc_main1(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("1.若者のネット",
            sana.think("プロットすらないと言われたが、それくらいでは引き下がらない",
                "作家とは締切を伸ばすためなら何でもする生き物なのだ"),
            sana.talk("今どきパソコンもスマホもないなんて、どうやってやり取りしてたんですか！？"),
            sana.talk("ちょっと探します"),
            noto.talk("人の言うことは素直に聞いた方が良い"),
            sana.talk("締切を守らない作家に人権はありません"),
            sana.think("それは前の雑誌編集部での教えだった"),
            sana.do("$Sは家探しする"),
            sana.do("ついでに掃除もする"),
            noto.talk("そういえばお腹すいたなあ"),
            sana.talk("出前でも取りますか？", "最近は宅配サービスも充実してて"),
            noto.talk("料理できないの？", "$fukayaさんの味噌汁は絶品だったんだよなあ"),
            sana.talk("作れますよ、一応"),
            sana.do("何故か料理することに"),
            )

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

def sc_main3(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("3.蜘蛛のスレッド",
            sana.talk("それで、その原稿はどこなんです？", "今話してくれましたよね？"),
            noto.talk("ない"),
            sana.talk("ない、んですか？", "全然？"),
            noto.talk("君が書けばいいじゃないか"),
            sana.do("突然そんなことを言い出す"),
            sana.talk("問題をすり替えないで下さい", "小説は特殊技能なんですよね？",
                "だから専門家である先生が書かないといけない", "$meはその原稿をちゃんと本にする義務がある"),
            noto.talk("なんだか最近は編集が書くとかいったことも聞くよ", "原稿三十枚程度なら君でも書けるだろう",
                "それにライトノベルには詳しいと豪語したじゃないか", "なら書いてみればいい"),
            sana.do("墓穴を掘った"),
            sana.talk("先生の作品でなければ掲載する価値がないんですよ",
                "$meの書いたものなんて誰が待っているっていうんですか"),
            )

def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("4.先生のマインド",
            sana.talk("それじゃあ本当にプロットどころか、どんな話を書こうというアイデアもないんですね？"),
            noto.talk("たった原稿用紙三十枚だろう？", "一晩で書いてしまうよ"),
            sana.talk("じゃあどうして原稿がないんですか？", "先輩と約束した締切ですよね？"),
            noto.talk("そこらにでも隠れてるんじゃないかな？"),
            sana.think("この作家、Ｓランクだと直感する",
                "ちなみに作家はその実力とは別に正確別にラベリングされている",
                "Ｓは最悪のＳだ"),
            sana.do("何故か$Sが短編小説を書くことになってしまった"),
            )


## episode
def ep_main(w: World):
    return w.episode("蜘蛛の糸",
            ## NOTE
            sc_main1(w),
            sc_main2(w),
            sc_main3(w),
            sc_main4(w),
            )
