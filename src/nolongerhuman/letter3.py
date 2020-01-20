# -*- coding: utf-8 -*-
"""Episode: 9-4.第三の手記／人間失格
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
def sc_letterlast(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("先生の手紙の最後",
            w.comment("手紙の最後にはいつか責任を取らなければならないと書かれていた"),
            sana.do("手紙の続きを読む"),
            sana.do("それは幼い頃に再放送で見たネバーエンディングストーリーのような心境"),
            sana.do("読んでいるうちにどんどんと不安に叩き落とされる"),
            sana.do("酷い嵐で、雷が鳴っている"),
            sana.explain("盗作してデビューしたこともそうだが、何よりそれを告げるより先に親友が知っていて、おめでとうと言ったその翌日、首を吊ったのだ"),
            sana.think("先生たちから多少聞いていたが、想像以上にトラウマな話だった"),
            camera=w.sana,
            stage=w.on_herroom,
            day=w.in_readletter, time=w.at_night,
            )

def sc_lastscene(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("ラストシーン",
            sana.explain("原稿用紙にして２５０枚の初の長編小説のラストシーンを書こうとしていた"),
            sana.do("キータイプしては消して、を繰り返す"),
            sana.think("初めての長編の完成を、したくない気持ちが強くなっていた"),
            _.do("それでも先生の言葉を思い出して無理やり進める"),
            _.explain("作品は終盤、息絶えた世界を見事に再生した無限の命の女王が、不治の病にかかる"),
            _.explain("その病の原因が自分が生み出した生命たちにあると知り、女王は自決する"),
            sana.do("ラストシーンを書きながら泣いていた"),
            sana.think("物語のラストシーンには、その作者の思いが滲んでいるという言葉を思い出す"),
            sana.do("最後に（了）の文字を入れて、保存した"),
            )

def sc_emergency(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    nira = W(w.nirasaki)
    return w.scene("緊急事態発生",
            w.comment("何とか作品を書き上げて寝てしまっていたところに、バイト君から連絡で、先生が病院から消えたと"),
            sana.do("気づくともう翌日の午前十時すぎ"),
            sana.do("ずっと携帯が鳴っている"),
            sana.talk("ん？"),
            sana.do("見ればバイト君"),
            sana.talk("どうしたの？"),
            tsuchi.voice("どうしたじゃないですって！", "大変なんです！", "先生が、消えました！"),
            nira.come("インタホンが鳴って、やってくる"),
            nira.talk("これ、あいつに渡しといて。じゃ"),
            nira.go(),
            sana.do("友達経由で茶封筒を受け取る", "中身は$tsuruの持ち込み原稿だった"),
            day=w.in_vanishmaster, time=w.at_midmorning,
            )

## episode
def ep_letter3(w: World):
    return w.episode("4.第三の手記",
            ## NOTE
            sc_letterlast(w),
            sc_lastscene(w),
            sc_emergency(w),
            )
