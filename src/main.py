# -*- coding: utf-8 -*-
"""Main story.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import PERSONS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## local files
from src.gingatrain.main import ch_gingatrain
from src.imcat.main import ch_Imacat
from src.kinkaku.main import ch_kinkakuji
from src.kinosaki.main import ch_kinosaki
from src.kokoro.main import ch_kokoro
from src.lemon.main import ch_lemon
from src.nolongerhuman.main import ch_nolongerhuman
from src.runmeros.main import ch_runmeros
from src.spidersilk.main import ch_spidersilk
from src.yukiguni.main import ch_yukiguni
## blocks
from src.substories.plagiarism import bk_plagiarism
from src.substories.publish_longnovel import bk_longnovel
from src.substories.publish_short import bk_shortnovel
## settings
from src.settings import asahi
from src.settings import azumino
from src.settings import fukaya
from src.settings import gero
from src.settings import king
from src.settings import komi
from src.settings import noto
from src.settings import owase
from src.settings import sana
from src.settings import tsuru
from src.settings import stages


## NOTE:
#   1. 走れメロス       アイデア        企画        異動、先生との出会い
#   2. 吾輩は猫である   起承転結        打ち合わせ  プロットすらないと
#   3. 蜘蛛の糸         プロット        編集会議    短編を書くことに、書けない告白
#   4. 檸檬             長編と短編      入稿        短編を書く、探していた本が先生の作品だった
#   5. 雪国             文章            慰安        長編を書くことに、先生の初恋
#   6. 城の崎にて       シーン          取材        小旅行、先生のトラウマ
#   7. こころ           キャラクタ      複数人      盗作がデビュー作だった
#   8. 金閣寺           サブストーリー  残業        書けない、先生入院
#   9. 人間失格         書き切る        ゲラ        長編執筆、先生急変
#   10. 銀河鉄道の夜    修正            製本        先生死ぬの？ゲラ地獄


## main
def create_world():
    """Create a world.
    """
    w = World("先生プロットがありません！")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.buildDB(PERSONS,
            STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(2017)
    # set persons
    asahi.set_person(w)
    azumino.set_person(w)
    fukaya.set_person(w)
    gero.set_person(w)
    king.set_person(w)
    komi.set_person(w)
    noto.set_person(w)
    owase.set_person(w)
    sana.set_person(w)
    tsuru.set_person(w)
    # set stages
    stages.set_stages(w)
    # set block
    w.entryBlock(
            *bk_plagiarism(w),
            *bk_longnovel(w),
            *bk_shortnovel(w),
            )
    # set outline
    w.setOutline("出版社に勤める沙奈は世話になった先輩の産休の穴埋めとして書籍部に異動になり、癖のある大先生の担当となるが、原稿を取りに行くとプロットすらないと言われた")
    return w

def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch_runmeros(w), # 走れメロス
            ch_Imacat(w), # 吾輩は猫である
            ch_spidersilk(w), # 蜘蛛の糸
            ch_lemon(w), # 檸檬
            ch_yukiguni(w), # 雪国
            ch_kinosaki(w), # 城の崎にて
            ch_kokoro(w), # こころ
            ch_kinkakuji(w), # 金閣寺
            ch_nolongerhuman(w), # 人間失格
            ch_gingatrain(w),# 銀河鉄道の夜
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

