# GitDuck Videos Downloader

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

First install `requests` with pip3 or via the requirements file:

- pip3 install requests
- pip3 install -r requirements.txt

Open the developer tools in your browser and get an `indexX.ts` url from Google Cloud Storage like this one:

- https://storage.googleapis.com/gitduck-live/app/4e41c9a00bc4e89bfb94b2b1679b2ec14a7470f215f7b0a1ff6cdf2bc5278c53/1576177423635-e6606a0a-ac69-4bc7-a916-2a1a40cd0fc7/index6.ts

Edit the `BASE_URL` and `OUTPUT_DIR` in download.py

Run the script

## Merge Files

You can use tools like Adobe Media Encoder or FFMPEG to merge the files from .ts -> .mp4

# Licence

The MIT License

Copyright (c) 2019 JUST1B

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
