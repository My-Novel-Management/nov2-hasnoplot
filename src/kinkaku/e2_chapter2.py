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
            _.do("それはとても古典的ないやがらせレターだった。中にカミソリの刃が入っている"),
            sana.think("こんなものを知っているのは先生とそう大差ない世代の大人だろうと思った"),
            sana.do("一応注意して中身を確認する"),
            sana.do("中に入っていたのは脅迫状で、盗作をばらされたくなければ金を支払えというもの"),
            sana.think("流石に相談すべきかと考える"),
            noto.talk("入ってこないけど、何かあった？"),
            noto.talk("どうしたの？　血が出てるじゃないか"),
            noto.talk("とにかく入りなさい"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_threaten2, time=w.at_afternoon,
            )

def sc_talkaboutthreaten(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("脅迫状について",
            sana.be("手に包帯が巻かれている"),
            noto.come("戻ってきて"),
            noto.talk("上手いもんだろう？"),
            sana.do("大きな蝶々結びを見て苦笑する"),
            noto.talk("なんだい。せっかく手当をしたのにそれはないだろう？"),
            sana.talk("本当に小説以外は何もできないんだなって"),
            noto.talk("そうだよ。作家に小説以外を求める今の風潮は間違っている、と断固言いたいね"),
            sana.think("同感だった"),
            sana.talk("ところで先生、この脅迫状なんですけど"),
            sana.do("封筒を見せる"),
            noto.talk("ああ、またか"),
            sana.talk("以前にも？"),
            noto.talk("ワープロの文字だが、その文章の句読点の癖がね、彼のものなんだよ"),
            sana.talk("彼？"),
            noto.talk("ここでは何だから、外に出て話そうか。そうだ、ついでに夕食にしよう。ワインが飲みたかった"),
            sana.think("どうやら先生には犯人の目星がついているようだ"),
            stage=w.on_hisapart_int,
            )

def sc_pulils(w: World):
    sana, noto = W(w.sana), W(w.noto)
    utsu = W(w.utsu)
    return w.scene("弟子について",
            sana.come("先生に連れられてやってくる"),
            utsu.be("グラスを磨いている"),
            sana.do("軽く会釈して挨拶する"),
            _.think("苦手だな、と感じる"),
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
            ## NOTE
            ##  ここで野迫川の事情（先生が把握している＝一般的な認識＋個人的情報）を教えておく
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
            sc_talkaboutthreaten(w),
            sc_pulils(w),
            sc_abouttrust(w),
            )
