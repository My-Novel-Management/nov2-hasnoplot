# -*- coding: utf-8 -*-
"""Episode: 4-3.檸檬／檸檬
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
def sc_writerwill(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("作家の気持ち",
            sana.do("正座して、いつもとは違う先生との関係だった"),
            sana.do("先生が読むのをじっと待っている"),
            sana.hear("ページを捲る音だけが響く"),
            sana.talk("あ、あの"),
            noto.talk("待って"),
            sana.talk("はい"),
            noto.do("もう一度読み直している"),
            noto.talk("ねえ"),
            sana.talk("はい？"),
            noto.talk("なぜ彼女は亡くなった人の命を集めているの？"),
            sana.talk("それは死神という設定だから"),
            noto.talk("死神が滅びた世界の神になる、というのは大筋としては面白いと思う"),
            _.talk("けどそこに読者は何故？　を感じるんだ"),
            _.talk("作者がいくら集めたかったからだ、と言いはったところで、この登場人物の考えではないからね"),
            _.talk("一体彼女が何を考えて、そう思ったのか"),
            _.talk("短編は多くは語れない、とは言った。けれど、語るべきことは語らないといけない"),
            _.talk("わずか原稿二十枚、三十枚としても、そこは彼らの人生の断片なんだ"),
            sana.think("間に合わせで書いた、というつもりはないけれど、突っ込まれると弱い"),
            noto.talk("最初に$meが言った意味が、少しは理解できた？"),
            _.talk("作者というのは常にこういった視線に晒されているんだ"),
            _.talk("その恐怖を一人で抱え込む。一人で戦うことになる"),
            _.talk("だから必死に書くし、調べるし、間違ってないか誰かに聞く"),
            _.talk("でも最終的にそれにゴーサインを出すのは自分自身だからね"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_deadline_short, time=w.at_night,
            )

def sc_lonleyroad(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("寂しい帰路",
            sana.be("一人暗い夜道を歩いている"),
            sana.look("目元が赤い。涙の跡だ"),
            sana.think("結局先生の原稿は貰えなかった"),
            _.think("自分の、編集としての浅はかさ、物足りなさが見透かされた"),
            _.think("大事な原稿は預けられない、と言われた"),
            _.think("そんなことにはならないと思いこんでいたので、ショックが大きい"),
            sana.talk("$meは、どこかで小説をバカにしていたんだ"),
            stage=w.on_street,
            time=w.at_night,
            )

def sc_sadreport(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("悲しいお知らせ",
            sana.do("残業を終えて帰ってきた$S"),
            sana.do("コンビニ弁当を食べて、軽くシャワーしてきたところ"),
            sana.do("テレビのニュースを見ながら原稿に目を通す"),
            sana.do("そこに$nirasakiから連絡"),
            sana.talk("え？"),
            sana.explain("そこには最近知名度を上げた若手作家の短編掲載がねじ込まれた、とあった"),
            stage=w.on_herroom,
            time=w.at_night,
            )

## episode
def ep_lemon(w: World):
    return w.episode("3.檸檬",
            ## NOTE
            sc_writerwill(w),
            sc_lonleyroad(w),
            sc_sadreport(w),
            )
