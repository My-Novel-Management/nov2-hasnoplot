# -*- coding: utf-8 -*-
"""Episode: 6-3.死の淵にて／城の崎にて
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
    return w.scene("3.死の淵にて",
            noto.talk("そしてその友人は亡くなってしまったんだ", "自分で首を吊ってね"),
            sana.do("言葉を失う"),
            noto.talk("その時に思ったよ",
                "小説というのは人殺しの道具にもなるんだと", "作品そのものもだが、小説を書いたりする行為そのものも、人を苦しめる",
                "$meは書くべきじゃなかった", "なのに今は作家をしている",
                "そんな矛盾を抱え込んでいるのが人間なのかも知れない"),
            sana.do("言いたいことは理解できたが、頷いていいのかどうか分からなかった"),
            )

## episode
def ep_edgeindead(w: World):
    return w.episode("3.死の淵にて",
            ## NOTE
            sc_main3(w),
            )
