# -*- coding: utf-8 -*-
"""Episode: 吾輩は猫である
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
    return w.scene("1.猫と先生",
            sana.talk("嫌です"),
            sana.explain("突然脱げと言われたが、$Sはそれをすぐに断った"),
            noto.talk("君の仕事は何？"),
            sana.talk("先生の担当編集です", "先生が良い作品を書いて本にできるようにお手伝いと橋渡しをする仕事です"),
            noto.talk("じゃあ脱ぐべきだな",
                "君が脱ぐことで$meは作品を書くことができる", "もし脱がなければ原稿は永遠に完成しない"),
            sana.think("面倒な作家が現れた"),
            sana.explain("なんとかいいすくめて、脱がなくて済ませる"),
            sana.do("足元に猫がやってきて、いつく"),
            noto.talk("へえ。そいつは人にあまり興味を示さないので有名なんだが、なるほどね"),
            )

def sc_main2(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("2.猫と小説",
            sana.do("まずは何とか編集として認めてもらおうとする"),
            sana.talk("先生の著作読みましたよ"),
            sana.talk("あ、デビュー作はまだ手に入ってないんですが"),
            noto.talk("売れ行きがよくなかったそうだからね"),
            sana.talk("でもこのシリーズなんか"),
            noto.talk("それは半分以上、$fukayaさんの功績だ",
                "彼女がいろいろと尽力してくれて、女性読者が増えたと聞いている"),
            sana.talk("文芸作品ばかり書かれていたのに、どうして急にライトノベルの方に？"),
            noto.talk("仕事がないからだ"),
            noto.talk("もう君のところの出版社くらいしか扱ってくれなくてね",
                "あとは電子なんとかにするしかないと言われた"),
            sana.talk("いいと思いますよ"),
            sana.do("端末を見せる。それで最近は何百冊と持ち歩けると"),
            noto.talk("まるで魔法だね", "けど、どうやって使うのかも分からず、何よりどんな読み方がされるかも分からない",
                "そんなものに自分の作品を出しても、読者はいるのだろうか"),
            sana.talk("いますよ",
                "古典なんか読まれないと言われていた中で、表紙を今風にしたりするだけで売れたりするんですから"),
            noto.talk("それはレコードなどのジャケット買いと同じで、中身に興味はないということじゃないのか？"),
            )

def sc_main3(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("3.猫とビール",
            noto.talk("小説にお酒はつきものでね"),
            noto.talk("ちょっとビールを買ってきてもらえるかね"),
            sana.go("仕方なく買い物に"),
            sana.explain("近所のコンビニで、気の良さそうなおばさん",
                "一緒に買ったおつまみで、また先生？　担当変わったのね、と言われる始末"),
            sana.come("両手いっぱいにして戻ってくる"),
            sana.do("先生が消えている"),
            sana.talk("どこですか！"),
            sana.do("探し回る"),
            sana.do("近所を歩き回ってやっと見つけた"),
            noto.talk("いや、こいつがね"),
            noto.do("猫を抱き上げて"),
            noto.talk("この自由さは見習いたい"),
            sana.think("充分自由人だがな、と思ったり"),
            )

def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("4.猫と原稿",
            sana.talk("今、なんて？"),
            noto.talk("だからないと言ったんだ", "プロットすらないよ"),
            sana.talk("嘘ですよね？"),
            noto.talk("$meは小説の中以外での嘘が嫌いでね"),
            sana.talk("プロットもないんですか？　ほんとに？"),
            sana.think("激しく混乱する"),
            sana.explain("今日原稿（初稿）をもらう手はずになっていると先輩からは聞いていた"),
            sana.talk("ちょっと確認します"),
            sana.do("電話する"),
            sana.talk("あの、先輩、今先生の家なんですけど"),
            sana.explain("そういうところがあるから気をつけて、がんばって原稿むしり取ってきてね、と笑われる"),
            sana.talk("探します"),
            noto.talk("だからないんだって"),
            sana.think("$Sは絶対に原稿を探し出すと決意した"),
            )

## episode
def ep_main(w: World):
    return w.episode("吾輩は猫である",
            ## NOTE
            sc_main1(w),
            sc_main2(w),
            sc_main3(w),
            sc_main4(w),
            )
