# -*- coding: utf-8 -*-
"""Chapter: 人間失格
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from nolongerhuman.finishwriting import ep_finished


## define alias
W = Writer


## chapter
def ch_nolongerhuman(w: World):
    return w.chapter("人間失格",
            ## NOTE: どんな駄作でも最後まで書く
            ##  - 自信喪失から書けなくなる
            ##  - 第一の手記：小学生の頃　（人間失格
            ##  - 第二の手記：中高生、思想の偏り　（人間失格
            ##  - 第三の手記：そして病院送り　（人間失格
            ##  - 人を疑う心のなさ＝ヨシ子＝主人公　と見た先生　（人間失格　→自分は作家失格だと言い出す
            ##  - バーのマダムから先生の話を聞かされる　（人間失格
            ##  - 先生の作品を読んで、気づく
            ##  - 自分が一番書きたかったことを思い出す
            ##  - 死にそうになって書き上げる
            ##  - 何とか書き上げたら、先生の容態について一報が
            ep_finished(w),
            )
