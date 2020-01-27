# -*- coding: utf-8 -*-
"""Episode: 7-4.先生と遺書／こころ
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
def sc_manymail(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("ポストの郵便物",
            sana.come("歩いて先生のアパートに戻ってくる"),
            noto.come(),
            sana.do("大量に突っ込まれた新聞などを見て、溜息"),
            sana.talk("先生。せめて家の中に入れておいて下さい。そのままにしておくと空き巣とかの標的になるんですからね"),
            noto.talk("もっと頻繁に君が来てくれたら、その心配をしなくて済む。$fukayaさんはね"),
            sana.talk("はいはい。分かりましたよ"),
            sana.think("本当に手の掛かる先生だ"),
            noto.go("中に入る"),
            sana.go("先生に続く"),
            camera=w.sana,
            stage=w.on_hisapart_ext,
            day=w.in_visitgrave
            )

def sc_friendwill(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru = W(w.tsuru)
    willpaper = W(w.willpaper)
    return w.scene("友人の遺書",
            w.comment("先生から友人の遺書を見せられ、預かっておいてもらいたいと言われる"),
            noto.be("くつろいでテーブルの前に座っている"),
            sana.come("お茶を入れて持ってきて"),
            sana.talk("とにかく原稿、頼みますからね"),
            noto.talk("大丈夫。$meは締切を落としたことはないんだ"),
            sana.think("何度も$fukayaが頭を抱えていたことを思い出す"),
            sana.talk("はい"),
            noto.talk("ともかく、今日は付き合ってくれてありがとう"),
            _.talk("いつかはちゃんと話すが、しばらくは作品に集中させてほしい"),
            sana.talk("分かってますよ。余計な詮索はしません"),
            noto.talk("意外なことを言うものだ。君なら遠慮せずにずかずかと訊いてくると思った"),
            sana.talk("なんですか、それは。$meだって分別くらいあります"),
            noto.talk("そうだ。少し待っててくれないか"),
            noto.go("立ち上がって行ってしまう"),
            sana.talk("はい？"),
            sana.do("その間に本棚の整理をしつつ、どんな本が並ぶか見ている"),
            sana.do("ライトノベルではなくやはり古典や文学作品が多い"),
            sana.do("と、隠されるように入っていた大学ノートを見つける"),
            sana.do("$Sはそれを開いて、先生の創作ノートだと分かった"),
            sana.have("そのノートを手にしていたが、先生の声が聞こえたので、慌てて鞄にしまい込む", w.masternote),
            noto.come("封筒を手に戻ってきて"),
            noto.talk("$sana君。これを"),
            noto.do("古い封筒を渡す", w.willpaper),
            sana.have("封筒を受け取る", w.willpaper),
            sana.explain("中を見ると、それは遺書だった。さっき墓参りした$tsuruという人のものだ"),
            sana.talk("中を読んでも？"),
            noto.talk("最初からそのつもりだ。読んでくれ"),
            noto.talk("彼も作家を目指していた。けれど、自殺した。自らその将来を断ったんだ"),
            sana.do("黙って遺書に目を通す"),
            willpaper.look("端が曲がって斜めに書かれた独特の文字"),
            sana.think("字が歪んで、読みづらい、と感じた。先生とは全く違う文字だ"),
            tsuru.voice("$meはこの夏、君から何度か手紙を受け取った。作家になる、それも東京で作家になるというのはこういうことかと忸怩たる思いだった"),
            sana.explain("そこに書かれていたのは、作家になれなかった友人の悔恨や積年の情だった"),
            tsuru.voice("君から何度か謝罪の言葉を貰ったが、何も謝ってもらうことなどない"),
            _.voice("そもそもこれは才能の差なのだ。君は作家として、生きてくれればいい"),
            _.voice("しかし人生とは皮肉なもので、なりたいと願ったものほど現実にそれを手にするには遠く、才能なんかないと悔やんでいた君が作家になるなんてね"),
            _.voice("この世の中は、いつも$meの思うがままとは程遠い姿へと変容していく"),
            _.voice("人生で一番楽しかったのは、君と$komiの三人で小説について議論をしていたあの制服の時代だ"),
            _.voice("あれほど色鮮やかで、笑顔と興奮に溢れた時があったろうか"),
            _.voice("日本ではやたらと学生時代を中心とした書物が流行っているそうだが、これも分からないでもない"),
            _.voice("人生で一番の輝かしい時代はあの頃だからだ"),
            sana.think("それは一つの小説のようでもあった"),
            _.think("便箋で十枚にも渡る遺書の大半は、学生時代の思い出に費やされていた"),
            tsuru.voice("走馬灯、というものがあるのを聞いたことがあるだろう"),
            _.voice("こうして遺書を書きながらも、$meはそれをまざまざと見ているよ"),
            _.voice("どれも楽しい思い出ばかりだ"),
            _.voice("こんなにも鮮やかで、温かくて、大切なものを心の中に持っていたんだと確認できたよ"),
            _.voice("あっちで彼女に会ったら、教えてやらなきゃな"),
            _.voice("こうしてわざわざ書いておくのは、これが自分自身で選んだ結末だということを証明するためだ"),
            _.voice("人は、いや、$meは何かを証明する為に常に書き続けたのかも知れない"),
            _.voice("$meを殺したやつの名をここに書き残す"),
            _.voice("$notoよ。お前にはそれを知っておいてもらいたい"),
            _.voice("$meを殺したのは「絶望」だ"),
            _.voice("これを記憶しておけ。$meはこんな風にしか生きられない男だったのだと"),
            w.comment("『記憶して下さい。私はこんな風に生きて来たのです』こころより"),
            sana.explain("そこには「絶望が自分を殺した」と書かれていた"),
            sana.do("読み終えて、溜息をつく"),
            willpaper.look("最後にはわざわざ血の拇印が押されていた"),
            sana.talk("何故これを$meに？"),
            noto.talk("$fukayaさんにも見せた。$meを担当する人には、どうしても見せておかなければならない"),
            _.talk("読んで分かったろう？"),
            noto.talk("彼は$meが殺したようなものなんだよ"),
            stage=w.on_hisapart_int,
            )

def sc_disturbing(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("不穏",
            sana.be("一人、自宅への路地を歩いている"),
            sana.think("先生の告白と遺書について考えていた"),
            sana.think("ふと誰かの気配を感じて振り返る"),
            sana.think("誰もいなくて安堵する"),
            sana.think("しかし遺書には先生が殺したとは書いていなかったのに、それでも先生は自分が殺したと言った"),
            _.think("それだけの何を、親友に対してしたのだろうか"),
            sana.do("スマホに着信があり、$azuminoから"),
            sana.explain("それは今日発表の一次選考で落選していた、という報告だった"),
            sana.talk("仕方ない。何か買って帰るかな"),
            sana.think("友達を殺した、と言えるような何か。そんなこと、とても考えられないでいるけれど、一方で、彼女は編集である自分に対して何か思うところがあるんじゃないだろうか、と不安になった"),
            stage=w.on_street,
            time=w.at_night,
            )

## episode
def ep_master_and_letter(w: World):
    return w.episode("4.続　先生と遺書",
            ## NOTE
            sc_manymail(w),
            sc_friendwill(w),
            sc_disturbing(w),
            )
