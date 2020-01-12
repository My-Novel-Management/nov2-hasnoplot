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
## local files
from nolongerhuman.childhood import ep_childhood
from nolongerhuman.finishwriting import ep_finished
from nolongerhuman.firstpart import ep_firstpart
from nolongerhuman.hishistory import ep_hissecret
from nolongerhuman.teenager import ep_schooldays


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
            ##  - 写真がキーになるが今回はアルバムを持ってくる　（人間失格
            ##  - バーのマダム的扱いで、深谷先輩を使う
            ep_firstpart(w),
            ep_childhood(w),
            ep_schooldays(w),
            ep_hissecret(w),
            ep_finished(w),
            note="死にそうになりながらも何とか長編執筆を終えた沙奈に先生が病院から消えたとの一報が入る",
            )
