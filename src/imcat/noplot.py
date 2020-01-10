# -*- coding: utf-8 -*-
"""Episode: プロットがありません
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
def sc_havenoplot(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("プロットすらないと告白",
            sana.talk("え？　今なんて言いました？"),
            noto.talk("だからさ、まだプロットすらないんだ", "ほら"),
            _.do("真っ白な原稿用紙を見せる"),
            sana.talk("先輩からの引き継ぎでは順調にいってるみたいだって聞いてましたよ？"),
            noto.talk("一応ライトノベルってものはなんとなく理解したとは答えたよ",
                "そもそもいつも彼女にプロットを見せたりはしてなかったからね"),
            sana.talk("プロット作らない派なんですよね？　そうですよね？"),
            noto.talk("$meはそんな天才肌じゃないよ"),
            sana.talk("プロットどこですか！"),
            _.do("部屋を探し回る"),
            noto.talk("おいおい、妙なものが出てきたらどうするんだ？"),
            sana.talk("別にえっちいものとか腐ったパンの入ったゴミ袋とか全然平気です"),
            noto.talk("まるで小姑だね", "ああ、早く$fukayaさん帰ってこないかな"),
            sana.talk("先生！"),
            noto.talk("まあまあ、お茶でも飲んで落ち着いて", "それとも酒がいいかな？"),
            sana.talk("仕事中です！"),
            _.talk("それよりプロットもらうまで今日は帰りませんから"),
            noto.talk("まいったなあ"),
            sana.talk("参るのはこっちの方ですから！"),
            )


## episode
def ep_noplot(w: World):
    return w.episode("プロットがありません",
            ## NOTE
            ##  - プロットすらないと告白された
            sc_havenoplot(w),
            )
