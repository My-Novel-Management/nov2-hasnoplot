# -*- coding: utf-8 -*-
"""Episode: 金閣寺
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
def sc_main1(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("第一章",
            noto.talk("ああ、そうだ", "$meは彼の作品を盗んだ",
                "それがデビュー作になったんだよ"),
            sana.do("先生はそう告白した", "密告の手紙は事実だった",
                "そしてそれを当時編集者だった編集長は知っていたのだ"),
            )

def sc_main2(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("第二章",
            sana.explain("$Sは編集者として以上に個人として、先生に弁明を求めた"),
            noto.talk("理由は簡単さ", "あいつの才能に嫉妬したからだ",
                "作家というのはね、自意識の塊なんだ", "醜悪な自分を褒めてもらいたくて何とか作品にして、芸術ということにして、",
                "それを他人に認めてもらいたい", "そんな矮小な存在でしかないんだよ", "全然偉くなんてない"),
            sana.do("先生の告白を聞きながら、自分はどうだったろうか、と考え込む"),
            noto.talk("だから君にも今の作品は見せられない", "今の$meを見れば分かるだろう？",
                "とても君を感動させたような話を書ける人間じゃあない", "ただのしょぼくれた、あと十年もすれば還暦を迎えるだけのつまらない男だ"),
            sana.talk("先輩は可愛らしい人だって言いました", "その意味が少しだけ分かりました"),
            _.do("$Sはそっと抱き締める"),
            noto.talk("な、何を？"),
            sana.talk("そんな風に自分をいじめなくてもいいんです", "書けなくても、誰も責めません",
                "その為に$meが今書いているんじゃないですか", "先生が書けるようになるまで、$meは待ちますから"),
            noto.talk("すまない……"),
            )

def sc_main3(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("第三章",
            sana.explain("先生の告白から数日が経過した"),
            _.explain("あれからぱたりと連絡が途絶え、アパートに確認にいっても鍵がかかっていることが増えた",
                "居留守ではなく、どこかに出ているらしい"),
            _.explain("近所の喫茶店やファミレス、行きつけの店を探してみたが、見つけられなかった"),
            sana.do("先生を探しつつも、編集として他の仕事をこなし、編集会議に出て、他の編集者との差を痛感したり"),
            sana.do("またバイト君の面倒を見なくてはならず"),
            sana.do("忙しさの中で、一日の終わりになんとか執筆を進めるという日々"),
            sana.do("そんな折、シェアハウスの友人たちも声がかかったり、仕事が入ったりと忙しくなっていく"),
            )

def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("第四章",
            sana.do("その日は久々の休日で、午前中は睡眠にかまけて、午後から執筆作業に入った"),
            sana.do("先生のメモを見返す"),
            _.do("サブストーリーについて"),
            _.think("先生の告白について思い返す"),
            _.think("まだ信じられないでいた"),
            _.do("執筆に集中できずに飛び出す"),
            sana.talk("先生？"),
            _.do("街を探して歩く"),
            _.hear("と、消防車と救急車のサイレン"),
            _.go("急いで追いかける"),
            _.come("先生のアパート近く"),
            sana.talk("そんな……"),
            sana.do("火事で先生のアパートが燃えている"),
            sana.explain("古い木造で趣があるとか言っていたが火事に対してはこの有様だった"),
            noto.come("燃え盛るアパートから救出される"),
            noto.have("その手には原稿を持っている"),
            sana.talk("先生！"),
            sana.do("だがその原稿はほとんど焼けてしまっていた"),
            noto.talk("すまない。折角の原稿が"),
            sana.talk("そんなものより先生が"),
            noto.talk("原稿は作家の命だよ、$sana君"),
            noto.go("救急車で運ばれていく"),
            sana.think("今の言葉の意味をよく噛みしめる"),
            )

## episode
def ep_main(w: World):
    return w.episode("金閣寺",
            ## NOTE
            sc_main1(w),
            sc_main2(w),
            sc_main3(w),
            sc_main4(w),
            )
