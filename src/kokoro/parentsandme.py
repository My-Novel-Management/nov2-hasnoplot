# -*- coding: utf-8 -*-
"""Episode: 7-2.私と両親／こころ
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
def sc_nearrestaurant(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("案内されて洋食屋に向かう路地",
            sana.do("閑静な場所を歩く"),
            sana.talk("どこなんですか？"),
            noto.talk("もうすぐだ"),
            sana.think("駅や大通りから結構離れた場所で、隠れ家的な店なんだろう"),
            sana.think("着物姿なことを後悔する"),
            camera=w.sana,
            stage=w.on_street,
            day=w.in_visitgrave, time=w.at_noon,
            )

def sc_restaurant(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生と洋食屋",
            sana.come("先生に連れられてやってくる"),
            noto.talk("特別な時に、ここに来るんだ"),
            noto.do("デミグラスソースハンバーグを注文する"),
            sana.do("$Sも同じものを"),
            sana.do("やってきたのを食べて"),
            sana.talk("これ、素敵です"),
            noto.talk("だろう？"),
            noto.do("嬉しそう"),
            noto.talk("作家と食べ物という観点も面白い"),
            noto.talk("それぞれ普段から食べているものや食に対する考えが出るからね"),
            noto.talk("料理はしないんだったかな？"),
            sana.talk("多少しますよ。でも上手くはないです。外食した方が良いですね"),
            noto.talk("将来大変そうだね"),
            sana.talk("みんなで「料理ができる旦那さん」をもらう予定にしてますから"),
            sana.do("笑う"),
            sana.explain("それから少し親の話をする"),
            noto.talk("素敵な親御さんに育てられたんだね"),
            sana.talk("そうですか？", "確かに色々と迷惑をかけたし、今も時々"),
            noto.talk("どうしても家庭環境というのは人生において大きい"),
            noto.talk("長く見れば少なくとも二十年程度はまず世話になる。それだけ一緒にいて、色々と知った仲だ"),
            noto.talk("結婚して暮らすまでは、一番長く一緒にいる他人かも知れない。それが家族だ"),
            noto.talk("$meの親はね、何も言わなかったが、これだけは言っていたよ。他人に迷惑をかけるな。あと、自分に嘘をつくな、かな"),
            noto.talk("その言葉がずっと呪詛のように残っている"),
            sana.think("色々あったのだな、と思った"),
            sana.explain("食べ終えて、コーヒーを"),
            noto.talk("ここね、来月潰れるんだ"),
            sana.talk("え？"),
            sana.think("確かに忙しいはずの時間帯に自分たち以外に客は一組だけ"),
            noto.talk("まあ趣味で続けていたらしいからね。これも原価は相当高い"),
            noto.talk("好きなことでも続けるのは大変だ"),
            noto.talk("それは君たちも考えなければいけない問題なんだよ"),
            sana.talk("どういうことですか？"),
            stage=w.on_masterrestaurant,
            )

## episode
def ep_parents_and_me(w: World):
    return w.episode("2.私と両親",
            ## NOTE
            sc_nearrestaurant(w),
            sc_restaurant(w),
            )
