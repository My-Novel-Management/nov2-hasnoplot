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
    road = W(w.road)
    sky = W(w.sky)
    return w.scene("走れ",
            w.comment("アイデア・企画に関する話題を中に盛り込んでおくこと。編集部のあたりでいい"),
            sana.explain("$full_sanaは激怒した"),
            _.explain("必ず、かの邪智暴虐の王を除かなければならぬと決意した"),
            _.explain("$Sには編集部の都合がわからぬ"),
            _.explain("$Sはただの平の編集者である。それもまだ転籍してきたばかりで新人に等しい"),
            _.explain("本を読み、データと戯れて暮して来た"),
            _.explain("けれども邪悪に対しては人一倍に敏感であった"),
            sana.think("そんな走れメロスの冒頭を改変したくなるほど、$Sは憤っていた"),
            sana.wear("スカートスーツ（パステルピンク）にスニーカー"),
            road.look("駅前の混雑した歩道"),
            sana.do("駅を出て、駆け抜ける"),
            sana.look("鞄二つ持ちの小柄な女性は、慌ててセットした髪は既に乱れている"),
            sana.explain("それもそのはず、急遽別の編集が休んで、半休だったのに呼び出されたからだ"),
            sana.talk("なんて日！"),
            sky.look("晴れていたと思ったら雨が降り始める"),
            sana.go("慌てて傘を買いにコンビニに立ち寄る"),
            ## NOTE:
            ##  走れメロスを意識した冒頭
            ##  慌ただしく、かつ舞台が「現代日本・東京」であることを示唆
            ##  主人公の容姿（小さい）、鞄二つ持ち、愛されボディ等
            ##  主人公の性格
            camera=w.sana,
            area=w.Tokyo,
            stage=w.on_street,
            day=w.in_firstmeet, time=w.at_midmorning,
            )

def sc_inconveni(w: World):
    sana, noto = W(w.sana), W(w.noto)
    rin = W(w.rin)
    shelf = W(w.bookshelf)
    inside = W(w.inside)
    return w.scene("コンビニにて",
            sana.come("店に慌てて駆け込む"),
            rin.be(),
            rin.talk("ラシャアセー"),
            rin.wear("紺色に緑白のボーダーの制服"),
            sana.hear("いつもの抑揚のないコンビニ店員の声だ"),
            inside.look("店内は混み合っていて、傘を買い求める列ができている"),
            sana.think("参ったなあ"),
            sana.do("腕時計を確認する"),
            sana.do("本棚に並ぶ文庫などを見て"),
            shelf.look("雑誌の棚には$weekmagazine1が並び、そこには不倫や汚職に並び『盗作騒動！？』と赤字が踊る"),
            w.eventStart("大手の盗作騒動"),
            sana.think("盗作？　と疑問に思ったが、それは映画原作でもめているという話でほっとすると共に、自分の会社のことも考えて不安になった"),
            sana.do("傘とホットレモネードを買って、出る"),
            sana.do("雨が上がっていた"),
            sana.talk("何なのよ！"),
            ## NOTE:
            ##  簡単にコンビニ説明（よく使うので、いつもいる外国人店員配置）
            ##  不運さ
            ##  別の出版社の話題で「盗作騒動」の週刊誌（ここで週刊誌名出しておく。あとで使う）
            stage=w.on_conveni1_int,
            )

def sc_imeditor(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, fukaya = W(w.nirasaki), W(w.king), W(w.fukaya)
    sky = W(w.sky)
    return w.scene("私は編集者",
            w.comment("ここ削除候補"),
            sana.be("会社への道を走っている"),
            sana.hear("救急車のサイレン"),
            sky.look("どんよりした空模様。青空も見えない"),
            sana.think("トラックに轢かれたら異世界にでもいけるのだろうか"),
            _.think("昨夜読んだ下読みの原稿の一つを思い出す"),
            _.think("みんなが異世界にあこがれている訳でもない"),
            _.think("でもそれが需要だからと作家は書く、応募する"),
            _.think("けど読んでいくと、本当に書きたいものは違うのだろうな、という気持ちが透けて見える"),
            sana.think("編集として、もっと作家の書きたいものを世間に届けたい"),
            _.think("そう願わずにはいられない"),
            ## NOTE:
            ##  不穏さを演出し、今後の行く末を暗示する
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
