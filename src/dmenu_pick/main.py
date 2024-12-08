from argparse import ArgumentParser
from subprocess import run
from tomllib import load


def pick(items: dict[str, str]) -> str:
    picked = run(
        ("dmenu",),
        input='\n'.join(items).encode("utf-8"),
        capture_output=True
    ).stdout.decode("utf-8")[:-1]
    return items[picked]


def main() -> None:
    parser = ArgumentParser(
        prog="dmenu_pick",
        description="Some script to pick things using dmenu"
    )
    parser.add_argument(
        "config",
        help="Some config written with associations written as `hello=\"world\"`\"`, one on each line"
    )
    args = parser.parse_args()

    with open(args.config, "rb") as f:
        print(pick(load(f)))


if __name__ == "__main__":
    main()
