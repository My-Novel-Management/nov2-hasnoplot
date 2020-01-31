# -*- coding: utf-8 -*-
"""Episode: 2-2.猫と小説／吾輩は猫である
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
def sc_aboutmaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    cat = W(w.mascat)
    return w.scene("先生について",
            sana.be("二人が対峙している"),
            noto.be(),
            cat.be("$CSの膝の上"),
            sana.talk("それで本日締切の原稿なんですが"),
            noto.talk("原稿？　締切？　知らないなあ。そもそも君は$meの担当じゃないだろう"),
            sana.talk("さっきの説明聞いてましたか？"),
            cat.talk("にゃおん"),
            sana.hear("猫が変わりに返事して"),
            noto.talk("お腹でも空いてるのかな。君、ちょっとキッチンの棚から猫缶を取ってきてそいつにあげてくれ"),
            sana.talk("$meがですか？"),
            noto.talk("$meの担当をしたいのだろう？"),
            sana.talk("はい……"),
            sana.do("とりあえず取ってきて、猫缶をやる"),
            noto.talk("で、用件は理解した。もう挨拶は済んだろう。帰り給え。$meは忙しいんだ"),
            sana.do("どう考えても本を読みながら猫とたわむれていたとしか思えない"),
            ## NOTE
            ##  どうしても原稿を渡さない先生に、せめてプロットだけでもと迫るが、返答は悪いし
            ##  まず担当として認めないと言い出して、ならばオーディションという流れ
            ##  ここで「妙な先生」と「引き下がらない沙奈」の構図にしておく
            camera=w.sana,
            stage=w.on_hisapart_int,
            day=w.in_firstmeet, time=w.at_noon,
            )

def sc_preparecatmeal(w: World):
    sana, noto = W(w.sana), W(w.noto)
    cat = W(w.mascat)
    phone = W(w.sphone)
    return w.scene("猫缶準備",
            sana.be("キッチンにやってきて猫缶を探す"),
            sana.think("あれは絶対原稿を書いていないんだ。とにかく何か貰って帰らないと、作家はつけあがる"),
            _.think("$fukayaから教わったことを思い出す"),
            sana.think("先生の取扱説明書を思い出す"),
            _.do("スマホを取り出して取説を呼び出す"),
            phone.look("先生の取説が表示される"),
            sana.think("一度へそを曲げたらその日は何もできない"),
            _.think("気分が乗らないと執筆しない"),
            _.think("ただし小説の話を始めると長い。話は大好きである"),
            sana.do("皿に猫缶を出して持っていく"),
            ## NOTE
            ##  ここでスマホで取説を確認すること。また先生に対する本音を書いておく
            stage=w.on_kitchen,
            )

def sc_negotiate(w: World):
    sana, noto = W(w.sana), W(w.noto)
    cat = W(w.mascat)
    shelf = W(w.bookshelf)
    return w.scene("交渉する",
            sana.come("猫の餌を持ってやってきて"),
            noto.be("猫を撫でてくつろいでいる"),
            cat.be("先生の膝の上で待っている"),
            cat.do("$CSを見て、のっそりとやってくる"),
            _.do("餌を食べ始める"),
            sana.talk("それで先生"),
            noto.talk("ああ、もう用はないから帰ってくれて良い"),
            sana.talk("こっちが用があるんですよ！"),
            _.do("スマホを見て、写真に収めた誓約書を出す"),
            _.talk("覚えてますか？　これ"),
            _.do("先生に見せる"),
            noto.talk("$meは機械が苦手でね。何だね、それ？　原稿？"),
            sana.talk("先生が書かれた誓約書ですよ！"),
            noto.talk("確かに$meの字によく似ているが、最近はそういったものも機械でちゃんちゃんと模造できるのだろう？"),
            sana.talk("先生の記憶も今後は全部メモリにコピーしておくようにします"),
            noto.talk("へえ、そんなことまでできるの？"),
            sana.talk("できません！　けどしたいです！"),
            _.talk("とにかく記憶を呼び起こして下さい。これ、もう三ヶ月も前の話なんですよ？"),
            noto.talk("ああ、そりゃあ忘れるねえ。昨日のご飯ですら覚えがない"),
            sana.talk("とにかく原稿を貰うまで$meは今日、帰りませんからね"),
            noto.talk("まるで$meの担当みたいなことを言うねえ"),
            sana.talk("本日$fukayaから担当を引き継ぎました$full_sanaですから！"),
            noto.talk("そういえば$fukayaさんは？"),
            sana.talk("産休です。まだ連絡ないんですが、今朝救急車で運ばれていきました"),
            noto.talk("大丈夫なのかい？"),
            sana.talk("分かりません。でも心配すること以外今の$meたちにできることはありません。それよりも先生、原稿どこですか？",
                "書いてますか？　探しますよ？"),
            sana.do("立ち上がる"),
            noto.talk("待った"),
            sana.talk("なんですか？"),
            noto.talk("初めてきた女性に家探しを許可するほど、$meも寛容ではなくてね"),
            sana.talk("先生本当に作家なんですか？"),
            shelf.look("沢山の本、小説が並ぶ", "その中に『$masternovel1』もある"),
            noto.talk("君こそ本当に編集なのかね？　多少は小説というものを理解しているのかね？"),
            sana.think("食いついた、と思った"),
            sana.talk("あなたが本物の先生なら$meの知識は遠く及ばないでしょうが、偽物なら余裕です。",
                "毎日毎日どれだけの文字と戦っていると思ってるんですか"),
            noto.talk("よし。なら君が本物の編集かどうか、オーディションをしようじゃないか"),
            sana.explain("テストではなく、何故かオーディションが始まった"),
            ## NOTE
            ##  小説の話をもちかけて、そこから「なら君を担当として相応しいかオーディション」と
            ##  今回のメインは割とここ
            stage=w.on_hisapart_int,
            time=w.at_noon.elapsedMin(10),
            )

## episode
def ep_cat_and_novel(w: World):
    return w.episode("2.猫と小説",
            ## NOTE
            sc_aboutmaster(w),
            sc_preparecatmeal(w),
            sc_negotiate(w),
            )
