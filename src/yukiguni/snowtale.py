# -*- coding: utf-8 -*-
"""Episode: 5-3.雪国抄／雪国
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
def sc_party(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("パーティにて",
            sana.do("夜は家に先生の知人や親戚が集まり、パーティだった"),
            sana.do("何故か結婚相手になってしまっていることに"),
            sana.talk("いや、違いますから"),
            sana.explain("だが親たちには宜しくと頼まれ、親戚のおじさんたちには「どうせ彼氏おらんのやろ」と茶化され"),
            stage=w.on_hishome,
            day=w.in_homevisit, time=w.at_night,
            )

def sc_talkmaster(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("先生と二人で",
            sana.do("何とか抜け出したところに、近づく影"),
            sana.talk("なんだ。先生か"),
            noto.talk("ごめんね。でもこれが実家なんだよ"),
            noto.talk("作家先生って持ち上げて、やれ芥川賞だ直木賞だってね"),
            noto.talk("彼らは本を読んだりなんかしていない。ただ芸能人に群がる野次馬と同じだ"),
            noto.talk("でも、応援してくれる人たちなんだよ。ああいう人たちが、沢山ではないけれども、確実にいる"),
            noto.talk("君にはそれを見てもらいたかった"),
            sana.talk("どういうことですか？"),
            noto.talk("作家というのが、どういう商売なのか、またその先の読者とは何なのか、ということについて"),
            noto.talk("君たちには分からない。でもこれが現実だということ"),
            noto.talk("細部の文章まで突き詰めて、ひらがな一文字に命を削る"),
            noto.talk("そこまでして、やっと届くかも知れないと思った作品でも、多くの人は買って適当にページを捲るだけだ"),
            noto.talk("小説というのはもともとマイナーな世界なんだ"),
            noto.talk("映画やドラマなどの実写になったものなら、また違うだろう。けど本は読まないといけない"),
            noto.talk("今の若い人たちは読み取れない人が増えているというじゃないか"),
            noto.talk("文章よりも展開ばかり重視され、そこには難解な文章などいらない、描写など最低限でいい、なんて声もある"),
            noto.talk("売れ筋の本はどうだ？", "読みやすく、伝わりやすい文章", "それを並べたもの"),
            noto.talk("ただ展開を書き連ね、大半をセリフで埋める"),
            noto.talk("キャラクターのやり取りで何ページも過ごす"),
            noto.talk("心情描写ばかりで、肝心の情景描写やそこから心情や状況を深く読み取ってもらうなんて読み方は歓迎されない"),
            noto.talk("小説はいつか滅びる文化なんだよ。物語は残ってもね"),
            sana.talk("そんなのって"),
            sana.talk("作家が小説を、自分の作品を信じなくてどうするんですか！"),
            noto.talk("だが事実。$meの本は売れなかった"),
            noto.talk("今回書いた短編だって、そこに書き込んだ本当の意味をいったい何人が読み取れる？"),
            noto.talk("どんな世界だって書く。どんな物語だって書く。けど、そこが本質じゃあない！"),
            asahi.come(),
            asahi.talk("また言ってる。そうやって追い詰めたの、忘れたの？"),
            )

def sc_anotherlady(w: World):
    sana, noto = W(w.sana), W(w.noto)
    tsuru, komi, asahi = W(w.tsuru), W(w.komi), W(w.asahi)
    return w.scene("先生の初恋",
            sana.do("苦手な人だ、と感じた"),
            asahi.talk("あなたは二人を殺したのよ。まだ、$meはそう思ってるから"),
            noto.do("黙っている"),
            asahi.talk("作家先生なんて言って、みんな偉い人のように扱ってるけど、知ってるでしょ。全然売れてないの"),
            _.talk("この前本屋に行ったらもう棚に並んでないのよ"),
            _.talk("これがあの二人と引き換えに手に入れた作家って地位かと思ったら、情けなくなってきちゃってね"),
            sana.talk("先生は"),
            noto.talk("いいんだ。事実だよ"),
            _.talk("これがね、大半の作家の現実なんだ"),
            _.talk("どの世界だってそうだよ。僅か１％の人材がその世界のトップで幅を利かせている"),
            _.talk("残りはほとんどが知られないまま、ひっそりと、何とか踏ん張って、でも踏ん張りがきかなくなったらドロップアウト"),
            _.talk("まだ$meみたいに声を掛けてもらえるのはありがたい方さ"),
            _.talk("たとえ本屋に本がなくてもね"),
            asahi.talk("ごめん。そんなつもりじゃ。ちょっと飲みすぎたかな"),
            noto.talk("いいんだ。事実だし"),
            asahi.talk("担当さん、だっけ？", "ちょっとだけ席を外してもらえる？"),
            sana.talk("はい。わかりました"),
            sana.go(),
            sana.think("それから二人で何を話したのかは知らない"),
            _.think("ただ、後ですれ違った彼女は、泣いていた"),
            )

## episode
def ep_snowtale(w: World):
    return w.episode("3.雪国抄",
            ## NOTE
            sc_party(w),
            sc_talkmaster(w),
            sc_anotherlady(w),
            )
