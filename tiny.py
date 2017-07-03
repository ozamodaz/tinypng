#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tinify
import os, sys
from datetime import datetime

tinify.key = 'YOUR API KEY'

in_path = os.path.dirname(__file__)
out_path = os.path.join(in_path, 'compressed')
log_file = os.path.join(in_path, 'error.log')
counter = 0

def log(log_msg):
    timestamp = datetime.now().strftime('%d.%m.%Y %H:%M')
    string = '%s  %s \n' % (timestamp, log_msg)
    string = string
    with open(log_file, encoding='utf-8', mode='a') as f:
        f.write(string)

def get_queue():

    def image_files(path):
        allowed_formats = ['jpg', 'jpeg', 'png']
        for fname in os.listdir(path):
            if os.path.isfile(os.path.join(path, fname)):
                extension = fname.split('.')[-1].lower()
                if extension in allowed_formats:
                    yield fname

    if os.path.exists(out_path):
        done = set(fname for fname in image_files(out_path))
    else:
        os.makedirs(out_path)
        done = set()

    in_files = set(fname for fname in image_files(in_path))
    uncompressed = in_files - done
    return uncompressed


def compress(fname):
    """
    Опять сжимаешь, ебучий шакал
    """
    try:
        source = tinify.from_file(os.path.join(in_path, fname))
        resized = source.resize(
        method="scale",
        width=1000,
        )
        resized.to_file(os.path.join(out_path, fname))
        global counter
        counter += 1
        sys.stdout.write("Progress: %s of %s  \r" % (counter, total))
        sys.stdout.flush()
    except tinify.errors.ConnectionError as e:
        log('A network connection error occurred.')
        log('Error message: %s' % e)
        log('Retry...')
        compress(fname)
    except tinify.AccountError as e:
        log('Account Error. Verify your API key and account limit.')
        log('Compression count: %s' % tinify.compression_count)
        log('Error message: %s' % e)
        sys.exit(0)
    except Exception as e:
        log('Error message: %s' % e)
        sys.exit(0)


if __name__ == "__main__":
    uncompressed = get_queue()
    total = len(uncompressed)
    for fname in uncompressed:
        compress(fname)
