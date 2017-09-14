# coding: utf-8
# author: Zhengpeng Xiang
# date: 2017/09/13
# function: 对zhwiki.simple.text进行分词处理

from pyltp import Segmentor
import logging
import os.path
import sys


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) != 4:
        print("Using: python segment.py zhwiki.simple.text zhwiki.simple.tokenized.text segmentor.model")
        sys.exit(1)

    i_fname, o_fname, s_model = sys.argv[1:4]
    count = 0

    segmentor = Segmentor()  # 初始化实例
    # '../../download/cws.model'
    segmentor.load(s_model)  # 加载模型

    # '../../word2vec/wiki/zhwiki.simple.tokenized.text'
    with open(o_fname, 'w') as output:
        # '../../word2vec/wiki/zhwiki.simple.text'
        for line in open(i_fname, 'r'):
            output.write(' '.join(list(segmentor.segment(line))) + "\n")
            count = count + 1
            if count % 10000 == 0:
                logger.info("Segmented " + str(count) + " articles")

    logger.info("Finished segmented " + str(count) + " articles")
