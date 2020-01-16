# -*- coding: utf-8 -*-
"""Episode: 10-1.カムパネルラはどこに消えた？／銀河鉄道の夜
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
    return w.scene("1.カムパネルラはどこに消えた",
            sana.talk("先生が消えた！？"),
            _.explain("連絡を受けて、先生の行きそうな場所を手当たりしだいに電話して確認する"),
            _.explain("しかし全然見つからない"),
            _.do("そこに来客"),
            sana.talk("こんな時に"),
            noto.talk("$sana君いるかい？"),
            sana.talk("先生？", "大丈夫なんですか！？"),
            noto.talk("大丈夫も何も、締切は守るものだと言ったのは君だよ？"),
            noto.do("その手には茶封筒を持っている"),
            sana.do("どう見ても病人だ"),
            sana.do("倒れそうになった先生を支える"),
            noto.talk("まだ、決まっていないんだろう？", "これが必要なんだろう？"),
            sana.talk("ですが、もう……"),
            _.think("ほぼ相手方で決まりと連絡を受けている"),
            noto.talk("まあ、そういうこともある", "この世界では変えの利かない作家など、ほとんどいないのだからね"),
            sana.talk("$meのちから及ばずです"),
            noto.talk("君はまだ若い", "失敗から学びなさい", "最近の若者はミスをすることを恐れる",
                "$fukayaさんは珍しくミスを恐れない女性だ", "彼女は$meが失敗をしても何とかしますと言ってくれる",
                "作家が文章で誰かの心を動かすなら、編集はその言葉で作家を支えるんだ"),
            noto.talk("$meはね、人生で一度大きな失敗をしている",
                "盗作をした", "そのことで大切な友人を失った", "初恋の女性も失った",
                "残ったのは作家という肩書だけだった"),
            )

## episode
def ep_campanella(w: World):
    return w.episode("1.カムパネルラはどこに消えた？",
            ## NOTE
            sc_main1(w),
            )
