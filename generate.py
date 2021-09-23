from subprocess import PIPE, Popen
from pathlib import Path

EXPORT_DIR = Path("./exports")

def find_collections(path: Path) -> list:
    """
    Finds all collections in the given path.
    """
    if type(path) is not Path:
        path = Path(path)
    collections = []
    for p in path.iterdir():
        if p.suffix == ".json":
            collections.append(p)
    return collections

def generate_collection(collection: Path, seed: str = "1") -> None:
    """
    Generates a Synth collection and output results to export directory under the collection name.
    """
    export_path = (EXPORT_DIR / collection.name).resolve()
    cmd = [
        "synth.exe", 
        "generate", 
        collection.parent.resolve(),
        "--collection", 
        collection.stem,
        "--seed",
        str(seed)
    ]
    
    export_file = open(export_path, "w")
    proc = Popen(cmd, stdout=export_file, stderr=PIPE)

    errors = proc.communicate()
    if len(errors) > 0 and errors[0]:
        err_msg = "generate_collection error: {collection}\n\terror: {errors}".format(
            errors="\n\t".join(errors),
            collection=collection
        )
        print(err_msg)


def main() -> None:
    """
    Walk through all collections in the given path and generate them.
    """
    global EXPORT_DIR

    collections_path = input("path to collections dir: ")
    export_dir = input(f"export directory (default {EXPORT_DIR.resolve()}): ")

    if str(export_dir).strip() and Path(export_dir).is_dir():
        EXPORT_DIR = Path(export_dir)
    
    collections = find_collections(collections_path)
    for collection in collections:
        generate_collection(collection)


if __name__ == "__main__":
    main()
