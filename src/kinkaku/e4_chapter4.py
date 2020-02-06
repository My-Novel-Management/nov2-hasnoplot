# -*- coding: utf-8 -*-
"""Episode: 8-4.第四章／金閣寺
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
def sc_writing(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    nira, tsuchi, king = W(w.nirasaki), W(w.tsuchiura), W(w.king)
    return w.scene("久々の執筆",
            w.comment("$notoの盗作騒動について、どう処理したのか、何もしていないのか、どう考えているのか、について記載しておくこと"),
            w.comment("久々の休日に、家でじっくり執筆を"),
            sana.be("#自室でノートパソコンを前にしている"),
            sana.explain("あの後すぐに先生に電話で盗作の件について確認してみたけれど、いつもの調子で「そんなことをすると君は思うのか？」とからかわれた",
                "$nirasakiが持ってきた週刊誌に載るんじゃないかというネットの噂もそれ以降続報はなく、",
                "半ば肩透かしのような思いでいる"),
            sana.think("――まあ、よくあるネットのフェイクニュースだったなら別にいいんだけど"),
            sana.explain("三月の最初の日は久しぶりの休日だった",
                "既に時計は正午を過ぎているが、まだ寝足りないという思いが強い"),
            sana.talk("けど、今日は書かなきゃ"),
            sana.explain("先生と約束した長編小説は、未だにプロットを作りかけた状態のまま放置してあり、いい加減に書き始めないと締切までに間に合わないことが判明して、",
                "内心ではかなり焦りを感じていた", "&"),
            sana.explain("それでも午前中に起きる予定が二時間以上も余分に夢の中だったことに、若い頃のように何日もほとんど寝ずに書くなんて真似はもう無理なんだな、と情けなくなる",
                "$geroなんかはコミケ前には一体いつ寝ているのだろうという有様だったけれど意外とケロッとあの地獄の四日間をクリアしていたから、",
                "絵描きも体力勝負なのだと実感する", "何より現役はやはり強い"),
            sana.do("リビングを覗くと$geroはアルバイトに出かけたようで、本を開いたままテーブルに突っ伏して眠りこけていた$azuの姿だけが見つかった"),
            azu.talk("あ、$sana", "おはよー"),
            sana.talk("ごめん、起こした？", "寝ちゃってていいよ",
                "バイト増やしたばかりで疲れてるんでしょ？"),
            sana.explain("$azuは先週から駅前のパン屋で週に三日、働くようになった",
                "&"),
            _.think("それが彼女の心境の変化によるものかそれともただ経済的な事情によるものか、$Sには判断がつかなかったが、",
                "ずっと落ち込んでいるよりは何かに没頭していられる方が今の彼女にとっては良いのかも知れない、と思っている"),
            sana.do("キッチンのコーヒーメーカーで新しくコーヒーを沸かすと、タンブラーに注いで備蓄のバターロールと一緒に部屋に持ち運ぶ",
                "ウェットティッシュを準備してテーブルにパソコンを広げると、電源を入れて起動音を聞き、コーヒーを一口啜った"),
            _.think("パソコンが立ち上がるのを待ちながら、ふと考えてしまう",
                "どうして自分まで長編小説を書かなければいけないのだろうかと", "&"),
            _.think("これを書かなくても誰も何も言わないだろう", "誰かに見せると言っても相手は先生くらいしかいない", "&"),
            _.think("誰にも読まれない小説を書くことはとても虚しい作業なんじゃないかと、$noseが語っていた言葉を思い出しながら$Sは考えていた"),
            sana.talk("そういえばあの人、先生に会いに行ったのだろうか"),
            sana.think("押し倒された時は正直人生の色々なものを全て駄目にされそうな気がした",
                "鬼気迫るとはああいう表情のことを言うのだろう",
                "それこそ鬼だ", "冷静さを失えば人間は容易に壊れてしまうのかも知れない"),
            sana.do("スマートフォンには何の連絡も入っていないことを確認し、パンを齧る"),
            sana.do("パソコンのモニタには滅びた世界をイメージするように荒涼とした砂漠を背景に設定してあったが、",
                "それを目にした途端に砂嵐に襲われた気分になりマウスを持つ手が脱力するのを感じた"),
            sana.think("原稿を書く前から何も思い浮かばない"),
            sana.talk("あー、なんか部屋だとまったりしちゃうのかも"),
            sana.do("ロールパンを口に詰め込み、コーヒーで流し込んで、ワープロソフトを立ち上げる",
                "原稿には仮タイトルとして『$snovel1kari』とあるが、そこに続く文章は一行も書かれていない",
                "同時にスケジュール管理ソフトも立ち上げて残り日数を確認するとあと二週間強しか残されていない",
                "一日に何文字書けばいいかを表示して絶望に叩き落とされつつ、それでも書き始めようキーボードに指を置くのだが、",
                "まだ思考回路のエンジンは掛かりそうにない"),
            sana.talk("仕方ない"),
            sana.do("ノートパソコンをスリープにして折り畳み、それを鞄に突っ込むと、部屋の電気を消してリビングに出た"),
            azu.talk("あれ？　仕事？"),
            sana.talk("ううん、違うけど、まあ似たようなものかな", "ちょっと喫茶店でも行ってくる"),
            sana.go(),
            ## NOTE
            ##  バイトを始めた安曇野のことと、彼女の落選の事実を突きつけられた後の心境変化をここで
            stage=w.on_herroom,
            day=w.in_firemaster, time=w.at_noon,
            )

def sc_aboutmaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, tsuchi, king = W(w.nirasaki), W(w.tsuchiura), W(w.king)
    inside = W(w.inside)
    return w.scene("先生について",
            sana.be("そこは時々使わせてもらっている、落ち着いた雰囲気の昭和感漂う喫茶店だった"),
            inside.look("還暦を過ぎていると思える女性店主が一人で切り盛りしている席数二十ほどの狭い店内で、", "&"),
            sana.do("$Sはいつも窓際の席を使っていた"),
            sana.do("作業中、それも小説に関わる作業をしている時はできる限り音楽は聞かない",
                "それは音や歌声で意識が散漫になるのを防ぐ為でもあるけれどそれ以上に周囲のちょっとした環境音や話し声の方が、意外と集中できる",
                "学生時代から変わらない、$Sの執筆スタイルだった"),
            sana.do("パソコンを広げて作品を書きながら、先生の創作ノートを確認する", "&"),
            sana.do("開いたページはサブストーリーについて書かれていた"),
            sana.explain("長編になるとメインとなるストーリーラインだけでは物語の筋道が単調になり、また登場人物の心情や履歴のエピソードを書くには使いづらい",
                "そこでサブストーリーが必要となる",
                "サブストーリーとは人物や世界観を広げる為のエピソードであり、時にはメインストーリーと入れ替わるようにして物語の前面に出てくることもある"),
            sana.talk("ただしあまりサブストーリーに力を入れすぎると本筋を見失い、物語の向かうべき方向を見失ってしまう",
                "酷い場合にはストーリーが破綻し、最悪書き続けることが不可能になり、作家はその物語を書くことを止めてしまうだろう……って、",
                "よくあるパターンだ"),
            sana.explain("自分の学生時代のことを思い出す",
                "いつも書き始めは楽しくて、でも書いている内にどんどん当初の思惑とは別方向へと物語が転がっていき、",
                "やがて収集がつかなくなって書くのを止めてしまう",
                "それでも何とか書き進めたいと思って考えているうちに別の物語や設定を思いついてしまい、",
                "そっちを書き始めてしまう"),
            sana.explain("作家の中には最初から一つの物語を完結まで書き終えた、という人がいる",
                "そういう人たちはきっと頭の構造が違うのだと思っていたのだけれど、先生が言うには彼らはただ一度書き始めたものにきっちりとエンドマークを付けたい性分なだけらしい",
                "それはそれで一つの才能だと思うが、果たして今の自分に長編小説を最後まで書き切る力や意志の強さがあるのか、自信を持てなかった"),
            sana.do("少しプロットや人物を整理して物語の道筋をしっかりさせてから書き出すと、意外と指が動く",
                "$Sはスマートフォンをマナーモードにして、しばらく自分の物語の世界に没頭した"),
            stage=w.on_cafe,
            time=w.at_afternoon,
            )

def sc_emergency(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, tsuchi, king = W(w.nirasaki), W(w.tsuchiura), W(w.king)
    gero, azu = W(w.gero), W(w.azumino)
    tv = W(w.tv)
    return w.scene("緊急事態",
            w.comment("火事のニュースに出ていたのは先生のアパートだった"),
            sana.come("マンションに戻ってくると遠くで救急車と消防車のサイレンが入り混じって鳴っているのが聞こえた"),
            sana.hear("#遠くでサイレン"),
            sana.talk("ただいま"),
            sana.think("何だろう、と思いながら玄関を入ると壁で逆立ちをしている$geroが目に入る"),
            gero.talk("あー、おーかえりー", "なんか美味いもんでも買ってきてくれた？"),
            sana.do("コンビニの袋が目に入ったのだろう"),
            sana.talk("新発売あったけど今日は見送った", "それより火事？"),
            tv.look("リビングの三十二型には現場のライブ映像だろうか、野次馬の前でアナウンサーが大声を張り上げて喋っている",
                "その背後には三台の消防車と多くの消防隊員の姿が映り、もうもうと煙を上げてアパートが炎上しているのが分かった"),
            azu.come(),
            azu.talk("そうみたい。$tvで三鷹の方って言ってるけど"),
            sana.do("台所で夕食でも作っていたのだろう",
                "エプロン姿で顔を出した$azuは"),
            sana.talk("え？　ちょっと待って"),
            sana.think("$azuの言葉で急激に嫌な予感が浮上し、", "&"),
            sana.do("$Sは慌ててスマートフォンで先生に連絡を取ろうと電話を掛ける",
                "一回、二回……繋がらない", "まだ焦ることはない、先生が電話を取らないことなんて今まで何度もあったじゃないか"),
            sana.think("それでも結局電話は繋がらず、溜息と共にスマートフォンをよく確認すると、先生からの着信履歴が三十分ほど前に残っていた"),
            sana.talk("あれ？　何だったんだろ"),
            _.think("酷い胸騒ぎがする", "というかお腹の中に入れた肉まんが元の世界に戻りたそうに暴れている"),
            sana.talk("ごめん。$me、ちょっと行ってくる"),
            sana.do("$Sは慌ててスニーカーに足を通し、玄関を飛び出る"),
            sana.talk("すみませーん！","乗ります！"),
            sana.do("通りに出たところで止まっていたタクシーを親切な初老の男性に譲ってもらい、先生の家へと急いだ"),
            stage=w.on_herhouse,
            time=w.at_evening,
            )

def sc_burning(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, tsuchi, king = W(w.nirasaki), W(w.tsuchiura), W(w.king)
    poli = W(w.police)
    return w.scene("燃え盛るアパート",
            w.comment("かけつけた沙奈は燃える先生のアパートを見て呆然と"),
            sana.come("#やってくる"),
            sana.do("$Sが現場を訪れた時には既にすごい人混みで、目の前には野次馬の頭がずらりと壁を作っていた",
                "飛び上がっても煙しか見えず、", "&"),
            sana.hear("近所のおばさんたちの会話の中に「古い木造アパートが燃えてるんですって」と聞こえた"),
            sana.talk("ちょっと、すみません", "通して、下さい、ね"),
            sana.do("何とか人垣を掻き分けて小さな体を野次馬の最前列まで持っていくと、そこには通い慣れた先生のボロアパートがキャンプファイヤーみたいに轟々と音を立てて燃え盛る様が、",
                "視界に飛び込んできた",
                "火の粉が舞い上がる中に消火剤が振りかけられる",
                "あんなものでどれくらい延焼が防げるのか分からないが、少なくともアパートはもう全焼を免れないだろう"),
            sana.talk("先生が……"),
            sana.think("一瞬、最悪の想像をしてしまったが、激しく首を左右に振ると、", "&"),
            sana.do("$Sは立っている警察の制服に掴みかかり、中の人が無事なのかを訊いた"),
            sana.talk("あの、先生……中の住人は？"),
            poli.talk("今助けに入っているところだ", "とにかく危ないから離れなさい"),
            sana.talk("嫌です！", "$meの大切な人があそこにいるんです！"),
            poli.talk("君は、家族か何かか？"),
            sana.talk("彼の、担当編集です！"),
            sana.do("そう答えた$Sの目が、消防隊員二名に覆われるようにして中から出てくる一つの影を捉えた"),
            sana.talk("先生！"),
            poli.talk("おい、こら！"),
            sana.do("顔が煤けていたが、紛れもなくそれは先生だった"),
            sana.talk("先生、大丈夫なんですか？"),
            noto.talk("ああ、$sana君。ごめん。原稿、焼けちゃったよ"),
            noto.do("力なく答えると、彼は手にぎゅっと握りしめていた原稿の燃え滓を$Sに差し出した"),
            sana.do("#それを受け取り"),
            sana.talk("原稿よりも先生が"),
            noto.talk("$meは死なない。大丈夫だ"),
            poli.talk("とにかく救急車に乗せるから、退きなさい。そもそも君はご家族か何か？"),
            sana.do("険しい表情の消防隊員に言われ、$Sは小さく首を振り、後ずさる"),
            noto.go("先生はそのまま担架に上げられ、救急車へと収容され、この場から運び出されていった"),
            sana.think("$Sは未だ火勢の衰えない先生の住処を見やり、ただ「どうしよう」という思いだけに支配されていたのだった"),
            ## NOTE
            ##  放火したのは野迫川である
            stage=w.on_hisapart,
            time=w.at_night,
            )

## episode
def ep_chapter4(w: World):
    return w.episode("4.第四章",
            ## NOTE
            sc_writing(w),
            sc_aboutmaster(w),
            sc_emergency(w),
            sc_burning(w),
            )
