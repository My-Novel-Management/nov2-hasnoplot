# -*- coding: utf-8 -*-
"""Episode: 9-4.第三の手記／人間失格
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
def sc_letterlast(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    mnote = W(w.masternote)
    return w.scene("先生の手紙の最後",
            w.symbol("　　　　※"),
            w.comment("手紙の最後にはいつか責任を取らなければならないと書かれていた"),
            noto.voice("――以上が$meの冒した罪の、全ての告白だ"),
            sana.be("#告白の日記を読んでいた"),
            sana.explain("そこまでは全て黒のインクで書かれていたが最後のページだけは色を変え、赤字で文章が綴られている",
                "文字も心なしか丁寧に書かれているように思えた"),
            noto.voice("彼は六月十三日、つまり敬愛する太宰治がその命を断ったのと同じ日に首を括ってこの世をおさらばした",
                "そのことについて遺書があったが$meのことは一切書かれていなかった",
                "しかしそこに何度もなぞって太くした「絶望した」という言葉の矛先は$meに向かっているものだと、",
                "$meだけが理解できるよう書かれていたのだ",
                "つまり、$meは彼の大切なものとその命、そして思い出という崇高な結晶までをも、奪い去ってしまった"),
            sana.think("その遺書については雑誌に一部抜粋で直筆のものが掲載されていたことを思い出す"),
            noto.voice("人は生きている限り、誰かから何かを奪うことは不可避だ",
                "それは全ての人間が平等にはいられない、いや、全ての生き物が平等にはいられないという自然界の真理だ",
                "けれど、人には心がある",
                "誰かを傷つけ、誰かを悲しませ、誰かの命を奪ったのであれば、",
                "それはいつか責任を取らなければならない",
                "$meはいつか、この責任を取るだろう",
                "できればその日までは、彼の墓前で許しを請おうと思う"),
            mnote.look("その末尾には十年前の日付と『$full_noto』という署名が、先生の達筆でなされていた"),
            sana.do("$Sはノートを手にしたまま、深い溜息をつく"),
            sana.talk("どうして、誰にも、何も、話さなかったのだろう"),
            _.think("そこに書かれていたのは、先生の作家として生きた時間と同じだけの苦悩だった"),
            _.think("普段接しているとそんなに深い闇を抱えて日々生活しているようには思えなかったし、",
                "$fukayaの引き継ぎメモにも小説が書けない理由やデビュー当時にあった盗作騒動、それにまつわる親友の自殺などの記述は、",
                "一切見当たらなかった",
                "それは先輩も全く把握していなかったということなのか、知っていて敢えて書く必要はないと考えたのか",
                "一度先生について先輩とより深い情報交換会を開かなければならないと思っているが、",
                "現在臨月真っ直中の$fukayaとそんな時間が持てるまでには、まだ幾分時間が掛かりそうだ"),
            _.think("それに先生は言っていた"),
            noto.voice("作家というのはね、$sana君。表に出て、あれやこれやと喋ってはならないんだ", "&"),
            _.voice("何故ならそれは自分が本来書くべきことを発散してしまっているということだから", "&"),
            _.voice("言葉は消えものだ。しかし文章にした時、小説になった時、それは時間と空間から切り離される", "&"),
            _.voice("その唯一無二の小説という世界ができあがるんだ", "&"),
            _.voice("だから本物の作家は無闇矢鱈に語らない", "&"),
            _.voice("語るのは、本にはならない、枝葉末節だけでいい"),
            sana.think("そんなポリシーがあるからこそ、先生はずっと自分の心のうちに抱え込んでいたのだろうか"),
            _.think("作家はいつか死を選ぶ、とも言っていた",
                "太宰治だけでなく芥川龍之介や川端康成、有島武郎", "海外でもヘミングウェイ等は有名だ",
                "統計を取れば作家以外の人間の自殺率とそう変わらないのだろうが、それでも死と向き合う職業だということは確かだと$Sにも思える"),
            _.talk("けど死ぬなんて、それも自殺だなんて、そんなこと$meが絶対許しませんからね"),
            _.do("決意を自分に言い聞かせるように声に出すと、そのノートを閉じて脇に置く"),
            _.do("目の前のモニタにはまだ最終章を残した原稿の冒頭部分だけが書かれ、カーソルが点滅していたが、", "&"),
            _.think("どんなことがあっても最後まで作品は書き切らなければいけない、という先生の言葉を思い出し、", "&"),
            _.do("大きく息を吸い込んで、今一度、キーボードに指を置いた"),
            ## NOTE
            ##  先生の手紙から戻ってきて、ここで沙奈の、手紙と先生の告白に対する心境吐露
            camera=w.sana,
            stage=w.on_herroom,
            day=w.in_readletter, time=w.at_night,
            )

def sc_lastscene(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuchi = W(w.tsuchiura)
    pc = W(w.mobilepc)
    return w.scene("ラストシーン",
            w.br(),
            sana.be("#パソコンに向かっている"),
            sana.hear("部屋にはキーボードを叩く音と、パソコンのファンの音、それに時折着信するスマートフォンが声を上げる程度で、",
                "あとの大半は静寂が満たしていた"),
            pc.look("モニタには原稿用紙にして二百五十枚を超える$S初の長編小説のラストシーンの部分の文章が、何度も表示されてはデリートされて、を繰り返し、",
                "その度にカーソルが忙しなく点滅を行き来させる"),
            sana.have("#脇には先生のぼろぼろの創作ノート。付箋がいっぱい貼ってある", w.masternote),
            sana.explain("作家を目指した学生時代、幾つも設定だけ考えて冒頭から少し書いただけでそのままになっている作品を、ノートに残してきた",
                "それらは稚拙だったり、既存作品の真似事だったり、見返すと何が書きたかったのかよく分からないものだったりと、",
                "どれも小説どころか物語の体を成していないものばかりだ"),
            _.think("それでもあの頃はただ設定を考えて、何か書いた気になっているのが楽しかったし、",
                "それが創作なんだと思っていた",
                "だから別に完結させなくても良かったし、何なら、次々に思いついたまま、新しい設定と新しい物語世界に没頭できれば、",
                "そこにはエンドマークなんて必要なかった"),
            sana.do("ふう、と吐息を一つ漏らし、少なくなったコップにボトルのコーヒーを注ぎ込む"),
            sana.think("不思議な気持ちだった",
                "長いものを最後まで書いてくると、今までとは違う「エンドマークを付けたくない」という感慨が湧き上がってくる",
                "それはこの一月ばかりずっと付き合っていた物語の彼ら彼女らとの別れが近づいているのを、少しでも、一ページでもいいから遠ざけようという心理だ",
                "作家はいつもこんな気持ちと戦っているのだろうか",
                "それでも物語に終わりを与えなければならないのだろうか"),
            noto.voice("$w_masterword001"),
            sana.think("彼らの人生が今後も続いていくとしても、作者はそれに何らかのエンドマークを与えなければならない",
                "それは彼らから物語を拝借する礼儀でもあり、読者に対する作者の言葉でもあると、先生は言っていた",
                "終わらない物語では小説ではないのだと"),
            _.explain("作品は終盤、息絶えた世界を見事に再生した無限の命の女王が、不治の病にかかる", "&"),
            _.explain("その病の原因が自分が生み出した生命たちにあると知り、女王は自決する", "そうプロットには書き込んだ"),
            sana.talk("でも、これだと……"),
            sana.do("一度はプロット通りに無限の命の女王が自決をしようとするところまで書いてしまったが、思い直して全て削除した", "&"),
            _.do("真っ白に戻したページを一睨みしてから、$Sは再び書き始める"),
            sana.think("死は物語に甘美なものとして横たわっているけれど、それに魅入られてはいけない",
                "先生の創作ノートにも書かれていた", "&"),
            _.explain("登場人物の死はそれが敵であれ味方であれ主人公であれ、大きな刺激となって読者に向かう",
                "だからこそ安易に死を持ち出してはいけない",
                "そうしないと何か物足りないと感じたらすぐ人を殺すようになってしまうからだ",
                "その思考の短絡性はやがて物語世界をはみ出して現実世界にも蔓延する",
                "フィクションは現実とは違うけれど、人はそこに夢を見る",
                "その夢には憧れが沢山含まれていて、そこに死が大量に横たわっていると、人は死んでもいいのだと思ってしまう",
                "だから、作家は安易に死を描いてはならない"),
            _.think("その言葉を思い出し、$Sは物語のラストを書き換える",
                "いや、主人公を殺そうというプロットの力に抗う"),
            _.think("女王は自分が冒した罪だったと気づく",
                "しかし人は誰もが様々な罪を冒した罪人だ。それが人間の有様なのだ", "&"),
            _.think("沢山の失敗をしてきた。間違いも犯した。人を傷つけたこともあった", "&"),
            _.think("でもそれらの全てを背負って、それでも生きていくのだ", "&"),
            _.think("そこにはもう、自決しようとした女王の姿はなかった"),
            sana.do("$Sはラストシーンを書きながら声も出さずに泣いていた"),
            noto.voice("$sana君。物語のラストシーンにはね、その作者の思いが滲んでいるんだよ"),
            sana.do("最後まで書き上げると大きくひと呼吸をしてから（了）の文字を入れ、保存した"),
            _.do("時刻を確認すると、もう深夜の三時を過ぎていた"),
            ## NOTE
            ##  長編の最後を一応書き上げる
            ##  それが無意味と分かってはいても、書き上げることと約束したから
            ##  それから考えようと思った
            )

def sc_emergency(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    tsuchi = W(w.tsuchiura)
    return w.scene("緊急事態発生",
            w.symbol("　　　　◆"),
            w.comment("何とか作品を書き上げて寝てしまっていたところに、バイト君から連絡で、先生が病院から消えたと"),
            sana.be("#机に突っ伏して寝ている"),
            sana.hear("どこか遠くでずっと何かのベルが鳴り響いていた", "&"),
            _.do("$Sはそれが何なのだろうと確かめる為に手を伸ばそうとするが、闇の中で何も掴めない",
                "自分がどこにいるのかも分からず、姿も見えず、この世界からすっかり消えてしまったかのような気持ちになったが、", "&"),
            sana.hear("ドアを激しくノックする音に続いて聞こえた「電話鳴っとるがな」という耳馴染みのある声で、ようやく現実に戻された"),
            sana.talk("え？　……あ、はい。もしもし？"),
            tsuchi.voice("もしもしじゃないっすよ！", "さっきから何度も掛けてるのにどうして出ないんすか？", "移動中すか？"),
            sana.do("突然耳の中に突っ込まれた$tsuchiuraの声にただ嫌な予感だけが胸に去来したが、",
                "起き抜けに聞きたい声ではないだけに、ただその寝覚めの悪さが原因なのだと思ってしまった"),
            sana.do("目覚ましのデジタル表示は十時過ぎだ", "&"),
            sana.think("今日の五時までなんて、もう先生の原稿は無理だなあ、とぼんやり考える"),
            tsuchi.voice("ちょっと$sanaさん$meの話聞いてるんすか？"),
            sana.talk("ん？　ごめん", "で、何？"),
            tsuchi.voice("何？　じゃないですって！", "大変なんすよ！", "あのおっさん、病院から消えました！"),
            sana.think("今彼は何と言ったのだろう", "寝ぼけた頭だからか意味が分からない"),
            sana.talk("あの、ちゃんと話して。$meまだ徹夜明けで頭が……"),
            sana.hear("額を押さえているところに、今度は玄関でインタフォンが鳴らされている"),
            azu.talk("はーい", "今出ますー"),
            sana.do("応対には$azuが出てくれたようだけれど、その彼女はすぐにノックしてドアを開けた"),
            sana.talk("どうしたの？"),
            azu.come("#荷物を手に入ってきて"),
            azu.talk("これ。$sana宛だって"),
            sana.do("$azuから受け取ったそのビニルの梱包材で包装された茶封筒には、$yuzawaの名前で『資料』と書かれていた", "&"),
            sana.have("慌てて中身を確認すると、 古い原稿用紙をコピーしたものが数枚、クリップで留められたものが出てきた",
                "その原稿用紙の隅に『$tsuru』と斜めになった文字が書かれている",
                "$yuzawaが言っていた持ち込み原稿のコピーだった", w.carryingpaper),
            tsuchi.voice("ちょっと？　$sanaさん？　もしもしもしもし？"),
            ## NOTE
            ##  先生が消えた、に加えて、証拠品まで突きつけられ、万事休す。そこに更に先生の出版枠に再度編集長がノミオを打ち込む
            day=w.in_vanishmaster, time=w.at_midmorning,
            )

## episode
def ep_letter3(w: World):
    return w.episode("4.$full_notoによる第三の手記",
            ## NOTE
            sc_letterlast(w),
            sc_lastscene(w),
            sc_emergency(w),
            )
