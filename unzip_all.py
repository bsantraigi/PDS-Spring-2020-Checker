import glob
import re
import os
import zipfile

zips = glob.glob("*.zip")

for zip in zips:
    print(zip)
    # m = re.search(r"(Assignment [^-]+)-.*\.zip", zip)
    m = re.search(r"(Problem [^-]+)-.*\.zip", zip)
    print(m)
    if m is not None:
        trg = f"{m.group(1)}"
        trg = re.sub(r"[()]", "_", trg)
        print(trg)
        try:
            os.makedirs(trg)
        except FileExistsError:
            pass

        with zipfile.ZipFile(zip, 'r') as zip_ref:
            zip_ref.extractall(f"{trg}/")