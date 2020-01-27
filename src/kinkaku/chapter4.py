# -*- coding: utf-8 -*-
"""Episode: 8-4.第四章／金閣寺
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
def sc_writing(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    nira, tsuchi, king = W(w.nirasaki), W(w.tsuchiura), W(w.king)
    return w.scene("久々の執筆",
            w.comment("久々の休日に、家でじっくり執筆を"),
            sana.be("自室でノートパソコンを前にしている"),
            sana.think("久しぶりの休日だったけれど、既に正午を過ぎている"),
            sana.think("予定よりも二時間以上ぐっすり眠っていたことに後悔する"),
            sana.talk("今日はしっかり書かなきゃ"),
            _.think("でもどうして自分まで長編小説を書かなければいけないのだろうか"),
            _.think("これを書かなくてもきっと誰も何も言わないだろう。どうせ先生に見せるくらいしか予定がない"),
            _.think("誰にも読まれない小説を書くことほど虚しいことはない"),
            sana.talk("ああ、駄目だ。考えてても仕方ないから、とにかく何かお腹に入れよう"),
            sana.hear("ドアのノック音"),
            sana.talk("はーい"),
            azu.talk("もう起きた？"),
            azu.come("お盆を手に入ってくる"),
            sana.do("$azuminoだ"),
            sana.talk("うん。ごめんね。用事だった？"),
            azu.talk("ううん。なら、ちょうど昼ご飯作ったからどうかなって"),
            sana.talk("ありがとう。でもさっさと残業しないといけないから"),
            azu.talk("これ、だけど"),
            azu.do("お盆に乗せた皿にはサンドウィッチがある"),
            sana.talk("それ、どうしたの？"),
            azu.talk("だから作ったの"),
            _.talk("パンを安くもらったから"),
            sana.think("パン屋のアルバイトを始めたことを思い出した"),
            sana.talk("忙しいのに、なんか気遣ってもらってありがとう"),
            azu.talk("お互い様だよ"),
            sana.talk("よし。がんばる"),
            azu.talk("コーヒーもあるからね"),
            sana.do("彼女の笑顔に心から感謝をする"),
            azu.talk("じゃね"),
            azu.go("コーヒーを置いて立ち去る"),
            sana.think("自分の作品にダメ出しをされて、凹んでいるはずなのに"),
            sana.do("サンドウィッチをつまみながらパソコンに向かう"),
            sana.do("自室に戻って小説の続きを書こうとする"),
            sana.do("パソコンには小説の断片がいくつも。書いては違う、けど、取っておこうとしたものたち"),
            sana.do("集中できず、立ち上がる"),
            sana.talk("やっぱ駄目だ"),
            sana.do("ノートパソコンと共に部屋を出る"),
            sana.talk("ちょっと喫茶店で書いてくる"),
            sana.go(),
            stage=w.on_herroom,
            day=w.in_firemaster, time=w.at_noon,
            )

def sc_aboutmaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, tsuchi, king = W(w.nirasaki), W(w.tsuchiura), W(w.king)
    return w.scene("先生について",
            sana.be("喫茶店でパソコンを広げている"),
            sana.do("音楽は聞かない。周囲の喋り声の雑音が心地良い"),
            sana.do("学生時代からそうだった。周りが何か喋っている方が集中できた"),
            sana.do("作品を書きながら、先生について考える"),
            sana.do("バッグから先生のノートを取り出して、覗き見る"),
            sana.do("そこにはサブストーリーについて書かれている"),
            sana.talk("そっか。あまりサブストーリーに傾倒しすぎると本筋を見失って、迷子になる。これが一番小説が書き終わらないパターン"),
            sana.think("自分の作品のサブストーリーの多さ、サブ人物の多さから、もう少し整理した方がいいな、と判断する"),
            sana.talk("うん。やっぱりこの方が捗る"),
            sana.do("スマホをマナーモードのまま"),
            sana.think("先生が美意識が大事と語っていたことを思い出す"),
            _.think("自分の作品の美意識とは何だろう"),
            _.think("先生はどんなことを考えながら普段作品を書いているのだろう"),
            _.think("一度聞いてみたいと思った"),
            _.do("創作ノートには沢山の書き込みがある。先生の字の丁寧さに感心する"),
            sana.do("自分の手帳の文字と見比べて、苦笑する"),
            stage=w.on_cafe,
            time=w.at_afternoon,
            )

def sc_emergency(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, tsuchi, king = W(w.nirasaki), W(w.tsuchiura), W(w.king)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("緊急事態",
            w.comment("火事のニュースに出ていたのは先生のアパートだった"),
            sana.come("マンションに戻ってくる"),
            sana.hear("遠くでサイレン"),
            sana.talk("ただいま"),
            gero.talk("おーかえり。なんか美味しいもの食べた？"),
            sana.talk("新発売あったけど今日は見送った。それより火事？"),
            azu.talk("そうみたい。三鷹の方って……"),
            sana.talk("ちょっと待って"),
            sana.think("嫌な予感"),
            sana.do("スマホを見る。先生からの通知のあと"),
            sana.talk("何だったんだろ"),
            sana.do("かけ直す。だがかからない"),
            sana.talk("ごめん。ちょっと行ってくる"),
            sana.do("タクシーを捕まえて"),
            stage=w.on_herhouse,
            time=w.at_evening,
            )

def sc_burning(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, tsuchi, king = W(w.nirasaki), W(w.tsuchiura), W(w.king)
    return w.scene("燃え盛るアパート",
            w.comment("かけつけた沙奈は燃える先生のアパートを見て呆然と"),
            sana.come("やってくる"),
            sana.do("既にすごい人混み"),
            sana.hear("古い木造アパートが燃えて、と聞こえる"),
            sana.do("見れば先生のアパートがほぼ全焼"),
            sana.talk("先生……"),
            sana.do("立っている警察にくいついて"),
            sana.talk("あの、先生……中の住人は？"),
            sana.explain("今助け出しているところと言われる"),
            sana.do("制止を突っ切って"),
            sana.talk("先生！"),
            noto.talk("ああ、$sana君。ごめん。原稿、焼けちゃったよ"),
            noto.do("手にした消し炭の原稿"),
            sana.do("それを受け取り"),
            sana.talk("原稿よりも先生が"),
            noto.talk("死なないよ。大丈夫だ"),
            noto.go("救急車に収容されて"),
            sana.think("どうしよう……"),
            stage=w.on_hisapart,
            time=w.at_night,
            )

## episode
def ep_chapter4(w: World):
    return w.episode("4.第四章",
            ## NOTE
            sc_writing(w),
            sc_aboutmaster(w),
            sc_emergency(w),
            sc_burning(w),
            )
