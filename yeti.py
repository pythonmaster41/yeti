#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import argparse

logging.basicConfig(format='%(levelname)s:%(module)s:%(message)s', level=logging.ERROR)

def webserver(args):
    from core.web import webapp
    webapp.debug = args.debug
    syncdb()
    print "[+] Yeti started. Point browser to http://localhost:5000/{}".format(" (debug)" if args.debug else "")
    webapp.run(host="0.0.0.0")

def syncdb(args=None):
    from core.internals import Internals
    Internals.syncdb()

COMMANDS = {
 'webserver': webserver,
 'syncdb': syncdb,
}

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='sub-command help', dest="command")

    webserver = subparsers.add_parser('webserver', help='Launch yeti webserver')
    webserver.add_argument('--debug', action='store_true', help="Run Flask in debug mode")

    syncdb = subparsers.add_parser('syncdb', help='Sync database with Yeti version')

    args = parser.parse_args()
    command = args.command
    COMMANDS[command](args)

if __name__ == '__main__':
    main()
