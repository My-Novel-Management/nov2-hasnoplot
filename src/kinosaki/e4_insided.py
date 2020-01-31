# -*- coding: utf-8 -*-
"""Episode: 6-4.心の内にて／城の崎にて
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
def sc_exchange_condition(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("交換条件",
            w.comment("長編原稿を捨てた先生に対して、沙奈も書くからもう一度チャレンジしてと頼む"),
            sana.be("寝ている"),
            sana.hear("何かを破る音を聞く"),
            noto.be("ゴミ箱の前にいる"),
            sana.talk("先生何してるんですか！"),
            noto.do("原稿を破っていた"),
            noto.talk("ああ、おはよう。朝起きて読んでみたら、こんな作品は$meのものじゃないと分かった"),
            sana.talk("でも折角書いたのに"),
            noto.talk("書いた、というものは原稿ではなく、ただの文章だよ。文字の塊だ"),
            _.talk("駄文ですらない"),
            _.talk("小説でないことは昨夜読んだ君が一番よく理解していると思ったのだが、違うかね？"),
            sana.talk("それは……"),
            _.think("自分の感覚に嘘はつけなかった"),
            noto.talk("やはり無理なんだ。もう$meには小説は書けない"),
            sana.talk("まだ書き始めたばかりじゃないですか"),
            sana.talk("先生は言いましたよね？　最初から完成している小説なんかないって"),
            sana.talk("書き上げてからがスタートなんだって"),
            sana.talk("一緒に作り上げていきませんか？", "駄作かどうかは作者が決めることじゃない。$meが決めることでもない"),
            sana.talk("読んだ誰かが面白かったかどうか、心を打ったかどうかです"),
            sana.talk("評価なんて百人いたら百通りなんです"),
            noto.talk("じゃあ君はあれを校正すれば売り物になったと思うのか？"),
            _.talk("$meの作品として楽しめたとでも？"),
            sana.do("答えられない"),
            noto.talk("残念ながら$meは、いや、作家というのは卑屈の塊なんだよ"),
            _.talk("いつだって、心のどこかでは誰かに褒めてもらいたい。すごいと言ってもらいたい。そういう気持ちが隠れている"),
            _.talk("でもおおっぴらには口にできないから、常に自信なさげか、逆に見栄っ張りで、自分の作品がどうして評価されないって思ってる"),
            _.talk("けどいざ書いている自作を読んでみると、これ本当に面白いのだろうかと悩む"),
            _.talk("そんなことの繰り返しなんだ"),
            _.talk("多くの作家が書けなくなる、続きを出せなくなるのは、何も売上が全てじゃない"),
            _.talk("やがて行き詰まるんだ"),
            _.talk("自分の全てを否定されたような気になる"),
            _.talk("それは作品だけじゃなく、自分自身の全てがそうなんじゃないか"),
            _.talk("この世界ではもう自分の作品は、いや、自分自身は必要とされていないんじゃないかって、そんな不安で押しつぶされる"),
            _.talk("だから夜中に窓を開けて思い切り叫ぶこともある"),
            _.talk("迷惑だからと公園まで出かけて走り回ったこともある"),
            _.talk("でもそこまで自分が追い詰められて、何とか捻り出した作品は本にすらならず"),
            _.talk("よしんば本になったとしても売れなくて、感想すらなく、担当に次がありますと言われて、大量の在庫を抱える"),
            _.talk("大半の作家がそうなんだよ！"),
            sana.talk("先生！"),
            sana.do("抱き締める"),
            sana.talk("分かってます"),
            sana.talk("でも、$meは待ってますから"),
            noto.talk("そうやって君たち編集はいつだって"),
            sana.talk("編集は待つのが仕事だと$fukaya先輩も言ってました"),
            noto.talk("いくら待ってももう$meからは何も"),
            sana.talk("それじゃあ、$meも書きます"),
            _.talk("長編小説を、書きます。それならいいでしょう？"),
            noto.talk("え？"),
            sana.talk("短編の時のように$meに教えながらなら、きっと素晴らしいものが書けますよ。先生は、そういう方がいいんです"),
            noto.talk("できるだろうか"),
            sana.talk("一人では無理でも、二人なら、可能性も大きくなります"),
            noto.talk("そうか。やってみようかな"),
            sana.talk("はい"),
            ## NOTE
            ##  初恋の女性のことを思い出して悲しくなった、心細くなった先生を励ますとともに、小説を書くことになる
            camera=w.sana,
            stage=w.on_oldinn,
            day=w.in_backhome, time=w.at_morning,
            )

def sc_intrain(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("電車の中にて",
            sana.be("帰りの新幹線車内"),
            noto.be("窓際の席で眠りこけている"),
            sana.do("眠りこける先生を見て笑う"),
            sana.do("そっとスマホを翳して写真を撮る"),
            sana.think("少し考え、"),
            sana.do("自分と一緒の写真も撮った"),
            w.comment("日記部分"),
            sana.explain("こうして$meも小説を、それも長編小説を書くことになりました"),
            _.explain("つい勢いで約束してしまったけれど、学生時代から一度として長編小説は完結させたことがないので不安です"),
            _.explain("それでも先生がもう一度、先生の小説を書くことができる、その応援ができるなら、精一杯書いてみようと思います"),
            stage=w.on_train,
            )

## episode
def ep_insided(w: World):
    return w.episode("4.心の内にて",
            ## NOTE
            sc_exchange_condition(w),
            sc_intrain(w),
            )
