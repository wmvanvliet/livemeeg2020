"""
This script performs a series of checks on the system to see if everything is
ready to run the analysis pipeline.
"""

import os
from importlib import metadata
from packaging.requirements import Requirement, SpecifierSet
from packaging.version import Version

# Check to see if the python dependencies are fullfilled.
dependencies = []
with open("./requirements.txt") as f:
    for line in f:
        line = line.strip()
        if len(line) == 0 or line.startswith("#"):
            continue
        dependencies.append(Requirement(line))

# Check installed packages against requirements
errors = []

for req in dependencies:
    try:
        installed_version = Version(metadata.version(req.name))
    except metadata.PackageNotFoundError:
        errors.append(f"Missing dependency: {req}")
        continue

    desired_version = SpecifierSet(str(req.specifier), prereleases=True)
    if installed_version not in desired_version:
        errors.append(
            f"Incompatible dependency: {req.name} "
            f"(installed: {installed_version}, required: {desired_version})"
        )

# Raise a single error if anything is wrong
if errors:
    raise RuntimeError("Dependency check failed:\n" + "\n".join(errors))

# Check that the data is present on the system
from config import fname

if not os.path.exists(fname.data_dir):
    raise ValueError(
        "The `raw_data_dir` points to a directory that does not exist: "
        + fname.data_dir
    )

# Prints some information about the system
import mne

mne.sys_info()

with open(fname.system_check, "w") as f:
    f.write("System check OK.")

print(
    "\nAll seems to be in order.\nYou can now run the entire pipeline with: python -m doit"
)
