# -*- coding: utf-8 -*-
"""Episode: 8-3.第三章／金閣寺
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
def sc_stalker(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nose = W(w.nose)
    return w.scene("ストーカー被害",
            w.comment("最近何か妙なことが起こると思っていたら、ストーカーされていた"),
            sana.do("会社からの帰り道"),
            sana.do("駅を出て、歩く"),
            sana.think("最近誰かに見られているとよく感じる"),
            sana.think("つけられているのかな？"),
            sana.do("コンビニに入って確かめる"),
            sana.do("気の所為と分かって、再びアパートに向かう"),
            w.eventPoint("沙奈のストーカー", "つけられている？"),
            ## NOTE
            ##  ストーカーを思わせて、野迫川を登場させる
            camera=w.sana,
            stage=w.on_street,
            day=w.in_stalking, time=w.at_night,
            )

def sc_intimidation(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nose = W(w.nose)
    return w.scene("脅迫",
            sana.do("薄暗い路地"),
            sana.hear("パトカーのサイレン"),
            sana.do("スマホで友人に連絡。だが二人ともバイトだった"),
            sana.think("確かに自分をつける影が一つある"),
            sana.do("慌てる"),
            sana.do("メッセージが送られてくる"),
            sana.think("それはまるで自分が書いたような文面"),
            sana.think("これってひょっとして……"),
            sana.talk("ひょっとして$noseさんですか？"),
            sana.do("立ち止まって振り返ると、フードの男が笑った"),
            noto.talk("知ってたか。もうあんたの家そこだろ。お茶くらい出してくれよ"),
            )

def sc_manstalk(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira = W(w.nirasaki)
    nose = W(w.nose)
    return w.scene("男の話",
            w.comment("ここで$noseの気持ち悪さと切実さを表現しておく。暴力には訴えない"),
            nose.be("くつろいでいる"),
            sana.talk("一体何なんですか？", "先生に用事があるなら直接言って下さい"),
            nose.talk("あんたは編集なんだろう？　だったら小説の話だ"),
            sana.talk("持ち込み、ということですか？　それなら明日出版社の方に"),
            nose.do("机を叩いて"),
            nose.talk("作家の話を聞かないのはよくないな。先生の原稿もってんだろ？　見せてくれ"),
            sana.talk("何言ってるんですか？"),
            nose.talk("あの人には世話になった。$meはもう一度あの人を喰らう"),
            sana.talk("くう？"),
            nose.talk("ノベルイーター。$meはそう呼んでる。良い小説をパクるんだよ。それで$meの小説にする。そうすれば、また復活できる"),
            sana.talk("あなたは盗作で、もうこの業界じゃ"),
            nose.talk("名義も何も変えればいいだけさ。芸能人と同じだ。顔が出る商売じゃない。名前もいくらでも使える"),
            nose.talk("$meに、小説を書かせろ"),
            nose.do("せまる$S"),
            sana.talk("やめて"),
            nose.talk("少女趣味はないんだがな……あんた、意外といいもの持ってるな"),
            sana.talk("お願い……"),
            sana.hear("インタフォンが鳴る"),
            nira.talk("おーい"),
            sana.talk("$nirasakiさん！"),
            nira.talk("あ、わりぃ。お邪魔だったか"),
            nose.talk("邪魔が入ったか"),
            nose.do("手を離して立ち上がる"),
            nira.talk("警察、呼ぼうか？"),
            nose.talk("何もしてないさ。作家にできるのは、小説を書くことくらいだ"),
            nose.go("気持ち悪い笑みを浮かべて出ていく"),
            nira.talk("大丈夫だったか？"),
            sana.talk("$nirasakiさん、どうして？"),
            nira.talk("いや、ちょっと別件で伝えておきたいことがあったんだが、偶然だ。何にしても良かった"),
            nira.talk("既に警察には連絡してあるけど、最近色々あるからな。注意しろよ"),
            sana.talk("うん"),
            sana.think("あんなに普段冷たいのに気にしていてくれたことに、感謝"),
            sana.talk("あ、それで伝えておきたいことって？"),
            nira.talk("近々週刊誌に盗作の話が出る。その作者は、お前の担当の先生だ。$notoだよ"),
            sana.talk("え！？"),
            stage=w.on_herhouse,
            )

def sc_checkmaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira = W(w.nirasaki)
    nose = W(w.nose)
    return w.scene("先生への確認",
            sana.be("翌日、先生に進捗確認にきている"),
            noto.be("テーブルに原稿を広げて書いている"),
            sana.talk("あの、原稿とは関係ないんですが"),
            noto.talk("何だい？"),
            sana.talk("実はある筋から、妙なことを耳に入れてしまって"),
            noto.talk("だから何だい？"),
            sana.talk("先生は盗作したことがありますか？"),
            noto.do("筆が止まる"),
            sana.talk("いえ。これだけ沢山作品が出ていれば、盗作だなんだと言ってくる人も沢山いるんですけど"),
            noto.talk("君は$meの担当編集だよね？", "$meのことを、信用できない？"),
            sana.talk("すみません。でも週刊誌に載ると聞いたので"),
            noto.talk("帰ってくれ。原稿が進められない"),
            sana.talk("すみません"),
            sana.do("立ち上がる"),
            noto.talk("全くブンヤというのはあれこれと嗅ぎ回っては、糞尿を掘り返す奴らなんだ"),
            _.talk("当時も散々言われた。今更何を言おうっていうんだ"),
            sana.think("珍しく苛立つ先生を見て、逆に不安になる"),
            sana.talk("また日を改めます。今日はつまらない話をしてしまい、申し訳ありませんでした"),
            noto.talk("全くだ。作品に没頭している時に余計なことを言わないでくれたまえ"),
            sana.go("おずおずと部屋を出ていく"),
            stage=w.on_hisapart_int,
            day=w.in_askplagiarism, time=w.at_afternoon,
            )

## episode
def ep_chapter3(w: World):
    return w.episode("3.第三章",
            ## NOTE
            sc_stalker(w),
            sc_intimidation(w),
            sc_manstalk(w),
            sc_checkmaster(w),
            )
