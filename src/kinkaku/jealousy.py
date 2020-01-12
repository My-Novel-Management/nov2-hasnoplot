# -*- coding: utf-8 -*-
"""Episode: 嫉妬心
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

## episode
def ep_jealousy(w: World):
    return w.episode("醜い心",
            ## NOTE
            ##  - 今まで他人を羨んだりしたことないのに、何故か黒い感情が芽生えた
            ##  - 先生にそのことについて尋ねる
            ##  - それは自分の中の「美」をけがされたからと説明
            ##  - 金閣寺について教わる
            note="2.作家として活躍する同級生の存在に心を乱される沙奈。そんな彼女の身辺で妙なことが頻発するようになる",
            )
