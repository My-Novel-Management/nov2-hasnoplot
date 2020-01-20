# -*- coding: utf-8 -*-
"""Episode: 8-1.第一章／金閣寺
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
def sc_beautiful(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("美意識",
            w.comment("先生は沙奈に作家の美意識について語る"),
            sana.come("先生に連れてこられる"),
            noto.talk("こういう場所も見ないと駄目だよ"),
            sana.talk("分かっているんですが、忙しいとなかなか"),
            sana.do("人は少ない"),
            sana.do("先生の知人の作家も参加している美術展。現代美術も入っていて、よく分からない"),
            noto.talk("作家にも美意識というのは必要でね。別に音楽や芸術をテーマとした作品を書かなくても、それぞれの作家の美意識というものが大事だ"),
            noto.talk("作品には強く反映される"),
            noto.talk("作品は一つの芸術作品と言ってもいい"),
            noto.talk("文章や出来事、物語のオチ、ちょっとした小物やそれらの描写。そういったことの全てが美意識なんだ"),
            sana.do("メモを取る。スマホで"),
            noto.talk("それは何とかならないかね？"),
            sana.talk("気になりますか？"),
            noto.talk("情緒がない。これも美意識の問題か"),
            sana.talk("じゃあ若者の美意識ですね！"),
            noto.do("目を覆う"),
            camera=w.sana,
            stage=w.on_artmuseum,
            day=w.in_visitmuseum, time=w.at_afternoon,
            )

def sc_aboutnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("作品について",
            sana.come("近所の喫茶店に立ち寄る"),
            sana.do("客は結構入っていて、カウンターで横並びになる"),
            noto.do("$Sは定食を注文"),
            sana.explain("$Sはサンドウィッチ系"),
            noto.talk("（やってきたのを見て）おお"),
            sana.talk("美味しそうですね、それ"),
            noto.talk("$meのだからね。あげない"),
            sana.talk("分かってますよ。けど先生って一人っ子だったんですよね？"),
            noto.talk("君は兄さんがいるんだったかな"),
            sana.talk("そうなんです。勝手に皿からカツとか取っちゃうんですよ"),
            noto.talk("そういうの、憧れるなあ"),
            sana.do("カツを取る$S"),
            sana.talk("これでも？"),
            noto.talk("じゃあこうだ"),
            noto.do("玉子サンドを取った"),
            sana.talk("ほんと、子どもですよ、先生"),
            noto.talk("ところで作品の方はどうかな？"),
            sana.talk("書いてますけど、大変ですね。長編"),
            noto.talk("短編とは全然違うからね"),
            noto.talk("とにかく最後まで書くことだ", "作品は書けば書くほど、色々と教えてくれる"),
            noto.talk("もちろん下調べなども大事だ。書くべき対象について調べられるものは調べる"),
            noto.talk("そして一番大事なことは、自分が変だ、と感じたら、そう書いておくこと"),
            noto.talk("変だ、という感覚は美意識に反しているからだ"),
            noto.talk("後でそこを見て、直せばいい"),
            noto.talk("書きながら、色々と考えることだ"),
            noto.talk("小説が、君の新しい美意識に気づかせてくれることもある"),
            noto.talk("二人三脚なんだよ、作家と小説は"),
            stage=w.on_cafe,
            )

## episode
def ep_chapter1(w: World):
    return w.episode("1.第一章",
            ## NOTE
            sc_beautiful(w),
            sc_aboutnovel(w),
            )
