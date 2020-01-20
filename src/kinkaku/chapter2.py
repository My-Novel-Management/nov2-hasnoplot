# -*- coding: utf-8 -*-
"""Episode: 8-2.第二章／金閣寺
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
def sc_threatening(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("脅迫状",
            sana.come("様子を見にやってくる"),
            sana.talk("またいっぱい詰め込んで……あれ、これ何だろ。痛っ"),
            sana.do("指を切る"),
            sana.think("例のあれだ、と思った"),
            sana.do("中身は脅迫状で、盗作をばらされたくなければ金を支払えというもの"),
            sana.think("流石に相談すべきかと考える"),
            noto.talk("どうしたの？　血が出てるじゃないか"),
            noto.do("先生が、不器用だが、手当してくれる"),
            sana.do("分厚く巻かれた包帯に苦笑"),
            sana.talk("先生、これなんですが"),
            sana.do("封筒を見せる"),
            noto.talk("ああ、またか"),
            sana.talk("以前にも？"),
            noto.talk("ワープロの文字だが、その文章の句読点の癖がね、彼のものなんだよ"),
            noto.talk("ここでは何だから、外に出て話そうか。そうだ、ついでに夕食にしよう。ワインが飲みたかった"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_threaten2, time=w.at_afternoon,
            )

def sc_pulils(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("弟子について",
            sana.come("先生に連れられてやってくる"),
            sana.do("$Sが苦手な店主のバーだ"),
            noto.talk("こういう場所はね、内緒の話をするのに使うんだよ。それにここのナポリタンが上手くてね"),
            noto.do("注文する"),
            sana.explain("昔ながらの洋食が好きな先生。基本的に子ども舌だった"),
            _.explain("食事の風景を（ナポリタンやオムライス）"),
            sana.explain("食事を終えて、食後のワインとともに話し始めた"),
            noto.talk("以前、$meが弟子を取っていた時期があると話したね？"),
            sana.talk("はい"),
            noto.talk("その彼なんだよ。この前盗作で出版が立ち消えになったのは"),
            sana.talk("え……"),
            _.think("それは先生の担当になった日に聞いた、大手出版社での騒動だった"),
            noto.talk("$meの紹介でそれなりに堅実にやっていると聞いていたんだ",
                "けどね、実情は違った"),
            noto.talk("彼はパッチワークを続けていたんだ",
                "最初は誰でも真似から入る。そういうものなんだよ、技術というのはね"),
            noto.talk("しかし、彼は真似がうまかった。$meの文章や作風もすぐに真似たよ"),
            noto.talk("そしてその能力が高く買われ、大手出版社の編集に声を掛けられた",
                "最初はゴーストライターだったそうだ"),
            noto.talk("そのうちに自分の作品を出してもらえるようになって、去年だったね",
                "やっとミステリの方で賞をもらってね", "少し名前が売れた"),
            noto.talk("ただ彼の作品を読めば分かるが、必ず誰かのものを下敷きにしたものなんだ",
                "うまく隠しているが、そこに彼自身の作品はない。ただうまく本歌取りをしているだけ"),
            noto.talk("$meはそうならないように教えていたつもりだったが、技術と周囲の評価が彼の才能をそういう風に歪めてしまったんだ"),
            noto.talk("気をつけなければならない。作家はね、自分で自分の作品の評価をしようとしても、無理なんだ"),
            noto.talk("客観視というものは難しい"),
            noto.do("全て話し終えて、首を振る"),
            noto.talk("人間で一番厄介な感情だよ、嫉妬というのは"),
            sana.talk("警察には？"),
            noto.do("首を横に"),
            sana.talk("どうしてですか！"),
            noto.talk("実害がないだろう。それに、$meはね。せめて$meだけでも彼を信じてあげたいんだ",
                "$meはもう、あんな思いは沢山だから"),
            noto.explain("何か（$tsuruのこと）に思いを馳せている"),
            sana.explain("その日は何事もなく終わった"),
            sana.explain("先生に長編執筆の経過を聞いたりして、別れた"),
            stage=w.on_masterbar,
            )

def sc_abouttrust(w: World):
    sana = W(w.sana)
    return w.scene("信頼について",
            sana.be("部屋にいた"),
            sana.do("ベッドで一人考える"),
            sana.think("信頼について"),
            sana.think("先生の過去について"),
            stage=w.on_herroom,
            time=w.at_night,
            )

## episode
def ep_chapter2(w: World):
    return w.episode("2.第二章",
            ## NOTE
            sc_threatening(w),
            sc_pulils(w),
            sc_abouttrust(w),
            )
