from config import subjects, fname

DOIT_CONFIG = dict(sort="definition")


def task_download():
    """Download the data."""
    for subject in subjects:
        yield dict(
            name=f"sub-{subject:02d}",
            file_dep=["01_download.py"],
            targets=[fname.mat(subject=subject)],
            actions=[f"python 01_download.py {subject}"],
        )


def task_preprocessing():
    """Convert to MNE-Python format and bandpass filter."""
    for subject in subjects:
        yield dict(
            name=f"sub-{subject:02d}",
            file_dep=[fname.mat(subject=subject), "02_preprocessing.py"],
            targets=[fname.filtered(subject=subject)],
            actions=[f"python 02_preprocessing.py {subject}"],
        )
