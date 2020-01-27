# -*- coding: utf-8 -*-
"""Episode: 9-1.はしがき／人間失格
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
def sc_notintime(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, tsuchi = W(w.nirasaki), W(w.tsuchiura)
    return w.scene("間に合わないことが決定",
            sana.come("病院にかけつける"),
            tsuchi.be("廊下でうろうろしている"),
            sana.talk("ねえ、先生の具合は？"),
            tsuchi.talk("命に別状はないらしいっすけど"),
            sana.talk("けど？"),
            tsuchi.talk("しばらく集中治療室から出られないだろうって"),
            sana.talk("そう"),
            sana.think("命が無事だったと聞いてほっとしたが、軽症という訳でもなさそうで複雑な気持ち"),
            sana.talk("面会は今は無理？"),
            tsuchi.talk("$meもまだ話してません"),
            sana.talk("意識はあるのよね？"),
            tsuchi.talk("看護師さんからはなんかうわ言のように悪かったって呟いてるって"),
            sana.think("考え込む"),
            tsuchi.talk("原稿、間に合いませんね……"),
            sana.talk("それはもういいのよ。原稿落としたところで$meが王に謝れば済む話だから"),
            _.talk("それよりも先生が折角また長編を書く気になってくれていたのに、その原稿を守れなかったのは、編集として失態だった"),
            sana.talk("とにかくありがとう。あとは$meがいるわ"),
            tsuchi.talk("いや、$meもいますよ"),
            sana.talk("何言ってんのよ。あんたには明日から毎日通ってもらわなきゃならないから"),
            tsuchi.talk("え？"),
            sana.talk("先生の様子見と経過報告、頼むわね"),
            tsuchi.do("苦笑している"),
            sana.think("自分の小説を書き上げてそれを穴に打ち込んで、何とか誤魔化す"),
            _.think("そんなことを考え始めていた"),
            camera=w.sana,
            stage=w.on_hospital,
            day=w.in_firemaster, time=w.at_night,
            )

def sc_alternative(w: World):
    sana, noto = W(w.sana), W(w.noto)
    nira, tsuchi = W(w.nirasaki), W(w.tsuchiura)
    king = W(w.king)
    return w.scene("代替案",
            w.comment("編集長から別の作家の作品をそこにぶちこむか、原稿を何とかするかと迫られ"),
            sana.come("翌日、沈痛な面持ちで出社してくる"),
            sana.look("髪はぼさぼさでメイクもそっけない"),
            sana.talk("おはようございます"),
            nira.talk("お、おう。大丈夫かよ？"),
            sana.talk("ええ。先生の方は何とか"),
            nira.talk("いや$ln_sanaの方だよ"),
            sana.talk("$meは丈夫なだけが取り柄なんで"),
            sana.think("実際疲労はすごいものがあった"),
            _.think("今朝もコンビニで買い込んだ栄養ドリンクをたらふく飲んで、それでほとんど朝食が食えなかったことを思い出す"),
            king.be("不機嫌な顔でパソコンを見ている"),
            king.talk("遅かったな。ちょっとあっち"),
            sana.talk("はい"),
            sana.do("編集長と二人で応接用パーテーションに"),
            king.talk("先生は無事と聞いたが"),
            sana.talk("はい"),
            king.talk("ただ原稿の方は焼けたそうだな？　コピーは？"),
            sana.talk("ありません"),
            king.talk("問題外だ。お前は編集として最低のことをしてる自覚はあるか？"),
            sana.talk("返す言葉はありません"),
            king.talk("前編集長のお気に入りだからってな、結果が出せなきゃ$meはやるからな"),
            _.talk("別のそれなりに知名度か人気がある作家の長編、今から間に合わせろ"),
            _.talk("できなきゃ減給。それにあと何人か面倒な作家の担当をおしつける。分かったな？"),
            sana.talk("ですが"),
            king.talk("商売なんだよ。本を売るのだって"),
            king.do("自分の席に戻ってしまう"),
            sana.do("溜息"),
            sana.think("これで完全に先生の出版は終わった"),
            nira.talk("ま、良かったかも知れないな。あの先生、ひょっとするとひょっとするし"),
            sana.talk("何よ？"),
            nira.talk("これ"),
            nira.do("スマホでネットニュースを見せる。そこには盗作疑惑？と"),
            sana.think("前に接触してきた雑誌記者だと直感"),
            sana.talk("どうしてこう次から次に"),
            stage=w.on_heroffice,
            day=w.in_nextfire, time=w.at_midmorning,
            )

## episode
def ep_firstnote(w: World):
    return w.episode("1.はしがき",
            ## NOTE
            sc_notintime(w),
            sc_alternative(w),
            )
