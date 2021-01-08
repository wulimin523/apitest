# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :read_json
# @Date     :2021/1/5 17:46
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import json


def read_json(filename):
    with open( "../data/" + filename, "r", encoding="utf-8" ) as f:
        return json.load(f)


if __name__ == '__main__':
    print(tuple(read_json( "dp_post.json" ).values()) )
