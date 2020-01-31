# -*- coding: utf-8 -*-
"""Episode: 4-1.洋梨／檸檬
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
def sc_introuble(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    return w.scene("小説を書くという混乱",
            sana.do("友人に現状を語る"),
            sana.talk("なんで$meが小説を書くことになるのよ！"),
            gero.talk("いやいや、あんたが約束したんだがな"),
            sana.talk("そりゃそうだけどさ"),
            azu.talk("でも先生に読んでもらえるってことでしょ？　それってすごいことじゃない？"),
            _.talk("それに、昔は作家目指してたんでしょ？"),
            sana.think("自分の学生時代を思い出す"),
            _.talk("あの頃の作品は今じゃ黒歴史だなあ"),
            gero.talk("そんなこといったら$meは黒歴史現在進行系だがな"),
            _.do("自分の描いたＢＬとかのえっちいのを見せて"),
            sana.talk("それ黒歴史って思ってる？"),
            gero.talk("コミケに向けて必死だから黒とか白とかない", "売上は正義！"),
            sana.do("苦笑"),
            azu.talk("あの……新人賞の選考って編集部の人も読んだりするの？"),
            sana.talk("うん読むわよ。基本うちみたいな小さなところだと、下読みバイトに出してる余裕もないし、",
                "なんだかんだ時間を見つけて手分けして読むことになる。大きなところだと一次の分くらいは下読みに出しちゃうんだけどね"),
            azu.talk("そっか"),
            sana.talk("ん？"),
            gero.talk("言っちゃいなよ。もう締め切った後なんだから、今更どうしようもないがね"),
            sana.talk("何よ？"),
            azu.talk("……うん"),
            gero.talk("あんたんとこの新人賞に応募してるんだって。発表はまだまだ先だけど、気になるがね"),
            sana.talk("へ、へえ、そうなんだ"),
            _.think("自分が下読みに当たりませんようにと、心の中で必死に祈った"),
            w.eventStart("安曇野の応募原稿"),
            ## NOTE
            ##  小説を書くことになって帰ってきて不満をぶちまける
            ##  ここで条件を確認しておくこと
            ##  また安曇野から「密かに応募していた」と告白されること
            camera=w.sana,
            area=w.Tokyo,
            stage=w.on_herhouse,
            day=w.in_nogetpaper3, time=w.at_night,
            )

def sc_oldnovel(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero = W(w.gero)
    shelf = W(w.bookshelf)
    sananote = W(w.sananote)
    return w.scene("黒歴史",
            sana.come("食事等を終えて自室に戻ってきた$S"),
            sana.wear("犬柄のペールピンクのパジャマ"),
            shelf.look("小さな本棚に、自社の文庫本とお気に入りのハードカバーが並ぶ"),
            _.look("一番上の棚の片隅のノートが数冊", w.sananote),
            sana.do("本棚から一冊のノートを出す", w.sananote),
            sananote.look("そこには学生時代に書き溜めた小説のネタがあった"),
            sana.talk("んん……"),
            sana.do("頭を抱え込む"),
            _.do("編集の視点を手に入れた自分から見ると稚拙なものばかりに思える"),
            sana.talk("ああああぁぁぁぁ"),
            sana.do("ベッドに倒れ込む"),
            gero.voice("$sana、うっさい"),
            sana.talk("……ごめん"),
            ## NOTE
            ##  余裕があればここに沙奈の創作能力がどの程度か分かりそうな文章とか入れておく
            stage=w.on_herroom_int,
            )

def sc_deadline_approach(w: World):
    sana, noto = W(w.sana), W(w.noto)
    gero, azu = W(w.gero), W(w.azumino)
    nira, king, yone = W(w.nirasaki), W(w.king), W(w.yonezawa)
    return w.scene("近づく締切",
            sana.come("会議室に慌てて入ってくる"),
            king.be("既に席についている"),
            nira.be(),
            yone.be(),
            sana.talk("すみません……"),
            sana.do("頭を下げつつ、席につく"),
            sana.think("既に不機嫌な編集長と、一人だけスマホをずっと触っている$nirasaki、に緊張が走っているのを感じる"),
            yone.do("$yonezawaはずっと資料に目を向けている"),
            yone.talk("じゃあ、そろそろ良いでしょうか。本日は『$hermagazine1』一月号特集についてです。お手元の資料をご覧下さい"),
            sana.do("$yonezawaの説明を聞きながら小説のネタを考えている"),
            yone.talk("$sanaさんはどうですか。引き継いだ$noto先生とのやり取りは？"),
            sana.do("雑誌の企画や作家とのやり取りの進捗報告を行う"),
            sana.talk("$noto先生ですが、顔合わせを済ませてからも何度かお宅の方に伺って、綿密に連絡を取っています",
                "携帯電話も持たれていないので今後も実際に訪問してのやり取りになると思います",
                "現在のところ、特集の短編の方の執筆に取り掛かられていて、原稿待ち、ですね"),
            king.talk("$fukaya君の置土産だから頼まれてやっているが、どうなんだ。そもそも文芸先生様にラノベが書けるのか？"),
            sana.talk("はい、もうバッチリです。資料用に大量にライトノベルを読まれてますし、本人のやる気ももりもりですから！"),
            sana.think("何いってんだ、と内心で"),
            king.talk("こっち界隈じゃ全然メジャーじゃないし、そもそもどれくらい読者ついてるか分からないけど、これで駄目だったらすぐ方向転換するからな"),
            sana.think("編集長は$fukaya先輩のことを気に入っていないが、実績があるので無下にもできないでいる"),
            ## NOTE
            ##  会議の様子（初登場）
            ##  厳しさを知らしめる
            stage=w.on_meetingroom_int,
            day=w.in_nogetpaper3.nextDay(), time=w.at_afternoon,
            )

## episode
def ep_pear(w: World):
    return w.episode("1.洋梨",
            ## NOTE
            sc_introuble(w),
            sc_oldnovel(w),
            sc_deadline_approach(w),
            )
