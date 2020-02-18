# -*- coding: utf-8 -*-
"""Episode: 1-3.急げ編集者／走れメロス
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
def sc_accident(w: World):
    sana, noto = W(w.sana), W(w.noto)
    trainman = W(w.trainman)
    inside = W(w.inside)
    sphone = W(w.sphone)
    man = W(w.rideman)
    return w.scene("電車は事故で止まってしまい",
            w.comment("ここで条件確認。締切や先生の略歴"),
            sana.be("その一時間後、$Sは電車の吊り革に手が届かない自分の身長を嘆くでもなく、八割くらい埋まった電車の中でスマートフォンを手にこの世の終わりみたいな顔をしていた"),
            man.be(),
            sana.explain("あの後すぐに$fukayaは救急車で病院へと運ばれていった",
                "担架に載せられながら何度も$Sに「先生のことお願い」と繰り返し、$Sの手をぎゅっと握り返してくれたその感触が、温もりがまだ、残っている"),
            _.explain("けれど改めて引き継ぎ資料に目を通すと、どうやら今日の午後一時には原稿を取りに行くと約束したことになっていた",
                "時刻を確認する","現時点で既に十二時三十五分", "$noto先生のアパートがある三鷹まではまだ十分以上かかるし、駅からも徒歩十五分と書かれていた"),
            sana.think("走れば間に合う走れば間に合う走れば間に合う――と、心の中で三回唱える",
                "そういえば緊張した時に飲む人の字も流れ星に願う時もどうして全部三なのだろうか",
                "そんなことを考えていたら、ガタン、と大きく車両が揺れ、耳障りなブレーキ音が響いた"),
            sana.explain("#今回先輩から引き継いで担当になったのは、元芥川賞候補作家の$notoだった"),
            _.explain("#デビュー作の『$masternovel1』で注目を浴びてその後立て続けに長編を発表したが、",
                "#ある時を境にして急に小説を書かなくなった。",
                "#その後、エッセイや紀行文などを小冊子に掲載したりしていると書かれているが、全然知らないものばかりだった"),
            trainman.talk("ご乗車中のみなさまにお知らせします。この先の区間にて人身事故発生の為、只今運転を見合わせております。",
                "発車までしばらくお待ち下さい"),
            sana.hear("落ち着いた口調の車掌のアナウンスだったが、車内は騒然としている"),
            man.talk("おいマジかよ"),
            man.talk("ちょっと事故だってさ"),
            man.talk("この後打ち合わせがあるのに"),
            sana.think("終わった、という思いで天井を見上げると、そこに天使か女神が浮かんでいるような気がした"),
            sana.think("引き継ぎ資料には『$noto先生は気難しく、特に約束した時間や待ち合わせで相手の機嫌を損ねないことは困難を極める』と注意書きしてあるくらいの、",
                "難敵らしいのだ"),
            sana.do("$Sはスマートフォンで他の経路を急いで確認する",
                "他の路線に乗り換えて迂回する案もあったがどれも時間的に余裕がない",
                "五分後に動き出したとして、すぐ隣の駅で降りてからタクシーというのが無難な線だろう"),
            sana.do("けれど一分待っても二分待っても何もアナウンスがなく、動き出す気配も感じられない",
                "乗客もざわざわが収まらず、中には「降ろせ」と怒鳴り始める人もいた"),
            sana.think("その気持ちはよく分かるけど、騒ぎ出すのは大人のやることじゃない",
                "そんな風に最初は悠長に構えていた$Sだったが、"),
            sana.talk("あの……このままじゃ、完全に遅刻するんですけど！"),
            sana.think("十分経っても動き出さないことには流石に焦りを通り越して憤りが爆発してしまっていた"),
            sana.talk("運転再開とかいいから、ちょっと下ろして！", "下ろして下さい！"),
            camera=w.sana,
            stage=w.on_train_int,
            day=w.in_firstmeet, time=w.at_beforenoon,
            )

def sc_rungirl(w: World):
    sana, noto = W(w.sana), W(w.noto)
    outside = W(w.outside)
    oldlady = W(w.oldlady)
    return w.scene("彼女は走る",
            sana.be("#タクシーを捕まえようと通りに出るが、なかなか捕まらず"),
            sana.do("息荒く駅から出て、タクシー乗り場に急ぐ", "&"),
            outside.look("だがこういう時に限って人の列が出来ていて、順番待ちをしていたらいつになるか分からない"),
            sana.think("何で！", "と叫び声を上げたくなったがそこをぐっと堪え、","&"),
            sana.do("$Sは通りの方に出て、自力でタクシーを探す"),
            sana.think("こういうことがあるから社用車で出かけたかったのに、単なる外回りで使うというと編集長があまり良い顔をしない",
                "経理担当でもないのにやたらと無駄遣いをするなが口癖で、その割に自分は経費で好きなものを買ったり接待交際費で有名作家とキャバクラに行ったりしているのだから、",
                "二枚どころか三枚舌もいいところである"),
            sana.talk("タクシー！"),
            sana.do("片側に車線の歩道ギリギリのところで百四十一センチの女性が大きな鞄を二つも肩から下げ、一生懸命に右腕を伸ばす",
                "けれどそんな姿を見て「可哀想だ」とか「大変だから」とか「女の子だから」と言ってタクシーが停まってくれる訳でもない"),
            sana.think("世の中は弱いものに対して優しいはずだ、という性善説みたいな思い込みは、自分が弱者側に立ったことのない人間の妄言だと$Sは思っている",
                "学生時代も今と変わらず大半の人間より小さくて、同級生からは「可愛くていいじゃない」「小動物みたいだ」と半分マスコット的な扱いを受けて弄られることが多かった",
                "きっと言っている方は可愛がっているだけだと思っていただろうけれど、言われている側の$Sはいつも曖昧な苦笑いしかしていなかったことを、彼らは見ていない"),
            sana.think("だからセーラー服を着ていたあの頃、$Sは図書館に駆け込んで、本と自分だけの世界で戯れた",
                "本は、小説は、$Sがどんな人間で背が小さくても女性でも声が子どもみたいに高くても、気にしない",
                "本はいつも自分と対等だった",
                "その中の人物に成り切ったり、がんばれって応援したり、時には憧れたり、学生生活にはなかったものを沢山与えてもらった",
                "だから$Sは今、本を作ってその頃の自分を同じ気持ちを抱えた誰かに「大丈夫」って伝えたい"),
            sana.talk("あ！"),
            sana.do("やっと一台、個人タクシーがゆるゆると減速して路肩に付けてくれた"),
            sana.think("がんばる自分を文芸の神様は見捨てなかった",
                "こういう時はそう思うことにしている"),
            sana.do("心の中で感謝をし、後部座席の開いたドアから乗り込もうとしたところで、しかし別の女性の声を聞いてしまった"),
            oldlady.talk("あのぉ、すみません"),
            sana.do("振り返ればシルバーカーを押した品の良さそうなおばあさんがじっと$Sを見ている"),
            sana.talk("あ、いいですよ", "どうぞ、使って下さい"),
            oldlady.talk("あらまぁ、すみませんねぇ"),
            sana.do("お構いなく、と精一杯の笑顔を作り、その女性が乗り込んだタクシーを見送ると、$Sは草の生えたコンクリートブロックの上に特大の溜息を叩きつけ、顔を上げる"),
            sana.think("――よし、少し走るか"),
            sana.do("次のタクシーを待つ",
                "そんな選択もあるだろうけれど$Sは走ることを選んだ",
                "今更少しくらい走ったところで、何も変わらない",
                "もう遅刻は確定的だ",
                "でも思うのだ",
                "何もしないでいるよりとにかく足掻いて必死になって目の前の問題にぶち当たってきた$Sには、それが自分の進む道だと"),
            sana.think("小さい頃からよく走っていた", "&"),
            sana.think("足も短いし、特別速くなんかないけれど、それでも走っていれば自分がそこに存在していると認めてもらえた",
                "運動会でかけっこになると元気になった$Sのことを両親はとても喜んでくれた",
                "今はもう墓の下だけれど、陸上部だったという父の遺伝子を受け継いでいるのかも知れない"),
            sana.do("$Sにとっては走ることは生きることで、働くことだった"),
            stage=w.on_street,
            )

def sc_timelimit(w: World):
    sana, noto = W(w.sana), W(w.noto)
    watch, sphone = W(w.wristwatch), W(w.sphone)
    exterior = W(w.exterior)
    gate = W(w.gate)
    door = W(w.door)
    return w.scene("タイムリミット",
            sana.come("タクシーを降りて、スマートフォンで地図を確認する"),
            sana.explain("十月半ばとはいえまだまだ日が高いと暑さを感じる",
                "既に背中は汗でべっとりしていたが、そんなことを気にしていたら編集なんて仕事はできない"),
            sana.explain("あの後、交差点まで出て何とかタクシーを捕まえることができたのは良かったが、それでも三鷹までの料金は高くついた",
                "経費では落としてもらえないだろうと覚悟しつつ一応領収書を貰っておいたけれど、今月は既に出費が多いのであまり財布事情としては宜しくない"),
            sana.do("$fukayaの資料には一応詳細な住所と地図も添付されていたが、目に付くのはどれも三階や四階建ての住宅ばかりだ",
                "木造の築四十年のアパートだと書かれているけれど、まだ視界には入ってこない"),
            sana.do("$Sは歩きながらもう一度確認しようとスマートフォンに$fukayaのメモを呼び出す"),
            sana.explain("$full_noto先生",
                "身長と体重が続けて書かれているが百八十（推定）と結構デカい",
                "隣に並ぶと四十センチも見上げなければならない",
                "代表作は『$masternovel1』で、芥川賞候補にもなった青春恋愛文学だとある",
                "他にも長編二作、短編集が二冊、リストにあったが、どういう訳か最近の作品については一切書かれていなかった"),
            sana.think("そもそもライトノベルは一度も書いていないようで、どういう経緯で現在ライトノベルのレーベル所属の$fukayaが担当になったのか不思議だ",
                "ただ先輩はレーベルやジャンルといった拘りなく、自分がこの人、この作品と思ったら突撃するタイプなので、何かがその琴線に触れたのだろう"),
            sana.talk("あれかな？"),
            sana.do("角を曲がったところで新築の三階建てマンションに挟まれる形でその二階建ての、外にところどころ錆びついて見える鉄の階段が付いたアパートが見つかった"),
            sana.think("ちょっと遅れたけど許容範囲かな、","と既に三十分は遅刻をしていることを確認してから、小走りで向かう"),
            gate.look("入り口の門に『$on_hisapart』という木の看板があり、それが十五度ほど傾いていた"),
            sana.think("確かにここだ", "&"),
            sana.think("放火でもされたら一気に燃え上がりそうだと感じつつも、先生の部屋に向かう", "一〇三号室だ"),
            sana.do("押しボタンになっているインタフォンを押し込むと、ジイィと瀕死の蝉の鳴き声のようなそれが響く"),
            sana.talk("あのー、すみません"),
            sana.hear("もう一度押してみたが中から応答はない"),
            sana.talk("すみません。$on_hercompanyから来ました$ln_sanaと申します。今日から$fukayaの代わりとして先生のご担当をさせていただくことになりまして……"),
            sana.do("ドア越しに声を掛けてみたが、やはり反応はない", "留守なのだろうか",
                "もしかすると約束の時間に遅れた所為で怒ってどこかに出かけてしまったのかも知れない"),
            sana.think("置き手紙でも入れておいてまた出直すかな"),
            sana.think("そんな風に考え始めた時だった"),
            sana.talk("ん？"),
            sana.do("よく見るとドアの覗き穴の下辺りに、小さく張り紙がされていた", "風で捲れ上がるとそれが原稿用紙を裏返したものだと分かる"),
            door.look("そこに書かれていたのは『編集よ去れ！』という一言だけだった"),
            sana.talk("はぁ！？", "何なのよこれは！"),
            stage=w.on_hisapart_ext,
            time=w.at_noon,
            )

## episode
def ep_hurryeditor(w: World):
    return w.episode("3.急げ編集者",
            ## NOTE
            sc_accident(w),
            sc_rungirl(w),
            sc_timelimit(w),
            )
