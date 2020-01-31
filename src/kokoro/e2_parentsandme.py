# -*- coding: utf-8 -*-
"""Episode: 7-2.私と両親／こころ
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
def sc_visit_grave(w: World):
    sana, noto = W(w.sana), W(w.noto)
    planting, sidewalk = W(w.planting), W(w.sidewalk)
    return w.scene("墓参り",
            w.comment("沙奈は先生につきそい、知らない誰かの墓参りにやってくる"),
            noto.come("墓地をゆっくりと歩く"),
            sana.come("先生についてやってくる"),
            sana.do("何も言わない先生について歩く"),
            sidewalk.look("石畳が続く"),
            planting.look("脇に植えられた杉や松、桜は綺麗に剪定されている"),
            sana.think("一体誰の墓参りなのか。それすら訊けそうな雰囲気じゃない"),
            _.think("こういう時は黙ったままいるのがベターだった"),
            noto.do("ある墓の前で立ち止まる"),
            sana.do("墓には「$tsuru」とあった"),
            noto.talk("あけましておめでとう"),
            sana.do("先生を一人にして、少し離れておく"),
            noto.do("何か小声で話している"),
            sana.think("$asahiに言われたことを思い出す。大切な友人たちが、一人は病気で、一人は自殺で亡くなったのだ"),
            noto.talk("ありがとう。行こうか"),
            sana.talk("はい"),
            ## NOTE
            ##  ここで親友の死について、ちゃんと説明がある
            camera=w.sana,
            stage=w.on_hiscemetery,
            day=w.in_visitgrave, time=w.at_midmorning,
            )

def sc_nearrestaurant(w: World):
    sana, noto = W(w.sana), W(w.noto)
    exterior = W(w.exterior)
    return w.scene("案内されて洋食屋に向かう路地",
            sana.do("閑静な場所を歩く"),
            sana.talk("どこなんですか？"),
            noto.talk("もうすぐだ"),
            sana.think("駅や大通りから結構離れた場所で、隠れ家的な店なんだろう"),
            noto.talk("そこの角を曲がったところだ"),
            sana.do("見えてきたのは傍目には何の店かよく分からない"),
            exterior.look("レンガ調の壁に深い緑の庇"),
            _.look("ドアにはＯＰＥＮとあるが、営業している雰囲気がない"),
            noto.talk("あれ。一応やってるみたいだね"),
            noto.do("ドアを開けて中に入る"),
            camera=w.sana,
            stage=w.on_street,
            time=w.at_noon,
            )

def sc_restaurant(w: World):
    sana, noto = W(w.sana), W(w.noto)
    hana = W(w.hanamaki)
    return w.scene("先生と洋食屋",
            sana.come("先生に連れられてやってくる"),
            noto.come(),
            hana.be("カウンターの掃除をしている"),
            noto.talk("特別な時に、ここに来るんだよ"),
            hana.talk("あら、先生。来るんじゃないかなって思ってたんですよ"),
            noto.talk("今日は休みかと思ったよ"),
            hana.talk("ああ、メニュー板を出しておかなかったから。いつものでいいですか？"),
            noto.talk("そうだね。頼むよ。彼女も同じで"),
            hana.talk("可愛らしい方ですね。わかりました"),
            noto.talk("あそこに座ろう"),
            sana.do("$notoについて、奥側のテーブル席に座る"),
            sana.do("やってきたのを食べて"),
            sana.talk("これ、素敵です"),
            noto.talk("だろう？"),
            noto.do("嬉しそう"),
            noto.talk("作家と食べ物という観点も面白い"),
            noto.talk("それぞれ普段から食べているものや食に対する考えが出るからね"),
            noto.talk("料理はしないんだったかな？"),
            sana.talk("多少しますよ。でも上手くはないです。外食した方が良いですね"),
            noto.talk("将来大変そうだね"),
            sana.talk("みんなで「料理ができる旦那さん」をもらう予定にしてますから"),
            sana.do("笑う"),
            sana.explain("それから少し親の話をする"),
            noto.talk("素敵な親御さんに育てられたんだね"),
            sana.talk("そうですか？", "確かに色々と迷惑をかけたし、今も時々"),
            noto.talk("どうしても家庭環境というのは人生において大きい"),
            noto.talk("長く見れば少なくとも二十年程度はまず世話になる。それだけ一緒にいて、色々と知った仲だ"),
            noto.talk("結婚して暮らすまでは、一番長く一緒にいる他人かも知れない。それが家族だ"),
            noto.talk("$meの親はね、何も言わなかったが、これだけは言っていたよ。他人に迷惑をかけるな。あと、自分に嘘をつくな、かな"),
            noto.talk("その言葉がずっと呪詛のように残っている"),
            sana.think("色々あったのだな、と思った"),
            stage=w.on_masterrestaurant,
            )

def sc_abouthuman(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("小説の人物描写について",
            w.comment("もう少しうまくまとめること。人物描写とキャラクタの類型について端的であること"),
            sana.explain("食べ終えて、コーヒーを"),
            noto.talk("さっき聞いたけど、ここね、来月潰れるんだ"),
            sana.talk("え？"),
            sana.think("確かに忙しいはずの時間帯に自分たち以外に客は一組だけ"),
            noto.talk("まあ趣味で続けていたらしいからね。これも原価は相当高い"),
            noto.talk("好きなことでも続けるのは大変だ"),
            noto.talk("それは君たちも考えなければいけない問題なんだよ"),
            sana.talk("どういうことですか？"),
            noto.talk("小説というのは大衆向けの文化のような認識があると思う。けどね、それは間違いだよ"),
            _.talk("小説というのはどこまでもマイナな趣味なんだ"),
            sana.talk("それは分かる人だけ分かればいい、という態度でしょうか"),
            noto.talk("折角だから小説のキャラクタについて話そう"),
            _.talk("基本的に作中の、特に主人公になる人物は読者の共感を呼びやすい方が良いとされる"),
            _.talk("これはより広く、様々な人に読んでもらいたい、という態度だ。分かるかい？"),
            sana.do("頷く"),
            noto.talk("だが誰もが理解できる、そういう人間を描くというのは、つまらない物語を書くことと同義だ"),
            sana.talk("どうしてですか？　分かりやすい主人公であっても面白いものはあります"),
            noto.talk("文学に限らないが、人が興味を持つのは、往々にして自分ではなく他人だ"),
            _.talk("それも目を引く他人。つまり変わり者だよ"),
            _.talk("理解できないからこそ、それを知りたいと願う"),
            _.talk("分かりきったものを人は読みたいとは思わない"),
            _.talk("変人が出てくるからこそ読みたい、という心理が強く働く"),
            sana.talk("なら何の魅力もない人物を主人公にして、誰もが持つ葛藤を描いても、それは小説にはならないと？"),
            noto.talk("小説だよ"),
            sana.talk("なら"),
            noto.talk("でもそれはごく少数の為のものだ。自分の悩みなど見たくはない"),
            _.talk("小説家になろうと呼ばれる傾倒の昨今のライトノベルがあるそうだね"),
            _.talk("そこには葛藤はほとんどなく、苦しみや成長の過程もないと聞く"),
            _.talk("実際$meが目を通したもの全てがそうだった訳ではないが、表面的な人間の描き方で、楽しむことを前提に書かれたものが多かった"),
            _.talk("これはゲームだ。と感じたよ"),
            _.talk("多くが類型的だ。でもそれが安心感だ"),
            _.talk("新しいものを求めない心理"),
            _.talk("これを君たちが売っている。そういう自覚があるか、という話なんだよ"),
            sana.do("黙り込んでしまう"),
            noto.talk("一部の人だけ分かればいい。そういう作品はこの店と同じでね、やがて潰れてしまう"),
            _.talk("なら大衆に迎合した、誰もが理解できて、現実離れした世界で、ただ刺激だけを享受するような、そんなゲームのような小説ばかりを売っていいのか？"),
            _.talk("という問いだ"),
            _.talk("ビジネスだから売らなければいけない。その建前は分かる"),
            _.talk("しかし、突飛な、刺激物というのは人間慣れてしまうものなんだ"),
            _.talk("本質的に十年百年と読みつがれるものは、人間そのものの真理に手を伸ばそうとしている"),
            _.talk("それを文学が背負ってきたが、売れないから、一部の人だけ、コアだけを囲い込んで、広げようとはしなかった。いや、できなかったのだ"),
            _.talk("君たちが、出版業界が、努力を欠いた証拠だ"),
            _.talk("どんな小説でも、小説は小説だ。読む人はいる"),
            _.talk("だが何を提供し、どう感じてもらうのか。何を喜んでもらうのか"),
            _.talk("目先の利益を追求して、大事なことを見落としているんじゃないだろうか"),
            sana.think("何も言い返せなかった"),
            _.think("少なくとも、今の編集長の方針は数字だからだ"),
            sana.talk("ならどうすれば、人間が描けますか？"),
            noto.talk("自分の内面と向き合うことだ。本物の人間は自分の内側にいる"),
            noto.talk("よく周囲を観察し、自分の内面に取り込み、考えなさい"),
            noto.talk("君はそういう目を持っている"),
            )

## episode
def ep_parents_and_me(w: World):
    return w.episode("2.中　私と両親",
            ## NOTE
            sc_visit_grave(w),
            sc_nearrestaurant(w),
            sc_restaurant(w),
            sc_abouthuman(w),
            )
