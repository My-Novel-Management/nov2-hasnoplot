# -*- coding: utf-8 -*-
"""Episode: 2-2.猫と小説／吾輩は猫である
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

## episode
def ep_cat_and_novel(w: World):
    return w.episode("2.猫と小説",
            ## NOTE
            sc_main2(w),
            )
