# -*- coding: utf-8 -*-
"""Episode: 4-3.檸檬／檸檬
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
# NOTE
#   ここを4-4の冒頭を持ってきて、その前部分に「最終編集会議」の部分と、その朝からを


def sc_writerwill(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("作家の気持ち",
            sana.do("正座して、いつもとは違う先生との関係だった"),
            sana.do("先生が読むのをじっと待っている"),
            sana.hear("ページを捲る音だけが響く"),
            sana.talk("あ、あの"),
            noto.talk("待って"),
            sana.talk("はい"),
            noto.do("もう一度読み直している"),
            noto.talk("ねえ"),
            sana.talk("はい？"),
            noto.talk("なぜ彼女は亡くなった人の命を集めているの？"),
            sana.talk("それは死神という設定だから"),
            noto.talk("死神が滅びた世界の神になる、というのは大筋としては面白いと思う"),
            _.talk("けどそこに読者は何故？　を感じるんだ"),
            _.talk("作者がいくら集めたかったからだ、と言いはったところで、この登場人物の考えではないからね"),
            _.talk("一体彼女が何を考えて、そう思ったのか"),
            _.talk("短編は多くは語れない、とは言った。けれど、語るべきことは語らないといけない"),
            _.talk("わずか原稿二十枚、三十枚としても、そこは彼らの人生の断片なんだ"),
            sana.think("間に合わせで書いた、というつもりはないけれど、突っ込まれると弱い"),
            noto.talk("最初に$meが言った意味が、少しは理解できた？"),
            _.talk("作者というのは常にこういった視線に晒されているんだ"),
            _.talk("その恐怖を一人で抱え込む。一人で戦うことになる"),
            _.talk("だから必死に書くし、調べるし、間違ってないか誰かに聞く"),
            _.talk("でも最終的にそれにゴーサインを出すのは自分自身だからね"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_deadline_short, time=w.at_night,
            ).omit()

def sc_lonleyroad(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira = W(w.nirasaki)
    return w.scene("寂しい帰路",
            sana.be("一人暗い夜道を歩いている"),
            sana.look("目元が赤い。涙の跡だ"),
            sana.think("結局先生の原稿は貰えなかった"),
            _.think("自分の、編集としての浅はかさ、物足りなさが見透かされた"),
            _.think("大事な原稿は預けられない、と言われた"),
            _.think("そんなことにはならないと思いこんでいたので、ショックが大きい"),
            sana.talk("$meは、どこかで小説をバカにしていたんだ"),
            sana.do("そこにスマホに$lineが入る", "$nirasakiだ"),
            nira.voice("王が突然打ち込んできた。$nomioの短編が$notoのところに打ち込まれる。残念だったな"),
            sana.talk("え？　なんで"),
            sana.explain("$nomioとは$w_dengekiで何作もヒットを出しているこの界隈では著名な作家だ"),
            sana.talk("一体どうやって引っ張ってきたの！？"),
            _.think("実績に知名度、全てが$noto先生とは比べ物にならなかった。完全に潰しにきたのだ"),
            sana.talk("どうしよう……"),
            ## NOTE
            ##  その日の帰路から。落ち込んで帰るところに、更に追い打ちが入る
            camera=w.sana,
            stage=w.on_street,
            day=w.in_deadline_short, time=w.at_night,
            )

def sc_lastemeeting(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, yone, king, fukaya = W(w.nirasaki), W(w.yonezawa), W(w.king), W(w.fukaya)
    return w.scene("最終会議",
            sana.come("入ってくる"),
            sana.look("緊張した面持ち"),
            nira.be(),
            yone.be(),
            king.come("入ってくる"),
            sana.do("煙草の臭いを感じる"),
            king.do("座って不機嫌そう"),
            sana.think("どうしてなんだろう"),
            yone.talk("それでは編集会議を始めます。今日が『$hermagazine1』一月号の最終決定となりますので"),
            sana.explain("$yonezawaの仕切りで会議が進む"),
            yone.talk("それで$noto先生の原稿まで全て揃っていますが、事前に目は通されたと思って、話を進めます"),
            sana.think("緊張気味に"),
            sana.explain("まず全部の作品についてタイトルと作家名を羅列し、それぞれについて各編集が意見を言い合う",
                "ここで問題があれば印刷入稿までに細部の調整を行う。その裁量は担当編集になる",
                "当然最終決定は編集長が行うが、小規模なので、ここで意見がなければほぼそのままということが多い"),
            yone.talk("次に$noto先生の作品ですが"),
            w.comment("実は$sanaの作品であり、ダミーだが、これでまず押し通そうと考えている"),
            nira.talk("発想は面白いと思うけどさ、なんか文芸の先生って割には文章力が壊滅じゃないですか"),
            sana.think("相変わらず言いたいことをはっきり言う$nirasakiである"),
            yone.talk("気になる部分はあります。しかしライトノベル風に寄せていると考えれば、まだ不慣れなだけとも思えます"),
            sana.think("一番頼りになる$yonezawaのフォローにほっとする"),
            king.talk("これ駄目だろ？　なんだよこれ。こんなもんが目玉になんのか？"),
            _.talk("なあ$yonezawa。どうして$meが折角声かけて確保した$nomio先生の作品外したんだ？"),
            yone.talk("企画意図からズレるし、作品もまだ拝見してません。締切との兼ね合いから次回に回す方が良いと思いますが"),
            king.talk("そんなちんたらやってっから古いとか遅れてるとかズレてるって言われんだよ。今やネットの時代だ。もっとテンポよく、即時即決みたいなノリでやらんといかんだろ？"),
            sana.think("$yonezawaの判断で外していたとは思わなかった"),
            yone.talk("ただ企画の趣旨からすると、$noto先生の作品もやはり掲載は見送った方が良いでしょう"),
            sana.talk("どうして、ですか"),
            yone.talk("$noto先生が書かれた、という前提で話しますが、その先生が書いた、ということ以上のバリューがない。",
                "$nirasakiが言ったが、これは今回の企画の目玉商品です。その要求に応えてはいない。物語の形をしているが小説としてはどうでしょう",
                "これを『$hermagazine1』の顔として出せますか？　今回はイラストもつけてもらいます。それだけの力がありますか？"),
            sana.do("ぐっと堪えている"),
            king.talk("だから言っただろ。$meが言うように$nomio先生を使え。これをきっかけにうちでも連載持ってもらって、ゆくゆくは看板商品をだな"),
            sana.think("終わった、と思った"),
            ## NOTE
            ##  決定会議の緊迫場面。ここでそれぞれの立場や矜持、を見せておく
            stage=w.on_meetingroom_int,
            day=w.in_meetingshortnovel, time=w.at_midmorning,
            )

## episode
def ep_lemon(w: World):
    return w.episode("3.檸檬",
            ## NOTE
            sc_writerwill(w),
            sc_lonleyroad(w),
            sc_lastemeeting(w),
            )
