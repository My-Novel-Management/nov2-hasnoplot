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
    fukaya = W(w.fukaya)
    return w.scene("自己紹介",
            sana.be("#立っている"),
            noto.be("#座っている"),
            w.comment("冒頭｜どこで生れたかとんと見当けんとうがつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。しかもあとで聞くとそれは書生という人間中で一番獰悪どうあくな種族であったそうだ。この書生というのは時々我々を捕つかまえて煮にて食うという話である。"),
            sana.do("吾輩は編集者である", "名前は$full_sana",
                "どこで間違ったかとんと見当がつかぬ",
                "何でも半休の日の布団というぬくぬくした所で急な呼び出しにギャーギャー喚いていた事だけは記憶している",
                "吾輩はこのアパートで初めて$full_notoという人間を見た",
                "しかもあとで聞くとそれは小説家という人間中で一番獰悪な種族であったそうだ"),
            w.br(),
            sana.do("テーブルを挟んでどっかりと腰を下ろした先生を前に、$Sは棒立ちになって緊張していた"),
            noto.talk("$meの方はいつでも良い",
                "どうぞ、自己紹介あたりから始めてくれたまえ"),
            sana.talk("は、はい"),
            sana.think("頭の中で『吾輩は猫である』の冒頭の文章に似た何かが読み上げられたが、とても自己紹介には使えそうにない"),
            _.think("確かに面接試験をさせて欲しいと頼んだのは$Sなのだが、実は就職試験の中でも面接が一番苦手と言って良かった",
                "今の出版社にも$fukaya先輩に声を掛けてもらっての引き抜きのような扱いだったので、形式だけと面接試験を受けたのだけれど、",
                "あの日最初に挨拶をしようと口を開けたら素人のヴァイオリンみたいな声しか出ずに苦笑されたことを、急に思い出して指先が震えてくる"),
            sana.talk("えっと、その……わ、$meは$full_sanaです", "$on_hercompanyで編集員をやっています"),
            noto.talk("その編集とは、どんな仕事なのかね？"),
            noto.do("先生は眉間に皺を作りながら尋ねた"),
            sana.talk("え？　編集の仕事ですか？"),
            sana.think("名古屋の実家の母親や親戚、同級生なんかに聞かれて一番困る質問がこれだった",
                "例えば印刷会社ならチラシやポスター、本を刷ったり製本したり、デザインを考えたりしている等と答えることができるが、",
                "編集が本を作る関係の何かという知識はあっても、実際にやっていることといえば企画会議と営業回り、イラストや装丁デザインなんかの発注に、校正作業、",
                "あとは作家の原稿の進捗状況の管理や連絡、取材などがあればその調整と、多岐に渡る",
                "人によっては夕食をご馳走したり、コーヒーを淹れたりすることだって編集の仕事だと言うだろう"),
            sana.talk("夢を作るお手伝いです"),
            noto.talk("夢？"),
            noto.do("その言葉がおかしかったのか、先生は小さく吹き出すと「その意味を教えて欲しい」と言ってきた"),
            sana.talk("先生の小説は、まだ読んでいないのでどのような内容を書かれるか分かりません",
                "あらすじや評論を見た感じですと文芸作品で青春や男女関係、人生について書かれているんだな、という程度の知識しかありません",
                "それでも作家になる、あるいは小説を出すというのは、先生の一つの夢だったんだと思うんです", "違いますか？"),
            noto.talk("夢、か"),
            noto.do("その言葉を噛みしめるように何度か口の中で繰り返し、腕組みをして先生は唸る"),
            noto.talk("もう随分と昔のことだから忘れてしまったが、そうだな、夢、だったのかも知れない"),
            sana.talk("$meは、言ったかも知れませんが、学生時代、趣味で小説を書いていました",
                "でも残念ながら作家になるとか、そういった才能はなくて、それでも何か本に関わる仕事をやりたいなと思って、雑誌の編集プロダクションに就職しました",
                "今の出版社に移る前の話です"),
            noto.do("ああ、という先生の相槌を見て続ける"),
            sana.talk("作家の先生方は、一人一人色々な思いをもって小説を書かれていると思いますけど、ただ書いている、仕事だからとりあえず原稿を埋めている、という人はほとんどいないと思います",
                "作家さんによってはそれが本になるか分からないまま、不安の中で執筆を続けていらっしゃる方もいるでしょう",
                "でもみなさん、その小説を本として世間に出すことを目標に書かれていますし、沢山の読者さんにそれを届けたいという思いで書いていると思います",
                "それは、先生方にとっても夢でしょうけれど、$meにとっても一つ一つが素敵な夢なんです",
                "そして、待っている読者のみなさんにとっても夢だと思うんですよ",
                "だから、その夢を作るお手伝いとして、コピーも取ればコーヒーも淹れるし部屋の掃除だって、取材の為にチケット取ったり、資料を買い込んだり、ヨガ教室に通ったりと、",
                "もう何でもします",
                "あ、脱ぐ以外は、ですけど"),
            noto.do("最初は懐疑的な目線を向けていた先生も、$CSが夢の意味を話したことが気に入ったのか、表情が柔らかくなり、最後には少し笑みも漏らしてくれた"),
            sana.talk("そういう訳だから、$meは先生の担当編集として、是非働きたいと思います",
                "というか、働かせて下さい",
                "先生の夢を一つでも多く、叶えさせて下さい"),
            noto.talk("君は、無茶を平気で口にする人なんだね"),
            sana.think("先生は微笑していたが、口調はやや厳しかった"),
            noto.talk("無茶というのは道理に合わないこと、という意味で使っている",
                    "程度の酷い様や知識がないという意味ではないから安心したまえ"),
            noto.do("先生はテーブルの上に置いたカップを手に取り、コーヒーを一口飲むと、その柔和な顔のままで続ける"),
            noto.talk("思えば$fukaya君も最初から無茶を口にする人だった",
                    "何年も小説を書けていない$meに向かって彼女が何と言ったか、分かるかい？",
                    "『先生が小説を再び書けるようになるまで書かなくても食べられるようにします』と、そんなことを言ったんだよ",
                    "あの時はこの女性は一体何を考えているのだろう、何だかとんでもない人が担当になったな、と思ったものだった"),
            sana.think("先輩なら言いそうなことだった",
                    "そういう訳の分からない、でも何だか信じたくなる無茶をするのが、$full_fukayaという人なのだ"),
            noto.talk("分かったよ",
                    "君は確かに彼女から引き継いで$meの担当編集になるのだと、認めようじゃないか",
                    "ねえ、仮担当君"),
            ## NOTE
            ##  オーディションでは最初の、やっと「小説講座」らしいもの登場させる
            camera=w.sana,
            stage=w.on_hisapart_int,
            )

def sc_aboutnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("小説とは",
            noto.be(),
            sana.be(),
            sana.talk("失礼します"),
            sana.do("そう断ってから、足を折って正座になる",
                "履いてきたスーツのスカートの丈は短くなくて良かったが、見えている部分のストッキングが伝線していないかやや不安だった"),
            noto.talk("では、一つ質問させてもらいたい",
                "夢だ、と語る君にとって小説とは一体何なのかね？"),
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
            ).omit()


def sc_1stmission(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("最初の仕事",
            noto.be(),
            sana.be(),
            sana.talk("それじゃあ、これで正式に先生の担当になれたということで宜しいですか？"),
            sana.do("極度の緊張感から解放され、脱力してその場にへたり込んだ$Sは、コーヒーを飲む先生を見ながら確認した"),
            noto.talk("君が$fukaya君の後任である、ということは了承したけれど、まだ仮だよ、仮",
                "そもそも人の信頼をそんなに簡単に得られると思うかね？",
                "信頼というのは日々の積み重ねだよ"),
            noto.do("先生は人差し指を立てて言い聞かせるように$CSを見る", "それでも今までよりは少し話をしようという気になってくれているのはその表情からもよく分かった"),
            sana.talk("それじゃあ、どうすればもっと信頼を得られますか？",
                "$meは今日、先生からどうしても約束の短編小説の原稿を貰って帰りたいんですが"),
            sana.do("スマートフォンには会社からの連絡は何も入っていない",
                "それだけ確認して脇に伏せ置くと、$Sの膝へと上がってきた黒猫の頭を撫でた",
                "ぬいぐるみとはまた違って、猫の頭のやや固い毛並みは良い具合に掌を刺激してとても素敵だ、と感じた"),
            noto.talk("そうだな"),
            noto.do("そんな$CSを見ながら先生は腕組みをし、しばらく考え込む"),
            sana.do("よく見れば部屋はあちこちに本や雑誌が積まれているし、ゴミ袋は口を開けたまま放置されている",
                "中に入っているのは紙類だけでなく、カップ麺の空やビールの空き缶、ペットボトルもまとめて突っ込まれていて、",
                "先生という人間の私生活を一部垣間見たような気がした"),
            noto.talk("そうだな",
                "それじゃあちょっと買い物を頼まれてくれないか。ビールを切らしてしまっていてね"),
            sana.talk("ビールですか？", "それが執筆に何か関係が？"),
            noto.talk("ビールは一日一缶、仕事を終えた後に飲むのだよ",
                "そういう行事によって一日を終えたという感覚を味わうことが精神衛生上とても大事なのだ",
                "ああ、あとおつまみも適当に見繕ってきてく"),
            sana.talk("ビールとおつまみ、ですね"),
            sana.do("$Sは一応手帳にメモを取り、立ち上がる"),
            sana.talk("$meが出かけている間にせめてプロットだけでも用意しておいて下さいよ。頼みましたからね"),
            noto.talk("またそんな簡単にプロットとか言うんだ、君ら編集は。あのね、プロットと一口に言っても……"),
            sana.talk("講義は後で聞きます。とにかく原稿お願いしますよ"),
            noto.talk("プロットから原稿に昇格しているじゃないか……"),
            sana.go("先生はぶつぶつと文句を言い始めたが、とりあえずさっさと買い出しを済ませようと駆け足で外に出かけて行った"),
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
            ).omit()

def sc_endmission(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("買ってきました",
            w.symbol("　　　　◆"),
            sana.come("#買い物袋と共に戻ってくる"),
            sana.explain("コンビニは一番近いところで歩いて三分程度の距離だった",
                "既に一時を過ぎ、オフィス街でもないこの住宅街の店内には、暇を持て余したおじいさんおばあさんが少し目に付いただけで、",
                "あとはパートのおばさんが欠伸をしている"),
            sana.do("目当てのビールとスルメやナッツ、チーズ鱈といった定番のつまみを購入し、さっさと戻る"),
            sana.think("しかし初日からこれでは先が思いやられ過ぎて、既に胃袋は不調の産声を上げていた"),
            sana.talk("あ、そういえば"),
            sana.do("先輩の引き継ぎメモに気になる文言があったことを思い出し、慌ててスマートフォンを取り出して確認する",
                "そこには詳細に書かれた中の注意事項の一つとして『よく逃げ出すから注意して』と二重下線付きで書かれていた"),
            sana.talk("え？　……えぇー！"),
            sana.do("その可能性を完全に失念していた$Sは小学生時代にリレーのアンカーを務めた頃の気持ちを思い出して、全力疾走でアパートへと戻った"),
            sana.talk("せ、先生！　買ってきました、よ？"),
            sana.do("だがリビングで$Sを迎えてくれたのは足元にじゃれ付いてきたあの黒猫だけだ"),
            sana.talk("先生！？"),
            sana.do("焦る気持ちで寝室の引き戸を開ける",
                "しかしそこには誰もいない",
                "トイレや浴室も当然不在だ"),
            sana.talk("やられた！", "ああ、もう！"),
            sana.think("上がる前に気づけば良かったのだが、確かに先生の履物と思しき下駄が一揃い、姿を消していたのだった"),
            sana.go(),
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
