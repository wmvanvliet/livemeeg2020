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


def task_epochs():
    """Cut epochs and compute evokeds."""
    for subject in subjects:
        yield dict(
            name=f"sub-{subject:02d}",
            file_dep=[fname.filtered(subject=subject), "03_epochs.py"],
            targets=[fname.epochs(subject=subject), fname.evokeds(subject=subject)],
            actions=[f"python 03_epochs.py {subject}"],
        )


def task_ga():
    """Compute grand average evoked potentials."""
    return dict(
        file_dep=[fname.evokeds(subject=subject) for subject in subjects]
        + ["04_grand_average.py"],
        targets=[fname.ga_evokeds],
        actions=["python 04_grand_average.py"],
    )


def task_figure1():
    """Make figure 1 of the manuscript: grand average evokeds"""
    return dict(
        file_dep=[fname.ga_evokeds, "figure_ga_evokeds.py"],
        targets=[fname.figure_ga_evokeds],
        actions=["python figure_ga_evokeds.py"],
    )
