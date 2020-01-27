# -*- coding: utf-8 -*-
"""Block: 盗作騒動
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer
_ = W.getWho()


## blocks
def bk_plagiarism(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return (
            w.block("盗作ニュース１",
                sana.do("スマホのニュースを見ていると、そこに盗撮騒動の話が流れてくる"),
                sana.talk("え？　これって"),
            ),
            w.block("盗作騒動1",
                sana.explain("#盗作騒動で出版予定だった本がポシャる"),
            ),
            w.block("盗作騒動2",
                sana.explain("#最後は猫のように酒に溺れて死ぬのも悪くないと言われる"),
            ),
            w.block("盗作騒動3",
                sana.explain("#悪いことはいつか自分に帰ってくると先生に言われた"),
            ),
            w.block("盗作騒動4",
                sana.explain("#雑誌記者から盗作疑惑があると教えられる"),
            ),
            w.block("盗作騒動5",
                sana.explain("#先生と親友はどちらが先に作家になるか競争していたと知る"),
            ),
            w.block("盗作騒動6",
                sana.explain("#先生と親友の関係について教わる"),
            ),
            w.block("盗作騒動7",
                sana.explain("#先生の告白日記を読んでしまう"),
            ),
            w.block("盗作騒動8",
                sana.explain("#$Sの盗作したのかという問いに先生は「そうだ」と答えた"),
            ),
            w.block("盗作騒動9",
                sana.explain("#親友の持ち込み原稿を手に入れる"),
            ),
            w.block("盗作騒動10",
                sana.explain("#実は親友の方が先生の作品を盗作していた"),
            ),
            )

