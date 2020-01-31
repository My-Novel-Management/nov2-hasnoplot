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
def mo_searchmaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, fukaya = W(w.nirasaki), W(w.fukaya)
    sphone = W(w.sphone)
    return (
            w.scene("先生を探す",
                sana.come("探して歩いている"),
                sana.do("スマホの引き継ぎ資料を頼りに行きそうな場所を見繕う"),
                sana.talk("全く！　初日からどうなってるの！"),
                sana.do("と$nirasakiから連絡が入る"),
                nira.voice("$fukayaさん、どうやら軽い出血だけで異常はなかったそうだ。ただ入院して経過を見るって"),
                sana.talk("なんでインフルで休んだあんたが連絡してきてんのよ！"),
                w.comment("実はこの時$nirasakiは自宅でゲーム実況配信をしていたが、それはまた別の話"),
                stage=w.on_street,
            ),
            w.scene("三鷹の街",
                sana.come("先生を探して歩く"),
                sana.explain("三鷹は作家の街、特に太宰治で有名だ"),
                _.think("先生もそんな憧れを持ってこの街にやってきたのだろうか、と"),
                sana.do("スマホを確認して"),
                sana.talk("お昼がどうこうって言ってたし、ひょっとして"),
                sphone.look("先生の行きつけの一つとして近所の喫茶店が出ている"),
                sana.go("そこに向かう"),
            ),
            ## NOTE
            ##  先生を探しつつ、どこの街なのかを改めて示しておく。街の雰囲気なども
        )

def sc_havenoplot(w: World):
    sana, noto = W(w.sana), W(w.noto)
    fukaya = W(w.fukaya)
    chiyo = W(w.chiyoda)
    inside = W(w.inside)
    return w.scene("プロットはない",
            sana.come("店に入ってくる"),
            inside.look("店内は半分程度入っている"),
            chiyo.be("コーヒーを落としている"),
            chiyo.talk("いらっしゃいませ。お好きなお席に……"),
            sana.talk("あの、$noto先生は？"),
            chiyo.talk("あら、先生のお知り合い？　いつもの席ですよ"),
            noto.be("観葉植物で隠れた席に座っている"),
            sana.do("先生を見つけて"),
            sana.talk("先生！"),
            noto.talk("まだ何も食べていなかったことを思い出してね", "君も何か食べるかい？"),
            sana.talk("頼まれたビールは冷蔵庫に、それから、合鍵、勝手に使わせてもらいましたよ",
                "鍵もかけずに外出するなんてありえないですよ"),
            noto.talk("なあに、すぐに帰るつもりだったさ。それに、取られて困るようなものは何もない"),
            sana.talk("原稿は？"),
            noto.talk("まだない", "原稿どころかプロットもない"),
            sana.talk("え"),
            sana.do("慌てて自分の手帳を確かめる"),
            sana.talk("あの先生、$meは今日先輩から原稿をもらってくるように頼まれているんです。わかりますか？"),
            noto.talk("先輩というのは$fukayaさんのこと？"),
            sana.talk("そうです"),
            noto.talk("ないよ。それにそんな約束したかなあ"),
            sana.do("さっき見せた誓約書を見せつけて"),
            sana.talk("いやいや、ここに書いてありますよ！"),
            noto.talk("うむ。しかし困ったなあ。ほんとに何もないよ。とにかくまだ資料を読んでいる段階でね"),
            sana.talk("ほんとに？"),
            sana.talk("あの、探してきてもいいですか？"),
            noto.talk("無駄だと思うが、散らかさない程度に見てくるといい。仮採用になった編集さん"),
            sana.think("仮採用、だと……"),
            sana.think("最悪中の最悪だと認定した"),
            camera=w.sana,
            stage=w.on_mastercafe_int,
            day=w.in_firstmeet, time=w.at_afternoon,
            )

def sc_nousepc(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("パソコンすらなく",
            w.comment("どこかで今日は出かけなくてはいけない風なことを先生が言う"),
            sana.come("合鍵を使って入ってくる"),
            sana.talk("あれは見つからない自信があるからなんだろうけど、見つけますから。得意なんですよ、$me"),
            sana.do("散らばっている部屋を掃除していく"),
            sana.talk("そもそもパソコンはどこ？"),
            _.do("探すがない"),
            _.do("テーブルの上の原稿用紙は真っ白。全部何も書いてない"),
            sana.talk("今どきパソコンも持ってないでどうやって執筆しているんだこれ"),
            _.talk("ううん。きっとこれはフェイクよ。絶対にあるんだからね"),
            _.do("そう言い聞かせて探すが、なかった"),
            w.comment("ここで先生の部屋の間取りや雰囲気を描写しておく"),
            sana.do("古いノートを見つけて、引き抜こうとしたところで"),
            noto.come("帰ってくる"),
            sana.talk("先生。パソコンはどこですか？"),
            noto.talk("だから$meは機械に疎いと言っただろう"),
            sana.talk("え？　じゃあどうやって執筆を？"),
            noto.talk("作家が原稿に書かなくてどうするんだい？"),
            sana.talk("全部ですか？　入稿はどうやってるんです？"),
            noto.talk("$fukayaさんに任せてたから分からないけど、彼女が直してたんじゃないの？"),
            sana.think("想像を絶する作業だった"),
            sana.talk("先輩だからいつも指が腱鞘炎だって言ってたのか"),
            sana.think("前途多難"),
            noto.do("ビールを出して飲み始める"),
            noto.talk("君も飲む？"),
            sana.talk("仕事中です！"),
            sana.talk("で、原稿はいつ書かれるんでしょうか？"),
            noto.talk("締切までにはね"),
            sana.talk("もう一度聞きますが、プロットとか、何か内容が確認できるものってないんですか？"),
            noto.do("自分の頭を指さして"),
            noto.talk("この中には入ってるんじゃないかなあ"),
            sana.talk("それ、かち割って中を見てもいいでしょうか？"),
            ## NOTE
            ##  この日は月命日なのでこれからお参りに出かける先生
            camera=w.sana,
            stage=w.on_hisapart,
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
            time=w.at_afternoon,
            )


## episode
def ep_cat_and_manupapers(w: World):
    return w.episode("4.猫と原稿",
            ## NOTE
            *mo_searchmaster(w),
            sc_havenoplot(w),
            sc_nousepc(w),
            sc_nobaggage(w),
            )
