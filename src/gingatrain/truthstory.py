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
    return w.scene("先生の原稿",
            w.comment("先生から書き終えたばかりの生原稿を受け取り、目を通す"),
            noto.do("原稿を$CSに渡す"),
            noto.talk("だって君は、$meの担当編集だろう？"),
            sana.talk("先生……"),
            sana.do("先生から原稿を受け取る"),
            noto.talk("色々とバイト君には無茶を言った"),
            sana.talk("あいつ……何も言ってなかったのに"),
            noto.talk("ちゃんと君の教えを守ってたよ。先生の言うことには従えってね"),
            sana.talk("あ……"),
            sana.talk("持ってこられたということは、これって……"),
            noto.talk("ああ。完成原稿だ。書き上げたよ……十年ぶりの新作長編だ"),
            sana.think("緊張してくる"),
            camera=w.sana,
            stage=w.on_hisnewapart,
            day=w.in_finishbook, time=w.at_afternoon,
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
            sc_decision_publish(w),
            )
