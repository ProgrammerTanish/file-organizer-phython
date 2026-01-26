import os
import shutil
import argparse
from config import FILE_CATEGORIES
from logger import log


def get_category(extension: str) -> str:
    if not extension:
        return "Others"

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


def organize_folder(path: str, preview: bool = False, include_hidden: bool = False):
    path = os.path.abspath(path)
    moved = skipped = errors = 0

    if not os.path.exists(path):
        print("❌ Path does not exist.")
        return

    log(f"Started organization | Preview={preview} | Include hidden={include_hidden}")

    with os.scandir(path) as entries:
        for entry in entries:

            # Skip non-files
            if not entry.is_file():
                continue

            # Skip hidden files unless explicitly allowed
            if not include_hidden and entry.name.startswith("."):
                skipped += 1
                log(f"SKIPPED (hidden): {entry.name}")
                continue

            try:
                _, ext = os.path.splitext(entry.name)
                ext = ext.lower().lstrip(".")

                category = get_category(ext)
                target_folder = os.path.join(path, category)
                target_path = os.path.join(target_folder, entry.name)

                if preview:
                    print(f"[PREVIEW] {entry.name} ➜ {category}/")
                    log(f"PREVIEW: {entry.name} ➜ {category}/")
                else:
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(entry.path, target_path)
                    moved += 1
                    log(f"MOVED: {entry.name} ➜ {category}/")

            except PermissionError:
                skipped += 1
                errors += 1
                log(f"PERMISSION DENIED: {entry.name}")

            except Exception as e:
                skipped += 1
                errors += 1
                log(f"ERROR: {entry.name} | {e}")

    print("\n📊 Summary Report")
    print("------------------")
    print(f"Files moved   : {moved}")
    print(f"Files skipped : {skipped}")
    print(f"Errors        : {errors}")

    log(f"Completed | Moved={moved}, Skipped={skipped}, Errors={errors}")
    print("✅ Operation completed. See organizer.log for details.")


def main():
    parser = argparse.ArgumentParser(
        description="File Organizer & Cleanup Automation Tool"
    )

    parser.add_argument(
        "path",
        help="Path of the folder to organize"
    )

    parser.add_argument(
        "-p", "--preview",
        action="store_true",
        help="Preview mode (no files will be moved)"
    )

    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include hidden files (e.g. .gitignore)"
    )

    args = parser.parse_args()

    organize_folder(
        path=args.path,
        preview=args.preview,
        include_hidden=args.include_hidden
    )


if __name__ == "__main__":
    main()
