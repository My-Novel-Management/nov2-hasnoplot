# -*- coding: utf-8 -*-
"""Episode: 10-2.ジョバンニの気持ち／銀河鉄道の夜
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
def sc_find_mymaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生を見つけ出した",
            w.comment("沙奈は何とか会話から先生の行く場所を割り出し、墓地にやってきた"),
            w.comment("墓地の寂しい空気感を描いておく"),
            sana.come("以前に連れてこられた墓地へとやってくる"),
            sana.explain("$yuzawaに原稿を見せてもらった後、コピーをバイク便で送ってもらうことにして、$Sは再度ここにやってきた"),
            sana.talk("ここにいたんですね"),
            noto.be("友人の墓の前にしゃがみこんでいる"),
            noto.talk("今日が何の日か、君に説明するまでもないようだな"),
            sana.think("親友、と先生が呼んだ$full_tsuruの月命日だった"),
            _.explain("太宰治が亡くなった日を選んで、$full_tsuruは自殺したのだ"),
            noto.talk("どうしても彼に聞いておきたかった", "もう一度、書いてもいいのかと"),
            noto.talk("ずっと彼への謝罪と後悔の気持ちを抱えて生きてきた"),
            _.talk("いや、ただ死なないようにしていただけだ"),
            _.talk("彼の作品を奪っておいて、それでのうのうと作家をやっていることに常に罪悪感があった"),
            _.talk("それでも書くことが、小説が好きなんだ。やめられない"),
            sana.talk("先生。先生は大きな勘違いをされています"),
            noto.talk("$meの半分程度しか生きたことのない君に、何が分かる？"),
            sana.talk("分かります"),
            noto.talk("分からないよ！"),
            sana.talk("$meは分からなくても、$tsuruさんは分かっていたんですよ！"),
            noto.talk("何が言いたい？"),
            sana.talk("来て下さい。$meの家に"),
            noto.do("訳が分からない、といった表情に"),
            ## NOTE
            ##  先生と対峙する
            camera=w.sana,
            stage=w.on_hiscemetery,
            day=w.in_vanishmaster, time=w.at_afternoon,
            )

def sc_inthecar(w: World):
    sana, noto = W(w.sana), W(w.noto)
    interior = W(w.interior)
    return w.scene("沈黙の車内",
            sana.be("運転している"),
            interior.look("フロントガラスの外に曇り空が広がる"),
            sana.do("車で移動する$Sたち"),
            noto.do("喋らない"),
            sana.talk("それより病院を抜け出して火傷は平気なんですか？"),
            noto.do("黙ったまま"),
            sana.think("仕方ない、と思い、一人で喋り始める"),
            sana.talk("$me、先生が自宅に隠し持っていた手紙、持ってます。焼けてません"),
            noto.talk("何だって！？"),
            noto.talk("あれには誰にも話したことのない秘密が"),
            sana.talk("盗作のことですか？"),
            noto.talk("読んだんだね"),
            sana.talk("担当作家のことを知るのも、編集の仕事ですから"),
            noto.talk("なら分かるだろう？", "$meは作家として最低のことをした。盗作だ。彼の才能を盗んだんだ"),
            sana.talk("そう、書かれていましたね"),
            noto.talk("盗作した作家がどうなったか、君も知っているだろう？"),
            sana.talk("盗作の証明はできません"),
            noto.talk("何を言うんだ？　$me自身がそうだと言ってるんだぞ？"),
            stage=w.on_car_int,
            ).omit()

def sc_truth_hissuicide(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("彼の自殺の真相",
            w.comment("先生に沙奈は親友の持ち込み原稿を見せて、真実を語った"),
            sana.come("先生を連れてやってくる"),
            gero.be("ゲームして遊んでいる"),
            azu.be("掃除している"),
            sana.do("シェアハウスの友人たちもいて、騒ぐ"),
            gero.talk("あんれま、先生さん？"),
            azu.talk("え？　ちょっと化粧してないのに、いきなり連れてこないでよ！"),
            azu.go("自室に引っ込んでしまう"),
            gero.do("にやにやとして見ながら"),
            gero.talk("遂に家にまで連れ込む仲になったんやな？"),
            _.talk("何も言わんでも分かっとるがな。あとは二人でどうぞ……"),
            sana.talk("そういうんじゃないんだけど……"),
            gero.talk("分かっとる分かっとる"),
            gero.go("自室に引っ込む"),
            sana.talk("ごめんなさい。いつもあんな感じなんで"),
            noto.talk("ああ"),
            sana.talk("ちょっとここで待ってて下さい"),
            sana.do("自室から茶封筒を持ってやってくる"),
            sana.talk("これを読んで下さい"),
            noto.talk("君のか？"),
            sana.do("答えない"),
            noto.do("とりあえず封筒から原稿を出す。古い原稿"),
            noto.talk("これは……"),
            noto.think("すぐに彼のものだと分かった"),
            noto.do("読み耽る"),
            noto.talk("これは……どうして。そんなはずは"),
            sana.talk("そこに書かれているのは紛れもなく$tsuruさんの小説です",
                "彼が盗作した、先生の小説です"),
            sana.explain("盗作、ということが分かるのは、先生が手紙の中で語っていた最後だけ変更した、という部分",
                "先生の出版された作品そのままのラストだったからだ"),
            sana.talk("盗作したのはどちらでしょうか？"),
            noto.talk("$meは、彼の作品のメモを見て、それで……"),
            sana.talk("これは知人の編集の手を借りて発掘したものです",
                "これがあったのは、別の出版社でした。没になった持ち込み原稿を、今はリタイヤした編集者が持っていたんです"),
            sana.talk("その方は盗作じゃないかと直感したそうです",
                "何故なら、他の持ち込み短編とは明らかに文章が違っていたから、と",
                "先生の文章だったからです"),
            sana.talk("文章の真似はできるかも知れません。けど、それは写真のようにはいかないでしょう",
                "特に手書き原稿だった時代には、完璧なコピーなど不可能です"),
            noto.talk("なんてことだ……"),
            sana.talk("遺書に書かれていた「絶望した」のは自分自身の才能と盗作してしまったことについて、だったんです"),
            w.eventEnd("先生の盗作騒動"),
            ## NOTE
            ##  ここで下呂たちは先生と初対面（それぞれ沙奈を通じて世話にはなっている）
            ##  バイク便を使って既に受け取っている
            camera=w.sana,
            stage=w.on_herhouse_int,
            time=w.at_evening,
            )

## episode
def ep_geovanni(w: World):
    return w.episode("2.ジョバンニの気持ち",
            ## NOTE
            sc_find_mymaster(w),
            sc_inthecar(w),
            sc_truth_hissuicide(w),
            )
