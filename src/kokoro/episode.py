# -*- coding: utf-8 -*-
"""Episode: こころ
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
def sc_main1(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("1.先生と私",
            sana.think("旅館で先生が語った「書けなくなった理由」がずっと気になっていた"),
            sana.do("仕事が手につかない"),
            sana.do("同僚に質問してみる"),
            sana.talk("作家が盗作をしたとバレたら、どうなるんだろう？"),
            sana.explain("多くはその作品の出版がなくなり、しばらく謹慎だろうと教わる"),
            sana.think("もしあの記者が言っていたように先生が盗作をしていた、と考えると、今原稿を書けないというのはとても納得できる"),
            sana.talk("ちょっと行ってくる"),
            sana.go("先生のアパートに"),
            sana.come("アパートにきて"),
            sana.talk("先生！"),
            noto.talk("ちょうどいいところにきた", "一緒に出かけようじゃないか"),
            )

def sc_main2(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("2.私と両親",
            sana.do("$notoに連れられて、彼が懇意にしている洋食屋に"),
            sana.do("近代文学がずらりと並ぶ本棚に囲まれている。文学亭"),
            sana.talk("こんな場所があったんですね"),
            noto.talk("今月で閉店だそうだ"),
            sana.think("時代の厳しさを教わる"),
            sana.do("先生に自分の家庭環境のことを話す"),
            sana.do("小さい頃から本に触れて育った"),
            sana.do("作家の夢は諦めたけれど、本に関わる仕事がしたいと思った"),
            noto.talk("君も書けばいいんだ", "あの短編は良かった"),
            sana.talk("流石に編集をやりながらは無理ですよ", "もうあんな大変な真似はできません"),
            sana.think("そう答えつつも、本当にそうなんだろうか？", "と自問していた"),
            )

def sc_main3(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("3.先生と両親",
            sana.do("先生に案内される"),
            sana.do("古本屋などを回る"),
            sana.do("先生の叔父は本屋をやっていた"),
            sana.do("けれど現在は廃業して、夢だったうどん喫茶をやっているらしい"),
            sana.explain("両親には金沢で世話になった",
                "立派な書斎を思い出すが、本が充実していた理由はそこにあったようだ"),
            noto.talk("そういう自由さは、$meも羨ましいところさ"),
            )

def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("4.先生と手紙",
            sana.come("先生のアパートにやってくる"),
            sana.do("留守でも掃除をしたりしている"),
            sana.think("世話女房だな、と苦笑"),
            sana.think("結婚相手はいないの？　と訊かれたことを思い出し"),
            sana.talk("先生？　ないない"),
            sana.do("と、本棚の後ろに隠されていたアルバムを見つける"),
            sana.do("更にその中に古くなった手紙が挟まれていた", "日記の破った欠片だ"),
            sana.think("最初にそれは隠しておきたかったものだと思った"),
            sana.do("その書き出しを読んで驚く"),
            sana.talk("本当のことなの？"),
            _.explain("そこには友人を殺したのは自分だと書かれていた"),
            )

## episode
def ep_main(w: World):
    return w.episode("こころ",
            ## NOTE
            sc_main1(w),
            sc_main2(w),
            sc_main3(w),
            sc_main4(w),
            )
