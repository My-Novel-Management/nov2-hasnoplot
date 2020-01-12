# -*- coding: utf-8 -*-
"""Episode: 憤れ編集者
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
def ep_angry_editor(w: World):
    return w.episode("憤れ編集者",
            ## NOTE
            ##  - どうしてそんなことになったのか、事前のいざこざについて
            note="2.元はといえば産休になった先輩もそうだが、前編集長に世話になっていた断れなかった沙奈。しかし新編集長は無理難題を出すパワハラ上司で有名だった",
            )
