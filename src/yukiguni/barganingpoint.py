# -*- coding: utf-8 -*-
"""Episode: 交換条件
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
def sc_exchange(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("交換条件",
            sana.talk("え？　どういうことですか？"),
            noto.talk("$meも小説を書く",
                "それもここに書かれた条件通りのものをね",
                "その代わりに君も長編小説を一本仕上げてくれと頼んでいるんだ"),
            sana.talk("$meは既に短編書いたじゃないですか！",
                "それで引き受けてくれたんじゃないんですか？"),
            noto.talk("君が書くのを見ながらだと書けるかも知れないと気づいた",
                "今度は長編を書いてくれたっていいだろう？"),
            sana.talk("な……"),
            _.think("先生の機嫌を損ねない、という注意を思い出す"),
            _.talk("分かりました", "けど$meの書くものなんてとても掲載できるような代物じゃありませんよ？"),
            noto.talk("君が書く、というだけでいいんだよ",
                "それに君は才能があると思うよ", "今まで$meが見た中でもその素直な文章は多くの人の心に届くだろう"),
            sana.explain("こうして、なぜか今度は長編執筆に挑戦することになった", "編集者なのに"),
            )


## episode
def ep_bargaining(w: World):
    return w.episode("先生の条件",
            ## NOTE
            ##  - 長編執筆する交換条件に沙奈も長編を書くことになった
            sc_exchange(w),
            )
