# coding=utf-8

from __future__ import print_function

from server import Server
from decorator import url
from helper import rest


__all__ = ["Welcome", "Server", "url", "rest"]


def Welcome():

    #
    # 输出欢迎信息。
    #

    import config
    from router import Router
    from string import uppercase

    from util import max_key_length, http_methods_flag

    def pprint(iterator, title, key, callback):
        print("\n=== {0} ===\n".format(title))
        d = sorted(iterator, key=key)
        n = max_key_length(d, key)
        map(lambda v: callback(v, n), d)

    # 配置信息。
    options = {k: v for k, v in vars(config).iteritems() if set(k) < set(uppercase + "_")}

    pprint(options.iteritems(),
           "Options",
           lambda (k, v): k,
           lambda v, n: print("  {0} : {1}".format(v[0].ljust(n), v[1])))

    # Handlers 信息。
    handlers = (
        (
            "{0}.{1}".format(h.__module__, h.__name__),  # handler
            u,  # url
            m,  # http methods
        ) for u, (h, m) in Router.instance.handlers.iteritems())

    pprint(handlers,
           "Handlers",
           lambda (h, u, m): h,
           lambda v, n: print(" {0} : [{2}] {1}".format(v[0].ljust(n), v[1], http_methods_flag(*v[2]))))

    print()
