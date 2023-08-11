text = "Hello, my name is Manmay , how are you?"

from TTS.tts.configs.bark_config import BarkConfig
from TTS.tts.models.bark import Bark
from scipy.io.wavfile import write as write_wavfile

config = BarkConfig()
model = Bark.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="/content/model/", eval=True)

model.to("cuda")

# with random speaker
# output_dict = model.synthesize(text, config, speaker_id="random", voice_dirs=None)

# cloning a speaker.
# It assumes that you have a speaker file in `bark_voices/speaker_n/speaker.wav` or `bark_voices/speaker_n/speaker.npz`
output_dict = model.synthesize(text, config, speaker_id="speaker", voice_dirs="bark_voices", temperature=0.95)

write_wavfile(filename="/content/output.wav", rate = 24000, data = output_dict['wave'])