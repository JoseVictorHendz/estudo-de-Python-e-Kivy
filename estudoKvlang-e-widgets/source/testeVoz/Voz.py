
import os


def main(args):
    os.system("espeak -vpt --stdout 'Bem vindo ao site do caderno de laboratorio.' | aplay")

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))