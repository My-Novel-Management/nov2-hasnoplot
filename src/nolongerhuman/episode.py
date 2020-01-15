# -*- coding: utf-8 -*-
"""Episode: 人間失格
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
    return w.scene("1.はしがき",
            sana.talk("はぁ"),
            _.explain("先生が無事に入院したことで、原稿が締め切りに間に合わないことは確実となった"),
            sana.talk("とにかく、今度こそは穴埋めを"),
            _.explain("何とか$Sがダミーの原稿を出すことで誤魔化す。これしかなかった"),
            sana.do("必死に原稿に向かう"),
            _.think("学生時代に作家を目指して書いていた頃を思い出す"),
            _.think("執筆は孤独な作業だし、見返すと、駄作を書いている実感しかない"),
            _.think("先生に言われたことを思い出す"),
            noto.voice("駄作でも最後まで書き切ることだ",
                "作品は一度書いて終わりじゃない。何度も書き直して、どんどん質を上げることができる",
                "しかし書き終えていない作品、特に頭の中にあるだけで無様でも言葉にまったくなっていない作品は、それだけで書き上がった駄作よりも価値は低い",
                "頭の中の傑作は咲かない花と同じだ"),
            sana.do("パソコンに向かう"),
            _.do("そこに連絡が来る",
                "監視しているバイト君", "先生に付き合いきれないと愚痴"),
            )

def sc_main2(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("2.第一の手記",
            ## 恥の多い生涯を送ってきました、の序文
            ## 少年時代
            sana.think("先生の日記を振り返る"),
            _.think("学生時代。当時から小説を書いていた先生。親友と競い合うようにして出版社に持ち込みをしていた"),
            _.think("今ならネットに投稿しているのだろうか", "ランキングを競い合っているのだろうか"),
            _.think("当時の読者は互いとその女性だけだった"),
            )

def sc_main3(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("3.第二の手記",
            ## 中学時代、高校時代
            ## 親友の原稿
            sana.do("知人から$tsuruの持ち込み原稿を手に入れる"),
            _.do("それに目を通す"),
            sana.talk("これって……"),
            _.explain("そこに書かれていたものは確かに先生のものとそっくりだった",
                "しかし決定的だったのは裏写りする文字が明らかにトレースしたそれだということだ"),
            )

def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("4.第三の手記",
            ## 女と酒に溺れる日々
            sana.do("先生が病院から消えた、とバイト君から連絡が入った"),
            sana.talk("なんで！？"),
            _.do("時刻を見れば十二時を回っている",
                "もう今日が締め切り日だった"),
            sana.do("編集長からのメールに気づく"),
            _.do("そこには既に別の作家で長編枠は埋まったと書かれていた"),
            )

## episode
def ep_main(w: World):
    return w.episode("人間失格",
            ## NOTE
            sc_main1(w),
            sc_main2(w),
            sc_main3(w),
            sc_main4(w),
            )
