#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A simple implementation of the inventor Arnie's gadget from Chapter
IX ("Fixed Point Puzzles") of Raymond Smullyan's "The Gödelian Puzzle
Book".
"""

import readline

def rule(method):
    method.is_rule = True
    return method


class GadgetBase(object):
    def __call__(self, s):
        if not s or len(s) == 1:
            return s
        f = getattr(self, s[0], None)
        if not f or not f.is_rule:
            return s
        return f(s[1:])

    def repl(self):
        def loop():
            while True:
                s = raw_input('>>> ')
                if s:
                    if s in ('quit', 'exit', 'bye'):
                        return
                    print self(s)
        try:
            loop()
        except (EOFError, KeyboardInterrupt):
            print
            return


class ArnieGadget(GadgetBase):

    @rule
    def Q(self, s):
        return s

    @rule
    def C(self, s):
        # evaluate s
        y = self(s)
        return '%sQ%s' % (y, y)

    @rule
    def R(self, s):
        # evaluate s
        y = self(s)
        return '%s%s' % (y, y)

    @rule
    def V(self, s):
        # evaluate and reverse
        return self(s)[::-1]

    @rule
    def P(self, s):
        # evaluate s
        y = self(s)
        return '%s%s' % (y, y[::-1])

    @rule
    def M(self, s):
        return s[1:] + s[0]


if __name__ == '__main__':
    ArnieGadget().repl()

    
    
