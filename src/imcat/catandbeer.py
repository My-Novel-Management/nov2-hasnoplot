# -*- coding: utf-8 -*-
"""Episode: 2-3.猫とビール／吾輩は猫である
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
def sc_1stmission(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("最初の仕事",
            noto.talk("そうだな。まあ、君が代わりということは理解したが"),
            noto.talk("ちょっと買い物を頼まれてくれないか。ビールをきらしてしまってね"),
            noto.talk("あ、ついでにこいつの餌を買ってきてくれ"),
            camera=w.sana,
            stage=w.on_hisapart,
            day=w.in_firstmeet, time=w.at_afternoon,
            )

def sc_gotoconveni(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("いざコンビニ",
            sana.do("近所のコンビニに向かう"),
            sana.think("何故ビールと猫缶を買いに出かけているのかと疑問"),
            sana.do("スマホとメモで先生の情報を確かめる"),
            sana.think("先輩のメモには癖が強いし、好き嫌いが激しい。食べ物も、言動も"),
            _.think("年齢は五十前だが、十代の子どものような言動が頻繁に見られる"),
            _.think("独身。冗談でセクハラ発言がある"),
            sana.think("あれは冗談ってレベルじゃないです"),
            sana.think("溜息をついているうちにコンビニに"),
            stage=w.on_street,
            )

def sc_endmission(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("買ってきました",
            sana.come("買い物袋と共に戻ってくる"),
            sana.talk("先生買ってきました、よ？"),
            sana.do("足元に猫がじゃれつくだけ"),
            sana.do("先生は不在"),
            sana.talk("やられた！"),
            sana.hear("と、浴室から水の音"),
            sana.think("メンタルが弱い、というメモを思い出して"),
            sana.think("まさかね……"),
            sana.talk("先生？　先生！"),
            sana.do("返事がないので心配になり"),
            sana.talk("開けますよ？"),
            sana.do("ドアを開けて浴室を確認すると、湯船でくつろいでいた"),
            noto.talk("ああ、早かったね"),
            sana.talk("なんで風呂はいってるんですか！"),
            noto.talk("今日初めての人が来るから"),
            sana.talk("もう来てます！"),
            stage=w.on_hisapart,
            )

## episode
def ep_cat_and_beer(w: World):
    return w.episode("3.猫とビール",
            ## NOTE
            sc_1stmission(w),
            sc_gotoconveni(w),
            sc_endmission(w),
            )
