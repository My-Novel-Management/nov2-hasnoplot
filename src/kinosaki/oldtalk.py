# -*- coding: utf-8 -*-
"""Episode: 6-2.昔の話にて／城の崎にて
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
def sc_main2(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("2.昔の話にて",
            noto.talk("彼女から少し話を聞いたようだね",
                "折角だからこの機会に話しておこうか", "そういえば$meのデビュー作は読んだかね？"),
            sana.talk("はい。先日読み終えました", "今は書店で取り扱ってなくて、先輩から借りたんですが"),
            noto.talk("本はずっと本屋に並んでいるものだと思っていた",
                "でもそれは幻想なんだよね", "本の仕事に関わればわかる", "よっぽどの名作、人気作家の人気作でもない限りは、",
                "本屋の棚から消えて、出版社の倉庫に眠ることになる", "古本屋にでも流れればまだ延命できている、というのは悲しいことだ"),
            noto.talk("これは$meの学生時代の話だ", "まだ作家になる前の話",
                "$meのデビューは二十歳の時だからもうかれこれ三十年以上前になるんだね"),
            sana.explain("先生の学生時代の思い出話が始まる"),
            noto.talk("彼と彼女と$meの三人は常に教室でも一緒で、休み時間には彼女が本を読む机に集まり、昨夜読んだ本について議論を交わしたりしていたよ"),
            noto.talk("彼女は$meらの最初の読者だった",
                "彼女に読んでもらい、どちらの作品が彼女を喜ばせるか、それを競い合った"),
            noto.talk("やがて彼がプロの小説家になると言い出して、今度はそれがどちらが先に作家になれるか、という競争に発展した"),
            noto.talk("$meは昔から意外と理論派でね、当時は今のようにとにかく公募ということもなかったから、知人を当たって持ち込みするのが主だった",
                "作家先生に弟子入りして、紹介してもらうというのもあった", "まあどれも細い糸だったけれども、それを掴んだ奴は大きな成功を手にできた"),
            noto.talk("結果は$meが先にデビューすることになった"),
            ## NOTE
            ##  - 出版点数は約80000／年
            ##  - 返品率は目標２割、実質４割
            ##  - コミックに限ると1997年から売上半額
            ##  - 近年は電子出版が伸びてきている
            ##  - 書店は1冊あたり２割の取り分があり、それが売上
            )

## episode
def ep_oldtalk(w: World):
    return w.episode("2.昔の話にて",
            ## NOTE
            sc_main2(w),
            )
