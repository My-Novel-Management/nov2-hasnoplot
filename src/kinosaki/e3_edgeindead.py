# -*- coding: utf-8 -*-
"""Episode: 6-3.死の淵にて／城の崎にて
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
def sc_confession(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("大切な人の死",
            noto.be("お酒が空になっている"),
            sana.be("正座をして、先生の話を聞いている"),
            noto.talk("彼女は$meの初恋だった"),
            sana.explain("それは先生の大切な思い出の告白だった"),
            noto.talk("以前に少しだけ話したと思うが、大切な友人と共に憧れだった女性だ"),
            _.talk("若い頃に死を意識するのは祖父母や親の知人が亡くなったりする時が多いと思う"),
            _.talk("特に思春期の人間にとって、他人の死というのは思考の中でかなり大きなウェイトを占めてくる"),
            _.talk("けれど直接の兄弟や両親でない限りは、やはりどこか他人の死というのは遠いものだ"),
            _.talk("しかしね、一つだけ違うものがある"),
            _.talk("それが、大切な仲間の命が失われる時だ"),
            _.talk("学生時代の別れとは、卒業などでバラバラになるということなのに、"),
            _.talk("$meらにとってそれは、命の別れとほぼ同義だった"),
            noto.do("涙が滲んでいる"),
            noto.do("お茶をおちょこに入れて飲む"),
            sana.do("すっかり酔いが冷めていて、ひざ掛けをしている"),
            noto.talk("未だにね、$meは考えるんだよ。何故彼女は死んでしまったのかと"),
            _.talk("原因はガンだってことは分かっている。でも原因が問題じゃない"),
            _.talk("人が死ぬ。それは誰もが避けられない"),
            _.talk("ただ何故その時に彼女だったのか、ということなんだ"),
            _.talk("小説では作者が殺すことも殺さないことも選択できる"),
            _.talk("好きな時に好きなように、その人物の生を操作して構わない"),
            _.talk("もちろんそれが傑作になる為にどうしてもそこで彼女が死ななければいけない、なんてこともあるだろうが、"),
            _.talk("そんなものはどちらが自分にとって重要か、ということでしかない"),
            _.talk("つまり作者の都合のいいように、何とでもできるという話だ"),
            _.talk("しかし現実は違う。現実世界は非情だ"),
            _.talk("考えや思慮なんて通用しない"),
            _.talk("願いなんかくそったれだ"),
            _.talk("彼女は死ぬ前に何も言い残さなかった"),
            _.talk("だからね、考えるんだよ"),
            _.talk("自分なら、最後に何と言うだろう。大切な人に、何と伝えるのだろうかって"),
            sana.explain("それは先生にとってとても大切な話だった"),
            _.explain("涙を流し、時に拭いながら、その最愛の女性の死というトラウマについて語った"),
            _.explain("全てをここに記すことはしないけれど、先生の外には出せない話なことだけは理解できた"),
            _.explain("だから日記にも全ては書かないでおこうと思う"),
            noto.talk("時に$sana君は友人たちと一緒に暮らしているんだったね？"),
            sana.talk("ええ、そうですけど"),
            noto.talk("今を、大切にするんだ。友人が宝とよく言うが、本当に大切なのは今その瞬間だから"),
            noto.look("優しくて、寂しげな瞳"),
            sana.talk("はい"),
            noto.talk("付き合ってくれて、ありがとう"),
            _.talk("少し酔い冷ましをしてから、原稿の続きを書くとしよう"),
            noto.go("立ち上がり、行ってしまう"),
            sana.do("それを見送るが、睡魔に襲われてそのまま寝てしまう"),
            camera=w.sana,
            stage=w.on_oldinn,
            day=w.in_trip_kinosaki, time=w.at_night,
            )

def sc_inmydream(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("夢の中",
            sana.be("その夜、夢を見た"),
            sana.do("小さい頃の夢だ"),
            sana.do("迷子になって怖くて泣いていたら、そこに父親が来てくれた"),
            sana.do("病気で父親を失っているからか、$Sにとって父のイメージはいつもあの日の父親だった"),
            sana.do("目覚めると、先生が側にいてくれて、父親を思い出して、また安眠に戻った"),
            stage=w.on_dream,
            )

## episode
def ep_edgeindead(w: World):
    return w.episode("3.死の淵にて",
            ## NOTE
            sc_confession(w),
            sc_inmydream(w),
            )
