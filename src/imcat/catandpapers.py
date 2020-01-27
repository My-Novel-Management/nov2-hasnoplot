# -*- coding: utf-8 -*-
"""Episode: 2-4.猫と原稿／吾輩は猫である
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
def sc_havenoplot(w: World):
    sana, noto = W(w.sana), W(w.noto)
    fukaya = W(w.fukaya)
    return w.scene("プロットはない",
            noto.talk("ああ、だからないよ", "原稿どころかプロットもない"),
            sana.talk("え"),
            sana.do("慌てて自分の手帳を確かめる"),
            sana.talk("あの先生、$meは今日先輩から原稿をもらってくるように頼まれているんです。わかりますか？"),
            noto.talk("先輩というのは$fukayaさんのこと？"),
            sana.talk("そうです"),
            noto.talk("ないよ。それにそんな約束したかなあ"),
            sana.talk("いやいや、ここに書いてありますよ！"),
            sana.do("引き継ぎ資料を見せて"),
            noto.talk("ああ、確かにこの可愛らしい書き込みは彼女だね"),
            _.talk("しかし困ったなあ。ほんとに何もないよ。とにかくまだ資料を読んでいる段階でね"),
            _.do("手にしているのは猫の写真集だ"),
            sana.talk("ほんとに？"),
            sana.talk("あの、確認します"),
            sana.do("$fukayaに連絡する"),
            fukaya.voice("ああ、そうきたか。先生あれこれ理由つけてなかなか書かないから、がんばって！"),
            sana.talk("がんばってじゃないです！"),
            sana.talk("本当にないんですか？　メモくらいは"),
            noto.talk("探してみる？"),
            noto.do("部屋を見ると、すごく散らかっていた。寝室も、キッチンも"),
            noto.talk("最近$fukayaさん忙しくてなかなか顔出してくれなかったからねえ"),
            sana.think("編集は家政婦じゃないし"),
            sana.think("最悪中の最悪だと認定した"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_firstmeet, time=w.at_afternoon,
            )

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
            noto.do("出かけようとしている"),
            sana.talk("どこかに取材ですか？"),
            noto.talk("いや、近所のコンビニに買い出しに。何なら君が作ってくれてもいいけど"),
            sana.talk("作れと言われれば作りますけど"),
            _.do("だが冷蔵庫には何もない"),
            sana.talk("どうやって普段暮らしているんですか？"),
            noto.talk("何とかなるよ。東京だもの"),
            noto.do("ビールを出して飲み始める"),
            noto.talk("君も飲む？"),
            sana.talk("仕事中です！"),
            sana.talk("で、原稿はいつ書かれるんでしょうか？"),
            noto.talk("締切までにはね"),
            sana.talk("もう一度聞きますが、プロットとか、何か内容が確認できるものってないんですか？"),
            noto.do("自分の頭を指さして"),
            noto.talk("この中には入ってるんじゃないかなあ"),
            sana.talk("それ、かち割って中を見てもいいでしょうか？"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_firstmeet, time=w.at_midmorning,
            )

def sc_nobaggage(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, yone = W(w.nirasaki), W(w.king), W(w.yonezawa)
    return w.scene("手荷物すらなく",
            sana.come("結局先生の原稿もプロットすらも貰えず、失意のまま帰社する$S"),
            nira.be("パソコンに向かいつつ菓子パン食っている"),
            nira.talk("おう、どうした？"),
            sana.talk("$me、無理です。あの先生"),
            nira.talk("ああ、$noto先生ね。ご苦労さん"),
            nira.do("含み笑いしただけで何も言わない"),
            sana.talk("$nirasakiさんはどうしてるんですか、合わない担当って"),
            nira.talk("仕事と割り切れ。ま、実際仕事でしかないんだがな"),
            sana.talk("そういう仕事人間に$meはなりたい"),
            stage=w.on_heroffice_int,
            time=w.at_noon,
            )


## episode
def ep_cat_and_manupapers(w: World):
    return w.episode("4.猫と原稿",
            ## NOTE
            sc_havenoplot(w),
            sc_nousepc(w),
            sc_nobaggage(w),
            )
