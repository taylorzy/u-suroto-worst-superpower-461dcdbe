from pathlib import Path


def write_entry(source: Path, destination: Path) -> None:
    data = source.read_bytes()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 140 or not text.strip():
        raise ValueError("Entry must contain 1 to 140 characters and be nonblank")
    if text.splitlines() != [text]:
        raise ValueError("Entry must be one line")

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)


if __name__ == "__main__":
    write_entry(Path(__file__).with_name("entry.txt"), Path("/output/entry.txt"))
