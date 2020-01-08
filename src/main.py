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


## NOTE:
#   1. 走れメロス
#   2. 吾輩は猫である
#   3. 蜘蛛の糸
#   4. 檸檬
#   5. 雪国
#   6. 城の崎にて
#   7. こころ
#   8. 金閣寺
#   9. 人間失格
#   10. 銀河鉄道の夜


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
    w.setBaseDate(2020)
    # set textures
    # set history
    # set lifenote
    # set block
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

