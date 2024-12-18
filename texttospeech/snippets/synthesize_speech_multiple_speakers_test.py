#!/usr/bin/env python
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os

import synthesize_speech_multiple_speakers


def synthesize_speech_multiple_speakers_text(capsys):
    synthesize_speech_multiple_speakers.synthesize_speech_multiple_speakers()
    out, err = capsys.readouterr()

    assert "Audio content written to file" in out
    statinfo = os.stat("output.mp3")
    assert statinfo.st_size > 0
