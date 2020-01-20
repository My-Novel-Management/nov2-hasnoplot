# -*- coding: utf-8 -*-
"""Episode: 1-2.憤れ編集者／走れメロス
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
def sc_mycompany(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("私の会社です",
            sana.do("何喰わぬ顔で会社ビルまでやってくる"),
            sana.do("遅めの出社の人たちもいる"),
            sana.do("ビルの一階はコンビニ"),
            sana.do("脇の入り口から入り、エレベータに"),
            camera=w.sana,
            stage=w.on_hercampany_ext,
            day=w.in_firstmeet, time=w.at_midmorning,
            )

def sc_myoffice(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("編集部です",
            sana.do("廊下を歩いて、第二文芸部の前"),
            sana.do("時刻を確認して、ちょっと過ぎたな、と"),
            sana.do("ドアを開けて"),
            sana.talk("おはようございます"),
            stage=w.on_heroffice_ext,
            )

def sc_callking(w: World):
    sana, noto = W(w.sana), W(w.noto)
    fukaya, king, nira = W(w.fukaya), W(w.king), W(w.nirasaki)
    return w.scene("王の呼び出し",
            fukaya.talk("ああ、ちょうどいいところに来た。今連絡しようと思ってたのよ"),
            sana.talk("え？"),
            fukaya.talk("急なことなんだけど、$meの担当している先生の一人を、担当してもらいたいの"),
            sana.talk("いいですけど、どうして急に"),
            fukaya.talk("産休を早めに取ることにしたのよ。ちょっと昨日診てもらったら、その方がいいってことで"),
            sana.explain("三十過ぎてから初出産で、それなのに色々と忙しくしていたのだ"),
            sana.talk("大丈夫です。あ、引き継ぎは"),
            fukaya.talk("ここに資料は用意してあるから"),
            king.talk("全く"),
            sana.do("新しく編集長になった通称「王」と呼ばれる男だ"),
            king.talk("（迷惑な一言）"),
            ## NOTE: 編集長の横暴をここで示しておく
            ## NOTE: アイデアについて、特に企画書について云々を
            stage=w.on_heroffice_int,
            )

def sc_emergency(w: World):
    sana, noto = W(w.sana), W(w.noto)
    fukaya, king, nira = W(w.fukaya), W(w.king), W(w.nirasaki)
    return w.scene("緊急事態",
            sana.come("編集長の話から戻ってくる"),
            sana.talk("先輩大丈夫ですか？　顔色が"),
            fukaya.talk("ごめん。ちょっと"),
            fukaya.do("顔を顰めてうずくまる"),
            sana.talk("あの、救急車呼びます！"),
            sana.do("慌てて"),
            fukaya.talk("頼んだわよ、先生のこと。大変だと思うけど"),
            sana.talk("任せて下さい。先輩はそれよりも無事に出産を"),
            fukaya.talk("ありがとう。助かるわ"),
            )

## episode
def ep_angryeditor(w: World):
    return w.episode("2.憤れ編集者",
            ## NOTE
            sc_mycompany(w),
            sc_myoffice(w),
            sc_callking(w),
            sc_emergency(w),
            )
