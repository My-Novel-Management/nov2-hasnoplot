# -*- coding: utf-8 -*-
"""Episode: 10-4.エピローグ／銀河鉄道の夜
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
def sc_main4(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("4.エピローグ",
            sana.explain("こうして先生の作品が無事長編出版枠を獲得し、現在絶賛ゲラ校正作業中です"),
            _.think("$meの作品は読み返してみれば確かに穴だらけで、でも先生が言ったように紛れもなくそこには$meが描かれていて、",
                "もっと磨き上げて本当の作品にしていこうと思っていますが、",
                "実際編集者としての残業の日々は忙しく、体力的にも精神的にも、とても自分の作品のことなんて構っていられません"),
            sana.come("先生の新しいアパートにやってくる"),
            _.talk("進捗どうですか？"),
            noto.talk("まだ文章を削らないといけないのかね？", "これ以上削ったら情緒も何もなくなってしまう"),
            sana.talk("一般文芸とは違います", "それに先生の作品は多少地の文を削ったくらいじゃ揺らぎませんよ"),
            _.think("少しは言い返せるようになった",
                "まだまだ不勉強なところはあるが、よく相談し、話を聞き、耳をすまし、何よりまずは作家の気持ちを尊重する"),
            _.think("それは$meが一度作家を経験しているからこそ、考えることができる"),
            sana.talk("あ、今日はこれです"),
            _.do("差し入れの和菓子を差し出す"),
            noto.talk("どこの店のものだね？"),
            sana.talk("今日は友人が作ったものですよ", "彼女も作家を目指してるんですけど、なかなか大変みたいで"),
            noto.talk("そうか。なら一度うちに来てもらいなさい"),
            sana.think("嫌な予感"),
            sana.talk("先生、まさか"),
            noto.talk("何を心配しているのかね？", "$meが今まで誰かを不当に扱ったことがあったかい？"),
            sana.think("自分の数々の不当な扱いを思い出して"),
            _.talk("今の発言が一番不当な気がします", "修正よろしいでしょうか？"),
            _.explain("こうして$Sの編集人生は幕を開けたのである"),
            )

## episode
def ep_epilogue(w: World):
    return w.episode("4.エピローグ",
            ## NOTE
            sc_main4(w),
            )
