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
            sana.come("数日後、再び先生宅を訪れる"),
            sana.talk("先生、原稿を"),
            noto.talk("ない"),
            sana.talk("あと何日か分かってますか？"),
            noto.talk("毎日来なくてもいいよ。分かってるから"),
            noto.do("壁掛けカレンダーの赤丸を見せて"),
            sana.talk("今どき固定電話しかない作家なんて先生くらいなものです"),
            noto.talk("百年くらい昔までまだ交換手が線を繋ぐのが普通だったんだ"),
            sana.talk("大正時代にでも転生してください"),
            sana.talk("とにかく、次回はちゃんと書いていることを示して下さい。じゃないとほんとに掲載枠取り消しですから"),
            noto.talk("そういうのパワハラって言うんだよ？"),
            sana.talk("先生が仕事しないからじゃないですか！"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_nogetpaper1, time=w.at_afternoon,
            )

def sc_changeofpace(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("気分転換",
            sana.be("先生と歩いている"),
            noto.talk("ほら、たまには気分転換も必要だろう？"),
            sana.talk("原稿"),
            noto.talk("まあまあ。今日はご飯をご馳走するから"),
            noto.talk("あそこだ"),
            stage=w.on_street,
            day=w.in_nogetpaper2, time=w.at_noon,
            )

def sc_lunchtime(w: World):
    sana, noto = W(w.sana), W(w.noto)
    hana = W(w.hanamaki)
    return w.scene("ランチタイム",
            noto.come(),
            sana.come(),
            noto.talk("こんにちは"),
            hana.be("カウンターで準備している"),
            hana.talk("あら先生。お元気ですか？"),
            noto.talk("この通りさ。まだ死ぬまでしばらく掛かりそうだ"),
            hana.talk("そちら、初めての方ですね。どうも、店主の$ln_hanamakiです"),
            noto.talk("こっちに出てきてから何度も世話になっているんだ。うまいよ、ここのハンバーグは"),
            hana.talk("そうおっしゃって下さるのは先生だけですよ"),
            sana.do("店内は閑古鳥"),
            noto.talk("あそこに座ろう"),
            noto.do("奥の席に座る"),
            sana.do("$Sも続く"),
            # NOTE: 食事の様子を少し
            stage=w.on_masterrestaurant,
            )

def sc_lightnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("ライトノベル",
            noto.be("食べ終えて食後のコーヒーを"),
            sana.be("コーヒーを前にじっとしている"),
            noto.talk("君をここに連れてきたのはね、少し考えてもらいたかったからなんだ"),
            sana.talk("またあれですか。説教ですか？"),
            noto.talk("説教なんてつもりはいつも持ってないんだが"),
            _.talk("君たちは原稿や文字を単なる数字として捉えていないか、ということだ"),
            noto.talk("作家にとっては一文字だろうが一枚だろうが、そこに自分が苦悩して書いたものがあれば作品の一部だと思える"),
            _.talk("しかし君らは原稿一枚や二枚ならすぐ書けるだろう、そんな風に考えている"),
            _.talk("駄文をいくら書いたって、それが百枚でも千枚になっても、作家にとって駄文なら作品ではないのだよ"),
            sana.talk("先生はライトノベルを書きたくないんですね？"),
            noto.talk("そうじゃないよ、$sana君"),
            _.talk("ライトノベルはね、$meにとって蜘蛛の糸なんだ"),
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
            sc_changeofpace(w),
            sc_lunchtime(w),
            sc_lightnovel(w),
            sc_novelvalue(w),
            )
