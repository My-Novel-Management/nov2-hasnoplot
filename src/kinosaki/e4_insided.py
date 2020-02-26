# -*- coding: utf-8 -*-
"""Episode: 6-4.心の内にて／城の崎にて
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
def sc_exchange_condition(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("交換条件",
            w.comment("長編原稿を捨てた先生に対して、沙奈も書くからもう一度チャレンジしてと頼む"),
            sana.be("#寝ている"),
            sana.hear("翌朝$Sが目を覚ましたのは、遠くで響く雷鳴を聞いた気がしたからだ"),
            noto.be("#ゴミ箱の前にいる"),
            sana.talk("先生？　何、してるんですか？"),
            noto.do("見ればゴミ箱の前に座って、一枚一枚原稿を引き裂いてはそこに捨てていた"),
            sana.talk("先生！"),
            sana.do("それに気づいて慌てて布団を抜け出そうとして足が抜けずに、$Sは派手に転んでしまう"),
            noto.talk("おはよう、$sana君",
                "朝から実に騒々しいことだ"),
            sana.talk("何言ってるんですか！",
                "そんなことより折角書き始めた長編小説の原稿、どうして破り捨てたりなんかするんです？"),
            noto.talk("$sana君は散々酔っ払ったあくる朝、アルコールで高揚した気分の中で自分がしでかしてしまった恍惚の正体が実は醜い獣だったと気づいた時、",
                "それを処分したい気持ちにならなかったかね？"),
            sana.talk("学生時代に一度だけ酷く酔って、もう二度と二日酔いはごめんだって思いましたけど、前後不覚になって目覚めたら血だらけみたいな経験はまだないです"),
            noto.talk("そうかい",
                "まあ君に見せるまでもないがね、こんな作品は$meのものじゃないと分かった"),
            sana.talk("でも明日になれば今破り捨てたことを後悔したりしませんか？"),
            noto.talk("後悔するくらいなら最初から書かなければ良い",
                "そもそも書いたと言うだけのものは原稿ではなく、ただの文章だよ。文字の塊だ", "駄文とすら呼べないよ、こんなものは"),
            noto.do("$CSが何も言い返せないのを確認すると、先生は二十枚ほどの原稿用紙を全て処分し、進捗をゼロに戻した"),
            noto.talk("書いてみて分かったが、やはり$meには無理なんだよ",
                "もう小説は書けない"),
            sana.talk("何言ってるんですか？　ちゃんとこの前ああして素晴らしい短編小説を書いて下さったじゃないですか！",
                "あれは既に先生の小説として世間に出ているんですよ？", "新しくファンになったという人の声も編集部に来てます",
                "何より$meが先生の長編小説を待っているんです！"),
            noto.do("先生は「ありがとう」と力なく言い、テーブルへと戻って蜜柑を剥き始める"),
            sana.talk("編集の言葉は、いえ、$meの言葉は力になりませんか？",
                "信じられませんか？"),
            noto.talk("そういうことじゃないんだよ、$sana君",
                "作家は、いや、$meという生き物は分かっていると思うが実に面倒な性格をしているんだ",
                "けれどその面倒臭さが$meの小説を小説たらしめているとすれば、変に妥協したり、迎合したりして、その面倒くさい自分を曲げてはいけないと思うんだよ"),
            sana.talk("でも先生言いましたよね？　最初から完成している小説なんかないって", "&"),
            sana.talk("書き上げてからがスタートなんだって"),
            noto.do("そう言い切った$CSを、先生は拗ねた子どもみたいな目で見て「まあそうだが」と消えそうな声を漏らす"),
            sana.talk("でしょ？", "だったら一緒に作り上げていきませんか？", "駄作かどうかは作者が決めることじゃない。$meが決めることでもない","&"),
            sana.talk("読んだ誰かが面白かったかどうか、心を打ったかどうかです", "&"),
            sana.talk("評価なんて百人いたら百通りなんです"),
            noto.talk("その見知らぬ百人の評価より先に、作者自身の評価が駄目なんだよ",
                "あれをいくらがんばって校正したところでとても売り物にはできない",
                "そう感じるほどの出来だったということだよ。分かるだろう？"),
            sana.think("書き直せば何とでもなる",
                "そういう気持ちもあったが、やはり一度書いてしまったものはどんなにがんばって修正したところである程度までしか良くならないものだと、$fukayaに言われたことがある",
                "それでも先生なら何とかなるんじゃないかと言いたかったが、そこまでの自信も持てず言葉を探してしまった",
                "その僅かな隙間に先生の言葉が差し込まれる"),
            noto.talk("ほら答えられないだろう？",
                "作家というのはね、いくら周囲が書いたものを褒めたり喜んだりしたところで、自分が納得しなければ世間的にどんな傑作だったとしても、作者自身からすれば駄作なんだよ", "&"),
            _.talk("そりゃあいつだって心のどこかでは誰かに褒めてもらいたいしすごいと言ってもらいたい。傑作だと絶賛してもらいたい",
                "そういう気持ちが隠れているさ", "&"),
            _.talk("でもおおっぴらには口にできないから、常に自信なさげか、逆に見栄っ張りで、自分の作品がどうして評価されないって思ってる", "&"),
            _.talk("けどいざ書いている自作を読んでみるとこれ本当に面白いのだろうかと悩む", "&"),
            _.talk("そんなことの繰り返しなんだ"),
            noto.do("先生は髪を掻き毟り、大きな溜息と共にテーブルを叩いた"),
            _.talk("多くの作家が書けなくなる、続きを出せなくなるのは何も売上が全てじゃない", "&"),
            _.talk("やがて行き詰まるんだ", "&"),
            _.talk("自分の全てを否定されたような気になる", "&"),
            _.talk("それは作品だけじゃなく、自分自身の全てがそうなんじゃないか、", "&"),
            _.talk("この世界ではもう自分の作品は、いや、自分自身は必要とされていないんじゃないかって、そんな不安で押しつぶされる", "&"),
            _.talk("だから夜中に窓を開けて思い切り叫ぶこともある", "&"),
            _.talk("迷惑だからと公園まで出かけて走り回ったこともある", "&"),
            _.talk("でもそこまで自分が追い詰められて何とか捻り出した作品は本にすらならず、", "&"),
            _.talk("よしんば本になったとしても売れなくて、感想すらなく、担当に次がありますと言われて、大量の在庫と罪悪感を抱える", "&"),
            _.talk("大半の作家がそうなんだよ！"),
            sana.talk("先生！"),
            sana.do("気づくとその大きな体を後ろから抱き締めていた"),
            sana.talk("分かってます", "もうそれ以上、言わなくていいですから"),
            noto.talk("何が、分かるんだよ……"),
            sana.talk("全部は分からないかも知れない",
                    "けど、今辛いってことは分かります",
                    "小説がずっと書けなくて、その間苦しみ続けて、やっとこの前短編が何とか書けて、それで長編もっていざ書いてみたらやっぱり納得いかなくて",
                    "きっと人生ってそういうことの繰り返しなんだって、それくらいは分かりますから！"),
            noto.do("先生は黙り込んだまま、$CSの手を解こうとはしない"),
            sana.talk("全部一人で抱えなくてもいいんですよ",
                    "先生だって$geroのことを相談したらそう言ってくれたじゃないですか？",
                    "ね、先生",
                    "一人で書けないのなら、二人で書きましょう",
                    "短編小説を書いた時みたいに、今度は$meに長編小説の手引きをして下さい",
                    "そしたら、きっと奇跡の一つくらい、起こりますよ", "起こしてみせて下さいよ"),
            noto.talk("またそんなことを言って",
                    "君ね、簡単に長編小説を書くなんて言うけれど、短編と長編は全く違う",
                    "以前も説明したが、短編は思いつきと瞬発力と、書き上げてからの校正でいくらでも良く仕上げることが可能だ",
                    "対して長編はしっかり準備して挑んでも、上手くゴールまで辿り着けるなんて保証はない",
                    "途中で何度も道に迷い、穴に落ち、途方に暮れて多くの人が道半ばで投げ出す",
                    "短編を十本書けても長編一本を書ける保証なんてないんだ"),
            sana.talk("だから、ですよ",
                    "学生時代、一度として書き上げたことのない$meに、先生が教えて下さい",
                    "一人じゃ無理でも、二人なら、いいえ、先生となら書けるって思うんです",
                    "そしてそれは先生が再び長編小説を書くことにも繋がると思うんです！"),
            noto.do("先生はそっと$CSの腕を退かすと、顔を向ける", "そこには「仕方ないなあ」という諦めの笑みと僅かばかり上向きになったやる気が見て取れた"),
            sana.talk("それに編集は待つのが仕事だと$fukaya先輩も言ってましたから、$meは何度先生が折れても、原稿を書き上げるまでずっと待ち続けますよ",
                    "もうそれは将来『伝説のすっぽん編集』なんて呼ばれてもいいくらいの執拗さで、です"),
            noto.talk("それじゃあ$meはせいぜい噛み千切られて別の意味で伝説にならないように、家に帰ったら早速新しい原稿用紙を広げるとしようかな"),
            sana.talk("なんですか、それ",
                    "$meは本気ですからね？"),
            noto.talk("長編を書く、というのも？"),
            sana.talk("ええ、そうです。一度口から出したからには絶対に$meも書きます", "書き上げてみせます", "あ、もちろん先生がしっかりと指導して下さいよ？"),
            sana.do("まるで意地の張り合いみたいだと思いながらも口を尖らせて宣言したが、そんな$Sを見て先生は実に楽しそうに笑い声を上げる"),
            noto.talk("君がそこまで言うなら、$meも腹を括ろう",
                    "改めて、宜しく頼むよ"),
            noto.do("そう言って、先生は右手を$Sへと差し出した", "&"),
            sana.do("その大きな手を握り返すと火傷をするかと思うような熱を感じて、ああ、これは先生の情熱なんだ、と思えて嬉しくなる"),
            sana.talk("はい、こちらこそです"),
            sana.do("しっかりと握り返した手は、いつまでもほかほかとしていた"),
            ## NOTE
            ##  初恋の女性のことを思い出して悲しくなった、心細くなった先生を励ますとともに、小説を書くことになる
            camera=w.sana,
            stage=w.on_oldinn,
            day=w.in_backhome, time=w.at_morning,
            )

def sc_intrain(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("電車の中にて",
            w.symbol("　　　　◆"),
            w.comment("ここで$geroから$lineをもらって、何とか事件解決したと知る"),
            w.comment("東京＝城之崎間は、城之崎（城崎温泉駅）＝京都を特急で、京都＝東京を新幹線になる"),
            sana.be("京都駅で新幹線に乗り換え、何とか今日中に東京に帰り着けそうなことを確認してほっとしていた"),
            noto.be("隣には窓際がいいと言い張った先生が、既にこくりこくりと船を漕いでいる", "&"),
            sana.do("高校生と赤ん坊ほどの年齢差があるのに、こうして見ている寝顔は何とも子どもっぽい","&"),
            _.think("普段は色々と$Sの知らないこと、至らない部分を、その穏やかな声で指摘、指導してくれるのに、",
                "時折びっくりするくらいな心の弱さを見せる",
                "その不安定で吹けば消えてしまいそうなロウソクの灯のような存在だからこそ、",
                "もっと力になりたいと思うのだろう"),
            sana.do("眠りこけるその口元が、小さな笑い声と共に何かを呟く"),
            sana.do("$Sは先生にスマートフォンを向けると、そっと翳して写真に収めた",
                "けれどそれを見て一瞬考え直し、今度は頭をその寝顔の隣に持っていき、自分との内緒のツーショットを撮る"),
            sana.think("後で知られたら、きっと先生は怒るだろう",
                "だからこれは、誰にも見せずに仕舞っておこう"),
            sana.talk("あ……"),
            sana.do("そこに$geroからの$lineがきた",
                "内容は盗作絵師の件で、どうやらあの後コミケで知り合った絵師仲間が協力して、その盗作絵師のＳＮＳが炎上してアカウント削除して消えてしまったということだった",
                "それで無事解決という訳ではないけれど、仲間が一緒にいて守ろうとしてくれたことが嬉しかった、と書かれていた"),
            sana.talk("とりあえずは良かったかな"),
            w.eventPoint("盗作絵師", "盗作だとバレて炎上してアカウント削除して逃亡した"),
            w.eventEnd("盗作絵師"),
            w.comment("日記部分"),
            w.symbol("　　　　※"),
            sana.explain("人はどうして盗作をしてしまうのだろう"),
            _.explain("それは自分の才能や作品を信じられないからだろうか？",
                "それとも必死に努力しても何も得られない現実に疲れて、より簡単に注目を浴びる方法に手を出してしまうのだろうか"),
            _.explain("誰かのもので自分を有名にしたい、という気持ちが、$meにはよく分からない"),
            _.explain("それは$meが作家ではなく、彼らを支える編集という仕事を選んだ側だからかも知れない"),
            _.explain("ひょっとすると先生もまた、彼らと同じように、心のどこかでは盗作という悪魔の囁きを聞いているのだろうか"),
            _.explain("もし先生がそんなことに手を染めてしまったことがあったら、その時に、$meはどんな態度を取れるだろうか",
                "ちゃんと駄目だと口にできるだろうか",
                "それとも……"),
            sana.explain("ともかく先生との約束で、$meは再び小説を、それも長編小説を書くことになった"),
            _.explain("勢いだったとはいえ、学生時代から一度として長編小説は完結させたことがないので不安だらけで仕方ないけれど、", "&"),
            _.explain("先生がもう一度、先生の小説を書くことができる、その応援ができるのなら、自分なりに精一杯書いてみようと思う"),
            w.symbol("　　　　※"),
            sana.do("日記の終わりをそう締めくくると、バッグに仕舞い、$Sもシートにもたれかかった"),
            stage=w.on_train,
            )

## episode
def ep_insided(w: World):
    return w.episode("4.心の内にて",
            ## NOTE
            sc_exchange_condition(w),
            sc_intrain(w),
            )
