# -*- coding: utf-8 -*-
"""Episode: 9-2.第一の手記／人間失格
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
def sc_getletter(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira = W(w.nirasaki)
    return w.scene("手紙を手に入れてしまって",
            sana.do("こっそり取っておいた先生のノートをどうしようと考え込む"),
            nira.talk("どうしたんだよ。それより先生の原稿燃えたんだろ？　もう流石に駄目なんじゃね？"),
            sana.talk("原稿どころじゃないわよ"),
            nira.talk("まあ、色々いわくつきだったから、これを教訓にもっとマシな作家担当しろよ"),
            sana.talk("マシな作家ね……"),
            sana.think("雑誌編集時代を思い返して"),
            sana.do("仕事に戻る"),
            sana.do("バイト君から朝の定時連絡を受けて"),
            sana.talk("まだ集中治療室か"),
            camera=w.sana,
            stage=w.on_heroffice,
            day=w.in_aftergetletter, time=w.at_midmorning,
            )

def sc_mynovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("とにかく自分の作品を",
            sana.do("外回りの後、待ち合わせの時間まで喫茶店で自作を書く"),
            sana.do("先生のノートには創作方法が書かれていて、参考にしていた"),
            sana.think("駄作でも最後まで書く、と、以前言われたことが書かれている"),
            sana.explain("無限の命を持つ女王が、世界を新生する。好きなようにできるはずなのに、好きなものだけ置いても壊れてしまう"),
            sana.explain("うまくいかないジレンマを抱える"),
            sana.explain("ファンタジィだが、それは編集作業と同じだった"),
            sana.explain("好きなものだけを盛り付けたバイキングの皿は、ただ汚い"),
            sana.think("バランスを考えて並べない、ということ。言い換えればバランスさえ取れていれば一見すると汚れて見えるものでも芸術になる"),
            sana.think("上司から教わったことを思い出す"),
            sana.do("作品の根幹を書き換える決意"),
            sana.do("新しく担当することになった作家が現れて、挨拶など"),
            stage=w.on_cafe,
            time=w.at_afternoon,
            )

def sc_masterletter(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生の手紙",
            w.comment("恥の多い生涯を送ってきました、という人間失格の書き出しになぞらえてある"),
            sana.do("残業を終えて帰ってきてから、風呂を浴びて、上がってきた"),
            sana.do("自室で髪を乾かしてから、もうひと仕事と思う"),
            sana.do("パソコンで作業しつつ、行き詰まって"),
            sana.do("先生の創作ノートを見ていて、後ろの方に挟まれていた、便箋を見つけてしまう"),
            sana.talk("何これ……"),
            sana.do("そこには人間失格の書き出しが書かれていた"),
            stage=w.on_herroom,
            time=w.at_night,
            )

## episode
def ep_letter1(w: World):
    return w.episode("2.第一の手記",
            ## NOTE
            sc_getletter(w),
            sc_mynovel(w),
            sc_masterletter(w),
            )
