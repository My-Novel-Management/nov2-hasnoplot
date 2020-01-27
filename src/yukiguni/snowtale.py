# -*- coding: utf-8 -*-
"""Episode: 5-3.雪国抄／雪国
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
def sc_newperson(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, tsuchi = W(w.nirasaki), W(w.king), W(w.tsuchiura)
    return w.scene("新人現る",
            sana.come("出社してくる$S"),
            king.be("珍しく談笑"),
            tsuchi.be("$kingと笑って話している若い男"),
            nira.be("相変わらず仏頂面で座っている"),
            sana.talk("おはよう。あれ誰？"),
            nira.talk("ああ。なんか王が連れてきたバイト。へらへらして、いつまで続くやら"),
            sana.talk("へえ"),
            tsuchi.look("パーカーにパッチワークされたジーパン、膝は穴あき"),
            sana.talk("王ってああいうのが好み？"),
            nira.talk("さあね"),
            king.talk("紹介するよ。$tsuchiura君だ。$ln_sanaが面倒を見てやってくれ"),
            sana.talk("え？　$meですか？"),
            king.talk("何か不満が？"),
            sana.talk("いえ。宜しくお願いします"),
            tsuchi.talk("ど、ども"),
            tsuchi.look("へらへらニタニタ笑っている"),
            sana.do("握手をすると手がべっとりした"),
            sana.talk("えっと"),
            sana.explain("一通り説明をしたけれど、たぶん何一つ理解していないだろうことは容易に想像がついた"),
            sana.talk("とにかく外に出ましょう。話はそれからね"),
            sana.think("新人のおもりなんて余計な仕事でしかなかった"),
            camera=w.sana,
            stage=w.on_heroffice,
            day=w.in_newparttimer, time=w.at_midmorning,
            )

def sc_greeting(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, tsuchi = W(w.nirasaki), W(w.king), W(w.tsuchiura)
    return w.scene("挨拶",
            sana.come("先生のところに挨拶にやってきた"),
            tsuchi.be("もそもそとついてきている"),
            sana.talk("先生、おはようございます"),
            sana.talk("あれ？　寝てるかな"),
            sana.do("合鍵を使って部屋に入る"),
            sana.talk("先生？"),
            sana.do("散乱している部屋を見て溜息"),
            sana.talk("とりあえずこれ、片付けて"),
            tsuchi.talk("え？　なんでそれが仕事なんですか？"),
            sana.talk("作家の面倒を見るのが編集の仕事だから"),
            tsuchi.talk("げっ。ハウスキーパーかよ"),
            sana.talk("似たようなもんよ"),
            sana.do("部屋の掃除は任せて、寝室を覗く"),
            sana.talk("先生？"),
            noto.be("テーブルを前にして腕組みしている"),
            sana.talk("先生"),
            noto.talk("ああ、おはよう。$sana君"),
            sana.do("覗き込むと原稿に文字が走っている"),
            sana.talk("早速書いているんですか？"),
            noto.talk("プロットだよ"),
            sana.talk("へえ"),
            tsuchi.do("部屋に入ってきて"),
            tsuchi.talk("あのー、ゴミ袋どこすか？"),
            noto.talk("どちら？"),
            sana.talk("紹介します。新人でアルバイトの$full_tsuchiura君です"),
            tsuchi.talk("あ、ども"),
            noto.talk("彼も編集に？"),
            tsuchi.talk("いや、とりあえず働けって言われて、ぶちこまれました"),
            noto.talk("色々あるね"),
            sana.talk("ええ"),
            sana.talk("本日はその挨拶と、あと、こちらを"),
            noto.talk("何？"),
            sana.do("会社主催の新年会の招待状を持ってきた"),
            noto.talk("十三日か。都合が悪いね"),
            sana.talk("先生にも来ていただけると、今後のこともありますし"),
            noto.talk("時間が空けば伺うよ。でも期待はしないでくれ"),
            sana.talk("は、はい"),
            sana.talk("失礼しました"),
            sana.do("部屋を出る"),
            tsuchi.talk("なんか恐い人すね"),
            sana.talk("原稿書いている時は仕方ないわよ"),
            sana.think("それでも何か様子が妙だとは思っていた"),
            stage=w.on_hisapart,
            )

def sc_printing(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, tsuchi = W(w.nirasaki), W(w.king), W(w.tsuchiura)
    oki = W(w.oki)
    return w.scene("印刷所",
            sana.come("印刷会社にやってきた二人"),
            tsuchi.be(),
            tsuchi.talk("ここで本ができるんすか"),
            sana.talk("ここじゃないわよ。印刷は工場が別にあるの。ここはオフィスだけね"),
            oki.be("仕事をしている"),
            sana.talk("どうも、今年も宜しくお願いします"),
            oki.talk("おお、$sanaちゃん。よろしく。そっちは作家先生？"),
            sana.talk("いや、新しいバイトの子で"),
            oki.do("じっと観察して、特に挨拶もなくパソコンに戻る"),
            tsuchi.talk("えっと、あの"),
            sana.talk("まあ、そっか。また来ます"),
            tsuchi.talk("え？"),
            sana.talk("みんな忙しいのよ。行くわよ"),
            tsuchi.talk("うす"),
            stage=w.on_bigprint,
            )

def sc_abouteditor(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, tsuchi = W(w.nirasaki), W(w.king), W(w.tsuchiura)
    return w.scene("編集者の仕事とは",
            sana.be("ファミレスに入っている"),
            tsuchi.be("大盛りのステーキセットを注文している"),
            sana.talk("編集って言ってもその多くは本を作る為の雑用と人の手配なのよ"),
            tsuchi.talk("そうっすね"),
            _.do("頬張りながら聞いている"),
            sana.talk("今の部署は書籍の出版が基本業務だけど、月刊誌や週刊誌を扱っているところはもっと忙しいわよ"),
            tsuchi.talk("そすか"),
            sana.talk("まあ$tsuchiura君は体力には自信ありそうだからいいけど、締切が重なってくるとみんな残業残業で寝不足の山よ"),
            sana.talk("実際ハードワークだからってことで、長続きしない人が多い職場でもあるもの"),
            tsuchi.talk("みんな机汚いっすもんね"),
            _.talk("そういやあの先生"),
            sana.talk("$noto？"),
            tsuchi.talk("そうそう。なんでラノベなんすか？　文芸だったんでしょ？"),
            sana.talk("たぶんどっちでもいいのよ。けど、この十年小説書いてないから。この前やっと久しぶりに短編を書いたの"),
            tsuchi.talk("それで作家なんてふんぞり返ってんのは流石にどうなんすかね"),
            sana.talk("色々と事情があるんでしょ。でもそんなことも呑み込んで、良い作品が書ける準備を整えてあげることが編集の仕事よ"),
            tsuchi.talk("まあ、$meは給料さえ貰えればなんでもいいっす"),
            sana.talk("そう"),
            _.do("苦笑"),
            stage=w.on_famires_int,
            )

## episode
def ep_snowtale(w: World):
    return w.episode("3.雪国抄",
            ## NOTE
            sc_newperson(w),
            sc_greeting(w),
            sc_printing(w),
            sc_abouteditor(w),
            )
