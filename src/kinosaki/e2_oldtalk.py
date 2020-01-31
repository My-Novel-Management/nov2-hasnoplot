# -*- coding: utf-8 -*-
"""Episode: 6-2.昔の話にて／城の崎にて
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
def sc_onsen(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("温泉に入る",
            sana.do("とりあえず温泉ということで、街に繰り出す"),
            sana.explain("足湯から、自由に入れる温泉から、いろいろある"),
            sana.talk("素敵ですね！"),
            sana.do("浴衣に着替えて上機嫌"),
            noto.do("着物姿もいいけれど、浴衣姿もまた良い"),
            sana.talk("先生はよくくるんですか？"),
            noto.talk("毎年来たいが、そうもいかないね"),
            noto.talk("まあ、予定や費用のことばかりでないんだけどね"),
            noto.do("遠い目"),
            noto.talk("それよりどう？　こういう慰安も良いだろう"),
            sana.talk("え？"),
            noto.talk("だいぶ疲れてたみたいだからね。短編の方では君に迷惑を掛けた"),
            sana.talk("先生の為に苦労するのは編集の義務ですから"),
            noto.talk("ぶったおれるのまで義務とは言わないでくれ"),
            sana.talk("分かりました"),
            sana.talk("あそこ、岩盤浴もありますよ！"),
            noto.talk("$meは普通の温泉でいいんだけどなあ"),
            sana.talk("何言ってるんですか。知的好奇心です！"),
            camera=w.sana,
            stage=w.on_street,
            day=w.in_trip_kinosaki, time=w.at_afternoon
            )

def sc_aboutscene(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("シーンについて",
            sana.do("水着姿の$S"),
            sana.do("先生と混浴の内風呂に入っている"),
            noto.talk("そんなもの、いつ用意したんだ？"),
            sana.talk("えろいです、先生"),
            noto.talk("だってそれ、スクール水着じゃないのか"),
            sana.talk("急だったからこれしかなかったんです。打ち合わせに必要でしょう？"),
            noto.talk("こんな時まで仕事しなくても"),
            sana.talk("先生"),
            noto.talk("はい"),
            noto.talk("一応この前の短編を膨らませて、$meだから書ける異文化の世界というのを題材にしようと思っている"),
            sana.talk("$meもその方向ですね"),
            noto.talk("最近は子連れものはどうなのだろうか"),
            sana.talk("一応ありますよ。子連れというより子育てというか、娘ものというか"),
            noto.talk("父親が傷つきながらも異形の世界で子どもを守る。この作品から今の児童虐待になってしまう親たちの気持ちに何か救いを見つけられたらと思うんだ"),
            sana.talk("いいと思いますよ"),
            noto.talk("ただ、家族を持たない$meからすると、ハードルが高い"),
            noto.talk("誰か小さなお子さんのいる家庭を紹介してもらえないかな、と思っている"),
            sana.talk("いくつか取材先をピックアップしてみます。たぶん雑誌時代に世話になったママさんたちに連絡すれば何とか"),
            noto.talk("それは助かるよ"),
            noto.talk("本当に担当編集は初めてなの？", "$fukayaさん譲りのフットワークとやる気、それはすごいね"),
            sana.talk("これでもいっぱいいっぱいですよ"),
            sana.talk("でも脱ぐ以外のことでしたら何でもします、と言った手前、やらないとは言えませんよ"),
            noto.talk("そういえばそんなこともあったね"),
            sana.explain("二ヶ月前の話に花が咲く"),
            w.load("シーンについて"),# シーンについての講義
            ## NOTE
            ##  温泉は「混浴」も考える。部屋に帰ってからでいいかな
            stage=w.on_onsen,
            )

def sc_currently(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("現在の出版状況",
            sana.do("旅館に戻り、そこで話の続きを"),
            noto.talk("そういえば最近はどうなんだろう", "随分と台所事情が厳しくなっていると"),
            noto.talk("そのせいで担当が一人ではなく何人、何十人と作家を抱えなければならずに、一人に割く時間、一作にかける時間も少なくなっていると"),
            sana.talk("そういうのはあります"),
            sana.talk("でも出版業界だけじゃありませんね"),
            sana.talk("どこでも必要な人材をどんどん削っていって、結果、仕事が回らなくなっているんです"),
            sana.talk("例えば、ＤＴＰになってから、印刷所への入稿ギリギリまでねばれるようになりました"),
            sana.talk("普通なら編集などにかける時間が増えるはずなんです"),
            sana.talk("でも実際は企画から入稿までの時間が減らされるんです。おかしいですよね"),
            sana.do("酒が入り、饒舌になってきている"),
            sana.talk("とにかく薄利多売で何とかもっているようなものです"),
            sana.talk("それこそ村上春樹先生みたいな売れっ子を抱えれば何とかなるかも知れませんけど、"),
            sana.talk("一人のバケモノ作家が他の全てを食わせる、なんてもう無理なんですよ"),
            sana.talk("わかってますよ", "出版て結局作家の才能にぶらさがる、才能ゴロだって"),
            sana.talk("でもそれは出版だけじゃない。音楽だってそうだし、芸能だってそう"),
            sana.talk("だからこその夢なんです", "自分にはそこまでの才能はない。けど、その夢を具現化している人を応援することはできる"),
            sana.talk("だから$meは編集になって、先生の本を出したいんです"),
            noto.talk("飲みすぎだよ……"),
            sana.talk("たまには愚痴りたいんですぅ"),
            noto.talk("ははは"),
            stage=w.on_oldinn,
            ## NOTE
            ##  - 出版点数は約80000／年
            ##  - 返品率は目標２割、実質４割
            ##  - コミックに限ると1997年から売上半額
            ##  - 近年は電子出版が伸びてきている
            ##  - 書店は1冊あたり２割の取り分があり、それが売上
            )

def sc_oldtalk(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("昔話",
            noto.talk("君が酔っているこんな時だから、言うんだが"),
            _.talk("$meは昔、人殺しをした。それも大切な人を二人もだ"),
            w.eventStart("先生と親友"),
            ## NOTE
            ##  ここ、先生の告白ではなくて、沙奈の下呂の件の相談を持ってくる。そこから「昔、大切な女性がいてね」という話
            )

## episode
def ep_oldtalk(w: World):
    return w.episode("2.昔の話にて",
            ## NOTE
            sc_onsen(w),
            sc_aboutscene(w),
            sc_currently(w),
            sc_oldtalk(w),
            )
