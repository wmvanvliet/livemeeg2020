# encoding: utf-8
"""
Convert the data into an MNE-Python Raw structure.
Bandpass-filter the data.
"""

from argparse import ArgumentParser
from scipy.io import loadmat
import joblib
import mne

from config import fname, n_jobs, sample_rate

parser = ArgumentParser(__doc__)
parser.add_argument("subject", type=int, help="Subject to process [1-64]")
args = parser.parse_args()

samples = loadmat(fname.mat(subject=args.subject))["samples"]
samples = samples.T

channel_types = ["misc"] + (16 * ["eeg"]) + ["stim", "stim"]
channel_names = [
    "Time",
    "Fp1",
    "Fp2",
    "F3",
    "AFz",
    "F4",
    "T7",
    "Cz",
    "T8",
    "P7",
    "P3",
    "Pz",
    "P4",
    "P8",
    "O1",
    "Oz",
    "O2",
    "Status",
    "Target",
]

# Convert unit of EEG channels from μV to V.
samples[[ch_type == "eeg" for ch_type in channel_types]] /= 1e6

raw = mne.io.RawArray(
    samples, mne.create_info(channel_names, sample_rate, channel_types)
)
raw.set_montage("standard_1005")

# Bandpass filter
joblib.parallel_config(backend="threading")
raw.filter(0.5, 30, n_jobs=n_jobs)

# Save result
raw.save(fname.filtered(subject=args.subject), overwrite=True)
