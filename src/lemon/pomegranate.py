# -*- coding: utf-8 -*-
"""Episode: 4-4.柘榴／檸檬
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
def sc_comemaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, yone = W(w.nirasaki), W(w.king), W(w.yonezawa)
    return w.scene("先生の来訪",
            sana.be("会議をしている"),
            king.be("座っている"),
            nira.be("渋い顔"),
            yone.be("資料を読み込んでいる"),
            sana.think("もう完全に先生の線は消えた。自分の作品ではやはり誤魔化せなかった"),
            _.think("先生に言われたように、自分の作品では全く短編小説になっていなかったのだ。やはり実際に雑誌に掲載されるレベルになると何か違う"),
            noto.come("ドアを開けて入ってくる"),
            noto.talk("こちらでよかったかな？"),
            sana.talk("先生！？"),
            _.think("どうして、という思い"),
            noto.talk("これを持ってきたんだ。確か今日が締め切りだったろう？"),
            sana.talk("先生、それはもう……"),
            noto.talk("あなたが新しい編集長かね。こちら、依頼された原稿だ。受け取ってくれますかな？"),
            king.do("立ち上がり、受け取る"),
            king.talk("先生の作品はフラワー三部作、全て読ませていただいております"),
            noto.talk("ありがとう"),
            sana.do("その原稿のタイトルは『$master_shortnovel1』とある"),
            sana.talk("先生……"),
            noto.talk("後は宜しく頼むよ。君が$meの担当なんだろう？"),
            noto.go(),
            sana.think("先生が新しく書き上げたライトノベル短編小説。何としても通さなければならない"),
            king.talk("いやあ、びっくりしたね。しかし、何だ"),
            _.talk("決定しておいて、今更これをねじ込む訳にもいかんだろう。そう思うだろ？"),
            sana.do("誰も答えない"),
            nira.do("黙ったまま"),
            sana.talk("あの"),
            king.talk("何だ？"),
            sana.talk("今一度、今回の短編連載企画の趣旨について思い出してみませんか？"),
            _.talk("最近は作品を出せていない、あるいはある程度知名度があるが新シリーズが奮わない作家に名前を覚えてもらう場を与えよう、そういうことでした"),
            _.talk("しかし選ばれた作者はどれも現在出しているシリーズが順調で、新シリーズの立ち上げ準備中の方が一人だけです"),
            _.talk("編集長の言われるように売上も大事ですが、短編そのものは既存シリーズのスピンオフでもなければ売上に直結することはあまりありません"),
            _.talk("今までのデータからもそうですよね？"),
            yone.talk("そうだね。ただ全く影響していないとも言えないし、今回揃えた作者先生方は爆発的な人気や知名度がある訳ではない"),
            _.talk("そういう観点から見れば、名前を覚えてもらいたい作家先生たちでもある"),
            king.talk("ということらしいがな。それで何が言いたいんだ？"),
            sana.talk("知名度もそうですが、再起をかけるという企画意図に一番相応しいのが$noto先生ではないでしょうか？"),
            _.talk("詳しい経緯は知りません。けど、文芸畑で培った技術や文章で新しい風を吹かせてくれる。そういう期待を読者も持つのではないでしょうか？"),
            sana.do("みんな黙っている"),
            sana.talk("$meは$noto先生の作品を目玉の一本にすることを提案します"),
            king.do("考え込む"),
            sana.talk("反論するなら、まず作品を、です"),
            sana.go("慌てて原稿をコピーしに出ていく"),
            camera=w.sana,
            stage=w.on_meetingroom_int,
            day=w.in_meetingshortnovel, time=w.at_afternoon,
            )

def sc_masternovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, yone = W(w.nirasaki), W(w.king), W(w.yonezawa)
    return w.scene("先生の小説",
            sana.be("みんな小説を読んでいる"),
            sana.explain("小説は予想に反して時代劇ファンタジィだった"),
            _.explain("最後まで異世界ものを書くのは渋っていた先生が出した回答は、今静かに流行しつつある和風ファンタジィだ"),
            yone.talk("これ、面白いですね。短編シリーズの第一作としても充分な出来ですよ"),
            nira.talk("でも鬼滅に似てませんか？"),
            yone.talk("あれは鬼退治だろう？　これは鬼が屍霊を斬るんだから違うだろう"),
            nira.talk("似たような作品ありますよ。そもそもうちの読者がこれを喜びますかね？"),
            sana.talk("そこです"),
            nira.do("何だ？　という顔"),
            sana.talk("思い出して下さい。この短編競作企画のもう一つの趣旨を"),
            _.think("それは新規読者の獲得だった"),
            _.explain("新しい読者への誘発剤となるような作品を揃えたいという希望があったのだ"),
            king.talk("確かに作品は面白い。個人的には今回揃えた中では一番読み応えがあった"),
            _.talk("だが、今はその読み応えが不要な時代なんだ。読みやすさ、キャラや設定の勢い、そういったものが好まれる"),
            _.talk("しかしこれはどうだ。確かに従来の$noto作品に比べればいくぶん優しい語彙ではある"),
            _.talk("けれどもこれを十代の読者が読めると思うか？"),
            sana.talk("そんなの、分かりませんよ"),
            king.talk("うちの息子など、漫画ばかりだ。それもスマホでな"),
            _.talk("教科書すら読むのが苦痛といっている奴らにどう読めというんだ？"),
            sana.talk("そういう顧客は最初からターゲットには入って"),
            king.talk("新規顧客とは、そういう層も含まれるんじゃないのか？　普段読まない、小説など買わない層だ"),
            _.talk("そこへの求心力があるかと聞いてるんだよ、$meは！"),
            sana.think("どうしても先生を掲載しないという強い意地を感じたが、言い返すだけの言葉がない"),
            yone.talk("読みますよ、これ"),
            king.talk("何だと？"),
            yone.talk("特に女性読者がつくでしょう。刀剣ブームもあり、現在若い女性の意識は歴史に向かっている"),
            _.talk("鬼滅のブームもそれに倣っています。この文体と表現力、特に心理描写の細かやかにアクション描写の力強さは、"),
            _.talk("今の若いラノベ作家さんたちじゃまだまだ太刀打ちできません"),
            _.talk("これこそ求めていた作品なんじゃないですか？"),
            sana.think("心の中で$yonezawaさんに感謝した"),
            king.talk("わかった。なら、この作品もいれて、今一度編成会議をやり直そう。それでいいな？"),
            )

def sc_formallyeditor(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("正式に担当に",
            sana.come("その足で急いでやってくる"),
            sana.talk("先生！"),
            noto.talk("騒がしいね"),
            sana.talk("決まったんですよ！"),
            noto.talk("そうか"),
            sana.talk("嬉しそうじゃないですね。どうしてですか？"),
            noto.talk("いや、嬉しいよ。けど、その陰で誰かは割を食ったのだろう？"),
            _.talk("作家は常に誰かの犠牲の上に立って作品を発表している。そういう自覚は持っておくものだ"),
            _.talk("だからこそハンパなものは出せない"),
            sana.think("自分の書いたものがどうだったのか、と問われているよう"),
            noto.talk("ああ、それから、君の小説ね、赤いれておいたから、あとで読み返してみて"),
            sana.talk("え？"),
            sana.do("ゲラになって帰ってきて、苦笑"),
            sana.talk("分かりました"),
            stage=w.on_hisapart,
            time=w.at_evening,
            )

## episode
def ep_pomegranate(w: World):
    return w.episode("4.柘榴",
            ## NOTE
            sc_comemaster(w),
            sc_masternovel(w),
            sc_formallyeditor(w),
            )
