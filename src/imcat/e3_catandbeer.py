# -*- coding: utf-8 -*-
"""Episode: 2-3.猫とビール／吾輩は猫である
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
def sc_introduction(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("自己紹介",
            sana.be("立っている"),
            noto.be("炬燵に入って待っている"),
            sana.talk("えっと、オーディションなんですね？　$me一人ですが"),
            noto.talk("$fukayaさんも最初にやったよ。彼女はなんでも応えてくれて、実に素晴らしい編集だった"),
            _.talk("作家と編集はお互いのことをよく知る必要がある、そうは思わないかね？"),
            sana.talk("そういわれれば、そうですけど"),
            noto.talk("では始めてくれ。まずは自己紹介からお願いしたい"),
            sana.talk("は、はい"),
            sana.talk("$full_sanaです。歳は二十五になりました"),
            noto.talk("なぜ編集の仕事を？"),
            sana.talk("本が、好きだったから……です"),
            _.think("$on_hercompanyの面接の時を思い出す。あの時は引き抜いてくれた$fukayaが人事部の人と一緒だった"),
            _.talk("中学の頃はただの本好きな少女でした。高校になってから作家を目指したこともあります"),
            _.talk("でもそれは挫折しました"),
            _.talk("大学時代は文芸部に所属こそしましたが、それでも書くよりは読んだり、作ったりするのを手伝う方が楽しいと感じて"),
            _.think("話しているうちに自分が編集に感じた魅力を思い出す"),
            w.comment("$sanaのことを語る。ここで彼女＝主人公がただ普通に会社に就職したりした訳ではない風なことを体感"),
            noto.talk("ありがとう。素直な人なんだ、$sana君は。うん。悪くない"),
            sana.talk("ありがとうございます"),
            ## NOTE
            ##  オーディションでは最初の、やっと「小説講座」らしいもの登場させる
            camera=w.sana,
            stage=w.on_hisapart_int,
            )

def sc_aboutnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("小説とは",
            noto.talk("では、そんな君にとって小説とは何かね？"),
            sana.think("どう答えようと迷う"),
            noto.talk("おそらく人間の数だけその解釈というのはある。で、君はなんと考えている？"),
            sana.talk("作家の人生です"),
            noto.talk("ふーん。その心は？"),
            sana.talk("小説は基本的に文字、文章だけで物語を紡ぐものです。そこには必然、その作者が何を考え、普段何を見て、どう感じているかが書かれます"),
            _.talk("それはその作家の人生といってもいい"),
            _.talk("物語はフィクションですが、そこに描かれたものは作者にとって真実なんです"),
            _.talk("だからこそ$meは小説を読むと同時に作者の人生を、その哲学を感じます"),
            noto.do("じっと腕組みをして聞いている"),
            sana.talk("じゃあ先生にとっての小説って何なんですか？"),
            noto.talk("何だろうね"),
            _.talk("それこそ十歳の頃からの付き合いだからもう四十年ほどになる。空気や水、そういってもいい"),
            _.talk("身の回りにあって、普段摂取しているのに、その実、何なのかはよく分からない"),
            _.talk("小説とは何か？　と問い続けることが、$meにとっての小説かも知れない"),
            w.eventStart("能登川にとっての小説"),
            ## NOTE
            ##  ここで「小説」が何か、についての「作者」と「ただの編集者」の認識の違いを明らかにする
            ##  また沙奈がどう思って取り組んでいるか、その夢を見せておく
            )


def sc_1stmission(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("最初の仕事",
            noto.talk("そうだな。まあ、君が代わりということは理解したが"),
            noto.talk("ちょっと買い物を頼まれてくれないか。ビールをきらしてしまってね"),
            noto.talk("あとおつまみも適当に見繕って。頼むよ"),
            sana.talk("はい、わかりました"),
            sana.think("諦めて今は先生の機嫌取りをしようと決意する"),
            sana.talk("$meが出かけている間にせめてプロットだけでも用意しておいて下さいよ。頼みましたからね"),
            noto.talk("またそんな簡単にプロットとか言うんだ、君ら編集は。あのね、プロットと一口に言っても……"),
            sana.talk("講義は後で聞きます。とにかく原稿お願いしますよ"),
            noto.talk("プロットから原稿に昇格しているじゃないか……"),
            sana.go("出かけてしまう"),
            )

def sc_gotoconveni(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("お使い",
            sana.be("近所のコンビニから戻っている"),
            sana.think("何故ビールを買いに出かけているのかと疑問"),
            sana.do("スマホとメモで先生の情報を確かめる"),
            sana.think("先輩のメモには癖が強いし、好き嫌いが激しい。食べ物も、言動も"),
            _.think("年齢は五十前だが、十代の子どものような言動が頻繁に見られる"),
            _.think("独身。冗談でセクハラ発言がある"),
            _.think("更に注意書きがある"),
            sana.talk("え？"),
            _.explain("そこにはよく編集の前から逃げ出すから要注意、と書かれていた"),
            sana.think("え？　ちょっと待ってよ"),
            sana.go("急いで戻る"),
            stage=w.on_street,
            ## NOTE
            ##  ここで改めて先生のメモを見て「よく脱獄する」と
            )

def sc_endmission(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("買ってきました",
            sana.come("買い物袋と共に戻ってくる"),
            sana.talk("先生買ってきました、よ？"),
            sana.do("足元に猫がじゃれつくだけ"),
            sana.do("先生は不在"),
            sana.talk("やられた！", "やっぱり逃げられたか！"),
            sana.go("慌てて外に探しに出る"),
            stage=w.on_hisapart,
            time=w.at_noon.elapsedMin(30),
            )

## episode
def ep_cat_and_beer(w: World):
    return w.episode("3.猫とビール",
            ## NOTE
            sc_introduction(w),
            sc_aboutnovel(w),
            sc_1stmission(w),
            sc_gotoconveni(w),
            sc_endmission(w),
            )
