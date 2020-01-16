# -*- coding: utf-8 -*-
"""Episode: 5-1.夕景色／雪国
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
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("1.夕景色",
            sana.do("先生のデビュー作をやっと手に入れて読んでいる"),
            sana.explain("作品はライトノベルとは全然違う、純文学よりの文芸作品で、地元の金沢の情景がよく滲んでいた",
                "切ない三角関係だった"),
            sana.come("駅を降りて"),
            noto.talk("やあ、遅かったね"),
            sana.talk("雪なんて聞いてません"),
            sana.do("足元はスニーカーだが、滑ってしまう"),
            noto.talk("あら？　君は雪国の人間じゃあなかったんだな"),
            sana.talk("知らない訳じゃないですけど、こんなには降ったことないです"),
            noto.talk("じゃあ行こうか"),
            sana.do("先生が自分で運転していた", "まだ昨年免許を取ったところだという"),
            sana.talk("$meが運転します"),
            noto.talk("いやいやここは$meの庭みたいなものだよ"),
            sana.do("早速道を間違えていた"),
            sana.come("先生の生家にやってくる"),
            )

## episode
def ep_sunsetsight(w: World):
    return w.episode("1.夕景色",
            ## NOTE
            sc_main1(w),
            )
