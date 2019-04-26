import os
from multiprocessing.dummy import Pool
import time


def all_files(filename):
    print(filename)
    time.sleep(10)


def process_files(files_directory):
    """
    process all the file chunks parallelly in pools of threads with each pool size of 8 and
    collect all the text outputs and make a list.
    :param files_directory:
    :return: output text that converted form audiofile
    """
    files = os.listdir(files_directory)
    files = [os.path.join(files_directory, file) for file in files]
    pool = Pool(10)
    all_text = pool.map(all_files, enumerate(files))
    pool.close()
    pool.join()
    transcript = []
    for t in sorted(all_text, key=lambda x: x['idx']):
        transcript.append(t['text'])
    return transcript


if __name__ == '__main__':
    files_directory = r'E:/Downloads/'
    process_files(files_directory)
