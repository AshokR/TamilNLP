#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk.data
import re
from RDRPOSTagger import *

rdr = RDRPOSTagger()
# Load the POS tagging model for Tamil
trainedmodel = os.path.join(os.path.dirname(__file__), 'Resources/TrainedModel.RDR')
rdr.constructSCRDRtreeFromRDRfile(trainedmodel)

# Load the lexicon for Tamil
generatedlexicon = os.path.join(os.path.dirname(__file__), 'Resources/GeneratedLexicon.DICT')
DICT = readDictionary(generatedlexicon)

# Load the file that contains the text to be tagged
tobetagged = nltk.data.load('/home/ashok/TamilCorpora/Fiction/WikiSource.txt')

# Open the target file for writing the tagged text
targetfile = open('/home/ashok/Machlearn/Sentseg/test_sentences.txt', 'wt')

# Segment the text into sentences and then into tokens (words and punctuation)
sentencesegment = os.path.join(os.path.dirname(__file__), 'Resources/SentenceSegment_Python2.pickle')
tokenizer = nltk.data.load(sentencesegment)
seg = tokenizer.tokenize(tobetagged)

# Read sentences one-by-one
for sent in seg:
    # Strip all double quotes - POS tagger is unable to handle these
    sent = re.sub(r'"', '', sent)
    # Strip all single quotes - POS tagger is unable to handle these
    sent = re.sub(r'\'', '', sent)
    # Change all ! to dot - POS tagger is unable to handle !
    sent = re.sub(r'!', '.', sent)
    # Change all ; to , - POS tagger is unable to handle ;
    sent = re.sub(r';', ',', sent)
    # Change all : to , - POS tagger is unable to handle :
    sent = re.sub(r':', ',', sent)
    # Add a space in front of the sentence ending dot - tagging is done based on whitespace
    sent = re.sub(r'\.\Z', ' .', sent)
    # Add a space in front of the sentence ending ? - tagging is done based on whitespace
    sent = re.sub(r'\?', ' ?', sent)
    # Add a space in front of the paragraph ending dot - tagging is done based on whitespace
    sent = re.sub(r'\.\n', ' .', sent)
    # Add a space in front of every comma - tagging is done based on whitespace
    sent = re.sub(r',', ' ,', sent)

    # Tag the sentence and write it to the file
    tagged = rdr.tagRawSentence(DICT, sent.encode('utf8'))
    print tagged
    targetfile.write(tagged + '\n')

