import os, shutil, sys
def organize(folder):
    moved = {}
    for fn in os.listdir(folder):
        p = os.path.join(folder, fn)
        if not os.path.isfile(p): continue
        ext = os.path.splitext(fn)[1].lstrip(".").lower() or "no_extension"
        dest = os.path.join(folder, ext); os.makedirs(dest, exist_ok=True)
        shutil.move(p, os.path.join(dest, fn)); moved[fn] = ext
    return moved
if __name__ == "__main__":
    print(organize(sys.argv[1]))
