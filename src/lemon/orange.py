# -*- coding: utf-8 -*-
"""Episode: 4-2.蜜柑／檸檬
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
def sc_masterprogress(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("進捗は",
            sana.do("先生の進捗を聞きにやってきたが、何もしていない"),
            sana.talk("どうしてなんですか！"),
            noto.talk("作家は何も原稿用紙に向かっている時ばかりが仕事ではない"),
            _.talk("こうしてぼーっとしているのも仕事なんだ"),
            sana.talk("まだ締め切りまで時間がありますからね。それでもプロットくらいあるんですよね？"),
            noto.talk("ない"),
            sana.do("溜息"),
            sana.talk("約束は守って下さいよ"),
            noto.talk("ちゃんと書いているんだね。いやあ感心感心"),
            sana.think("まるで他人事だ"),
            w.load("短編と長編の違い"),
            noto.talk("そういう訳で、短編の方が長編よりも書く枚数が少ないからといって時間がそれだけ少なくて済む、という訳じゃないということだ"),
            _.talk("原稿用紙二十枚程度だと侮っていたんじゃないかと思ってね"),
            sana.talk("そんなことは……"),
            _.think("ない、とは言えなかった"),
            sana.talk("分かりました。今日は帰りますが、締切まで毎日伺いますから"),
            noto.talk("そういうところは$fukayaさんに教わったのかい？"),
            _.talk("彼女も諦めない人だった。作家は諦めが早い人もいる。だからこそ編集は諦めの悪い人の方が良い"),
            _.talk("でもね、時には飴も欲しいものだよ、$sana君"),
            sana.talk("あ！　差し入れですか！　それなら得意です"),
            noto.do("苦笑する$Sだった"),
            camera=w.sana,
            stage=w.on_hisapart,
            time=w.at_afternoon,
            )

def sc_harddays(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("苦労した日々",
            sana.do("仕事に出て、合間にスマホでメモを書き溜めて"),
            sana.do("残業を終えて帰ってから、何とか原稿にする"),
            sana.do("そんな日々を二週間ばかり送った"),
            )

def sc_uppaper(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("原稿が上がった",
            sana.do("残業の後、何とか徹夜で執筆"),
            sana.do("栄養ドリンクで目をさましつつ"),
            sana.do("執筆は最後が決まらなかった"),
            sana.do("物語は終盤、自分が愛する者たちの命を奪う死神の女性が、どうしても奪えないと悩む"),
            sana.do("なぜ彼女が奪い始めたのか、それが分からなくなっていた"),
            sana.do("殺してくれ、と、助けてくれ、を言われて、最後は涙と共にその命を奪う"),
            sana.do("全てを奪ってまっさらにした世界に、再びちゃんとした世界を作るのだと立ち上がろうとしたが、永遠の命の死神は心が疲弊していた"),
            sana.do("何とか書き上げて、そのまま突っ伏す"),
            sana.do("寝てしまう"),
            sana.do("翌朝、$azuminoに原稿印刷を頼み、とにかく仕事に。途中で立ち寄って原稿回収し、先生の家に向かおうと"),
            stage=w.on_herroom,
            time=w.at_night,
            )

def sc_discard(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("原稿を捨てられた",
            sana.do("翌日、印刷した原稿を持っていったら、先生にその手でゴミ箱に捨てられた"),
            sana.talk("なんでですか！？"),
            noto.talk("それ、ちゃんと書いた？"),
            noto.talk("とりあえず枚数さえ満たせばとか、思ってなかった？"),
            sana.talk("$meがどんな気持ちでこの二週間、原稿に向かっていたかなんて、先生に分からないでしょ！"),
            noto.talk("そうだよ"),
            _.talk("でも、それは君たちが作家にしているのと同じことじゃないかな"),
            _.talk("どんなに必死だったのか、そんなこと考えていないよね？　面白いかどうか、だけじゃないか？"),
            sana.talk("それは"),
            sana.think("何も言い返せなかった"),
            noto.talk("しかし約束だ。君は書き上げた。だから明日、原稿を取りに来なさい。いいね？"),
            sana.talk("はい"),
            stage=w.on_hisapart,
            )

## episode
def ep_orange(w: World):
    return w.episode("2.蜜柑",
            ## NOTE
            sc_masterprogress(w),
            sc_harddays(w),
            sc_uppaper(w),
            sc_discard(w),
            )
