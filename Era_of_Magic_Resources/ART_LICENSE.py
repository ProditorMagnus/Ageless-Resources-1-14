import os

license = "Original work under the CC BY-SA v4 license by inferno8."

# this script is only used for files that need to be renamed. Most files are loaded from dependency Era_of_Magic_Resources
rename = {}
for dname, dirs, files in os.walk("."):
    for fname in files:
        if ".png" != fname[-4:]:
            continue
        fpath = os.path.join(dname, fname)
        if "unit-groups" in dname:
            # Exceptions that keep GPL
            if "_cyclops_30" in fname:
                continue
            # Files not needed for Ageless
            if "_roc_30" in fname:
                raise Exception("Keeping Default Gryphon icon for AE Roc ")
            newName = fname.replace("eoma_","AE_mag_")
            rename[fpath] = os.path.join(dname, newName)
        else:
            raise Exception("Unsupported folder "+fpath)

for fname in rename:
    os.rename(fname, rename[fname])
    with open(rename[fname]+".license", "w") as f:
        f.write(license)