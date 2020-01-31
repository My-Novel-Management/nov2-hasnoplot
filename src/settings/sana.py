# -*- coding: utf-8 -*-
"""Setting: sana
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer
_ = W.getWho()


## setting person
def set_person(w: World):
    sana = W(w.sana)
    ## lifenote
    w.entryLifeNote(
        w.lifenote("$sanaの日常", w.sana,
            sana.do("出勤の一時間前に起床"),
            _.do("慌ただしく化粧をし、ルームメイトの誰かが作ってくれた朝食をご馳走になる"),
            _.go("出勤（電車を乗り継ぎ）"),
            _.come("出社"),
            _.do("まずメール等連絡事項の確認"),
            _.do("担当している作家や依頼している業者などに連絡"),
            _.do("昼食はコンビニか、軽食、うどんやそば等"),
            _.do("先生の家に行く、か、編集会議に出るか"),
            _.do("外回りを終えて帰社"),
            _.do("夜にならないと連絡が取れない人がいるので、そっちに連絡等"),
            _.do("原稿などのチェック"),
            _.do("基本残業があり、帰りは終電前なら御の字"),
            )
    )

    ## history
    w.entryHistory(w.sana,
    *w.createHistories(
        (6, "小学校入学"),
        (18, "大学入学"),
        (22, "大学卒業"),
        (23, "中堅出版社に就職"),
        (24, "雑誌部で鍛えられる"),
        (25, "急遽異動で第二文芸部に"),
            ),
    )
    ## texture
    w.setTexture("sana", "140cm台の小柄、肉付きは良い。髪は耳が隠れる程度のボブ")

