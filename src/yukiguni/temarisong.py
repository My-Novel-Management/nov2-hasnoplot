# -*- coding: utf-8 -*-
"""Episode: 5-2.手鞠歌／雪国
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
def sc_lunch(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("昼食を取る",
            sana.do("先生に連れられて、古いファミレスにやってくる"),
            sana.do("先生が学生時代によく使っていたものらしい"),
            sana.do("店に入ると、先生の知り合いらしき女性もいる"),
            asahi.talk("あら、こっちに帰ってきてたんだ"),
            noto.talk("$full_asahiさん。学生時代の同級生だ"),
            sana.talk("はじめまして。先生の担当編集をしています"),
            asahi.talk("へえ、まだ作家やってたんだね"),
            sana.think("嫌な感じがした"),
            camera=w.sana,
            stage=w.on_oldfamires,
            day=w.in_homevisit, time=w.at_noon,
            )

def sc_unknownthings(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("知らないこと",
            sana.do("昼食を食べ終えた"),
            noto.talk("ちょっと席を外すよ"),
            noto.go("昔の知人の集団の方に"),
            asahi.come("隣の席にやってきて"),
            asahi.talk("ねえ、先生とはどれくらいの付き合いなの？"),
            sana.talk("まだ十月からなんで二ヶ月ほどですけど"),
            asahi.talk("色々なお世話もするんでしょ？"),
            sana.talk("まあ、そうですけど"),
            asahi.talk("ねた？"),
            sana.do("顔が真っ赤になる"),
            asahi.talk("うぶなのね。見た目通り若いのかしら"),
            sana.talk("見た目のことを言われるのはあまり好きじゃありません"),
            asahi.talk("まああの人の好みじゃないわよね。それとも歳とって変わったのかしら"),
            sana.talk("何なんですか？"),
            asahi.talk("別に。ただあの人殺しがまだのうのうと生きてるのが許せないだけ"),
            sana.talk("人殺し？"),
            asahi.talk("何も知らないのね。$full_tsuru。調べてみたら"),
            noto.come("戻ってくる"),
            noto.talk("何を話していた？"),
            asahi.talk("別に。古い歌の話よ"),
            asahi.do("童謡を歌う"),
            asahi.go(),
            sana.think("先生の鼻歌で聞いたことがある、と思い出す"),
            noto.talk("昔、いろいろとあってね。まあ何を言われたかしらないが、気にしないことだ"),
            noto.do("不機嫌な顔"),
            )

## episode
def ep_temarisong(w: World):
    return w.episode("2.手鞠歌",
            ## NOTE
            sc_lunch(w),
            sc_unknownthings(w),
            )
