# -*- coding: utf-8 -*-
"""Block: 沙奈と能登川の関係
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
def bk_sana_and_noto(w: World):
    sana, noto = W(w.sana), W(w.noto)
    manupaper = W(w.manupaper)
    return (
            w.block("先生に料理を披露する",
                sana.do("結局近所のスーパーに買い出しにいって惣菜と味噌汁やらを"),
                noto.talk("なかなか美味しいね"),
                sana.talk("ほとんどできあいものですから。$meは味噌汁作っただけです"),
                noto.talk("味噌汁が作れればあとはどうにかなるよ。結婚は？　と尋ねるのはセクハラかね？"),
                sana.talk("セクハラですね。まだしてません"),
                noto.talk("最近はちょっと神経質すぎる気がするが、これも時代なんだろうね"),
                sana.talk("できるだけ嫌な思いをしたくない、のが基本なんじゃないでしょうか"),
                noto.talk("だから、楽をして強くなりたい？　夢を見たい？"),
                sana.talk("先生？"),
                noto.do("積み上がった大量のライトノベルから一冊抜いて"),
                noto.talk("これを$meは書くのか、と思うとね"),
                sana.talk("素晴らしい作品もあります。でも大半は先生のおっしゃる通りです。でもそれが売れているんですから"),
                noto.talk("何を、買っているのだろう", "ブランドバッグと同じかね"),
                sana.talk("持っているだけで価値がある、自分もそうなれると？"),
                _.talk("$meは辛い現実生活から逃れる一つの逃避だと思ってます"),
                _.talk("できるだけ楽しい時間を過ごしたい。今もそうですが、重くつらい現実を描いた作品というのは沢山あります"),
                _.talk("中には本当に救いようのないバッドエンドもあります"),
                _.talk("どうしてフィクションの世界まで痛めつけられなきゃならないんだ。そんな声も聞こえてきます"),
                _.talk("夢を売る商売だ、という考え方もあるでしょう"),
                _.talk("先生の作品読みました"),
                _.talk("人生に迷った時に、友人にすすめようと思いました"),
                _.talk("あれは、素晴らしいです。ライトノベルという軽い読み物を、書いてもらっていいのだろうかと迷います"),
                noto.talk("いやあ、美味しかったよ。ありがとう"),
                sana.talk("あれ。なんで$me、こんなことを"),
                noto.talk("いい話を聞かせてもらったよ"),
                _.talk("ところで原稿探しはいいのかね？"),
                sana.talk("あ……"),
                ),
            )

