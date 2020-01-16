# -*- coding: utf-8 -*-
"""Episode: 1-3.座れ編集者／走れメロス
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
    return w.scene("3.座れ編集者",
            noto.talk("新しい編集か？　座れ"),
            noto.do("笑みもなくすごむ"),
            sana.do("ただただおそれ、どうしようと"),
            sana.think("作家の言葉を尊重する",
                "それが教えだった"),
            sana.do("言われた通りに座る", "ストッキングの足で正座", "スカートで来なければよかったと"),
            )

## episode
def ep_sitdowneditor(w: World):
    return w.episode("3.座れ編集者",
            ## NOTE
            sc_main3(w),
            )
