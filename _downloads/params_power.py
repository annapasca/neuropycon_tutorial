""" Parameters file for run_power_analysis.py """

data_type = 'fif'

main_path = '/run/media/pasca/paska/meg_data/omega/sample_BIDS_omega/'

data_path = main_path

# subject_ids = ['sub-0002', 'sub-0003', 'sub-0004', 'sub-0006', 'sub-0007']
subject_ids = ['sub-0002']
sessions = ['ses-0001']

# -------------------------- SET power variables --------------------------#
freq_bands = [[2, 4], [5, 7], [8, 12], [13, 29], [30, 59], [60, 90]]
freq_band_names = ['delta', 'theta', 'alpha', 'beta', 'gamma1', 'gamma2']

is_epoched = False

fmin = 0.1
fmax = 150
sfreq = 600
power_method = 'welch'  # for sensor PSD
n_fft = 2048  # the FFT size (n_fft). Ideally a power of 2

if is_epoched:
    overlap = 0
else:
    overlap = 0.5

power_analysis_name = 'power_pipeline'
src_power_analysis_name = 'src_power_pipeline'
