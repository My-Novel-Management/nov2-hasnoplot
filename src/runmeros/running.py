# -*- coding: utf-8 -*-
"""Episode: 1-1.走れ編集者／走れメロス
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
def sc_running(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, fukaya = W(w.nirasaki), W(w.king), W(w.fukaya)
    return w.scene("走れ",
            sana.explain("$full_sanaは激怒した"),
            _.explain("必ず、かの邪智暴虐の王を除かなければならぬと決意した"),
            _.explain("$Sには編集部の都合がわからぬ"),
            _.explain("$Sはただの平の編集者である。それもまだ転籍してきたばかりで新人に等しい"),
            _.explain("本を読み、データと戯れて暮して来た"),
            _.explain("けれども邪悪に対しては人一倍に敏感であった"),
            sana.think("そんな走れメロスの冒頭を改変したくなるほど、$Sは憤っていた"),
            sana.do("駅を出て、駆け抜ける"),
            sana.do("鞄二つ持ちの小柄な女性は、慌ててセットした髪は既に乱れている"),
            sana.do("それもそのはず、急遽別の編集が休んで、半休だったのに呼び出されたからだ"),
            sana.talk("なんて日！"),
            sana.do("晴れていたと思ったら雨が降り始める"),
            sana.do("慌てて傘を買いにコンビニに立ち寄る"),
            camera=w.sana,
            stage=w.on_street,
            day=w.in_firstmeet, time=w.at_midmorning,
            )

def sc_inconveni(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("コンビニにて",
            sana.do("本棚に並ぶ文庫などを見て"),
            sana.think("自分の出版社のものはなくて"),
            sana.do("傘とホットレモネードを買って、出る"),
            sana.do("雨が上がっていた"),
            sana.talk("何なのよ！"),
            stage=w.on_conveni_int,
            )

def sc_imeditor(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, fukaya = W(w.nirasaki), W(w.king), W(w.fukaya)
    return w.scene("私は編集者",
            sana.do("会社への道を走る"),
            sana.hear("救急車のサイレン"),
            sana.think("トラックに轢かれたら異世界にでもいけるのだろうか"),
            _.think("昨夜読んだ下読みの原稿の一つを思い出す"),
            _.think("みんなが異世界にあこがれている訳でもない"),
            _.think("でもそれが需要だからと作家は書く、応募する"),
            _.think("けど読んでいくと、本当に書きたいものは違うのだろうな、という気持ちが透けて見える"),
            sana.think("編集として、もっと作家の書きたいものを世間に届けたい"),
            _.think("そう願わずにはいられない"),
            stage=w.on_street,
            )

## episode
def ep_runeditor(w: World):
    return w.episode("1.走れ編集者",
            ## NOTE
            sc_running(w),
            sc_inconveni(w),
            sc_imeditor(w),
            )
