# -*- coding: utf-8 -*-
"""Episode: 3-1.若者のネット／蜘蛛の糸
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
def sc_nousepc(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("パソコンすらなく",
            sana.talk("見つけます。得意ですから"),
            sana.do("散らばっている部屋を掃除していく"),
            sana.talk("そもそもパソコンはどこですか？"),
            noto.talk("ないよ"),
            sana.talk("今どきパソコンも持ってないでどうやって執筆しているんです？"),
            noto.talk("これだよ"),
            noto.do("原稿用紙を見せる"),
            sana.talk("え？"),
            noto.talk("作家が原稿に書かなくてどうするんだい？"),
            sana.talk("全部ですか？　入稿はどうやってるんです？"),
            noto.talk("$fukayaさんに任せてたから分からないけど、彼女が直してたんじゃないの？"),
            sana.think("想像を絶する作業だった"),
            sana.talk("先輩だからいつも指が腱鞘炎だって言ってたのか"),
            sana.think("前途多難"),
            sana.do("キッチンや浴室も掃除しつつ"),
            noto.talk("そうだ。何か作ってよ。食べに行こうと思っていたところなんだ"),
            sana.talk("はい！"),
            sana.think("怒りが満ちてくる"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_firstmeet, time=w.at_afternoon,
            )

def sc_afternoonfood(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("午後の食事",
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
            )

def sc_notfound(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("原稿が見つかりません",
            sana.do("原稿がどうしても見つからない"),
            sana.talk("先生！"),
            noto.talk("もう諦めたかな？"),
            noto.look("笑っている"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_firstmeet, time=w.at_midmorning,
            )

## episode
def ep_teenweb(w: World):
    return w.episode("1.若者のネット",
            ## NOTE
            sc_nousepc(w),
            sc_afternoonfood(w),
            sc_notfound(w),
            )
