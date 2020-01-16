# -*- coding: utf-8 -*-
"""Episode: 7-1.先生と私／こころ
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
    return w.scene("1.先生と私",
            sana.think("旅館で先生が語った「書けなくなった理由」がずっと気になっていた"),
            sana.do("仕事が手につかない"),
            sana.do("同僚に質問してみる"),
            sana.talk("作家が盗作をしたとバレたら、どうなるんだろう？"),
            sana.explain("多くはその作品の出版がなくなり、しばらく謹慎だろうと教わる"),
            sana.think("もしあの記者が言っていたように先生が盗作をしていた、と考えると、今原稿を書けないというのはとても納得できる"),
            sana.talk("ちょっと行ってくる"),
            sana.go("先生のアパートに"),
            sana.come("アパートにきて"),
            sana.talk("先生！"),
            noto.talk("ちょうどいいところにきた", "一緒に出かけようじゃないか"),
            )

## episode
def ep_master_and_me(w: World):
    return w.episode("1.先生と私",
            ## NOTE
            sc_main1(w),
            )
