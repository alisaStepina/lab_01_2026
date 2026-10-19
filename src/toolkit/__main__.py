import argparse
import sys

from .converter import convert


def main():
    p = argparse.ArgumentParser(prog="toolkit")
    sub = p.add_subparsers(dest="cmd", required=True)

    pc = sub.add_parser("calc")
    pc.add_argument("expr")

    pv = sub.add_parser("convert")
    pv.add_argument("v", type=float)
    pv.add_argument("--from", dest="f", required=True)
    pv.add_argument("--to", dest="t", required=True)

    a = p.parse_args()

    try:
        if a.cmd == "convert":
            print(convert(a.v, a.f, a.t))
            return 0
        elif a.cmd == "calc":
            import json

            from .calculator import calculate, tokenize
            tokens = tokenize(a.expr)
            result = calculate(tokens)
            print(result)

            try:
                with open("history.json", "a") as f:
                    f.write(json.dumps({"expr": a.expr, "result": result}) + "\n")
            except OSError:
                pass

            return 0
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())