# -*- coding: utf-8 -*-
"""Episode: 9-4.第三の手記／人間失格
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
def sc_letterlast(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("先生の手紙の最後",
            w.comment("手紙の最後にはいつか責任を取らなければならないと書かれていた"),
            sana.be("告白の手紙を読んでいた"),
            noto.voice("そのことはすぐに彼に知れた"),
            _.voice("彼は何も$meに言うことなく、太宰治が命を断ったのと同じ日に首を吊った"),
            _.voice("それ以来、$meはずっと、自分がまともな作家ではないことを隠して生きている"),
            _.voice("いつかはこの罪が罰となって帰ってくるだろう"),
            _.voice("毎月の彼の月命日に欠かさず墓参りをしているが、未だに彼の言葉は聞けない"),
            _.voice("彼の言葉が聞けた日には、$meもおそらく"),
            _.do("読み終えて、溜息"),
            sana.think("どうして何も話してくれなかったのだろう"),
            _.think("そこに書かれていたのは、先生の作家として生きた時間と同じだけの苦悩だった"),
            _.think("言っていたことを思い出す"),
            noto.voice("作家というのはね、表に出て、あれやこれやと喋ってはならないんだ"),
            _.voice("何故ならそれは自分が本来書くべきことを発散してしまっているということだから"),
            _.voice("言葉は消えものだ。しかし文章にした時、小説になった時、それは時間と空間から切り離される"),
            _.voice("その唯一無二の小説という世界ができあがるんだ"),
            _.voice("だから本物の作家は無闇矢鱈に語らない"),
            _.voice("語るのは、本にはならない、枝葉末節だ"),
            sana.think("先生はずっと自分の心のうちに抱え込んでいたのだろうか"),
            _.think("作家はいつか死を選ぶ、と言っていたことも思い出す"),
            _.talk("そんなこと、$meが許しませんからね"),
            _.think("そして決意した。先生だけの為に、この小説を書き上げようと"),
            camera=w.sana,
            stage=w.on_herroom,
            day=w.in_readletter, time=w.at_night,
            )

def sc_lastscene(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("ラストシーン",
            sana.be("パソコンに向かっている"),
            sana.have("脇には先生のぼろぼろの創作ノート。付箋がいっぱい貼ってある", w.masternote),
            sana.explain("原稿用紙にして２５０枚の初の長編小説のラストシーンを書こうとしていた"),
            sana.do("キータイプしては消して、を繰り返す"),
            sana.think("初めての長編の完成を、したくない気持ちと、しなければいけない気持ちがせめぎ合っていた"),
            _.do("それでも先生の言葉を思い出して無理やり進める"),
            _.explain("作品は終盤、息絶えた世界を見事に再生した無限の命の女王が、不治の病にかかる"),
            _.explain("その病の原因が自分が生み出した生命たちにあると知り、女王は自決する"),
            sana.talk("でも、これだと……"),
            sana.do("$Sは一度書いてしまった自決シーンを全て消す"),
            _.do("真っ白にしたページに、再び書き始める"),
            sana.think("それでも、生きていく"),
            _.think("自分が冒した罪だと気づいても、人は様々な罪を冒した罪人だ。それが人間の有様なのだ"),
            _.think("沢山の失敗をしてきた。間違いもおかした。人を傷つけたこともあった"),
            _.think("でもそれらの全てを背負って、それでも生きていくのだ"),
            _.think("そこにはもう、自決しようとした女王の姿はなかった"),
            sana.do("ラストシーンを書きながら泣いていた"),
            sana.think("物語のラストシーンには、その作者の思いが滲んでいるという言葉を思い出す"),
            sana.do("最後に（了）の文字を入れて、保存した"),
            _.do("時刻を確認すると、もう深夜の三時を過ぎていた"),
            )

def sc_emergency(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    tsuchi = W(w.tsuchiura)
    return w.scene("緊急事態発生",
            w.comment("何とか作品を書き上げて寝てしまっていたところに、バイト君から連絡で、先生が病院から消えたと"),
            sana.be("机に突っ伏して寝ている"),
            sana.do("気づくともう翌日の午前十時すぎだった"),
            sana.do("ずっと携帯が鳴っている"),
            sana.talk("ん？"),
            sana.do("見ればバイト君だ"),
            sana.talk("どうしたの？"),
            tsuchi.voice("どうしたじゃないですって！", "大変なんです！", "先生が、消えました！"),
            sana.think("え？　意味が分からない"),
            sana.talk("あの、ちゃんと話して。$meまだ徹夜明けで頭が……"),
            sana.hear("インタフォンが鳴る"),
            sana.talk("はーい"),
            sana.talk("ちょっと待ってね"),
            azu.come("荷物を手に入ってきて"),
            azu.talk("これ。$sana宛だって"),
            sana.do("$azuminoから茶封筒を受け取る"),
            sana.talk("これ……"),
            sana.have("$tsuruの持ち込み原稿が入っていた", w.carryingpaper),
            sana.do("差出人は$yuzawaだった"),
            day=w.in_vanishmaster, time=w.at_midmorning,
            )

## episode
def ep_letter3(w: World):
    return w.episode("4.第三の手記",
            ## NOTE
            sc_letterlast(w),
            sc_lastscene(w),
            sc_emergency(w),
            )
