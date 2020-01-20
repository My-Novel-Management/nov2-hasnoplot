# -*- coding: utf-8 -*-
"""Episode: 7-4.先生と遺書／こころ
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
def sc_friendwill(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("友人の遺書",
            sana.come("歩いて先生のアパートに戻ってくる"),
            sana.do("大量に突っ込まれた新聞などを引き抜いて"),
            noto.talk("今日は付き合ってくれてありがとう"),
            sana.talk("担当編集の義務ですから"),
            noto.talk("そういう時はただ笑顔を返しておけばいいんだ"),
            noto.talk("どうリアクションするか、というのが人物を表現する時に大切なんだよ"),
            noto.talk("今、君は何を思ってそう答えたのかな？"),
            sana.talk("えっと……当然です、というような"),
            noto.talk("普段から人間観察はしているだろう"),
            noto.talk("誰でも人間は書ける。けどね、それをどう表現するかはその人のセンスに寄っている"),
            noto.talk("よく「嬉しい」ではなく、何が嬉しかったのかを書きなさいと国語の作文の時間に指導されたね"),
            noto.talk("あれは君にとって何が嬉しかったのか、それを君らしく表現してほしい、ということだったんだ"),
            noto.talk("で、どんな風に素敵だったかね？"),
            sana.talk("あ……"),
            sana.think("$Sの口癖をいじられてしまった"),
            noto.talk("ちょっと待ってくれ"),
            noto.do("先生が寝室に引っ込む"),
            sana.do("その間に本棚の整理をしつつ、どんな本が並ぶか見ている"),
            sana.do("ライトノベルではなくやはり古典や文学作品が多い"),
            sana.do("と、隠されるように入っていた大学ノートを見つける"),
            sana.do("$Sはそれを開いて、先生の創作ノートだと分かった"),
            sana.do("帰ってくる気配がしたので、慌てて懐に突っ込んだ"),
            noto.talk("$sana君。これを"),
            noto.do("古い封筒を渡す"),
            sana.explain("それは遺書だった。さっき墓参りした$tsuruという人のものだ"),
            noto.talk("彼も作家を目指していた。けれど、自殺した。自らその将来を断った"),
            sana.explain("そこには「絶望が自分を殺した」と書かれていた"),
            noto.talk("$meが殺したようなものなんだ"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_visitgrave
            )

def sc_threatening(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("不穏",
            w.comment("短編のファンレターかと思えば、先生宛ての脅迫めいた謎の投書だった"),
            sana.talk("これ、何だろ"),
            sana.do("中身は新聞の切り抜きをはりつけたもの"),
            sana.explain("そこにははっきりと「先生は人殺しだ」と書かれていたのです"),
            stage=w.on_heroffice,
            day=w.in_threaten1, time=w.at_midmorning,
            )

## episode
def ep_master_and_letter(w: World):
    return w.episode("4.先生と遺書",
            ## NOTE
            sc_friendwill(w),
            sc_threatening(w),
            )
