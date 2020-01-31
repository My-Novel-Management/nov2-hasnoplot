# -*- coding: utf-8 -*-
"""Episode: 1-3.急げ編集者／走れメロス
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
def sc_accident(w: World):
    sana, noto = W(w.sana), W(w.noto)
    trainman = W(w.trainman)
    inside = W(w.inside)
    sphone = W(w.sphone)
    return w.scene("電車は事故で止まってしまい",
            w.comment("ここで条件確認。締切や先生の略歴"),
            sana.be("電車に乗っている"),
            inside.look("人が混み合っていて、座席は空いていない"),
            sana.have("いつものように大きな鞄を二つ肩からかけている", w.shoulderbag, 2),
            sana.do("スマホで情報確認（ここで盗作騒動など）"),
            sphone.look("画面には引き継ぎ資料を撮影したものが映っている"),
            _.look("$full_notoのプロフィール"),
            sana.explain("今回先輩から引き継いで担当になったのは、元芥川賞候補作家の$notoだった"),
            _.explain("デビュー作の『$masternovel1』で注目を浴びてその後立て続けに長編を発表したが、",
                "ある時を境にして急に小説を書かなくなった。",
                "その後、エッセイや紀行文などを小冊子に掲載したりしていると書かれているが、全然知らないものばかりだった"),
            sana.think("ずっと小説に関わる仕事がしたいと思っていたが、こんな風に転機が訪れるとは"),
            _.think("これをチャンスと思って、何としてでも掴む。そして編集者として独り立ちするのだ。と決意する"),
            sana.talk("あ、いきなり今日一次締切の原稿あるじゃないですか。参ったなあ"),
            _.think("作家と編集者にとって締切とは胃の痛くなる言葉だった"),
            sana.do("と、ブレーキで止まる"),
            trainman.talk("ご乗車中のみなさまにお知らせします。この先の区間にて人身事故発生の為、只今運転を見合わせております。",
                "発車までしばらくお待ち下さい"),
            sana.hear("車内アナウンスだ。声は落ち着いている"),
            sana.talk("え？　ちょっと待って"),
            sana.do("待ち合わせの時間に間に合わない！"),
            sana.talk("ちょっと下ろして下さい！"),
            camera=w.sana,
            stage=w.on_train_int,
            day=w.in_firstmeet, time=w.at_beforenoon,
            )

def sc_rungirl(w: World):
    sana, noto = W(w.sana), W(w.noto)
    outside = W(w.outside)
    return w.scene("彼女は走る",
            sana.be("タクシーを捕まえようと通りに出るが、なかなか捕まらず"),
            outside.look("大通りを車が走り抜けている"),
            sana.think("タクシーが止まりそうな気配はなかった"),
            sana.think("仕方ない。走るか"),
            sana.do("とにかく走り出す"),
            sana.think("小さい頃からよく走っていた"),
            sana.think("小さいのにやたらと走るから小動物感が強いと笑われた"),
            sana.do("でも走らなければ動かない"),
            sana.do("$Sにとっては走ることは生きることだった、働くことだった"),
            stage=w.on_street,
            )

def sc_timelimit(w: World):
    sana, noto = W(w.sana), W(w.noto)
    watch, sphone = W(w.wristwatch), W(w.sphone)
    exterior = W(w.exterior)
    gate = W(w.gate)
    door = W(w.door)
    return w.scene("タイムリミット",
            sana.come("タクシーから降りて、息荒く歩いてくる"),
            sana.do("腕時計を確認して", w.wristwatch),
            watch.look("十二時過ぎを差している"),
            sana.think("ちょっと遅れたけど、許容範囲かな"),
            sana.do("$sphoneを見て、住所を地図で確認する"),
            sphone.look("三鷹の地図と番地が表示されている", "建物名は『$on_hisapart』である"),
            gate.look("$on_hisapartという看板が掛かっている"),
            sana.think("ここだ"),
            sana.think("火をつけられたら一気に燃えそうな古い木造住宅だな、と思う"),
            sana.do("本当に人が住んでいるんだろうかと思う静けさを感じる"),
            sana.do("ジィィという音がするインタホンを押して"),
            sana.talk("すみません。$on_hercompanyから来ました$ln_sanaと申します。今日から$fukayaの代わりとして先生のご担当をさせていただくことになりまして……"),
            sana.do("反応がない"),
            sana.talk("先生？"),
            sana.do("よく見ると小さく張り紙が"),
            sana.talk("何これ？"),
            door.look("『編集よ去れ』の張り紙"),
            sana.talk("はぁ！？"),
            stage=w.on_hisapart_ext,
            time=w.at_noon,
            )

## episode
def ep_hurryeditor(w: World):
    return w.episode("3.急げ編集者",
            ## NOTE
            sc_accident(w),
            sc_rungirl(w),
            sc_timelimit(w),
            )
