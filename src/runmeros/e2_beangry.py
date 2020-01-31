# -*- coding: utf-8 -*-
"""Episode: 1-2.憤れ編集者／走れメロス
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
def sc_mycompany(w: World):
    sana, noto = W(w.sana), W(w.noto)
    exterior = W(w.exterior)
    return w.scene("私の会社です",
            sana.come("何喰わぬ顔で会社ビルまでやってくる"),
            exterior.look("六階建てのビル"),
            _.look("壁面はガラス張りになっている"),
            sana.do("遅めの出社の人たちもいる"),
            sana.explain("三階と四階が$Sがこの秋から勤務する『$on_hercompany』"),
            exterior.look("ビルの一階はコンビニ"),
            sana.go("脇の入り口から入り、エレベータに乗り込む"),
            ## NOTE:
            ##  外観でどれくらいの規模の会社か、あと立地なんかの条件をさらっと伝える
            ##  あと時間帯（駅からどれくらいの距離とか、肌感覚で）
            camera=w.sana,
            stage=w.on_hercompany_ext,
            day=w.in_firstmeet, time=w.at_midmorning,
            )

def sc_myoffice(w: World):
    sana, noto = W(w.sana), W(w.noto)
    fukaya, king, nira, yone = W(w.fukaya), W(w.king), W(w.nirasaki), W(w.yonezawa)
    wall = W(w.wall)
    door = W(w.door)
    return w.scene("編集部です",
            sana.come("廊下を歩いて、第二文芸部の前"),
            wall.look("色々と刊行本やアニメ、漫画のポスターがずらりと貼られている"),
            wall.look("人気作『$isesui』のポスターもある", w.poster_isesui),
            w.comment("イセスイの簡単な雰囲気描写。ポスターの絵柄でそれっぽく。できればこのすば的なの"),
            door.look("ドアノブのついた引き戸にプレートで『第二文芸部』とある"),
            sana.do("腕時計で時刻を確認して、ちょっと過ぎたな、と思うが、ドアを開けて"),
            king.talk("もっとバーンと数字出そうな企画ないの？"),
            sana.hear("編集長の大きな濁声が外まで響く"),
            sana.think("また機嫌悪いのかな、と思いつつ"),
            sana.talk("おはようございます"),
            ## NOTE:
            ##  何階か、あとざっと廊下や外観
            ##  主力のIP何か（それを書いている人が、短編参加予定だが後で引き抜かれる）
            stage=w.on_heroffice_ext,
            )

def sc_myteam(w: World):
    sana, noto = W(w.sana), W(w.noto)
    fukaya, king, nira, yone = W(w.fukaya), W(w.king), W(w.nirasaki), W(w.yonezawa)
    interior = W(w.interior)
    desk = W(w.desk)
    return w.scene("同僚たち",
            sana.come("オフィスに入ってくる"),
            interior.look("パーテーションで区切られた空間"),
            _.look("パソコンの載った事務机が四つの島を作る"),
            _.look("営業部と第二文芸部のプレートが天井から下がる"),
            yone.be("仕事をしている"),
            yone.wear("シャツにベスト、ストライプのズボン、ネクタイ"),
            sana.do("自分のデスクに向かう"),
            fukaya.be("慌ただしく自分の机で準備中"),
            fukaya.wear("ゆったりしたディープグリーンのロングワンピにストレッチ素材のパンツ"),
            _.do("$sanaを見つけてやってきて"),
            fukaya.talk("ああ$sana。ごめんね、今日午後からだったのに"),
            sana.talk("いいですよ。どうせ半日寝てるくらいですし"),
            _.talk("でもまだインフルには早いんじゃないです？　$nirasakiさん"),
            w.comment("$nirasakiは本日不在なので、若干説明入れる"),
            sana.explain("$nirasakiとは$Sより先輩で、とにかく人付き合いの悪い、編集者としてあるまじき人間性の男だ"),
            fukaya.talk("人が嫌いなんだって普段言ってる癖に、ウイルスには好かれてるのかしら。去年も罹ってるからね"),
            sana.explain("$full_fukayaは$Sをこの出版社に引き抜いてくれた恩人でもあり、前勤務していた編プロの敏腕編集者でもあった"),
            _.explain("雑誌よりも書籍の編集がやりたくてステップアップしたのだ"),
            _.explain("人生で尊敬する女性の一人だった"),
            yone.do("ちらっと見やる"),
            sana.explain("$yonezawaは副編集。まるでロボットみたいに冷たい反応なことから密かにＡＩと呼ばれている",
                "#$yonezawaのあだ名"),
            fukaya.talk("さっき$lineでも書いたけど、急でごめんね。$meの担当している先生の一人を、受け持ってもらいたいの"),
            sana.talk("いいですけど、どうして急に"),
            fukaya.talk("産休を早めに取ることにしたのよ。ちょっと昨日診てもらったら、その方がいいってことで"),
            sana.explain("三十過ぎてから初出産で、それなのに色々と忙しくしていたのだ"),
            sana.talk("大丈夫です。あ、引き継ぎは"),
            fukaya.talk("ここに資料は用意してあるから"),
            desk.look("大量に積み上げられたファイルとプリントアウト"),
            w.eventStart("先生の担当引き継ぎ"),
            ## NOTE:
            ##  主戦場（オフィス）紹介
            ##  メインキャラたち軽く紹介（説明なしに、やり取りだけで紹介すること）
            ##  深谷の外見に人柄、能力はここで紹介しないと後は場面が少ない
            ##  当面の目標設定「先生の担当引き継ぎ」
            ##  締切のこともちらっと触れる
            stage=w.on_heroffice_int,
            )

def sc_callking(w: World):
    sana, noto = W(w.sana), W(w.noto)
    fukaya, king, nira, yone = W(w.fukaya), W(w.king), W(w.nirasaki), W(w.yonezawa)
    return w.scene("王の呼び出し",
            king.come("$CSの方にやってくる"),
            king.talk("全く"),
            king.wear("恰幅のいいお腹が目立つ、ぴちぴちのスーツ、前を開けている"),
            sana.explain("編集長でその言動から通称「王」と呼ばれる男だ"),
            king.talk("全く$fukaya君も編集部が忙しい時に産休とはね"),
            fukaya.talk("もう少し働かせてもらうつもりだったんですが、人事部の方からもちゃんと休むように言われましたもので"),
            king.look("不機嫌な顔"),
            king.talk("それはともかくとして、$noto先生の担当、ほんとに彼女で大丈夫なんだろうな？"),
            sana.talk("$noto先生？"),
            fukaya.talk("大丈夫ですよ。$meが編プロ時代に指導してますし、何より彼女、ガッツは一人前ですから"),
            w.comment("編プロの説明は巻末用語解説にでも"),
            king.talk("ガッツだ根性だなんて前時代的なものは現代じゃいらないんだよ。それより数字っていう結果を出してもらいたいね"),
            _.talk("彼女が八月にやってきてから、一体何の結果を残したっていうんだ？"),
            sana.think("内心で苦笑"),
            _.think("やらされたのは雑用ばかりだったのに何が結果だろう"),
            king.talk("$fukaya君の頼みだから枠を開けてるけど、昔有名だった程度の作家、腐るほどいるからね。$full_nisinoクラスの大先生様なら歓迎するけど、", "&"),
            _.talk("今更あのクラスがラノベ書いてくれるとは思わん"),
            king.do("文庫本のサンプルを手にとって"),
            king.talk("今やうちみたいな弱小出版社じゃ薄利多売で凌ぐしかない。メディアミックスも望めない古豪作家が今更ラノベ書いたところでね"),
            fukaya.talk("こういう時だからこそ、本物が必要なんですよ。本物の小説は、心を動かします。それを$meたちが信じなくてどうするんですか"),
            king.go("鼻で笑って行ってしまう"),
            ## NOTE: 編集長の横暴をここで示しておく
            ## NOTE: アイデアについて、特に企画書について云々を
            )

def sc_emergency(w: World):
    sana, noto = W(w.sana), W(w.noto)
    fukaya, king, nira, yone = W(w.fukaya), W(w.king), W(w.nirasaki), W(w.yonezawa)
    return w.scene("緊急事態",
            sana.talk("いつもの先輩の力強い演説、素敵です"),
            fukaya.talk("ありがと……ん"),
            fukaya.do("お腹を押さえて屈み込む"),
            sana.talk("先輩大丈夫ですか？　顔色が"),
            fukaya.talk("ごめん。ちょっと"),
            fukaya.do("顔を顰めてうずくまる"),
            sana.talk("あの、救急車呼びます！"),
            sana.do("慌てて電話を取る"),
            yone.come("やってきて"),
            yone.talk("$fukayaさん？"),
            fukaya.talk("うん……"),
            _.do("それしか言えない"),
            sana.talk("あ、あの"),
            yone.talk("何やってるの、$sanaさん。救急車"),
            sana.talk("えっと"),
            yone.talk("$meが掛けるから、君は彼女に付いてて"),
            yone.talk("あ、もしもし。はい。こちら$on_hercompanyの第二文芸部ですが、妊婦が急に体調を崩しまして。ええ……"),
            fukaya.talk("$sana、頼んだわよ。先生のこと。大変だと思うけど"),
            sana.talk("は、はい"),
            fukaya.talk("ありがとう。助かるわ。あと先生に合鍵を返しておいて。使ってもいいけど、一応断ってからの方がいいと思うの", w.sparekey),
            _.do("苦笑しつつも立ち上がれない"),
            sana.explain("それから十分ほどして救急車で先輩は運ばれて行った"),
            )

## episode
def ep_angryeditor(w: World):
    return w.episode("2.憤れ編集者",
            ## NOTE
            sc_mycompany(w),
            sc_myoffice(w),
            sc_myteam(w),
            sc_callking(w),
            sc_emergency(w),
            )
