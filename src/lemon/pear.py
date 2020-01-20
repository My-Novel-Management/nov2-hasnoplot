# -*- coding: utf-8 -*-
"""Episode: 4-1.洋梨／檸檬
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
def sc_introuble(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("小説を書くという混乱",
            sana.do("友人に現状を語る"),
            sana.talk("なんで$meが小説を書くことになるのよ！"),
            gero.talk("いやいや、あんたが約束したんだがな"),
            sana.talk("そりゃそうだけどさ"),
            azu.talk("でも先生に読んでもらえるってことでしょ？　それってすごいことじゃない？"),
            _.talk("それに、昔は作家目指してたんでしょ？"),
            sana.think("自分の学生時代を思い出す"),
            _.talk("あの頃の作品は今じゃ黒歴史だなあ"),
            gero.talk("そんなこといったら$meは黒歴史現在進行系だがな"),
            _.do("自分の描いたＢＬとかのえっちいのを見せて"),
            sana.talk("それ黒歴史って思ってる？"),
            gero.talk("コミケに向けて必死だから黒とか白とかない", "売上は正義！"),
            sana.do("苦笑"),
            camera=w.sana,
            stage=w.on_herhouse,
            time=w.at_night,
            )

def sc_oldnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("黒歴史",
            sana.do("自室に引っ込み、本棚から一冊のノートを出す"),
            _.do("そこには学生時代に書き溜めた小説のネタがあった"),
            sana.do("頭を抱え込む"),
            _.do("編集の視点を手に入れた自分から見ると稚拙なものばかりに思える"),
            sana.talk("ああああぁぁぁぁ"),
            )

def sc_deadline_approach(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    nira, king = W(w.nirasaki), W(w.king)
    return w.scene("近づく締切",
            sana.do("会議に参加する"),
            sana.do("雑誌の企画や作家とのやり取りの進捗報告など"),
            king.talk("で、肝心の先生とのやり取りはうまくいってるのか？"),
            sana.talk("はい、もうバッチリです。バッチリすぎるくらいです"),
            sana.think("何いってんだ、と内心で"),
            king.talk("こっち界隈じゃ全然メジャーじゃないし、そもそもどれくらい読者ついてるか分からないけど、これで駄目だったらすぐ方向転換するからな"),
            sana.think("前の編集長の置土産が気に入らないのだ"),
            stage=w.on_heroffice,
            )

## episode
def ep_pear(w: World):
    return w.episode("1.洋梨",
            ## NOTE
            sc_introuble(w),
            sc_oldnovel(w),
            sc_deadline_approach(w),
            )
