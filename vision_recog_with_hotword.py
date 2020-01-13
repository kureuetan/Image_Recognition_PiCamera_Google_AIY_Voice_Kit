#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import argparse
import logging
import signal
import sys
import subprocess

from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient

import mod.snowboydecoder as snowboydecoder
from visionRecog import VisionRecog
from words import words_dict

def volume(string):
    value = int(string)
    if value < 0 or value > 100:
        raise argparse.ArgumentTypeError('Volume must be in [0...100] range.')
    return value

def sensitivity(string):
    value = float(string)
    if value <= 0 or value > 1:
        raise argparse.ArgumentTypeError('Sensitivity must be float between 0 and 1.')
    return value

def main():
    logging.basicConfig(level=logging.DEBUG)
    signal.signal(signal.SIGTERM, lambda signum, frame: sys.exit(0))

    # if you use the English version
    # vision_recog = VisionRecog()

    # if you use the Spanish version
    # vision_recog = VisionRecog('es','es-ES')

    # if you use the Japanese version
    vision_recog = VisionRecog('ja','ja-JP')

    work = True

    with Board() as board:
        while work:
            board.led.state = Led.PULSE_SLOW
            lang = vision_recog.lang
            lang_code = vision_recog.lang_code
            client_cloudSpeech = CloudSpeechClient()

            parser = argparse.ArgumentParser(description='Assistant service example.')
            parser.add_argument('--language', default=lang_code)
            parser.add_argument('--volume', type=volume, default=100)
            parser.add_argument('--model',
                                default='Shin chan.pmdl')
            parser.add_argument('--sensitivity', type=sensitivity, default=0.5)
            args = parser.parse_args()
            detector = snowboydecoder.HotwordDetector(args.model,
                                                    sensitivity=args.sensitivity)

            vision_recog.show_say('talk_start_hotword', True)
            hints = vision_recog.get_hints()
            hints_str = "\n".join(hints)
            vision_recog.show_say('command_list')
            logging.info(hints_str)

            vision_recog.show_say('waiting_hotword')
            detector.start()

            # If you use the sound of button pushed
            subprocess.run(['aplay', './button_sound.wav'])
            vision_recog.show_say('waiting_command')

            text = client_cloudSpeech.recognize(language_code=lang, hint_phrases=hints)
            if text is None:
                vision_recog.show_say('talk_sorry', True)
            else:
                results = None
                text = text.lower()
                vision_recog.show_say('your_command')
                logging.info(text)
                if text in hints:
                    if text in words_dict[lang]['finish_list']:
                        vision_recog.show_say('talk_finish', True)
                        work = False
                    else:
                        results= vision_recog.recognition_process(text)
                        vision_recog.say(results)
                else:
                    vision_recog.show_say('talk_again', True)

if __name__ == "__main__":
    main()
