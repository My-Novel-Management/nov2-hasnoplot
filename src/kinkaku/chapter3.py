# -*- coding: utf-8 -*-
"""Episode: 8-3.第三章／金閣寺
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
    return w.scene("第三章",
            sana.explain("先生の告白から数日が経過した"),
            _.explain("あれからぱたりと連絡が途絶え、アパートに確認にいっても鍵がかかっていることが増えた",
                "居留守ではなく、どこかに出ているらしい"),
            _.explain("近所の喫茶店やファミレス、行きつけの店を探してみたが、見つけられなかった"),
            sana.do("先生を探しつつも、編集として他の仕事をこなし、編集会議に出て、他の編集者との差を痛感したり"),
            sana.do("またバイト君の面倒を見なくてはならず"),
            sana.do("忙しさの中で、一日の終わりになんとか執筆を進めるという日々"),
            sana.do("そんな折、シェアハウスの友人たちも声がかかったり、仕事が入ったりと忙しくなっていく"),
            )

## episode
def ep_chapter3(w: World):
    return w.episode("3.第三章",
            ## NOTE
            sc_main3(w),
            )
