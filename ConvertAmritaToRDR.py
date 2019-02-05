#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

input_text = """
அவர் <PRP>
இந்த <DET>
ஜாதியில் <NN>
இருந்துதான் <VNAV>
வரமுடியும் <VAX>
, <COMM>
இந்த <DET>
மதத்தில் <NN>
இருந்துதான் <VNAV>
வரவேண்டும் <VF>
என்பது <COM>
இல்லை <VAX>
. <DOT>
ஆக <CNJ>
, <COMM>
மஞ்சள் <NN>
நீராட்டு <NNC>
என்பது <COM>
இன்று <ADV>
நேற்று <ADV>
ஏற்பட்டதல்ல <VF>
, <COMM>
2700 <CRD>
ஆண்டுகளாய் <ADV>
இந்தப் <DET>
பழக்கம் <NN>
இருந்திருக்கிறது <VF>
. <DOT>
“அறிவுக்கலை <NNP>
ஒரு <DET>
புத்தாக்கப் <NNC>
பயணம்” <NNC>
என்ற <COM>
நிரந்தர/NN
கண்காட்சியும் <NN>
அங்கு <ADV>
இடம்பெறவிருக்கிறது <VF>
. <DOT>
“அறிவுக்கலை <NNP>
ஒரு <DET>
புத்தாக்கப் <NNC>
பயணம்” <NNC>
என்ற <COM>
நிரந்தர/NN
கண்காட்சியும் <NN>
அங்கு <ADV>
இடம்பெறவிருக்கிறது <VF>
. <DOT>
1985 <CRD>
ஆண்டு <NN>
முதல் <PPO>
‘‘அறிவியல் <NN>
மக்களுக்கே’’ <NN>
அறிவியல் <NN>
. <DOT>
 /NNP
 /NNC
 /NN
 /VF
 /VINT
 //NNP
 //NNC
 //NN
 //VF
 //VINT
 /சிதைப்புகள்/NN
//NNP
//NNC
//NN
அதிர்வடைதல் அசைதல்
"""
def _convert_amrita_to_rdr(string):
    """Convert Amrita POS Tagger output format to the RDRPOSTagger training format"""
    # Replace all <QM> with <DOT>
    string = re.sub(r'<QM>', '<DOT>', string)
    # Replace all "\n" with " "
    string = re.sub(r'\n', '', string)
    # Replace all <DOT> with /.\n
    string = re.sub(r' <DOT>', '/.\n', string)
    # Replace all <COMM> with /,
    string = re.sub(r' <COMM>', '/, ', string)
    # Replace all " <" to "/"
    string = re.sub(r' <', '/', string)
    # Remove all ">" to " "
    string = re.sub(r'>', ' ', string)
    # Remove all single and double quotes
    string = re.sub(r'“', '', string)
    string = re.sub(r'”', '', string)
    string = re.sub(r'‘', '', string)
    string = re.sub(r'’', '', string)

    string = re.sub(r' /NNP', '', string)
    string = re.sub(r' /NNC', '', string)
    string = re.sub(r' /NN', '', string)
    string = re.sub(r' /VF', '', string)
    string = re.sub(r' /VINT', '', string)

    string = re.sub(r' //NNP', '', string)
    string = re.sub(r' //NNC', '', string)
    string = re.sub(r' //NN', '', string)
    string = re.sub(r' //VF', '', string)
    string = re.sub(r' //VINT', '', string)
    string = re.sub(r'//NNP', '', string)
    string = re.sub(r'//NNC', '', string)
    string = re.sub(r'//NN', '', string)

    string = re.sub(r' /', ' ', string)
    string = re.sub(r'(?<=[\u0B80-\u0BFF] [\u0B80-\u0BFF]{0})', '???', string)

    return string
'''
converted_text = _convert_amrita_to_rdr(input_text)
print(converted_text)
'''
f = open('Balanced_corpus_train.txt', 'r', encoding='utf-8')
old_text = f.read()
new_text = _convert_amrita_to_rdr(old_text)
fw = open('Balanced_corpus_rdr_train.txt', 'wt', encoding='utf-8')
fw.write(new_text)

