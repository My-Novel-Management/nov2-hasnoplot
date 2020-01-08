# -*- coding: utf-8 -*-
"""Demo: story no1
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_bymyself(w: World):
    sana, tani = W(w.sana), W(w.tani)
    return w.scene("自分自身で", "先生の助けを借りずに書き切った作品だったが",
            sana.talk("終わった"),
            sana.look("パソコン画面を"),
            sana.look("全部で十二万字の文字が並んでいるのを"),
            sana.talk("ほんとに、終わった"),
            sana.think("書き上げた実感を"),
            sana.talk("でも、これ……"),
            sana.do("誤字を見つける"),
            sana.talk("あー、駄目だ"),
            tani.come("やって"),
            tani.talk("終わったようだね"),
            sana.talk("先生……終わってないんです"),
            sana.do("立ち上がろうとしてそのまま倒れる"),
            w.br(),
            sana.do("知らない部屋で目覚めて"),
            tani.talk("やあ"),
            tani.have("飲み物を"),
            tani.talk("特製ジュースだ。どうぞ"),
            sana.do("飲む"),
            sana.talk("何ですかこれ"),
            tani.talk("バナナベースに色々とアレンジをね"),
            sana.talk("最悪です"),
            tani.talk("それより、どうだね？"),
            sana.talk("あ、まだ全然かけてないんです。あんなのじゃ"),
            tani.talk("少し休み給え。今やっても同じだ"),
            sana.talk("けど"),
            tani.talk("一度書き上げても、まだまだそこからが本番なんだ。何度も書き直す。ああでもないこうでもないと試行錯誤を繰り返す。その末に小説は小説となる"),
            sana.talk("先生のおっしゃった通りでした"),
            tani.talk("$meは何も言ってない。君一人の力で書き切った。それだけで君はもう立派な作家だ"),
            sana.talk("でもあれは駄作です"),
            tani.talk("今はまだ、ね"),
            tani.talk("$meが見てあげよう。赤だらけになるかも知れないが"),
            sana.talk("お願いします"),
            sana.think("先生はこれを何度もやってきたんだと"),
            sana.look("亡くなった父にも見えた"),
            )

## episode
def ep_demo(w: World):
    return w.episode("Demo", "書き上げた末に",
            sc_bymyself(w),
            )
