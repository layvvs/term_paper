import librosa
import numpy as np

class Processor:
    def bpm_finder(self) -> str:
        tempo, _ = librosa.beat.beat_track(y=self.y, sr=self.sr)
        return str(int(tempo))

    def key_finder(self) -> int | tuple:
        pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        maj_profile = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
        min_profile = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]

        waveform, _ = librosa.effects.hpss(self.y)
        tstart = librosa.time_to_samples(0, sr=self.sr)
        tend = librosa.time_to_samples(30, sr=self.sr)
        y_segment = waveform[tstart:tend]
        chromograph = librosa.feature.chroma_cqt(y=y_segment, sr=self.sr, bins_per_octave=24)

        chroma_vals = []
        for i in range(12):
            chroma_vals.append(np.sum(chromograph[i]))

        keyfreqs = {pitches[i]: chroma_vals[i] for i in range(12)}
        keys = [pitches[i] + ' maj' for i in range(12)] + [pitches[i] + ' min' for i in range(12)]

        min_key_corrs = []
        maj_key_corrs = []
        for i in range(12):
            key_test = [keyfreqs.get(pitches[(i + m) % 12]) for m in range(12)]
            maj_key_corrs.append(round(np.corrcoef(maj_profile, key_test)[1, 0], 3))
            min_key_corrs.append(round(np.corrcoef(min_profile, key_test)[1, 0], 3))

        key_dict = {**{keys[i]: maj_key_corrs[i] for i in range(12)},
                         **{keys[i+12]: min_key_corrs[i] for i in range(12)}}

        key = max(key_dict, key=key_dict.get)
        bestcorr = max(key_dict.values())

        altkey = None
        altbestcorr = None

        for key, corr in key_dict.items():
            if corr > bestcorr * 0.9 and corr != bestcorr:
                altkey = key
                altbestcorr = corr

        main_key = max(key_dict, key=key_dict.get)
        return main_key if altkey is None else (main_key, altkey)

    def audio_valid(self, path: str) -> bool:
        self.path = path
        return True if librosa.get_duration(filename=path) > 30 else False

    def load_audio(self):
        self.y, self.sr = librosa.load(self.path)


