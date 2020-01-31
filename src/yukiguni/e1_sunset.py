# -*- coding: utf-8 -*-
"""Episode: 5-1.夕景色／雪国
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
def sc_kanazawa(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("金沢に向かう",
            sana.explain("トンネルを抜けたらそこは、本当に雪国でした"),
            sana.be("新幹線に乗っている"),
            sana.talk("さっむ"),
            sana.do("自分の日記帳を出して書き込んでいる", w.sananote),
            sana.do("新幹線の窓から見た北陸の雪景色"),
            sana.explain("雑誌の見本を手に、何故か金沢に向かっています", w.magazine1_mihon),
            sana.do("何の連絡もなく実家に帰った先生を追いかけて"),
            sana.do("やっと手に入れた先生のデビュー作を読んでいる", w.masternovel1),
            _.explain("文学作品で、小さな賞だったがそれが話題になり、$on_Kawadeから出版された"),
            _.explain("内容は青春ものだ。男女の三角関係を軸に、昭和の家庭環境の差などが色濃く影を落としている"),
            sana.think("これを書きながら先生は何を考えていたのだろうかと"),
            _.explain("作品では先生らしき主人公と、そのライバルとなる金持ちの作家崩れ、それに芸者を目指す女性が書かれている"),
            _.explain("しかし最後、彼女は死んでしまう"),
            _.explain("その死を受けて、作家崩れの青年も死に、愚直に生きていた主人公だけが生き残った"),
            _.explain("いつも心のどこかで二人を羨んでいた主人公だけが、生き延びてしまった"),
            _.explain("ラストは二人の墓に、アネモネを供えている"),
            _.explain("はかない恋、見放された、という花言葉があるそうだ"),
            ## NOTE
            ##  半分は先生の過去編の話を匂わせる
            ##  先生のデビュー作についての内容は、ここで初めて出てくる
            ##  作品は先生と親友、初恋の女性の三角関係を思わせるもの
            camera=w.sana,
            area=w.Tokyo,
            stage=w.on_train,
            day=w.in_homevisit, time=w.at_midmorning,
            )

def sc_welcome(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生の出迎え",
            sana.come("新幹線を降りて歩いていく"),
            w.comment("駅の描写を"),
            sana.do("駅を降りると先生が出迎えに待っていた"),
            sana.talk("どうも"),
            noto.talk("いやあ、よく来てくれたね"),
            noto.talk("とりあえず乗ってくれ"),
            sana.think("昨年取ったばかり、と思い出す"),
            sana.talk("$meが運転します"),
            noto.talk("いやいや、大丈夫だから"),
            noto.do("だが車はいきなりエンスト"),
            sana.talk("どうしてオートマじゃないんですか……"),
            noto.talk("昔から男はマニュアルの免許を取るものだろう？"),
            sana.talk("運転変わります"),
            ## NOTE
            ##  駅構内や空気の違いなどを描写
            stage=w.on_station_int,
            time=w.at_beforenoon,
            )

def sc_masterhome(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生の実家",
            sana.do("先生のひどい運転で、酔った$S"),
            sana.talk("ここって民宿ですか？"),
            noto.talk("小さい頃はやってたんだけどね、今は頼まれた時に出すくらいで、基本的に仕出し弁当を作ったり、そんなことをしているよ"),
            sana.do("先生の両親が出てきて、挨拶"),
            sana.explain("何故か嫁さんを連れてきたと勘違いされてしまい、その誤解を解くのが大変だった"),
            sana.do("先生に部屋に案内される"),
            sana.do("先生の部屋を見て、感慨深い"),
            sana.do("そこに学生時代の写真を見つける。そこには先生とハンチング帽の男子、それに着物姿の女性が映っていた"),
            sana.talk("これは？"),
            noto.talk("昔のものを……誰が飾ったんだ？"),
            noto.do("その写真を引き出しに仕舞ってしまう"),
            ## NOTE
            ##  先生の家の描写
            ##  写真は朝日が置いた
            stage=w.on_hishome,
            )

## episode
def ep_sunsetsight(w: World):
    return w.episode("1.夕景色",
            ## NOTE
            sc_kanazawa(w),
            sc_welcome(w),
            sc_masterhome(w),
            )
