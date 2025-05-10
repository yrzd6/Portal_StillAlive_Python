from argparse import ArgumentParser


SUPPORTED_LANGS = ["en_US", "zh_CN"]
config = {"language": "en_US", "nosound": False, "stay": False}

def shell():
    global config
    parser = ArgumentParser(description="Portal \"Still Alive\" for Terminal")

    parser.add_argument(
        "-l",  "--language",
        help="Change the language of the output",
        nargs="+",
        default=None
    )

    parser.add_argument(
        "-ns", "--nosound", "--no-sound",
        help="Turn off the sound",
        action="store_true"
    )

    parser.add_argument(
        "-s", "--stay",
        help="Do not exit the program after the run ends",
        action="store_true"
    )

    args = parser.parse_args()

    if args.language:
        if args.language[0] in SUPPORTED_LANGS:
            config["language"] = args.language[0]
    if args.nosound:
        config["nosound"] = True
    if args.stay:
        config["stay"] = True


shell()