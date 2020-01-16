# -*- coding: utf-8 -*-
"""Episode: 10-3.ほんとうのものがたり／銀河鉄道の夜
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
def sc_main3(w: World):
    sana, noto = W(w.sana), W(w.noto)
    king = W(w.king)
    return w.scene("3.ほんとうのものがたり",
            sana.talk(""),
            sana.do("先生の原稿を読む"),
            _.explain("それは一人の少女が、初めての小説を書き終えるまでの物語だった"),
            _.explain("小説を書く様を異世界冒険譚にしあげ、愛や勇気や友情や信頼関係、裏切り、そういったものをふんだんに盛り込んであるが、",
                "ただの少女冒険小説ではなく、小説を書くということは一つの旅であり、冒険でもあるということが、確かな筆致で書かれている"),
            noto.talk("どうだろうか"),
            sana.talk("すごいです。こんな感想しか言えないのがもどかしいくらい、今$me、原稿を持つ手が震えてしまっています"),
            noto.do("照れくさそうにした"),
            sana.do("そこに編集長から電話が入る"),
            king.voice("原稿は受け取ったのか？"),
            sana.talk("はい。今確かにこの手にあります。今からそっちに"),
            king.voice("急がなくてもいい。もう決まったんだ"),
            sana.talk("え？"),
            king.voice("#長編出版枠は先生のもので決定した、と告げる"),
            sana.explain("事情はよく分からなかったが、もう一人の有力候補だった○○は辞退した、と聞かされた"),
            sana.explain("#実は大手出版社の編集から声をかけられて、かっさらわれたのが事実"),
            sana.explain("ともかく、こうして無事に出版することが決まった"),
            )

## episode
def ep_truthstory(w: World):
    return w.episode("3.ほんとうのものがたり",
            ## NOTE
            sc_main3(w),
            )
