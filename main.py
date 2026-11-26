from argparse import ArgumentParser
from pathlib import Path


def write_entry(destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(b"When I clap, I can make the sound come from the other hand.")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("/output/entry.txt"))
    write_entry(parser.parse_args().output)
