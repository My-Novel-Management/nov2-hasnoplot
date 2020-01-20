# -*- coding: utf-8 -*-
"""Episode: 9-3.第二の手記／人間失格
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
def sc_readletter(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("告白の手紙を読む",
            sana.do("食事を片付けて、部屋に戻ってくる"),
            sana.do("パソコンには書きかけの原稿"),
            sana.do("どうしても気になり、先生の手紙を開けてしまう"),
            sana.explain("そこには自戒の念が書かれていた"),
            sana.explain("ざっと内容の説明"),
            sana.think("それは中学の頃から始まっていた"),
            camera=w.sana,
            stage=w.on_herroom,
            day=w.in_readletter, time=w.at_afternoon,
            )

def sc_schooldays(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("先生の学生時代",
            sana.explain("学生時代、先生は親友と初恋の女性、三人でよく一緒にいた"),
            sana.explain("二人が書いた小説を彼女が読む", "彼女が最初の読者だった"),
            sana.explain("どちらが一番彼女を喜ばせるのか、という勝負"),
            sana.explain("先生は当時を振り返り、彼女も二人の気持ちを分かっていたが彼女にとっては三人という関係性が一番だったのかもと"),
            sana.explain("高校に入り、彼女が病気になる"),
            sana.explain("見舞いに行くついでに二人は小説を持ち寄った"),
            sana.explain("病院は嫌いと言っていたのは、これが関係しているらしい"),
            sana.explain("彼女の病状はどんどん悪くなる"),
            sana.explain("ある時、$tsuruが言い出す"),
            tsuru.voice("作家になった方が彼女と結婚するんだ"),
            sana.explain("先生もそれに乗った"),
            sana.explain("その時から二人は家に篭って小説を書く日々"),
            sana.explain("その間にも彼女はどんどん弱っていく"),
            )

def sc_theirfuture(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("彼らの未来に",
            sana.explain("どちらも作家になれないまま、彼女は亡くなった"),
            sana.explain("先生はその日のことをこう書いている"),
            noto.voice("もう二度とあの声に笑顔に触れられないのだと思うと、ああ人の死というのはこんなにも残された者にとって重く辛い、どうしようもない出来事なんだなと"),
            sana.think("$Sも思い出す。祖父母が亡くなった日のことを"),
            sana.think("優しかったおばあちゃん。学校から帰ると親戚一同集まっていて、まだ何かしゃべっていた"),
            sana.think("でもその内容は分からなくて、ただ「ありがとう」と何度も繰り返していたのを思い出す"),
            sana.think("人生も最後で決まるというなら、おばあちゃんは良い人生だったんじゃないだろうか"),
            sana.explain("彼女が亡くなっても作家レースは終わらなかった。むしろ過激になった"),
            sana.explain("大学に通いながら作家を目指す先生と、フリーターで親の金を食いつぶしながら色々な出版社に出入りして、コネで何とかしようとしていた$tsuru"),
            sana.explain("結果として、先生が公募に出した作品でデビューを先に決めた"),
            sana.explain("決まった時は嬉しい、というより、もっと早くになんとかできなかったのかという思いだったそうだ"),
            sana.explain("そして、ここまで書いてから、本当の告白文が始まった"),
            noto.voice("これは墓場まで持っていくつもりだった。けれどここに書いておかねばならない。自分の人生の、作家としての、けじめとして"),
            noto.voice("$meは、$meのデビュー作は、$tsuru君の創作メモを読み、書いたものだ。つまり盗作である"),
            time=w.at_evening,
            )

## episode
def ep_letter2(w: World):
    return w.episode("3.第二の手記",
            ## NOTE
            sc_readletter(w),
            sc_schooldays(w),
            sc_theirfuture(w),
            )
