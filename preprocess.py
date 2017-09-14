# coding: utf-8
# author: Zhengpeng Xiang
# date: 2017/09/12
# from https://github.com/panyang/Wikipedia_Word2vec/blob/master/v1/process_wiki.py
# function: 将中文的维基百科页面从zhwiki-latest-pages-articles.xml.bz2提取到zhwiki.text中

from __future__ import print_function

import logging
import os.path
import sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) != 3:
        print("Using: python preprocess.py zhwiki-latest-pages-articles.xml.bz2 zhwiki.text")
        sys.exit(1)

    i_fname, o_fname = sys.argv[1:3]
    count = 0

    output = open(o_fname, 'w')
    wiki = WikiCorpus(i_fname, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        try:
            output.write(' '.join(text).encode('utf-8') + "\n")
        except UnicodeEncodeError:
            print(' '.join(text).encode('utf-8'))
            exit()
        count = count + 1
        if count % 10000 == 0:
            logger.info("Saved " + str(count) + " articles")

    output.close()
    logger.info("Finished Saved " + str(count) + " articles")
