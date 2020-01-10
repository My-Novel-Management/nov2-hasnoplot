# -*- coding: utf-8 -*-
"""Episode: エピローグ
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
def sc_gera(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("ゲラ",
            )

def sc_end(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("最後の日記",
            sana.do("恒例となった日記を書いている"),
            _.voice("こうして何とか先生の初めてのライトノベル長編企画は幕を閉じました"),
            _.voice("たぶん$meはまだまだ小説の何も理解できていないのだろうけれど"),
            _.voice("先生を担当していくことで少しずつでもその深淵を覗ければな、と思います"),
            sana.do("万年筆を置いて"),
            _.talk("次の企画立てなくっちゃだ"),
            _.do("と、誰かからLINE"),
            sana.talk("編集長？"),
            _.do("見れば先生から", "慣れないのか誤字もあるし、ひらがなが多い"),
            noto.do("プリンが食べたくなった。市販のものでは、どうにもね、と書いてある"),
            sana.talk("はいはい。わかりましたよ"),
            _.do("時計を見て、外に出る"),
            _.do("車に乗り込み、エンジンをかける"),
            _.think("一心同体になんてならなくてもいいけど、どうしようもない作家を元気づけるのも編集の仕事だ"),
            _.explain("$Sの苦難の日々は続く"),
            )


## episode
def ep_epilogue(w: World):
    return w.episode("エピローグ",
            ## NOTE
            ##  - まだまだゲラ作業は続く、けれど、これにて一旦編集日記は終わろうと思います、で締める
            sc_gera(w),
            sc_end(w),
            )
