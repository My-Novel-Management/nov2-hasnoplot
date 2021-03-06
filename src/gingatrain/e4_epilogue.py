# -*- coding: utf-8 -*-
"""Episode: 10-4.エピローグ／銀河鉄道の夜
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
d = Writer.continuedAct


## scenes
def sc_hurrygirl(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    bento = W(w.bento)
    return w.scene("急げ編集",
            w.comment("１話の冒頭オマージュ"),
            sana.be("#着替えている"),
            sana.do("$full_sanaは激怒した"),
            _.do("だがその相手は邪智暴虐の王ではない", "自分自身だ", "あるいはモニタの中のゲームキャラたちにだ"),
            sana.talk("もう！　なんでアーサーばかりなのよ！　ランスロットはあんなに優しくしてくれるのに！"),
            w.comment("ここ乙女ゲームを何するかは後で決める。薄桜鬼と刀剣乱舞が候補だが全く関係ないやつか、長年のファンが多いコルダあたり"),
            gero.talk("やから攻略法見れって言うたがね"),
            sana.talk("ゲームデザインされたキャラの気持ちくらい読み取れなくて編集やってらんないでしょ？"),
            _.do("シャツのポタンを止めながら$Sは眉毛を折り曲げた$geroを睨めつける", "&"),
            gero.do("ジャージに眼鏡といった完全引きこもり装備の$geroは眠そうに欠伸を一つ零し、座椅子の背もたれで大きく腕を伸ばした"),
            sana.explain("編集長からの命令で女性向けレーベルの立ち上げも考えているから乙女ゲームでもしてレポート出してくれと言われ、",
                "それなら$geroの十八番だとばかりに徹夜でゲームをしていたのだ", "&"),
            _.think("自業自得の四文字熟語が風船付きで頭上に浮かぶ"),
            gero.talk("そもそも今流行ってる悪役令嬢ものと実際の乙女ゲームの中身は史実と戦国バサラくらい差があるのよ"),
            sana.think("何が違うのかいまいち理解できないが、確かに彼女の言う通りだった"),
            sana.talk("それに何？　長いっていっても限度があるでしょ？",
                "時間のない社会人に睡眠時間を削ってまでゲームキャラとの色恋沙汰に没頭しろってのは、興味のない人にとっては単なる拷問なんじゃない？"),
            gero.talk("その割にあと一周だけとか言ってあんた楽しんどったがな"),
            sana.do("両手を広げた$geroに言い返す言葉を見つけられず、$Sは大人しく春物スーツの上着を羽織るとスタンドミラーで確認する"),
            azu.talk("ねーえー、準備できたぁ？"),
            azu.come("キッチンで物音をさせていた$azuが二段になった弁当箱を手にやってくる", "&"),
            bento.look("中にはにっこり笑った小さなおにぎりと、ブロッコリィに卵焼き、焼き鮭の切り身が入れてあった"),
            sana.talk("$azu、助かる", "ほんとお嫁さんとして欲しいくらい！"),
            azu.talk("会社で食べてね"),
            azu.look("髪を後ろで綺麗に縛り、口紅も引いてあった", "&"),
            sana.think("これからパン屋のアルバイトなのだろう", "自分ばかりへこたれてはいられないな、", "&"),
            sana.have("と気を引き締めて弁当を受け取ると、右の拳をぎゅっと握る"),
            sana.talk("よおーし。今夜は$meが焼き肉奢っちゃうからね！"),
            gero.talk("おう。いい気合だが期待しないで待っとくわ"),
            azu.talk("豚肉でいいからね。じゃあ気をつけて"),
            sana.talk("もうちょっと期待してよ", "これでも三人の中じゃ一番稼いでるんだから"),
            sana.do("そう言った$Sに二人とも「無理せんで」「いつもお世話になってます」とそれぞれの笑顔を向け、出かける彼女のことを見送ってくれた"),
            sana.go("#出かける"),
            ## NOTE
            ##  ここで冒頭オマージュ。エピローグ感を醸し出す
            camera=w.sana,
            stage=w.on_herhouse_int,
            day=w.in_getfirstbook, time=w.at_midmorning,
            )

def sc_runninggirl(w: World):
    sana, noto = W(w.sana), W(w.noto)
    fuka = W(w.fukaya)
    sphone = W(w.sphone)
    return w.scene("走れ編集",
            w.symbol("　　　　◆"),
            sana.come("#走っている"),
            _.do("アパートを飛び出し、おろしたてのスニーカーで通りを駆け抜ける"),
            _.think("物心ついた頃からどうしてあんたはどんなにせっかちなのと母親に言われてきたけれど、",
                "小さい体だからこそ必死にもがいて踏ん張ってこれでもかってくらい自分がここにいるってことをアピールしなければいけなかった",
                "黙って縮こまっていたら誰にも見つけてもらえないし、見てもなめられて不遇を被る"),
            d("だから走る"),
            d("走ることは$Sにとって生きることだった", "生命力の表現そのものだった"),
            d("創作という場にそれを求めたのも、やはり自分はここで精一杯生きてますと伝えたかったからだ"),
            sana.do("ハァハァ……"),
            _.think("息が荒い", "&"),
            _.do("駅舎が見え始めたところで一旦膝に手を置いて、腕時計を見やる",
                "時間は八時半を過ぎたところ", "電車を降りてから再度走れば間に合うだろう"),
            d("そうほっとしたところでコートの右ポケットに突っ込んだスマートフォンが震えているのに気づいた",
                "見ると$fukaya先輩だ"),
            fuka.voice("ついさっき、無事三〇四五ｇの生命を生み出しました。母、つらい"),
            sana.talk("つらいって書きながら笑ってるじゃないですか"),
            sphone.look("一緒に添付されていた写真にはすっぴんでも先輩らしい気の強い眼差しと、その胸元に抱かれた生まれたての命が渋い顔をしているのが、写っていた"),
            w.eventEnd("深谷の出産"),
            ## NOTE
            ##  ここで深谷出産の報告を受け取る
            stage=w.on_street,
            )

def sc_firstbook(w: World):
    sana, noto = W(w.sana), W(w.noto)
    king, nira, tsuchi = W(w.king), W(w.nirasaki), W(w.tsuchiura)
    door = W(w.door)
    book = W(w.book)
    return w.scene("先生の本",
            w.symbol("　　　　◆"),
            w.comment("初めての$sana担当での先生の製本された本を手にして"),
            sana.come("エレベータの扉が開くと小走りにオフィスに向かう"),
            w.comment("廊下のポスターに先生の出版予定作品も潜ませる"),
            door.look("$on_hercompanyのプレートを視界に捉え、", "&"),
            sana.think("何とか間に合った、という安堵と共にドアを潜ると「おはようございます」と力が抜けたような声が喧騒の中に染み込んでいった"),
            nira.be("#パソコンに向かっている"),
            tsuchi.be("#椅子を並べて寝ている"),
            king.be("#座ってコーヒーを飲んでいる"),
            sana.do("既にそれぞれが席に就き、パソコンとにらめっこをしながら連絡や進捗の確認をしている",
                "ちらりと見る者もいたが大半は気にせず自分の仕事を続ける", "ふんぞり返っている編集長だけがその脂ぎった視線を向けてきたが、",
                "愛想笑いを返しておいてそそくさと自分の席に向かい、二つ鞄を肩から外した"),
            nira.talk("おう"),
            sana.think("また風邪なのだろうか", "&"),
            nira.look("大きなマスクをした$nirasakiは相変わらず寝不足で隈の目立つ眼を向けて小さく頭を下げる"),
            sana.do("#座りつつ"),
            _.do("席に座ろうとして、机の上に見慣れないものが置いてあった",
                "誰かの忘れ物かと手に取ろうとして$nirasakiがぼそりと呟いた言葉ですぐにその正体に思い至る"),
            sana.talk("え、嘘。どうして"),
            book.look("本だ。表紙には暗い森の中で光る刀を手にした袖のない着物姿の少女が描かれている",
                "銀字の印刷で『$master_novel1』とタイトルが刻まれ、その著者として$full_notoの名前がしっかりと入っていた", "&"),
            sana.think("製本サンプルだ", "&"),
            _.explain("実はあの酷い雨の日、$tsuchiuraは先生の原稿を$Sたちに届けただけでなく、コピーしたものを事前に編集長に提出していたのだ",
                "それを知った時には意外とできる男だったのかと見直そうとしたが、ただ$nirasakiに指示されただけと聞いて納得してしまった"),
            nira.talk("印刷所の何とかってやつが朝一で持ってきてくれたよ"),
            sana.talk("ありがとうございます"),
            nira.talk("$meは何もしてねえよ"),
            nira.look("それでも$nirasakiは少し嬉しそうに目を細める"),
            _.talk("あ、そうそう。それよりな、$noseの奴、出頭したそうだ。よかったな"),
            sana.talk("そうなんですか？　ほっとしました"),
            _.think("殺人には至らなかったけれどそれでも放火の罪は重い。有罪は免れないだろう",
                "その罪を償い、今度こそ本当に自分の力で自分自身の作品を書いてもらいたいと$Sは願っている",
                "もしその時彼女の力を必要とするなら迷うことなく手助けしよう",
                "何故ならそれもまた、編集の仕事だからだ",
                "少なくとも$Sはそう思っている"),
            sana.do("パソコンを立ち上げてすぐに対応が必要な案件がないことを確認すると、製本サンプルを風呂敷で包んでから鞄にそっと入れた", "&"),
            _.explain("$fukayaが一度丁寧にビニル袋に入れてラッピングしていたので理由を聞いたら「この方が作家さんも嬉しいでしょ」と言うので、",
                "それ以来、いつか自分が一人で担当させてもらった作家の製本サンプルが上がった時には真似をしようと思っていたのだ"),
            sana.talk("じゃあ、ちょっと行ってきます"),
            ## NOTE
            ##  文芸部の面々を出しておく
            ##  深谷さん出産情報も追記
            ##  放火犯の情報も
            ##  編集長のことはカットで。あと社用車のことも。
            camera=w.sana,
            stage=w.on_heroffice,
            )

def sc_gotomaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    return w.scene("先生の許へ",
            w.comment("見本を手に先生の家に急ぐ"),
            sana.do("車に乗り込み、シートベルトなど"),
            sana.think("初めての本です。自分が担当した初めての、そして先生の初めてのライトノベル"),
            sana.do("都内の道路を軽快に走る"),
            sana.do("スマホに何か通知するが、出られないので無視する"),
            sana.explain("しかしこれが次の悲劇の幕開けだった"),
            sana.explain("なんとスマホを手に入れた先生が、勝手にツイイッターを始めてしまったのだ"),
            sana.explain("だがそれで問題になるのはまた別の話。後日のことであった"),
            stage=w.on_car_int,
            ).omit()

def sc_nextbook(w: World):
    sana, noto = W(w.sana), W(w.noto)
    interior = W(w.interior)
    floor = W(w.floor)
    monitor, mobilepc = W(w.monitor), W(w.mobilepc)
    return w.scene("次の本について",
            w.symbol("　　　　◆"),
            w.comment("先生から新しいシリーズの提示があり、それについて取材旅行費用がこれだけかかると言われて"),
            w.comment("彼女の編集人生はまだ始まったばかりだ"),
            sana.come("インタフォンすら押さずに鍵が掛かっていなかったドアを開け、$Sは興奮気味に部屋に上がった"),
            sana.talk("先生！"),
            interior.look("けれどもまだ毛布が掛けられたままの炬燵には主人不在で、一週間前には綺麗に$Sが片付けたカーペットの上には既に雑誌や辞書、カップ麺の空が転がっていた"),
            sana.talk("もう先生まだ寝てるんですか？"),
            sana.do("$Sが寝室を覗くと、ぼさぼさ頭をした作務衣姿の先生がどっしりと胡座をかき、テーブルの上に置いたノートパソコンを前にうんうん唸っている","&"),
            noto.look("右手と左手それぞれの人差し指を指揮棒のように突き出して、それでキーボードにおっかなびっくりといった体で触れるのだが、","&"),
            _.do("思ったようにならないのか一つ押しては天を仰ぎ、一つ押しては溜息を零し、何度めかの落胆で首をひょいとこちらに向けると、バツが悪そうに後頭部を掻いた"),
            sana.talk("機械、苦手だって言ってたじゃないですか"),
            floor.look("畳の上には長細いダンボールが転がっていて、ノートパソコンのマニュアルと思しきものが広げられ、そこには既に沢山の付箋が付けられている", "&"),
            sana.think("一体何時間格闘して起動までいったのだろうかと思うと、どうしようもなく先生が可愛く思えて仕方ない"),
            sana.talk("早朝でも夜中でも、呼んでくだされば駆けつけますよ？"),
            noto.talk("その残業代を払えるだけ儲けが出たなら、そうさせてもらうよ",
                "しかし機械というのはどうしてこう、面倒なように造られているのだろうかね",
                "本来は人間が楽をできるように便利を供給するもののはずなのに、実際に目の前にあるのは不便の塊じゃないか",
                "ただ『おはよう』と書くだけなのに$meの目の前には未だによく分からない窓が出たままだ",
                "やはり昨日店員さんに勧められたように初期サービスとやらも一緒に頼んでおくべきだったよ"),
            monitor.look("モニタにはまだ初期設定の最初の質問が出たままだ", "住んでいる地域を答えたかったのだろうが何故かイタリアが選ばれていた"),
            sana.talk("パソコンくらい$meが設定しますよ",
                "それよりも先生にはこっちの方が大事なんですから"),
            _.do("鞄から風呂敷に包んだサンプル本を取り出すと、その結び目を解いてから、表紙を向けて先生に渡す"),
            noto.talk("ああ、できたのか"),
            noto.do("特に感動した様子もなく、手を出してそれを受け取ると、先生はぺらぺらと冒頭から順にページを捲っていく",
                "途中イラストが挿入されているところで何か考え込むように捲るのを止めたが、",
                "それでも何も言わずにそのページを送ると、口元をいくらか緩めて$Sにこう言った"),
            noto.talk("作品が本になった、と感じられるこの瞬間がね、一番緊張するんだよ"),
            sana.talk("書店に並んだ時よりですか？"),
            noto.talk("それは君たち出版社の人間の方だろう？",
                "作家は、いや、$meはね、このもう後戻りができないという感覚が一番強くなる製本されてしまった時こそが、何より恐ろしいんだ",
                "本当にこれを出してしまっていいのだろうか、という自分への不安、そして読者の期待に応えられるだろうかという不安、",
                "それ以上にもっと書けたんじゃないだろうか、あそこの描写は大丈夫だろうか、本当にこんな作品で良かったのだろうか、",
                "そうやって自問自答の闇の中に閉じ込められる",
                "小説なんてものはね、常に孤独や不安との戦いなんだよ"),
            sana.think("普段は自信ありげに小説論や創作論、作家論などを語っているのに、こんな時に見せる意外な先生の弱気が、ちょっぴり愛おしい"),
            sana.talk("先生"),
            noto.talk("何だね？"),
            sana.do("こちらを見た$notoを狙い、スマートフォンを光らせた"),
            sana.talk("紹介記事に使いますね"),
            noto.talk("お、おい。何をするんだ。やめてくれないか。流石に素顔は恥ずかしいよ"),
            sana.talk("何言ってるんですか。知ってるんですよ。当時、散々雑誌に取り上げられて『若手美形作家』なんて持ち上げられてたの"),
            noto.talk("あれは若気の至りと言うんだ", "そしてそれを持ち出す方は大人気ないと言うんだよ、$sana君"),
            sana.talk("意外とよく撮れたと思いますよ？"),
            noto.do("そう言ってスマートフォンを見せると、先生の顔が歪む"),
            noto.talk("$sana君！　君ってやつは！"),
            sana.talk("あーん、許してくださいよー"),
            w.symbol("　　　　※"),
            sana.explain("こうして先生の作品は今月末、無事に発売される運びとなりました", "&"),
            d("けれどそれは先生と$meにとってまだほんの序章にしか過ぎず、数々の困難と文芸という得体の知れない巨大な壁が待ち構えていたのです",
                "当然この時の$meはまだそれらを知ることはできなかったし、知っていたとしてもやはり逃げ出すことはしなかったでしょう",
                "何故なら$meは$full_sanaだから"),
            d("そして$meの壮絶な$full_notoの担当編集人生は本格的に幕を開けたのです"),
            w.symbol("　　　　※"),
            sana.explain("そこまで書き終えて日記帳を閉じると、$Sは思い切り両腕を伸ばした"),
            sana.talk("あれ？　何だろ"),
            sana.explain("$lineに通知がある",
                    "珍しく$nirasakiから、こんな夜中に何だろうか、と思って内容を目にした$Sはそれを見なかったことにしてスマートフォンをテーブルに放り出す"),
            sana.explain("$full_sanaの苦難はまだ終わらない",
                    "がんばれ$S、負けるな$S、力の限り編集の仕事をがんばるのだ",
                    "そんな掛け声を心の中で呟いて、目を閉じた"),
            sana.explain("しかしこれが後にあんな大きな火種になるとは$Sも、当人も、思わなかっただろう",
                    "だがそれはまた、別の物語である"),
            w.symbol("（了）"),
            stage=w.on_hisnewapart,
            )

## episode
def ep_epilogue(w: World):
    return w.episode("4.エピローグ",
            ## NOTE
            sc_hurrygirl(w),
            sc_runninggirl(w),
            sc_firstbook(w),
            sc_gotomaster(w),
            sc_nextbook(w),
            )
