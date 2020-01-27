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
    interior, calendar = W(w.interior), W(w.calendar)
    clock = W(w.clock)
    return w.scene("手紙の内容の序文",
            w.comment("恥の多い生涯を送ってきました、という太宰治の人間失格の序文から始まる"),
            noto.be("丸テーブルに向かっている"),
            interior.look("まだ移ってきたばかりで真新しいフローリング"),
            noto.do("考えながら手紙を書いている"),
            noto.do("目は壁の大きなカレンダーを見ている"),
            calendar.look("六月十三日に赤い丸がしてある"),
            noto.think("どうしてもこれを書いておかねばならない"),
            _.think("やっと筆を取る決意ができた"),
            _.think("それまでに十年も掛かってしまった"),
            noto.do("少し書いては休む"),
            _.do("湯呑にコーヒーを注ぎ、それを飲む"),
            noto.do("古い創作メモノートを取り出して見る"),
            noto.talk("これを付けるようになったのも、お前の助言からだったな"),
            _.think("現実では時は巻き戻らないが、思い出の中ではいくらでも戻すことが可能だ"),
            _.think("だから$meはこうして書いている"),
            _.think("書くことは、時空を超えることができる"),
            _.think("さあ、そろそろ始めよう"),
            _.think("後悔と懺悔の為の告白を"),
            camera=w.noto,
            stage=w.on_hisapart,
            day=w.in_writeletter, time=w.at_night,
            )

def sc_jrschooldays(w: World):
    noto, tsuru, komi, asahi = W(w.noto), W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("中学時代",
            noto.be("教室にいる"),
            tsuru.be("$notoと二人で話している"),
            komi.come("やってくる"),
            komi.talk("また小説の話？"),
            tsuru.talk("$meが書いてきたんだよ"),
            komi.talk("え？　$tsuru君が？"),
            noto.talk("$komiに読ませたいってさ"),
            komi.talk("読みたい！"),
            noto.talk("素人の書いたものやぞ？"),
            komi.talk("読む方にはプロでも素人でも関係ないもん"),
            noto.think("彼女の言葉にはいつもはっとさせられた"),
            noto.explain("中学の頃はいつもこの三人でつるんでいた"),
            noto.explain("彼女が二人の書いた小説を読み、どちらが面白いかを競い合った"),
            _.explain("それが$meの小説体験だった"),
            stage=w.on_classroom_int,
            day=w.in_master_jrschool, time=w.at_afternoon,
            )

def sc_schooldays(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("高校時代",
            noto.be("教室にいる"),
            tsuru.be("じっと$komiを見つめている"),
            komi.be("二人の小説を読んでいる"),
            noto.explain("高校になってからもこの関係は続いていた"),
            komi.talk("これ、面白いね"),
            tsuru.talk("だろ？"),
            komi.talk("けど、どうしていつも悲しいラストばかりなの？"),
            tsuru.talk("なんかそういうもんだろ？　日本文学なんて大半悲しい最後だよ"),
            noto.talk("$tsuruは現実的すぎるんだ。もっと夢とか希望とか、そういうのに溢れててもいいんじゃないのか？"),
            tsuru.talk("そういうお前はすぐ奇跡だなんだって、リアリティのない描写してるじゃねえか"),
            _.talk("だいたいさ、そんな簡単に奇跡なんざ起こる訳ねえんだよ"),
            _.talk("それこそ$meやお前が明日にでも作家デビューするなんて考えられないだろ？"),
            komi.talk("それは分からないじゃない"),
            _.talk("現実なんていつ何が起こってもおかしくない"),
            _.talk("事実は小説より奇なりよ"),
            noto.explain("その通りだった"),
            _.explain("この年の秋、彼女は体調を崩し、入院した"),
            day=w.in_master_highschool,
            )

def sc_hersick(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("彼女の病気",
            komi.be("ベッドの上で本を読んでいる"),
            noto.come("$tsuruと共にやってくる"),
            tsuru.come(),
            tsuru.talk("おい、どうだ？"),
            tsuru.do("見舞いのメロンを置いてやりつつ"),
            komi.talk("二人ともありがとう"),
            komi.look("抗がん剤の副作用で髪が抜けている"),
            komi.look("病院着に帽子を被っている"),
            tsuru.talk("これ、新しいやつ書いてきたから"),
            noto.talk("$meも"),
            noto.do("二人は新しい小説の原稿を渡す"),
            komi.talk("楽しみに読むね"),
            tsuru.talk("今、出版社に持ち込みに行ってんだ。$me絶対に作家になって、お前の病気も直してやるから"),
            komi.talk("病気はお医者様が治してくれるのよ"),
            tsuru.talk("わ、わかってらい"),
            noto.explain("その場では楽しげに笑う。けれど、いざ病室を離れると辛い思いが二人を満たした"),
            stage=w.on_sickroom_int,
            day=w.in_visithospital, time=w.at_afternoon,
            )

def sc_ourvow(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("二人の誓い",
            noto.be("病室を出た二人"),
            tsuru.be("廊下を歩いている"),
            tsuru.do("壁を殴りつけ"),
            tsuru.talk("なんであいつなんだよ！"),
            noto.talk("おい"),
            tsuru.talk("あいつが何したってんだよ！"),
            noto.talk("お前が小説でいつも書いてる現実ってやつじゃないのか？"),
            _.talk("誰のせいでもない。ただ目の前に転がってきただけだ"),
            tsuru.talk("そういう考え、嫌いだよ"),
            _.talk("医者は心まで治せない"),
            _.talk("病気は医者に任せて、$meはあいつの心を治す"),
            noto.talk("そうだな"),
            noto.explain("けれど$meたちのがんばりに対して、彼女の容態はどんどん悪化していった"),
            stage=w.on_sickroom_ext,
            )

def sc_theirfuture(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("彼らの未来に",
            noto.be("黒服で佇んでいる"),
            tsuru.come("煙草を咥えながらやってきて"),
            tsuru.talk("こっちにいたのかよ。彼女の寝顔、綺麗だったな"),
            noto.talk("ああ"),
            noto.explain("彼女は$meたちが二十歳の年の十一月に亡くなった"),
            noto.explain("$meは当時悲しさよりも今までつっかえ棒になっていたものが急に外れてしまって、どうすればいいか分からない"),
            _.explain("そんな空虚さのただ中に放り込まれた感覚がずっと消えなかった"),
            tsuru.talk("$me、作家になるわ"),
            noto.talk("まだ目指すのかよ"),
            tsuru.talk("だってそれが彼女との約束だし"),
            _.talk("お前も目指してるんだろ、作家"),
            noto.talk("$meは"),
            tsuru.talk("知ってるよ。必死に創作ノートつけてんの"),
            noto.talk("お前、見たのかよ？"),
            tsuru.talk("$me、作家になって物語の中で彼女を生かしたい"),
            noto.talk("そういうのは、やめておけよ"),
            tsuru.talk("彼女が好きだった。愛していた。それなら、この愛をどうにかしなきゃ、$meという魂は浮かばれないだろ？"),
            noto.think("自分はどうなんだろう、と悩んでいた"),
            noto.explain("しかし$meが先に作家としてデビューすることになる"),
            _.explain("創作ノートに落書きされた彼の構想をパクって、投稿したからだった"),
            stage=w.on_funeralhall_ext,
            day=w.in_komi_funeral, time=w.at_evening,
            )

## episode
def ep_letter2(w: World):
    return w.episode("3.第二の手記",
            ## NOTE
            sc_readletter(w),
            sc_jrschooldays(w),
            sc_schooldays(w),
            sc_hersick(w),
            sc_ourvow(w),
            sc_theirfuture(w),
            )
