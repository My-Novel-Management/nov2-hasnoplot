# -*- coding: utf-8 -*-
"""Block: 小説について
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer
_ = W.getWho()


## blocks
def bk_aboutnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    manupaper = W(w.manupaper)
    return (
            w.block("プロットとは",
                noto.talk("プロットと言葉を君たち編集は安易に使うけれど、それが一体どういうものを差すのか理解しているかね？"),
                sana.talk("お話の筋みたいなものですよね？　どんな話か確認したい時にプロットを、と言います"),
                noto.talk("筋が知りたいならあらすじを尋ねれば良いじゃないか。プロットはあらすじのことか？"),
                sana.talk("あらすじだけじゃなくて、メインキャラクターのこととか、世界観とか、そういったものもあれば嬉しいです"),
                noto.talk("ならそれをまとめたものがプロットか？"),
                sana.talk("そんな感じだと思いますけど"),
                noto.talk("何の為にそれが必要になるのかね？"),
                sana.talk("短編ならまだしも長編は初稿が上がるまでに時間がかかります。取材費用とかもあるし、会社の方にも出版枠があります"),
                _.talk("編集会議などでどの作品をどう打っていくのか、ラインナップするのか、そういった時にプロットがあると話がしやすいです"),
                _.talk("だからまずはプロットを、と言うみたいですけど"),
                noto.talk("つまり、企画書が欲しいという訳だね？"),
                sana.talk("そうですね。ただ企画書だと世界設定とかしか書かれてなかったり、そもそもこういう話が書きたいです、みたいな宣言文だったりして、"),
                _.talk("なかなか企画会議や編集会議に持っていけないものだったりするので、できればお話の雰囲気くらいはつかめるものが欲しいんです"),
                noto.talk("それは編集が欲しいプロットだ"),
                _.talk("しかし作家にとってプロットというのは異なる"),
                _.talk("作家が欲しいのは物語の指針となる、あるいは設計図となるプロットだ"),
                noto.talk("どんな出来事があり、どんな展開になっていくのか。そういったことを全く何のメモもなしに書くのは心もとない"),
                _.talk("当然小説には行き先を決めずに書くという手法もあるし、純文学などはこういった模索しながらというのも多いだろう"),
                _.talk("だがミステリだと逆にトリックから逆算して作ることになるからプロットが重要になる"),
                noto.talk("ひとくちにプロットと言っても、一体誰が何の目的で使うのかということで必要とされる項目も内容も規模も違ってくる"),
                noto.talk("しかし何でもかんでもプロットと言ってしまうから間違いが起こる"),
                noto.talk("言葉を使う職業をしておきながら、その意味するところが多岐に渡るのにプロットはありますか？　というのはいかがなものかと言っているのだ"),
                ),
            w.block("短編と長編の違い",
                noto.talk("確かに、初心者は短編の方が枚数も少なくて書きやすいと考えがちだけれど、",
                    "実際に書いてみると長編のような余裕もなく、書きながら考えているとすぐに枚数が尽きてしまう",
                    "それはね、$sana君、短編と長編が全然異なるスタイルを求められているからなんだ"),
                sana.think("$Sはメモ帳を取り出して新しいページを開きつつ、先生の話に耳を傾ける"),
                noto.talk("短編と長編の、一番の違いは何だろうか"),
                sana.talk("文字数、でしょうかね"),
                _.think("実際読む時にその程度しか意識したことはなかった"),
                noto.talk("まあ、そう答えるだろうと思ったよ"),
                noto.do("そう言って微笑すると、先生は机の上に原稿用紙の新しいページを広げ、そこに何か書き込む", w.manupaper),
                sana.talk("それは何ですか？"),
                manupaper.look("二つの丸囲いがあり、その中にそれぞれ左側は大小いくつもの丸が飛び出すように書いてあったが、"),
                _.look("右側は三つの小さな丸が円に収まるように書かれている"),
                noto.talk("長編はその中にいくつものテーマやサブストーリーを持っている",
                    "この大小いくつもの丸囲いがそれだ", "&"),
                _.talk("スケールの大きいものになると当然一冊の中では問題は解決されず、複数巻に渡りそれを扱うということになる",
                    "ここまでは分かるね？"),
                sana.talk("はい"),
                noto.talk("対して短編だが、", "&"),
                _.talk("これは特殊な場合を除き、その作品内で問題は解決しておかなければならない", "&"),
                _.talk("言い方を変えると短編は箱庭なんだよ", "それもすごく小さな箱に造られている", "&"),
                _.talk("短編の場合その小さな箱の中で如何に世界やテーマを表現するかという、いわば作家同士の技巧の勝負の場とも言える訳だ"),
                sana.think("短編は難しい、と作家からよく言われると$fukayaは言っていた",
                    "その感覚がいまいち分からなかったのだが、技巧の勝負と言われて初めて腑に落ちた"),
                noto.talk("けれど長編の場合、これは箱庭ではない。もっと広大な、言い換えるならサグラダファミリアだろう", "&"),
                _.talk("構想はあってもその全容を見るのはいつになるか分からない", "連載作品ともなれば書いている本人ですらいつ終わりに到達できるだろうと不安になる", "&"),
                _.talk("短編なら一度書き上げてから何度も推敲を重ねてどんどん無駄を省いて削っていくことで作品を磨くのだが、",
                    "長編ではそういったことは難しい、というか、規模によっては不可能だ",
                    "そういうところからも、作家によって短編向き、長編向きという資質があるのは理解してくれると思う"),
                sana.talk("先生の場合はどちらなんですか？"),
                noto.talk("そうだね", "$meは学生時代は短編よりももっと短い掌編を数多く書いていた",
                    "けれどデビューに繋がったのは当然長編だし、作家になってからも求められたのは長編の方だった",
                    "短編もいくつか雑誌に載せてもらったが、読者は長編をより求める人が多かったように記憶している"),
                ),
            w.block("文章について",
                noto.talk("そういえば$sana君は小説の文章について、どう考えているだろうか？"),
                sana.talk("文章、ですか。編集としての立場から言わせてもらえば、まず読みやすいこと。理解しやすいこと",
                    "とにかく分かりやすいのが大事ですね。対象年齢もありますが、扱っているのがライトノベルなので、",
                    "古典文学でよく見られる難しい漢字や言い回しでページを埋められると、それだけでブラバされかねません"),
                noto.talk("ぶらば？"),
                sana.talk("本を閉じられるってことです"),
                noto.talk("文章というのは日本語が理解できる人なら誰でも書けると思われがちだが、なかなかそうではないことは、",
                    "小説を持ち出すまでもなく想像が容易い",
                    "これが小説となると、単なる文章ではなく、そこに様々な感情や思考が入り込む",
                    "けれど勝手我侭に書いてしまうとただの自己の吐き出しにしかならない",
                    "作家の文章というのはまずその読者に対して開かれていなければならない",
                    "分かりやすいというのもその一つだろう",
                    "ただしわかりやすさを追求しても行き着く先は国語の授業で習うようなあれだ",
                    "無味乾燥な味気のない、ただ情報の羅列にすぎない",
                    "小説の文章は握手なんだ。読者との対話というが、それ以上に、もっと感触や温度、手触り、そういったものを介して相手に何かを伝えようとする、",
                    "その行為そのものなんだよ"),
                ),
            w.block("シーンについて",
                noto.talk("$sana君はそもそも小説、あるいは物語でもいいけれど、それらが何によって出来ているのかは理解している？"),
                sana.talk("文章と台詞、みたいな話ですか？", "それとも起承転結のような構造のお話？"),
                noto.talk("どちらかといえば構造論に近いけれども、特殊な文学でなければ、物語というのは何らかのシーンを繋げたものになるんだ",
                "シーンと呼ぶと映画や映像作品のようにも感じるかも知れない",
                "けれどね、漫画でもそうだが、$meたちは本を読む時にそこに書かれた情報からストーリーラインや登場人物の心情ばかりでなく、",
                "それが一体今どこで何をしているのか、というのを自然と考えているんだ"),
                sana.think("また小説講座が始まったな、と思いつつも、湯船から上半身を露出している先生を$Sは直視することができず、自分の目の前の泡の消えたビールを見つめながら頷く"),
                noto.talk("小説を書く、物語を作る、といった時にね、まずはどんな話にしようか、つまり設定やラストのオチだったり、ミステリ作品ならそのトリックだったりを端緒にする訳だ",
                    "それで全体の流れを掴んだら、今度はプロットといってそれを細かくしたものを作ることになる",
                    "プロットのことは以前説明したね？"),
                sana.talk("はい", "必要と思われるエピソードを書き出して、どんな人物が必要か、どんな情報が必要か、またその配置の仕方なんかを考える叩き台です"),
                noto.talk("よろしい"),
                noto.do("満足そうに頷くと、先生は$Sにビールのお替りを頼む"),
                sana.talk("それじゃあシーンというのは、プロットをより細かくしたものですか？"),
                sana.do("なるべく見ないように顔を背けつつコップを渡すと、先生は特に気に掛けた様子もなくそれを受け取り、一口飲んでから、脇に置いた"),
                noto.talk("プロットはお話のまとまりで考えるから、厳密に考えるとシーンはまた違うものだね",
                    "シーンというのは場面、つまり場所と時間をベースとした概念だ"),
                sana.think("半分徹夜明けみたいな頭ではぼんやりとした理解が追いつかないが「はい」と頷いて次を促す"),
                noto.talk("例えば、そうだね、今$meたちは泊まっている部屋で会話をしている",
                    "そこで急に$sana君が土産物屋が見たいと言い出して、部屋から外に出てしまう",
                    "プロットでいうお話のまとまりとしては部屋から出て外を歩いていても会話は続いているけれど、",
                    "シーンを厳密に適用すれば、部屋での会話と歩きながらの会話、そして土産物屋に入ってからの会話というのは、別のシーンになる"),
                sana.talk("場所が変わるだけでもう別のシーンなんですか？"),
                noto.talk("厳密に考えるとそうだね",
                    "まあ小説の場合はそこまで細かく分けなくてもいいが、それでも今どんなシーンを書いているのかは意識しておいた方が良い",
                    "つまり場所と時間、それに誰がいて、どんな状態で、どういう意味合いを持つ場面なのか、ということを"),
                sana.talk("ちょ、ちょっと待って下さい"),
                sana.do("$Sは慌ててポーチに手を突っ込み、メモ帳を取り出す"),
                sana.talk("場所と時間だけじゃないんですか？"),
                noto.talk("文章の基本でもやったが、５Ｗ１Ｈのようにごくごく基本的な情報が入っているか、というのを意識する為にもシーンという考え方を持っておくと良いんだよ"),
                sana.talk("そこまで考えて書いたことありませんよ"),
                noto.talk("書いたことが無くても編集としては、普段からそういった意識をして読書したり作品を見るべきだよ？"),
                sana.think("専門的な勉強をした訳ではないので常々創作や小説のハウツー本くらいは目を通そうと思っているが、なかなか時間が取れないのが現実だった",
                    "$fukaya先輩は一体そういう時間をどうやって捻出したのか一度訊いてみたい"),
                ),
            w.block("物語のジレンマ",
            sana.do("鞄から先生の創作ノートを取り出し、ページを捲る", "最近は執筆で行き詰まる度にとにかくこれに目を通すようにしていた"),
            sana.explain("物語とは言い換えれば何かしら発生した、あるいは既に存在しているジレンマについて、登場人物たちがどう振る舞うかを書いたものだ", "とある", "&"),
            sana.explain("これは展開ばかりが評価される昨今、それでも人間について描くべきだ、という$Sの考えに合致する"),
            sana.explain("ジャンルが恋愛であれミステリであれ、レーベルが文芸でも純文学でもライトノベルであっても、",
                "基本はそこに描かれるのは人間ドラマであって、魅力的なキャラクターたちが悩み、苦しみ、時に笑い、愛を語り、そういう喜怒哀楽をその作家なりの文章と哲学で書いたものを、",
                "$Sは読みたいと考えている",
                "編集長や$nirasakiは全然違う意見だけれど、おそらく$yonezawaは$Sに近い考えを持っていると勝手に思っている"),
            sana.think("当然最終的には作品はその作家が書くものだし、編集が手伝えるのは精々自分の意見を言ったり、取材や調べものの手伝いをすることくらいだ"),
            sana.think("だが編集から作家側の立場になってみると、口で言うほどそれは簡単なことではないのだな、と痛感する"),
            sana.do("目の前には真っ白な画面が浮かんでいて、まだ一文字と進んでいない"),

                ),
            )

