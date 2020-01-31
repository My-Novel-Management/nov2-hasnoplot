# -*- coding: utf-8 -*-
"""Episode: 2-1.猫と先生／吾輩は猫である
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
def sc_cannot(w: World):
    sana, noto = W(w.sana), W(w.noto)
    cat = W(w.mascat)
    kotatsu = W(w.kotatsu)
    return w.scene("脱ぎません",
            w.comment("会話劇が主体なので描写心持ち多めにして、間を作る"),
            sana.be("正座している"),
            noto.be("座ってテーブルに肘を突き、じっと$CSを見ている"),
            kotatsu.look("四角形のどっしりした炬燵"),
            sana.talk("いやです。脱ぎません"),
            noto.talk("そう。じゃあ、出ていっていいよ"),
            sana.think("これくらいではへこたれないと気合を入れて"),
            sana.talk("本日より$fukayaの担当を引き継いで先生の編集になりました$full_sanaです"),
            noto.talk("何も聞いていないんだが"),
            sana.explain("体調を崩して産休を早めに取得することになった都合を説明"),
            noto.talk("ああ、そういえば来年出産だったね。それは大事にしてもらいたい"),
            sana.talk("で、その代役が$meです"),
            noto.talk("ベテランには見えないけど、経験は？"),
            sana.talk("別の編プロにいたんで、月刊誌を一年ばかり。こっちはまだ一月ちょっとですね"),
            noto.talk("そうか。つまり、$meはその程度でいいと、そういう判断だね？"),
            sana.talk("どういうことですか？"),
            noto.talk("そのままさ"),
            noto.talk("編集にも格というものがある。やはり大事にしたい作家にはそれなりの担当がつくものだよ"),
            sana.talk("先生は一般文芸だから分からないでしょうけれど、ライトノベルの方では編集一人が何人も担当することが普通で、"),
            _.talk("また入れ替わりも激しいんで、そこまで気を回してられないのが現状なんですよ"),
            noto.talk("それはそっちの事情だろう"),
            sana.do("引き継ぎ用に先輩に作ってもらった資料を見せて"),
            sana.talk("本来なら一緒に$fukayaも来ることになっていたんですが、急に体調を崩して。それで$meだけで参りました"),
            sana.talk("何か気に障りましたら、担当変えなども考えますが"),
            cat.come("一匹のでぶったぶち猫がやってくる"),
            cat.look("白と黒のぶち"),
            sana.talk("きゃっ"),
            noto.talk("へえ、珍しい。その子なかなか他人になつかないのよ"),
            sana.talk("ね、猫かってるんですか？"),
            sana.talk("$me、ちょっと苦手で"),
            sana.do("だが胸元にやたらとすり寄ってくる"),
            sana.talk("ちょ、ちょっと"),
            noto.talk("そいつ、名前はマダナイね"),
            sana.talk("名前ないのか"),
            noto.talk("いや、マダナイ君。そして$meの飼い猫ではなくて、いつも勝手にやってきてくつろいでいく。たぶん野良猫ではないと思うけど"),
            sana.do("首輪を見て"),
            sana.talk("何も書いてませんね"),
            noto.talk("しかしそいつが興味を示したということは、実に興味深い"),
            ## NOTE
            ##  ２話冒頭なので今一度、先生と、沙奈を印象づけておく
            ##  回想せずに状況説明を含ませておくこと
            ##  アパート内の細かい描写はまだなので、ここでしっかりと描写して冒頭パートを終える
            ##  最後に猫登場で、笑顔になる先生
            camera=w.sana,
            area=w.Tokyo,
            stage=w.on_hisapart,
            day=w.in_firstmeet, time=w.at_noon,
            )

## episode
def ep_cat_and_master(w: World):
    return w.episode("1.猫と先生",
            ## NOTE
            sc_cannot(w),
            )
