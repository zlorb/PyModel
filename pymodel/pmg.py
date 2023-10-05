#!/usr/bin/env python
"""
PyModel Graphics - generate graphics from pymodel FSM
"""
import os.path

from pymodel import GraphicsOptions
from pymodel.Dot import dotfile
import importlib
import sys

def main():
    (options, args) = GraphicsOptions.parse_args()
    if not args or len(args) > 2: # args must include one FSM module
        GraphicsOptions.print_help()
        exit()
    else:
        sys.path.append(os.path.dirname(os.path.abspath(args[0])))
        fsm = importlib.import_module(args[0])
        fbasename = options.output if options.output else args[0]
        fname = '%s.dot' % fbasename
        dotfile(fname, fsm, options.transitionLabels, options.noStateTooltip,
                options.noTransitionTooltip)

if __name__ == '__main__':
    main ()
