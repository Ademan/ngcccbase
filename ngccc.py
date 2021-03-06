#!/usr/bin/python

from wallet_controller import WalletController
from pwallet import PersistentWallet
from console_interface import CommandInterpreter
import json


def main():
    import sys
    import getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", [])
    except getopt.GetoptError:
        print "arg error"
        sys.exit(2)

    if len(args) == 0:
        args = ['help']
    # special command
    if args[0] == 'import_config':
        with open(args[1], "r") as fp:
            config = json.load(fp)
        pw = PersistentWallet(config)
        sys.exit(0)

    pw = PersistentWallet()
    try:
        pw.init_model()
    except Exception as e:
        print "failed to initialize wallet model: %s" % e

    wallet_model = pw.get_model()
    controller = WalletController(wallet_model) \
        if wallet_model else None
    interpreter = CommandInterpreter(pw, controller)

    interpreter.run_command(*args)

if __name__ == "__main__":
    main()
