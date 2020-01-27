# -*- coding: utf-8 -*-
"""Episode: 10-3.ほんとうのものがたり／銀河鉄道の夜
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
def sc_master_paper(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    paper = W(w.longpaper)
    return w.scene("先生の原稿",
            w.comment("先生から書き終えたばかりの生原稿を受け取り、目を通す"),
            noto.talk("ちょっと、ここで待っててくれないか"),
            noto.go("そう言って立ち上がり、自室へと引っ込んでいく"),
            sana.think("言い過ぎただろうか、と先生の顔を見て反省する"),
            _.think("いつも言い過ぎる。それは長所でもあるけど短所にもなる"),
            _.think("先輩からは時にはじっと腰を据えて相手の話を聞くのも大事と言われたことを思い出す"),
            sana.talk("あー、またやっちゃったかなあ"),
            noto.come("戻ってきて"),
            noto.have("原稿が手にされている", w.longpaper),
            noto.do("原稿を$CSに渡す"),
            sana.talk("え、これって", "燃えたって言ってたんじゃないんですか？"),
            noto.talk("今日が締め切りだろう？"),
            sana.talk("あの、答えになってません"),
            _.talk("火事で原稿は全て燃えてしまったんじゃないんですか？"),
            noto.talk("燃えたよ", "でも原稿という物理的なものが燃えただけで、作品は消えたりしない"),
            sana.talk("入院中に書いたんですか？", "大火傷で動けないって聞いてたのに"),
            noto.talk("見てみなさい"),
            sana.do("原稿を見る"),
            paper.look("字が歪んでいるし、汚い"),
            sana.talk("これ、先生の字じゃないのが混ざってる"),
            sana.talk("あ……"),
            _.think("気づいた"),
            noto.talk("そうだよ", "バイト君には後で君から特別手当を出してあげて欲しい"),
            sana.talk("何も言ってなかったのに……"),
            _.think("でも様子がちょっと妙だったことを思い出す"),
            _.think("先生のことを最初はもう面倒見に行くの大変で嫌と言ってたのに、何故か途中から率先して病院に行くようになっていた"),
            _.think("そういう事情があったのだ"),
            noto.talk("だって君は、$meの担当編集だろう？"),
            sana.talk("先生……"),
            sana.do("先生から原稿を受け取る"),
            noto.talk("ああ。完成原稿だ。書き上げたよ……十年ぶりの新作長編だ"),
            sana.think("緊張してくる"),
            camera=w.sana,
            stage=w.on_hisnewapart,
            day=w.in_finishbook, time=w.at_afternoon,
            )

def sc_master_novel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生の小説",
            sana.do("先生の原稿を一枚一枚丁寧に捲って読んでいく"),
            _.explain("それは聞いていた話とは全然違っていた"),
            _.explain("当初、先生が絶対に書かないと言い張っていた”異世界もの”だ"),
            _.explain("小説家を目指していた一人の少女は、事故で夢半ばで亡くなってしまう"),
            _.explain("彼女は転生した見たこともない異世界で、多くの助けを借りながら、暮らしていく"),
            _.explain("その過程で小説というもののない世界で、彼女は唯一の小説家として、各地に残る伝説や民話を本にしていく"),
            _.explain("ベースはガリバー旅行記のような紀行もので、一巻ではまだ基本的な世界観の説明と主要キャラが揃っていく展開だけだったが、"),
            _.explain("小さい頃に胸踊らせた読んだ少年少女の冒険ものの趣があった"),
            sana.talk("先生、これ、素晴らしいです！"),
            noto.talk("君はいつもそれしか"),
            sana.talk("本当に素晴らしい時はこれでいいんです！"),
            _.do("嬉しすぎて抱きついてしまう"),
            noto.do("照れる"),
            sana.talk("これ、$me、絶対に本にします。もっと多くの人に読んでもらいたい。何より先生ともっと仕事がしたいです"),
            noto.talk("ありがとう"),
            sana.do("原稿を読み耽る$S"),
            )

def sc_decision_publish(w: World):
    sana, noto = W(w.sana), W(w.noto)
    king = W(w.king)
    return w.scene("出版が正式に決定",
            sana.do("編集長から電話が入る"),
            sana.talk("はい、もしもし。$ln_sanaです"),
            king.voice("あー、その、原稿はあるのか"),
            sana.talk("はい。今手元にあって、確認で読んでいる最中です"),
            king.voice("ならいい。伝えてくれ。ぜひ、三月の刊行予定でお願いしますと"),
            sana.talk("え？"),
            king.voice("聞こえんかったのか？", "枠が一つ空いたから、そこにお願いしたいとだな"),
            sana.talk("先生！", "聞きましたか！"),
            noto.talk("あ、ああ"),
            sana.talk("やったんですよ！", "$meたち、遂にやったんです！", "本になるんですよ、この作品が！"),
            king.voice("おーい。とにかく、今から大急ぎで校正作業頼むよ"),
            sana.talk("はい！", "任せて下さい！", "これで月刊誌で鍛えられたんですから！"),
            sana.do("電話切れる"),
            sana.think("どういう風なのか分からない。でも確実に良い風向きだった"),
            sana.explain("後で$nirasakiに確認すると、どうも決まっていた主力作家が途中から大手のＫに引き抜かれて、そっちで出すことになったと"),
            sana.explain("ともかく、こうして先生の御本は無事に出版されることになりそうです"),
            sana.talk("先生、早速なんですが"),
            noto.talk("いきなりダメ出しかね？"),
            sana.talk("これ、素晴らしいです！"),
            sana.explain("それは一人の少女が初めて小説を書き上げるまでの道のりを、ファンタジィ世界を絡めて書かれた、まさしくライトノベルだった"),
            )

## episode
def ep_truthstory(w: World):
    return w.episode("3.ほんとうのものがたり",
            ## NOTE
            sc_master_paper(w),
            sc_master_novel(w),
            sc_decision_publish(w),
            )
