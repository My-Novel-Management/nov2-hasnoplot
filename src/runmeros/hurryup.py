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
    return w.scene("電車は事故で止まってしまい",
            sana.be("電車に乗っている"),
            sana.have("いつものように大きな鞄を二つ肩からかけて"),
            sana.do("スマホで情報確認（ここで盗作騒動など）"),
            sana.think("ずっと小説に関わる仕事がしたいと思っていたが、こんな風に転機が訪れるとは"),
            sana.do("と、ブレーキで止まる"),
            sana.do("アナウンスで人身事故のため、と"),
            sana.talk("え？　ちょっと待って"),
            sana.do("待ち合わせの二時に間に合わない！"),
            sana.talk("ちょっと下ろして下さい！"),
            camera=w.sana,
            stage=w.on_train,
            day=w.in_firstmeet, time=w.at_midmorning,
            )

def sc_rungirl(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("彼女は走る",
            sana.do("タクシーを捕まえようと通りに出るが、なかなか捕まらず"),
            sana.think("走るか"),
            sana.do("とにかく走り出す"),
            sana.do("小さい頃からよく走っていた"),
            sana.think("小さいのにやたらと走るから小動物感が強いと笑われた"),
            sana.do("でも走らなければ動かない"),
            sana.do("$Sにとっては走ることは生きることだった、働くことだった"),
            stage=w.on_street,
            )

def sc_timelimit(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("タイムリミット",
            sana.do("時計を確認して"),
            sana.think("な、何とか間に合った"),
            sana.do("住所を地図で確認する"),
            sana.do("建物の名前も一致している"),
            sana.think("ここだ"),
            sana.do("火をつけられたら一気に燃えそうな古い木造住宅"),
            sana.do("本当に人が住んでいるんだろうかと思う静けさ"),
            sana.do("ジィィという音がするインタホンを押して"),
            sana.talk("すみません。先生、$fukayaの代わりとして今日から担当になった……"),
            sana.do("反応がない"),
            sana.talk("先生？"),
            sana.do("よく見ると小さく張り紙が"),
            sana.talk("何これ？"),
            sana.do("編集よ去れ、と"),
            stage=w.on_hisapart_ext,
            )

## episode
def ep_hurryeditor(w: World):
    return w.episode("3.急げ編集者",
            ## NOTE
            sc_accident(w),
            sc_rungirl(w),
            sc_timelimit(w),
            )
