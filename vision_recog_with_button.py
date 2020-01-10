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

import logging
import subprocess

from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient

from visionRecog import VisionRecog
from words import words_dict

def main():
    logging.basicConfig(level=logging.DEBUG)

    # if you use the English version
    vision_recog = VisionRecog()

    # if you use the Spanish version
    #vision_recog = VisionRecog('es','es-ES')

    # if you use the Japanese version
    #vision_recog = VisionRecog('ja','ja-JP')

    work = True

    with Board() as board:
        while work:
            board.led.state = Led.PULSE_SLOW
            lang = vision_recog.lang

            vision_recog.show_say('talk_start_button', True)
            hints = vision_recog.get_hints()
            hints_str = "\n".join(hints)
            vision_recog.show_say('command_list')
            logging.info(hints_str)

            vision_recog.show_say('waiting_button')

            client_cloudSpeech = CloudSpeechClient()
            board.button.wait_for_press()

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

