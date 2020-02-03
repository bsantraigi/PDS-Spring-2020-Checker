import glob
import re
import os
import zipfile

zips = glob.glob("*.zip")

for zip in zips:
    print(zip)
    m = re.search(r"(Assignment [0-9]+\(.\)).+\.zip", zip)
    print(m)
    trg = f"{m.group(1)}"
    trg = re.sub(r"[()]", "_", trg)
    print(trg)
    try:
        os.makedirs(trg)
    except FileExistsError:
        pass

    with zipfile.ZipFile(zip, 'r') as zip_ref:
        zip_ref.extractall(f"{trg}/")