# -*- coding: utf-8 -*-
"""Episode: 10-4.エピローグ／銀河鉄道の夜
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
def sc_hurrygirl(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("急げ編集",
            w.comment("１話の冒頭オマージュ"),
            sana.be("着替えている"),
            sana.explain("徹夜で$geroの相手をしていて遅刻しそうに"),
            gero.talk("だからエンディングまで長いよって言ったんだがね"),
            sana.talk("長いっていっても本当に明け方まで掛かると思わなかったから！"),
            _.explain("最近流行っている悪役令嬢ものの勉強と、乙女ゲームを教えてもらっていたのだ"),
            azu.come("小さな弁当を持ってやってくる"),
            azu.talk("会社で食べてね"),
            sana.have("弁当を受け取る"),
            sana.do("着替え終わり"),
            sana.talk("それじゃ、今夜は焼き肉奢るからね！　いってきます！"),
            gero.talk("おう、期待しないで待っとく"),
            azu.talk("気をつけてね"),
            sana.go("出かける"),
            camera=w.sana,
            stage=w.on_herhouse_int,
            day=w.in_getfirstbook, time=w.at_midmorning,
            )

def sc_runninggirl(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("走れ編集",
            sana.do("走っている"),
            _.do("横断歩道で駆け足"),
            stage=w.on_street,
            )

def sc_firstbook(w: World):
    sana, noto = W(w.sana), W(w.noto)
    king, nira, tsuchi = W(w.king), W(w.nirasaki), W(w.tsuchiura)
    return w.scene("先生の本",
            w.comment("初めての$sana担当での先生の製本された本を手にして"),
            ## NOTE
            ##  文芸部の面々を出しておく
            ##  深谷さん出産情報も追記
            ##  放火犯の情報も
            sana.come("出社してくる"),
            sana.look("嬉しそう"),
            _.think("今朝もらった$fukaya出産の連絡を思い出し", "#深谷出産"),
            nira.be("パソコンに向かっている"),
            tsuchi.be("椅子を並べて寝ている"),
            king.be("座ってコーヒーを飲んでいる"),
            nira.do("ちらっと見て"),
            sana.do("自分のデスクに製本された先生の本を見つける"),
            _.talk("え？　これって"),
            nira.talk("印刷所の何とかってやつが朝一で持ってきてくれたよ"),
            sana.talk("ありがとうございます"),
            nira.talk("$meは何もしてねえよ"),
            _.talk("それより$noseの奴、出頭したそうだ。よかった"),
            sana.talk("そうなんですか。ほっとしました"),
            _.think("罪を償って、今度こそ本当に自分の作品を書いてもらいたい"),
            sana.do("本の出来を確かめつつ"),
            sana.do("編集長のところに行き"),
            sana.talk("先生のところに持っていってもいいですか？"),
            king.talk("余計な修正入れられないようにしてくれ", "これ以上あれこれでコストが掛かっても困るんだよ"),
            sana.talk("分かってますよー"),
            sana.talk("じゃあ借りていきますねー"),
            sana.go("鞄を手に、社用車の鍵を手に、出かける"),
            camera=w.sana,
            stage=w.on_heroffice,
            )

def sc_gotomaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生の許へ",
            w.comment("見本を手に先生の家に急ぐ"),
            sana.do("車に乗り込み、シートベルトなど"),
            sana.think("初めての本です。自分が担当した初めての、そして先生の初めてのライトノベル"),
            sana.do("都内の道路を軽快に走る"),
            sana.do("スマホに何か通知するが、出られないので無視する"),
            sana.explain("しかしこれが次の悲劇の幕開けだった"),
            sana.explain("なんとスマホを手に入れた先生が、勝手にツイイッターを始めてしまったのだ"),
            sana.explain("だがそれで問題になるのはまた別の話。後日のことであった"),
            stage=w.on_car_int,
            )

def sc_nextbook(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("次の本について",
            w.comment("先生から新しいシリーズの提示があり、それについて取材旅行費用がこれだけかかると言われて"),
            w.comment("彼女の編集人生はまだ始まったばかりだ"),
            sana.talk("先生！"),
            _.come("元気よくやってくる"),
            sana.talk("まだ寝てるんですか？"),
            sana.do("寝室を覗くと、ノートパソコンを持ってきて、何とか原稿を書こうとしている"),
            sana.talk("言って下さい。教えますって"),
            noto.talk("全く、どうしてこう、機械というのは面倒なんだろう", "人間に便利を与えるはずのものが不便とはどういうことなんだ"),
            sana.talk("それより先生、これ"),
            _.do("鞄から本を取り出す"),
            noto.talk("ああ、できたのか"),
            noto.do("受け取り、嬉しそう"),
            noto.talk("この瞬間が何よりも緊張するよ"),
            sana.talk("書店に並んだ時よりですか？"),
            noto.talk("後戻りができない、という感覚が一番強くなる",
                "本当にこれを出してしまっていいのだろうか、という自分への不安、そして読者の期待に応えられるだろうかという不安",
                "小説なんてものは常に不安との戦いだ"),
            sana.think("先生の意外な弱音に、かわいさを感じてしまう"),
            sana.talk("先生"),
            sana.do("写真を撮る"),
            sana.talk("紹介記事に使います"),
            noto.talk("やめてくれないか。流石に素顔は恥ずかしいよ"),
            sana.talk("何言ってるんですか。散々当時雑誌に写真載ったじゃないですか"),
            noto.talk("あれは若気の至りというんだ"),
            sana.talk("意外とよく撮れたと思いますよ？"),
            noto.do("見て、顔が歪む"),
            noto.talk("$sana君！　君ってやつは！"),
            sana.talk("あーん、許してくださいよー"),
            sana.explain("こうして先生の作品は来月無事に発売される運びとなりました"),
            _.explain("こうして$Sの壮絶な$full_notoの担当編集人生は幕を開けたのである"),
            stage=w.on_hisnewapart,
            )

## episode
def ep_epilogue(w: World):
    return w.episode("4.エピローグ",
            ## NOTE
            sc_hurrygirl(w),
            sc_runninggirl(w),
            sc_firstbook(w),
            sc_gotomaster(w),
            sc_nextbook(w),
            )
