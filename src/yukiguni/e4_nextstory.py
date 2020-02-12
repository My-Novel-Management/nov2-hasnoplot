# -*- coding: utf-8 -*-
"""Episode: 5-4.続雪国／雪国
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
def sc_newperson(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, tsuchi = W(w.nirasaki), W(w.king), W(w.tsuchiura)
    return w.scene("新人現る",
            sana.come("#出社してくる$S"),
            sana.do("週明けの、まだ新年の空気漂うオフィスに、珍しく息を荒くすることなく到着した$Sは、そこで王と談笑している謎の茶髪を発見した"),
            king.be("#珍しく談笑"),
            tsuchi.be("#$kingと笑って話している若い男"),
            nira.be("#相変わらず仏頂面で座っている"),
            sana.talk("おはよう。あれ誰？"),
            sana.do("頭だけ下げて（そんなものちらりとも王は見なかったけれど）、自分の席に就き、既に出社していた$nirasakiにそれとなく尋ねる"),
            nira.talk("ああ。なんか王が連れてきたバイトだってさ",
                "へらへらして、どうにもあの手のは苦手なんだよね", "いつまで続くやら"),
            sana.talk("へえ"),
            sana.think("$Sからすれば$nirasakiもそう大差なく思えるがそれを口にすることは禁則事項だ", "$fukayaを除けば現在唯一まともに会話が成立する人なので、",
                "その信頼を損ねてはいけない", "しかし、と腕組みをしてそのアルバイトだという茶髪の彼を見やる"),
            tsuchi.wear("黄色いパーカーにパッチワークでステッカーがべたべた貼り付けられたジーパン、膝はお決まりの穴開きで、",
                "笑う顔がその大きな目玉もあってカエルか蛇のように思える"),
            sana.talk("王ってああいうのが好みなんですか？"),
            nira.talk("さあね", "それより王の連れてきた人間で使えたのがいたためしがないから、そっち注意した方がいいわ"),
            sana.do("その会話を聞いていた訳ではないと思うが、編集長が茶髪を伴って二人の方へとやってきて、わざわざいつもはしない挨拶を口にした"),
            king.talk("やあ、おはよう、君たち"),
            sana.talk("おはようございます、編集長"),
            sana.do("その隣でへらへらとした茶髪は「ども」ともごもご口にしただけで、$Sを見てよく目立つ犬歯を出して笑う"),
            king.talk("紹介するよ。$tsuchiura君だ",
                "彼は$meの知人の甥っ子でね、ちょっと社会見学をさせてやって欲しいと頼まれてね",
                "しばらくはバイト扱いだが、後々はうちの戦力にと考えているよ"),
            sana.think("それはほぼ正規社員雇用の予定ではないのですか、と文句を言いそうになったが、人の出入りの多い業界だから純粋に戦力になるのなら助かる",
                "戦力になるのであれば"),
            king.talk("そうだな、しばらくは……$ln_sana。君が面倒を見てやってくれ",
                "よろしく頼むよ"),
            sana.talk("え？　$meですか？"),
            king.talk("何か不満が？"),
            sana.talk("いえ。分かりました。お引き受けいたしましょう"),
            king.talk("それでは、後は頼んだよ、$ln_sana"),
            king.go("満足そうに頷くと、王は機嫌良さそうに自分のデスクへと戻っていく"),
            tsuchi.talk("$ln_sanaさんてベテランすか？"),
            sana.talk("一番下っ端です"),
            tsuchi.talk("じゃあ見た目通りすか！　ははは！"),
            tsuchi.do("何が面白いのか分からないが大声で笑うと「とにかくヨロシクす」と手を差し出してきた", "&&"),
            sana.do("あまり気は進まなかったがその手を握り返して握手をすると、手汗なのか、べっとりとした感触が$Sの右手に残った"),
            nira.talk("ああ、$meはちょっと外回り行ってくるわ", "ご苦労さん"),
            sana.talk("えっ……"),
            sana.do("指導と言っても何をすればいいのか分からないのでとりあえず$nirasakiに助けを求めようと思ったのだが、案の定、",
                "鞄を手にさっさと立ち上がると、", "&"),
            nira.go("彼は半笑いを浮かべてオフィスから出て行った"),
            sana.talk("ちょっと！", "ああ、もう！"),
            tsuchi.talk("何すか？", "ひょっとしてカレシさんすか？"),
            sana.talk("違うわよ！"),
            sana.do("普段温厚（だと思い込んでいる）な$Sですら、そのへらへら顔で言われたら思い切り張り飛ばしたくなる"),
            sana.talk("とにかく、そうね、まずは社内の案内からかな？"),
            tsuchi.talk("へへへ"),
            sana.talk("せめてさ、社会人なんだから返事は『はい』って言ってもらいたいんだけど……まあいっか"),
            sana.do("意味を全く理解してなさそうな彼に背を向け、$Sはデスクに『新人案内中』とメモを残す",
                    "どこから案内したものかと考えながら「じゃあまずは第二文芸部から簡単に行くわね」と、編集長から順に説明を始めた"),
            sana.talk("この$on_hercompanyには編集部として第一文芸部と第二文芸部があるわ",
                    "一文は上の四階の方で、主に一般文芸を扱っている", "対してこの二文ではティーン向けのライトノベルや一部児童書なんかがそのテリトリね",
                    "今話したこと、理解できる？"),
            tsuchi.talk("それ覚えなきゃ駄目すか？",
                    "ていうか、時給いくらなんすかね", "$me今週中に友人に三万返さなきゃいけなくて"),
            sana.do("理解する気がないという返答をもらい、$Sの笑顔は砕け散った"),
            ## NOTE
            ##  今後のキーとなる新人登場
            ##  できるだけ不快さと編集っぽくない、一般の会社の使えそうにない新入社員風
            camera=w.sana,
            stage=w.on_heroffice,
            day=w.in_newparttimer, time=w.at_midmorning,
            )

def sc_guideoffice(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, yone, tsuchi = W(w.nirasaki), W(w.king), W(w.yonezawa), W(w.tsuchiura)
    return w.scene("会社の案内",
            sana.be("$tsuchiuraを案内"),
            tsuchi.be("突っ立っている"),
            w.comment("それぞれの案内と紹介"),
            king.be(),
            yone.be(),
            nira.be(),
            w.comment("簡単に四階に「二文と営業などがあって」四階に「一文と総務など」と"),
            ## NOTE
            ##  ここで再度、第二文芸部の編成などを見せる
            stage=w.on_heroffice_int,
            ).omit()

def sc_greeting(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, tsuchi = W(w.nirasaki), W(w.king), W(w.tsuchiura)
    return w.scene("挨拶",
            sana.come("#先生のところに挨拶にやってきた"),
            tsuchi.be("#もそもそとついてきている"),
            sana.explain("会社案内から始まって、ちょうど雑誌の見本も貰っていたのでそのお礼も兼ねて印刷所の方まで$ln_tsuchiuraを連れて回ってきたのだけれど、",
                "紹介する誰もが彼に対して眉毛を顰めていた",
                "それはそうだろう、と$Sも思ったが、無駄口を叩いて相手を怒らせなかったことだけは評価しようと心に決めた"),
            tsuchi.talk("で、担当てそもそも何なんすか？"),
            sana.do("腕時計を確認すればちょうど昼前だった。そろそろ起きているだろうといううことで駐車場に車を停め、先生のアパートへと向かっていた"),
            sana.talk("担当っていうのは作家の担当のことで、うちで出版したり、これから出版をする作家や出版に向けて面倒を見ている作家さんたちをそれぞれ個別に編集が受け持つことよ",
                "多い人だと十人とか二十人くらい抱えていることもある",
                "伝説の、なんてレベルになるともう五十人とかって話もあるけど正直眉唾なんじゃないかなって思ってる"),
            tsuchi.talk("それじゃあ$meは女の先生がいいっすね！", "特に若くてピチピチしたの"),
            sana.think("ここにもセクハラ魔人がいたかと溜息を零すが、アパートが見えてきたので小言は留め置いた"),
            sana.talk("あそこよ"),
            tsuchi.talk("へー、なんかもっと豪邸とか都心のタワマンの最上階に住んでるのかと思ってたっすけど"),
            sana.do("確かに木造の古いアパートというのは色々な面で心もとないが、まだどうなるか分からない先生一人に高級マンションを借りて使ってもらうような予算が降りる訳もなく、",
                "それでもせめて週に一度くらいはホームクリーニングを入れてあげたいという気持ちで、$Sがこまめに様子を見て掃除をしに来ていた"),
            sana.talk("先生、おはようございます"),
            sana.do("二度、三度とインタフォンを鳴らすが応答する気配がない"),
            sana.do("仕方なく合鍵を使ってドアを開け、中に入る"),
            sana.talk("先生？", "寝てますか？"),
            sana.do("いつもの調子で声を掛けながら一歩、足を踏み入れたところで、呼吸が止まった"),
            tsuchi.talk("事件現場すか、これ！？"),
            sana.talk("事件は起きてないけど、とりあえず片付けて、$ln_tsuchiura君"),
            tsuchi.talk("え？　なんで$meが？　それが仕事なんですか？"),
            sana.talk("作家の面倒を見るのが編集の仕事だから"),
            sana.do("辛うじて炬燵は見えるが、その周囲にはゴミと雑誌と本と食べかすと、コップや茶碗や、カップ麺の食べ残しや、それでも片付けようとしたのか可燃ごみ用のゴミ袋が何枚か、",
                "見える範囲に散乱していた",
                "そう、見える範囲でだ"),
            tsuchi.talk("げっ、マジかよ！？", "掃除苦手でバイト辞めてんすよね"),
            sana.talk("とりあえず本は端にまとめて、それ以外はゴミ袋に放り込んじゃっていいから"),
            sana.do("部屋の掃除を茶髪君に任せ、$Sは足元に気をつけながら右手の奥へと進み、そっと寝室の戸を開ける"),
            sana.talk("先生？"),
            noto.be("寝ているものと思った先生は、着物姿でテーブルを前にして、じっと腕組みしていた"),
            sana.talk("先生、おはようございます"),
            noto.talk("ああ、$sana君か", "おはよう"),
            noto.do("テーブルの上には原稿用紙の束が置かれ、その一番上のページの半分くらいを文字が埋めているのが分かった",
                "よく整い、ペン習字の手本のような先生の文字だ"),
            sana.talk("早速約束の長編を書いて下さってるんですね！"),
            noto.talk("いや。単なるプロットだよ"),
            sana.do("言われてよく見てみれば確かに小説の文章ではない",
                "異世界やファンタジーといった文言が見つかることから、本当にライトノベルの長編小説を構想してくれているらしいことだけは分かった"),
            tsuchi.talk("あのー、中の汁とか、なんか溶けてるのとかも一緒でいいんすか？"),
            tsuchi.do("口にマスクをしてどこから取り出したのかサングラスまで掛けている$ln_tsuchiuraが顔を出したが、知らなかったら明らかに不審者が侵入してきたといった風にしか見えない"),
            noto.talk("どちら様？"),
            sana.talk("あ、えっとですね、紹介します。新人でアルバイトの$full_tsuchiura君です"),
            tsuchi.talk("あ、ども"),
            noto.do("先生も今までの人たちと同様に眉を顰めて彼を見ていたが、すぐに興味を失ったのか、それ以上は何も言わずに視線を原稿へと戻してしまった"),
            sana.talk("先生、本日は彼の顔合わせと、もう一件、こちらの用事で伺いました"),
            noto.talk("何？"),
            sana.do("バッグから取り出したのは社主催の新年会パーティの招待状だ",
                    "毎年、主に作家同士の繋がりや、作家と編集部各員の顔合わせの目的で行われているそうだ",
                    "昨年夏入社なので、$Sは今年初めて参加する"),
            noto.talk("十三日か。都合が悪いね"),
            noto.do("だが先生はそれをちらっと見るなり、すぐにテーブルの上に投げ置いてしまった"),
            sana.talk("十分でも十五分でもいいので、少しでも顔を出していただけると助かります",
                    "今後のこともありますし、他の先生方と色々意見交換などもできますよ？"),
            sana.think("できる限り出席させるようにと編集長から言付かっているが、どうにも先生の反応はよくない"),
            noto.talk("分かったよ", "時間が合えば伺おう", "ただ、あまり期待しないでもらいたい"),
            sana.talk("分かりました。それで大丈夫です"),
            sana.do("いつもならここであれこれと買い出しやコーヒーを淹れてくれないか等と頼まれるのだが、今日は構想中だからか、",
                    "何も言わずに原稿に向かってしまった"),
            sana.talk("それでは失礼しました"),
            sana.do("そう言って、まだ顔を出したままだった$ln_tsuchiuraと共に部屋を出る"),
            tsuchi.talk("なんか恐い人すね"),
            sana.talk("いつもはもうちょっと違うんだけど……まあ、執筆中はどんな作家も仕方ないわよ",
                    "それよりぱぱっと残りを片付けちゃいましょう"),
            tsuchi.talk("ああ、やっぱり最後までやるんすね"),
            sana.do("げんなりした表情の茶髪君の肩を叩き、$Sは笑った"),
            ## NOTE
            ##  先生との対面も印象悪くする
            stage=w.on_hisapart,
            )

def sc_printing(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, tsuchi = W(w.nirasaki), W(w.king), W(w.tsuchiura)
    oki = W(w.oki)
    return w.scene("印刷所",
            sana.come("印刷会社にやってきた二人"),
            tsuchi.be(),
            tsuchi.talk("ここで本ができるんすか"),
            sana.talk("ここじゃないわよ。印刷は工場が別にあるの。ここはオフィスだけね"),
            oki.be("仕事をしている"),
            sana.talk("どうも、今年も宜しくお願いします"),
            oki.talk("おお、$sanaちゃん。よろしく。そっちは作家先生？"),
            sana.talk("いや、新しいバイトの子で"),
            oki.do("じっと観察して、特に挨拶もなくパソコンに戻る"),
            tsuchi.talk("えっと、あの"),
            sana.talk("まあ、そっか。また来ます"),
            tsuchi.talk("え？"),
            sana.talk("みんな忙しいのよ。行くわよ"),
            tsuchi.talk("うす"),
            ## NOTE
            ##  最後の方で世話になるので顔見世程度
            stage=w.on_bigprint,
            ).omit()

def sc_abouteditor(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, tsuchi = W(w.nirasaki), W(w.king), W(w.tsuchiura)
    return w.scene("編集者の仕事とは",
            sana.be("ファミレスに入っている"),
            tsuchi.be("大盛りのステーキセットを注文している"),
            sana.talk("編集って言ってもその多くは本を作る為の雑用と人の手配なのよ"),
            tsuchi.talk("そうっすね"),
            _.do("頬張りながら聞いている"),
            sana.talk("今の部署は書籍の出版が基本業務だけど、月刊誌や週刊誌を扱っているところはもっと忙しいわよ"),
            tsuchi.talk("そすか"),
            sana.talk("まあ$tsuchiura君は体力には自信ありそうだからいいけど、締切が重なってくるとみんな残業残業で寝不足の山よ"),
            sana.talk("実際ハードワークだからってことで、長続きしない人が多い職場でもあるもの"),
            tsuchi.talk("みんな机汚いっすもんね"),
            _.talk("そういやあの先生"),
            sana.talk("$noto？"),
            tsuchi.talk("そうそう。なんでラノベなんすか？　文芸だったんでしょ？"),
            sana.talk("たぶんどっちでもいいのよ。けど、この十年小説書いてないから。この前やっと久しぶりに短編を書いたの"),
            tsuchi.talk("それで作家なんてふんぞり返ってんのは流石にどうなんすかね"),
            sana.talk("色々と事情があるんでしょ。でもそんなことも呑み込んで、良い作品が書ける準備を整えてあげることが編集の仕事よ"),
            tsuchi.talk("まあ、$meは給料さえ貰えればなんでもいいっす"),
            sana.talk("そう"),
            _.do("苦笑"),
            ## NOTE
            ##  ここでやっと土浦の人となり。やる気はなくて、ただ金の為とだけ（そこらが韮崎と後々感性が合ってくる）
            stage=w.on_famires_int,
            ).omit()

def sc_newyearparty(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, king, tsuchi = W(w.nirasaki), W(w.king), W(w.tsuchiura)
    return w.scene("新年会にて",
            sana.explain("一月の十三日、午後からはホテルで会社の新年会が行われた"),
            sana.be("珍しくスカート姿で会場にいる"),
            tsuchi.be("だが穴あきジーンズ姿の$S"),
            sana.talk("こういうところに来る時はせめてもう少しマシな格好をしてきて"),
            tsuchi.talk("何言ってんすか。このジーンズ十三万すよ！"),
            sana.do("顔を覆う"),
            sana.talk("やっぱり先生来てくれなかったな"),
            nira.come("シャンペン片手にやってきて"),
            nira.talk("何やってんだよ。さっさと作家に顔合わせしてこい"),
            sana.talk("$meの担当してる人ほとんど来てないし"),
            nira.talk("別に自分の担当じゃなくてもいい。作家はみんな不安なんだから"),
            _.talk("とにかく声と名刺くらいは配っとけって。編集は人脈が命だ"),
            sana.talk("そういうもんですか"),
            nira.go("手を振って行ってしまう"),
            king.come("やってきて"),
            king.talk("どうかね。うまくやってるか？"),
            sana.talk("はあ"),
            king.talk("うちで書いてもらえそうな先生いたらツバつけといてよ"),
            king.go(),
            tsuchi.talk("なんか大変すね"),
            sana.talk("まあ、ね"),
            _.think("$nirasakiが言うことも分かってはいた。だが沢山に声をかけても覚えていなかったら意味がないだろう"),
            _.think("$fukayaから人脈は確かに大事だけど、それが名刺集めになってたら意味がないと言われたことを思い出す"),
            sana.talk("名刺を貰っても五分で顔も名前も忘れる。でも情熱をもって話せばそのことだけは覚えてもらえる"),
            tsuchi.talk("人付き合いとかめんどいっす"),
            sana.talk("あんたは気楽でいいわね。人生楽しいでしょ？"),
            tsuchi.talk("最近格闘ゲームでプロもいいかなって思ってるんす。知ってます？　プロゲーマーって"),
            sana.talk("話には聞いてるけど、なかなか難しいんじゃない？"),
            tsuchi.talk("でも小説だってもとを正せばただの趣味みたいなもんなんだから、それが金にできる世の中になれば関係ないんじゃないすか？"),
            sana.talk("一理あるわね"),
            _.think("考え込む"),
            tsuchi.do("スマホで何かしている"),
            sana.talk("何してんの？"),
            tsuchi.talk("ＳＮＳで面白いつぶやき探してるだけ"),
            sana.talk("うちの先生は機械オンチだからそういうの全然駄目で助かってるけど"),
            _.talk("この前$nirasakiさんが文句言ってた。どうでもいいことで噛み付いて炎上した作家の新刊が半年延期になったって"),
            _.talk("ほんと、面倒ばかりじゃない、そんなの"),
            tsuchi.talk("変なこと書かなきゃいいだけっすよ"),
            _.do("スマホの画面を見せる"),
            sana.talk("え……"),
            tsuchi.voice("新年会なう。ご馳走と共に"),
            sana.talk("何勝手に個人情報垂れ流してんのよ！"),
            sana.do("慌てて削除させる"),
            sana.talk("先が思いやられるわ……"),
            ## NOTE
            ##  新年会。ここでノミオとかと顔合わせしておく。あと野迫川もこっそり遭遇させておく
            ##  さり気なく新人賞選考会の話も出す
            camera=w.sana,
            stage=w.on_hotelhall,
            day=w.in_newyearparty, time=w.at_afternoon,
            ).omit()

def sc_ourparty(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("私たちの新年会",
            sana.explain("しかし言われた通り、新年会には先生の姿はなかった",
                "出産を控えている$fukaya先輩は流石に出席しなかったが、それでも一文の面々も集まりなかなかの賑わいだった",
                "$Sは早々に酔っ払った茶髪君の介護であまり多くの作家先生とは話せなかったが、それでもライトノベルの先生方は思ったよりも若い人は少なく、",
                "大半が$Sより年上ばかりだった"),
            sana.explain("その夜、$Sたちシェアハウスの三人も、ささやかながら新年会を開いた"),
            gero.be("#座っている"),
            azu.come("#鍋を運んできて"),
            sana.be("#飲み物を入れている"),
            sana.explain("#準備はみんなでした"),
            sana.explain("目の前にの鍋には$Sの冬のボーナスを投入した牛肉がたっぷりと入っており、野菜や豆腐と共に美味しそうに煮えている",
                "三人で暮らすようになって初めて開いた飲み会の時も今みたいにすき焼き風鍋をしては、夜中まであれやこれやと話し合ったことを思い出す",
                "四月に$azuが加わってから最初こそややギクシャクした感じがあったが、今は何でも相談し合える仲になったと$Sは思っている"),
            sana.talk("じゃあ、乾杯！"),
            gero.talk("おーし。飲んで食うぞー"),
            azu.talk("明日も仕事だからほどほどにね"),
            gero.talk("そういや$azuはあれなんやない？　もうすぐ一次発表"),
            azu.talk("それ言わないで。胃がきりきりするよ"),
            sana.think("胃がきりきりするのは$Sの方だった",
                "何故自分のところの新人賞に応募をしたのだろう",
                "そして、その原稿の審査をしたのが自分だとは、未来永劫言い出せないんじゃないかと思えた"),
            azu.talk("どうしたの、$sana？"),
            sana.talk("ううん、ちょっと先生のことで思い出しただけ"),
            gero.talk("どうせまた無理難題ふっかけられとるんやがね"),
            sana.talk("今度は長編だから時間かけて取り組んでくれてるみたいだけど、新年会も出てくれなかったし、やっぱりライトノベルのレーベルじゃあ力が発揮できないんじゃないかなあって"),
            sana.think("一度、単刀直入に訊いてみた方が良いのだろうか",
                "$fukaya先輩の顔が浮かんだけれど、出産を間近に控えた彼女に頼る訳にもいかず"),
            sana.talk("ああ、もう", "とにかく飲む"),
            gero.talk("おう、その意気やよしだがね"),
            azu.talk("でも飲みすぎは駄目だよお", "明日もみんな仕事あるし"),
            gero.talk("分かっとるがね", "だが時には羽目を外すことも学ばにゃあかん"),
            gero.do("そう言って$geroは何故か上着を脱ぎ始めた"),
            azu.talk("あーん！", "もう酔い始めてるじゃないのぉ"),
            sana.do("困り顔になった$azuと、にへらと破顔した$geroを見て、$Sはグラスのビールを流し込んだ"),
            ## NOTE
            ##  久々にゆっくり三人で話す会
            ##  今後に向けて英気を養う部分であるが、SNSのことを話題にしておく（後に利用する）
            stage=w.on_herhouse_int,
            time=w.at_night,
            )

## episode
def ep_nextstory(w: World):
    return w.episode("4.続雪国",
            ## NOTE
            sc_newperson(w),
            sc_guideoffice(w),
            sc_greeting(w),
            sc_printing(w),
            sc_abouteditor(w),
            sc_newyearparty(w),
            sc_ourparty(w),
            )
