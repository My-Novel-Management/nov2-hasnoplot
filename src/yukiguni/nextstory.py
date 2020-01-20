# -*- coding: utf-8 -*-
"""Episode: 5-4.続雪国／雪国
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
def sc_goodbye(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("先生に見送られて",
            sana.do("先生の運転で駅まで送られる"),
            sana.do("精神衛生上悪い、と感じつつも感謝"),
            sana.talk("それじゃあ東京で待ってます"),
            sana.talk("原稿、がんばってくださいね"),
            noto.talk("ああ、任してくれ。最高傑作を書き上げてやろう"),
            sana.talk("待ってますから"),
            sana.do("電車に乗り込み"),
            camera=w.sana,
            stage=w.on_station,
            day=w.in_back_kanazawa, time=w.at_midmorning,
            )

def sc_returningtrain(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("帰りの車内で",
            sana.do("トンネルを抜けて戻っていく"),
            sana.do("考え込んでいる"),
            sana.think("$asahiの言ったことが気になっていた"),
            stage=w.on_train,
            )

def sc_backhome(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("帰宅して",
            sana.do("シェアハウスの友人たちと新年会"),
            gero.talk("またまた。実家に行って何もなかったってこたぁないやろ"),
            sana.talk("そっちの妄想ばっか逞しいんだから"),
            sana.talk("ねえ、$azumino？"),
            azu.talk("う、うん"),
            azu.do("様子が変"),
            azu.explain("この時、作家をやめる決断をするような問題が彼女に立ちはだかっていた"),
            stage=w.on_herhouse,
            time=w.at_night,
            )

## episode
def ep_nextstory(w: World):
    return w.episode("4.続雪国",
            ## NOTE
            sc_goodbye(w),
            sc_returningtrain(w),
            sc_backhome(w),
            )
