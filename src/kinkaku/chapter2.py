# -*- coding: utf-8 -*-
"""Episode: 8-2.第二章／金閣寺
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
    return w.scene("第二章",
            sana.explain("$Sは編集者として以上に個人として、先生に弁明を求めた"),
            noto.talk("理由は簡単さ", "あいつの才能に嫉妬したからだ",
                "作家というのはね、自意識の塊なんだ", "醜悪な自分を褒めてもらいたくて何とか作品にして、芸術ということにして、",
                "それを他人に認めてもらいたい", "そんな矮小な存在でしかないんだよ", "全然偉くなんてない"),
            sana.do("先生の告白を聞きながら、自分はどうだったろうか、と考え込む"),
            noto.talk("だから君にも今の作品は見せられない", "今の$meを見れば分かるだろう？",
                "とても君を感動させたような話を書ける人間じゃあない", "ただのしょぼくれた、あと十年もすれば還暦を迎えるだけのつまらない男だ"),
            sana.talk("先輩は可愛らしい人だって言いました", "その意味が少しだけ分かりました"),
            _.do("$Sはそっと抱き締める"),
            noto.talk("な、何を？"),
            sana.talk("そんな風に自分をいじめなくてもいいんです", "書けなくても、誰も責めません",
                "その為に$meが今書いているんじゃないですか", "先生が書けるようになるまで、$meは待ちますから"),
            noto.talk("すまない……"),
            )

## episode
def ep_chapter2(w: World):
    return w.episode("2.第二章",
            ## NOTE
            sc_main2(w),
            )
