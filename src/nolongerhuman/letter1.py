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
def sc_magazinewriter(w: World):
    sana, noto = W(w.sana), W(w.noto)
    yuzawa = W(w.yuzawa)
    return w.scene("雑誌記者",
            sana.come("先生の見舞いを終えた$Sが病院から出てくる"),
            yuzawa.come("それを待ち構えていたカメラを担いだ記者がやってきて"),
            yuzawa.talk("$noto先生の担当編集の方ですね？"),
            sana.talk("やっぱりあなただったんですね"),
            camera=w.sana,
            stage=w.on_hospital_ext,
            )

def sc_writertalk(w: World):
    sana, noto = W(w.sana), W(w.noto)
    yuzawa = W(w.yuzawa)
    return w.scene("記者の話",
            sana.be("近所のファミレスに入り、対面で座っている"),
            yuzawa.be(),
            yuzawa.do("注文した大盛りのスパゲティを前に"),
            yuzawa.talk("集中治療室で全治三ヶ月。結構な火傷でしたね。なんでも放火っていう話ですが"),
            sana.talk("警察の方から、そういう可能性もあると聞いてます"),
            yuzawa.talk("原稿も焼けて大変だとか"),
            sana.talk("どこで？"),
            yuzawa.talk("こっちも商売ですからね、出処は教えられませんよ。けど、まあ色々ツテはありますしね"),
            _.talk("それよりも、ネットニュースは見られました？"),
            sana.talk("なんですか盗作って。今度はうちを狙ってるんですか？"),
            yuzawa.talk("世間は今盗作に目が厳しくなってます。盗作ってのはいけないことだ"),
            _.talk("元の作者の権利を侵害する酷い行為だ。そう思いませんか？"),
            sana.talk("先生は盗作なんてしてません"),
            yuzawa.talk("はい、言質とったよ"),
            _.do("ボイスレコーダを見せる"),
            sana.talk("知ってますか。そういうのって証拠能力がないんですよ"),
            yuzawa.talk("肝が座ってるなあ"),
            _.talk("こっちはね、証拠をちゃんと持ってるんですよ"),
            sana.talk("何が証拠になるっていうんです？"),
            yuzawa.talk("$full_tsuru、知ってますね？"),
            sana.do("黙り込む"),
            yuzawa.talk("先生のデビュー作が、彼の盗作だって告発文書があるの、知ってますか？"),
            sana.think("先生が見せてくれた遺書のことだろう"),
            yuzawa.talk("編集ならもっと担当作家のこと、調べておいた方が良いですよ"),
            sana.talk("作家を信頼するのも、編集の仕事ですから。失礼します"),
            yuzawa.talk("そこまで言うなら、後で良いものをお送りしますよ。楽しみにしてて下さい"),
            sana.go("行ってしまう"),
            stage=w.on_famires_int,
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
            sc_magazinewriter(w),
            sc_writertalk(w),
            sc_mynovel(w),
            sc_masterletter(w),
            )
