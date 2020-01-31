# -*- coding: utf-8 -*-
"""Episode: 5-2.手鞠歌／雪国
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
def sc_lunch(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("昼食を取る",
            sana.do("先生に連れられて、古いファミレスにやってくる"),
            sana.do("先生が学生時代によく使っていたものらしい"),
            sana.do("店に入ると、先生の知り合いらしき女性もいる"),
            asahi.talk("あら、こっちに帰ってきてたんだ"),
            noto.talk("$full_asahiさん。学生時代の同級生だ"),
            sana.talk("はじめまして。先生の担当編集をしています"),
            asahi.talk("へえ、まだ作家やってたんだね"),
            sana.think("嫌な感じがした"),
            ## NOTE
            ##  よく使っていたファミレスが、ここではまだ残っている、という描写（洋食屋が潰れたのと対比）
            camera=w.sana,
            stage=w.on_oldfamires,
            day=w.in_homevisit, time=w.at_noon.elapsedMin(30),
            )

def sc_unknownthings(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("知らないこと",
            sana.do("昼食を食べ終えた"),
            noto.talk("ちょっと席を外すよ"),
            noto.go("昔の知人の集団の方に"),
            asahi.come("隣の席にやってきて"),
            asahi.talk("ねえ、先生とはどれくらいの付き合いなの？"),
            sana.talk("まだ十月からなんで二ヶ月ほどですけど"),
            asahi.talk("色々なお世話もするんでしょ？"),
            sana.talk("まあ、そうですけど"),
            asahi.talk("ねた？"),
            sana.do("顔が真っ赤になる"),
            asahi.talk("うぶなのね。見た目通り若いのかしら"),
            sana.talk("見た目のことを言われるのはあまり好きじゃありません"),
            asahi.talk("まああの人の好みじゃないわよね。それとも歳とって変わったのかしら"),
            sana.talk("何なんですか？"),
            asahi.talk("別に。ただあの人殺しがまだのうのうと生きてるのが許せないだけ"),
            sana.talk("人殺し？"),
            asahi.talk("何も知らないのね。$full_tsuru。調べてみたら"),
            w.eventStart("$tsuruという男"),
            noto.come("戻ってくる"),
            noto.talk("何を話していた？"),
            asahi.talk("別に。古い歌の話よ"),
            asahi.do("童謡を歌う"),
            asahi.go(),
            sana.think("先生の鼻歌で聞いたことがある、と思い出す"),
            noto.talk("昔、いろいろとあってね。まあ何を言われたかしらないが、気にしないことだ"),
            noto.do("不機嫌な顔"),
            ## パーティに出て、不穏なことを言われて、日帰りで東京に戻る
            )

def sc_masterhome(w: World):
    sana, noto = W(w.sana), W(w.noto)
    road = W(w.road)
    return w.scene("先生の故郷",
            sana.come("先生と歩いている"),
            noto.come("歩いている"),
            road.look("雪がまだ残る道"),
            sana.talk("いつもこんなに雪が降るんですか？"),
            noto.talk("小さい頃はそうだったが最近は少なくなったようだね。$meも東京の方が長くなってしまったから聞いた話と、記憶との照合からだけれど"),
            noto.look("普段より楽しげな顔"),
            sana.talk("先生はもう一度文芸に復帰する気はないんですか？"),
            noto.talk("気持ちがない訳じゃない。ただ、今の$meに果たして書けるだろうか。そういう不安の方が大きくてね"),
            _.talk("今回だって君の書いたものがあって、あれができた訳だから、今の自分がゼロから何か作れるかと言われるととても悩むよ"),
            w.comment("先生の本音が、この故郷では聞ける"),
            w.load("文章について"), # 文章についての先生講義
            noto.talk("だからこうしてただ外を歩いている時も、作家はその感性の中に色々なものを取り入れようとしている",
                "決してサボっている訳ではないんだ"),
            sana.talk("はいはい。結局それなんですね",
                "大丈夫ですよ。$meは原稿さえ貰えれば何も文句は言いませんから"),
            ## NOTE
            ##  金沢の街というか、先生の地元の界隈を歩きつつ、店に立ち寄りつつ
            ##  ここで「描写」と「文章」について語る
            stage=w.on_street,
            time=w.at_afternoon,
            )

def sc_backtohome(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("帰りの車内で",
            sana.be("帰りの車内"),
            ## NOTE
            ##  帰りの車内。色々な問題の端緒が見えてくる
            ##  後半へのターニングポイントなので、何か「不穏さ」と「今後の暗示」を
            stage=w.on_train,
            time=w.at_night,
            )

## episode
def ep_temarisong(w: World):
    return w.episode("2.手鞠歌",
            ## NOTE
            sc_lunch(w),
            sc_unknownthings(w),
            sc_masterhome(w),
            sc_backtohome(w),
            )
