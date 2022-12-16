import numpy as np
import librosa
# import librosa.display

class Tonal_Fragment:
    def __init__(self, waveform, sr, tstart, tend):
        self.waveform = waveform
        self.sr = sr
        self.tstart = tstart
        self.tend = tend

        self.tstart = librosa.time_to_samples(self.tstart, sr=self.sr)
        self.tend = librosa.time_to_samples(self.tend, sr=self.sr)
        self.y_segment = self.waveform[self.tstart:self.tend]
        self.chromograph = librosa.feature.chroma_cqt(y=self.y_segment, sr=self.sr, bins_per_octave=24)

        self.chroma_vals = []
        for i in range(12):
            self.chroma_vals.append(np.sum(self.chromograph[i]))
        pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.keyfreqs = {pitches[i]: self.chroma_vals[i] for i in range(12)}

        keys = [pitches[i] + ' maj' for i in range(12)] + [pitches[i] + ' min' for i in range(12)]

        maj_profile = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
        min_profile = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]

        self.min_key_corrs = []
        self.maj_key_corrs = []
        for i in range(12):
            key_test = [self.keyfreqs.get(pitches[(i + m) % 12]) for m in range(12)]
            self.maj_key_corrs.append(round(np.corrcoef(maj_profile, key_test)[1, 0], 3))
            self.min_key_corrs.append(round(np.corrcoef(min_profile, key_test)[1, 0], 3))

        self.key_dict = {**{keys[i]: self.maj_key_corrs[i] for i in range(12)},
                         **{keys[i+12]: self.min_key_corrs[i] for i in range(12)}}

        self.key = max(self.key_dict, key=self.key_dict.get)
        self.bestcorr = max(self.key_dict.values())

        self.altkey = None
        self.altbestcorr = None

        for key, corr in self.key_dict.items():
            if corr > self.bestcorr * 0.9 and corr != self.bestcorr:
                self.altkey = key
                self.altbestcorr = corr

    def get_key(self) -> int | tuple:
        main_key = max(self.key_dict, key=self.key_dict.get)
        return main_key if self.altkey is None else (main_key, self.altkey)

