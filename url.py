import os
from androguard.misc import AnalyzeAPK
from androguard import session
import matplotlib.pyplot as plt
import networkx as nx
from itertools import chain
from itertools import product
from itertools import starmap
from functools import partial
import argparse
import re
import datetime
import psutil


def url_search(a, dx, url_pattern):
    idx = 0
    #strategy 1 using url pattern:
    print("\n[*]url patern found:")
    for url in url_pattern:
        results = dx.find_strings(url)
        for res in results:
            idx += 1
            print("FOUND:",idx,res.get_value())
            print(res)
    
    #strategy 2 using url class path pattern:
    print("\n[*]url class path found:")
    results=list(dx.find_strings('http://'))
    for res in results:
        url_class = list(res.get_xref_from())[0][0]
        if 'pay' in url_class.name.lower():
            idx += 1
            print("FOUND:",idx,res.get_value())
            print(res)

    print("Total Found:", idx)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analysis of Finger-Jacking Attack')
    parser.add_argument('apk', metavar='FILE',
                        help='APK file to analysis')

    args = parser.parse_args()
    apk_name = args.apk

    time_begin = datetime.datetime.now()
    print("start at:{}".format(time_begin))

    print("\n[*] Analyzing APK ...")
    a, d, dx = AnalyzeAPK(apk_name)

    #strategy 1: using [pay] pattern to directly search payurl 
    url_pattern=['http://payment','http://pay']
    url_search(a,dx,url_pattern)

    time_end = datetime.datetime.now()
    time = time_end - time_begin
    print("\nend at:{}".format(time_end))
    print("total time:{}".format(time))
    process=psutil.Process(os.getpid())
    print("Maximum Memory Usage: {} MB".format(process.memory_info().rss/1024/1024))