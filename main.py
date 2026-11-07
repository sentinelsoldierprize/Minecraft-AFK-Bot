"""Entry point for engine."""

from utils import build


def main():
    result = build(10)
    print(f"Project: {result}")


if __name__ == "__main__":
    main()
