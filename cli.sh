#!/bin/bash

# cloning the `ljspeech` voice
tts --model_name  tts_models/multilingual/multi-dataset/bark \
--text "This is an example." \
--out_path "cli_output.wav" \
--voice_dir bark_voices/ \
--speaker_idx "speaker" \
--progress_bar True

# Random voice generation
tts --model_name  tts_models/multilingual/multi-dataset/bark \
--text "This is an example." \
--out_path "cli_rand_output.wav" \
--progress_bar True