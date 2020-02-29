# -*- coding: utf-8 -*-
"""Episode: 10-1.カムパネルラはどこに消えた？／銀河鉄道の夜
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
def sc_whereishe(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    gero, azu = W(w.gero), W(w.azumino)
    pc = W(w.mobilepc)
    return w.scene("先生はどこへ？",
            w.comment("バイト君から先生失踪の報を受けた沙奈"),
            ## NOTE:
            ##  冒頭文：ではみなさんは、そういうふうに川だと言われたり、乳の流れたあとだと言われたりしていた
            sana.be("スマホを手にした右手から急速に熱が失われていくような気分で、$Sは固まっていた", "&"),
            _.think("『銀河鉄道の夜』のジョバンニもこんな気持ちになったのだろうか、と考えるくらいには、酷く混乱していて、",
                "今一度頭の中で$ln_tsuchiuraの言葉を整理してから聞き返す"),
            sana.talk("先生が、病院から、消えた？", "あんたのその日本語は正しいのね？"),
            tsuchi.voice("何言ってんすか！", "とにかく何も言わずにするっと病室からドロンですわ！"),
            sana.think("するっとかドロンとか、相変わらずの語彙の無さと表現力をどこかに置き去りにしてきた文章だったが、",
                "緊急事態だということだけは理解できる"),
            sana.talk("ちょっと待って","分からない", "そもそもどうして先生が病院から消えなきゃならないの？", "何かのミステリ？"),
            tsuchi.voice("$meだって知らないっすよ",
                "とにかく何とか朝起きて仕事しに来たら看護師さんが騒いでて", "とてもあんな火傷で出歩いていいもんじゃないって"),
            sana.talk("分からないけど分かったから、そこで待ってて！", "いや、病院内を探しててて！"),
            tsuchi.voice("ててて、って。落ち着いて下さいよ"),
            sana.talk("落ち着ける訳ないでしょ！"),
            _.do("電話を切り、$Sはスマートフォンをテーブルに放り出して天を仰ぐ"),
            _.think("今日が先生の原稿の最終締切日",
                "それに何とか間に合わせるようにと明け方まで掛けて初めて長編小説を完結させた",
                "それに意味なんかないことは充分理解しているけれど、『$master_shortnovel1』の掲載を滑り込みで決めたように何か奇跡でも起こるんじゃないかと、",
                "そんな神頼みにも似た思いだった", "それがだ"),
            _.talk("なんでこう次から次に不運が襲いかかってくるのよ！"),
            gero.talk("$sana、うっさいがね！"),
            sana.do("$geroの壁ドンに心の中で謝罪してテーブルの上のマウスに手を掛ける","&"),
            pc.look("スリープアウトしていたモニタが光り、書き終えた原稿の最終ページが浮かび上がった",
                "右下に表示されている時刻は既に十時を回っている"),
            sana.think("会社に連絡を入れた方がいいだろうか"),
            _.do("それを考えるより前に、とりあえず顔だけでも洗おうと立ち上がった"),
            ## NOTE
            ##  慌てた心境と、最終回の騒動を想像させる
            camera=w.sana,
            stage=w.on_herhouse_int,
            day=w.in_vanishmaster, time=w.at_midmorning,
            )

def sc_investigation(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("先生の捜索",
            w.symbol("　　　　◆"),
            sana.come("それから三十分後、五分でメイクを終えポーチにスマホと財布を放り込んだ$Sは慌ててタクシーで病院に駆けつけた"),
            sana.talk("あ、いた。ね、見つかった？"),
            tsuchi.be("ロビィでうろうろしている$Sを見つけて声を掛けると「やっと来た」といった表情を見せながら彼は椅子から立ち上がる"),
            sana.talk("ちゃんと探してたの？"),
            tsuchi.talk("探すも何もあのおっさん、窓から出てったんすよ？"),
            sana.talk("は？"),
            sana.explain("彼が看護師から聞いたところによると、個室のカーテンが結ばれ三階の窓から中庭まで垂れ下がっていたらしい",
                "それに加えて入院着姿の長身の男性がタクシーの列に強引に割り込んで出て行ったという目撃証言もあり、先生が既に病院内にいないことは確実なようだった"),
            sana.talk("なんてことなの……"),
            tsuchi.talk("ほんとにあのおっさん、作家なんすか？", "$meでもあんな状態で病院抜け出そうなんて思わないすよ"),
            sana.think("$fukaya先輩から聞いた数々の作家缶詰伝説が脳裏を過った",
                "一番酷かったのはホテルのルームサービスの制服に着替えて部屋を抜け出し、友人たちとクラブで飲み歩いていた作家がいたという",
                "先生はそんなことをするようなタイプとは引き継ぎのメモにもなかったし、実際にこの半年ばかり接してきた$Sもやらない人だと判断していた",
                "だからこそ尚のこと、今回の脱走騒動は得心がいかない"),
            sana.talk("ほんと作家ってやつは！"),
            _.do("その声の勢いのまま長椅子を蹴飛ばしそうになったが、周囲の看護師や入院患者の視線に気づいて振り上げた足をリノリウムの床に不時着させた"),
            sana.talk("仕方ないけど手分けして探すしかないわね"),
            tsuchi.talk("探すってどこを？"),
            sana.talk("$a_tsuchiはバイクで近所回って目撃情報とか何かないか当たってみて",
                "$meは先輩や$nirasakiさんに連絡して協力を仰ぐ。とにかく先生が行きそうな場所を片っ端から当たってみる",
                "何かあったら連絡ちょうだい！"),
            ## NOTE
            ##  改めて状況説明
            area=w.Mitaka,
            stage=w.on_hospital_int,
            time=w.at_beforenoon,
            )

def sc_writervisit(w: World):
    sana, noto = W(w.sana), W(w.noto)
    yuza = W(w.yuzawa)
    return w.scene("記者さんお願い",
            w.br(),
            sana.come("頭に血が上ったまま苛立つ足取りで病院から出てくると、目の前で突然フラッシュが炊かれる"),
            yuza.be("#待ち構えていて"),
            yuza.talk("どうです、先生の具合は"),
            sana.talk("あー！"),
            sana.explain("雑誌記者の$yuzawaだった", "まだしつこく先生のインタビュー機会を狙っていたのだ"),
            yuza.talk("相変わらずうるさいな、あんた。それより送りつけたアレは楽しんでもらえたかい？",
                "こっちは全部のコピー持ってる。あの作家先生がどれだけ否定したところで第二第三の弾があるんだ",
                "もしインタビューさせてもらえるなら今週掲載予定の分は見送ってもいいとデスクも言ってるが、どうだ？"),
            w.eventPoint("先生の盗作騒動", "$yuzawaは原稿オリジナルを持っている"),
            sana.talk("その件について実は相談があるんですけど、その前に"),
            _.explain("$Sは手早く先生の失踪を伝える"),
            yuza.talk("は？　病院から消えた？　なんだいそりゃミステリか？"),
            sana.think("全く同じ感想を呟いた彼に共感を覚えつつも、", "&"),
            sana.do("とにかくとその手を掴み、彼のバイクへと急ぐ"),
            yuza.talk("お、おい。何だよ？",
                "今まで取材拒否だなんだって散々遠ざけてたのに急にナンパか？",
                "一応$meはこれでも既婚者だからな。そういうのはやめろよ？"),
            sana.talk("何勘違いしてるんですか？",
                "先生を探すの手伝って下さい", "&"),
            _.talk("先生見つけたら好きなだけ取材してくれて構わないから！"),
            yuza.talk("まあ、そういうことなら……って、おい！"),
            sana.think("$tsuruの原稿の話を持ち出され、$Sはある可能性を思いついてしまった",
                "けれど決してそんな悲劇的な選択を先生がするとは信じたくない",
                "だからこそ一刻も早く先生を見つけなければならなかった"),
            sana.talk("早く！　行きますよ！"),
            yuza.talk("何なんだよ、急に……"),
            ## NOTE
            ##  誰でも味方につけてしまう沙奈の能力発動
            ##  湯沢はあまり活躍シーンないので、この道中で多少彼の人となりを見せておく。それがどこか親心みたいなものに繋がっているように
            ##  沙奈はファザコンであること
            stage=w.on_parking,
            )

def sc_anywhere(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    yuza = W(w.yuzawa)
    chiyo = W(w.chiyoda)
    return w.scene("どこにもいない",
            sana.come("行きつけの喫茶店にやってくる"),
            yuza.come("一緒にやってきて"),
            chiyo.be("掃除をしている"),
            sana.talk("あの、先生来てませんか？"),
            chiyo.talk("最近見てないわ。入院したって聞いたけどぉ？"),
            sana.explain("簡単に説明して、何か手がかりがないか訊いてみるが、分からないとのことだった"),
            sana.talk("ほんと、もう！"),
            ## NOTE
            ##  千代田さんもここくらいしか出番がないので、印象づけておく（あるいは後でちょろっと出す）
            ##  ここはDE候補でカット
            stage=w.on_mastercafe,
            time=w.at_noon,
            ).omit()

def sc_accident(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi, fukaya = W(w.tsuchiura), W(w.fukaya)
    yuza = W(w.yuzawa)
    utsu = W(w.utsu)
    return w.scene("人身事故報道",
            sana.come("やや苦手なバーにやってくる"),
            yuza.come("一緒にやってくる"),
            utsu.be("グラスを磨いている"),
            sana.talk("すみません、先生探してるんですが"),
            utsu.talk("また逃げられたんでしょうか"),
            sana.talk("そうじゃないんですけど、そうでもあるんです"),
            utsu.look("苦笑している"),
            sana.explain("だが何も分からないまま"),
            sana.explain("そこにテレビでちょうど中央線の人身事故報道"),
            sana.talk("え？"),
            sana.explain("ちょうど年齢や背格好が同じに"),
            sana.do("そこに$fukayaから連絡"),
            fukaya.voice("先生見つかった？"),
            sana.talk("いえ、まだです"),
            fukaya.voice("そっか。今日、なのよね"),
            sana.talk("何がですか？"),
            fukaya.voice("ちょっと気になることがあって"),
            sana.talk("はい","え？", "玉川上水？"),
            fukaya.voice("$meが行ってあげられたらいいんだけど、もしもの時は$sana、お願いね"),
            sana.think("先生にまさかはないと思いたい。でも自殺しないとは断言できなかった"),
            ## NOTE
            ##  バーもここくらいなので、印象づけておく
            ##  ここもDE候補でカット
            stage=w.on_masterbar,
            ).omit()

def sc_river(w: World):
    sana, noto = W(w.sana), W(w.noto)
    yuza = W(w.yuzawa)
    tsuchi = W(w.tsuchiura)
    return w.scene("玉川上水",
            w.symbol("　　　　◆"),
            sana.come("#先生と歩いた玉川上水に"),
            yuza.come("#一緒に歩いている"),
            sana.explain("行きつけの喫茶店、ファミレス、コンビニ、本屋",
                "それらは全て空振りだった"),
            yuza.talk("で、なんで玉川上水なんだ？", "まさか太宰治よろしく誰かと心中するってか？"),
            sana.do("かつて先生と二人で巡った玉川上水を歩いていた",
                "川には小雨がぱらつき、小さな波紋をいくつも作っている",
                "傘を持っていない二人はただ濡れるがままで歩を進めているが、どちらも傘の購入を申し出ない"),
            sana.talk("心中とか、妙なこと言わないで下さいよ"),
            yuza.talk("けどな、盗作した作家の末路ってのは本当に悲惨なもんだぜ",
                "それが一度有名になった作家なら尚の事",
                "世間は忘れても自分は一生忘れねえ。そういう業の深い行いが盗作なんだぜ"),
            sana.think("盗作、という言葉の重みは一般人よりは理解しているつもりだった",
                "事実、先生はあの日記の告白文でずっと苦しんでいる胸の内を綴っていた"),
            sana.think("けれど$Sには妙な引っ掛かりがあり、どこかボタンの掛け違えのようなことが起こっているんじゃないだろうかと思えて仕方ない",
                "そもそも本当に盗作に手を出したのであれば、苦しくなった時に再び盗作に手を出すんじゃないだろうか",
                "しかしそんな素振りも志向も先生の執筆には一ミリと見えないのだ"),
            _.think("これは$Sの編集として直感だが、今はその感覚を信じたかった"),
            sana.talk("そもそも何故先生は病院を出たんだろう", "締切のため？", "ううん。もう原稿はないんだし、それなら他に何か理由が"),
            yuza.talk("盗作をしていた、という証拠があるならその隠滅だな",
                "後ろめたいところがある奴は何かと隠したがるものだ",
                "実際デビュー当時はその人気もあり有耶無耶にされたが、ライトノベルで再デビューしようという矢先に盗作騒動で作家生命潰されたら、",
                "今度こそ完全に終わりだからな"),
            sana.think("一人の作家生命を終わらせようとしている本人の言葉だけあって、耳から毒薬を入れられている心地がする"),
            sana.talk("あの、$yuzawaさん。ちょっとお願いがあるんですけど"),
            yuza.talk("な、何だよ？"),
            sana.talk("あなたが持っている$tsuruさんの原稿、全部見たいんです。どうしても確かめたいことがあって。お願いです"),
            _.do("$Sはそう言って頭を下げると、", "&"),
            yuza.do("$yuzawaは「駄目だ」と言いかけた口を閉じて腕組みをした"),
            yuza.talk("本当に先生のインタビュー、やらせてくれるんだな？　それも独占で"),
            sana.talk("はい"),
            _.do("営業用のＡ５ランクの笑顔で$Sは答えたのだった"),
            w.eventPoint("先生の盗作騒動", "敦賀の原稿を見せてもらうよう頼む"),
            ## NOTE
            ##  ここで沙奈は気づく
            stage=w.on_tamagawariver,
            time=w.at_afternoon,
            )

def sc_hurry(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    return w.scene("急げ",
            w.comment("沙奈はある場所に急いだ"),
            sana.be("運転席で慌てた様子でいる"),
            sana.do("車である場所に急いだ"),
            sana.think("お願い、間に合って"),
            sana.do("やがて見えてくる"),
            sana.do("太宰の墓がある場所。そこに彼の親友の墓もある"),
            stage=w.on_car_int,
            ).omit()

## episode
def ep_campanella(w: World):
    return w.episode("1.カムパネルラはどこに消えた？",
            ## NOTE
            sc_whereishe(w),
            sc_investigation(w),
            sc_writervisit(w),
            sc_anywhere(w),
            sc_accident(w),
            sc_river(w),
            sc_hurry(w),
            )
