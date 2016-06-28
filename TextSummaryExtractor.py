#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import re

# This is a naive text summarization algorithm
# Created by Shlomi Babluki
# April, 2013
# http://thetokenizer.com/2013/04/28/build-your-own-summary-tool/
# https://gist.github.com/shlomibabluki/5473521

class SummaryTool(object):

    # Naive method for splitting a text into sentences
    def split_content_to_sentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")

    # Naive method for splitting a text into paragraphs
    def split_content_to_paragraphs(self, content):
        return content.split("\n\n")

    # Caculate the intersection between 2 sentences
    def sentences_intersection(self, sent1, sent2):

        # split the sentence into words/tokens
        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))

        # If there is not intersection, just return 0
        # if (len(s1) + len(s2)) == 0:
        if len(s1.intersection(s2)) == 0:
            return 0

        # We normalize the result by the average number of words
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)

    # Format a sentence - remove all non-alphbetic chars from the sentence
    # We'll use the formatted sentence as a key in our sentences dictionary
    def format_sentence(self, sentence):
        # sentence = re.sub(r'\W+', '', sentence)       # [\u0B80-\u0BFF]
        sentence = re.sub(r'[\u0B80-\u0BFF]', '', sentence)
        # print sentence
        return sentence

    # Convert the content into a dictionary <K, V>
    # k = The formatted sentence
    # V = The rank of the sentence
    def get_sentences_ranks(self, content):

        # Split the content into sentences
        sentences = self.split_content_to_sentences(content)

        # Calculate the intersection of every two sentences
        n = len(sentences)
        values = [[0 for x in xrange(n)] for x in xrange(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])

        # Build the sentences dictionary
        # The score of a sentences is the sum of all its intersection
        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.format_sentence(sentences[i])] = score
        return sentences_dic

    # Return the best sentence in a paragraph
    def get_best_sentence(self, paragraph, sentences_dic):

        # Split the paragraph into sentences
        sentences = self.split_content_to_sentences(paragraph)

        # Ignore short paragraphs
        if len(sentences) < 2:
            return ""

        # Get the best sentence according to the sentences dictionary
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s

        return best_sentence

    # Build the summary
    def get_summary(self, title, content, sentences_dic):

        # Split the content into paragraphs
        paragraphs = self.split_content_to_paragraphs(content)

        # Add the title
        summary = []
        summary.append(title.strip())
        summary.append("")

        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)

        return ("\n").join(summary)


# Main method, just run "python summary_tool.py"
def main():


    title = """
குத்துச்சண்டை ஜாம்பவான் முகமது அலி மறைவு
    """

    content = """
அமெரிக்காவின் முன்னாள் ஹெவி வெயிட் குத்துச்சண்டை வீரர் முகமது அலி காலமானார். அவருக்கு வயது 74. சுவாசக்கோளாறு காரணமாக முகமது அலி மரணமடைந்ததாக அவரது குடும் பத்தினர் வெளியிட்டுள்ள அறிக்கையில் கூறியுள்ளனர்.
உலக குத்துச்சண்டை சாம்பியன் பட்டத்தை 3 முறை வென்று சாதனை படைத்தவர் முகமது அலி. அமெரிக்காவின் கென்டகி மாநிலத்தில் 1942-ம் ஆண்டு பிறந்த முகமது அலியின் இயற்பெயர் காசியஸ் க்ளே. தனது 18 வயதில் குத்துசண்டை களத்தில் இறங்கிய முகமது அலி 1960-ல் ஹெவிவெயிட் ஒலிம்பிக் தங்கப் பதக்கத்தை பெற்றார். இதைத்தொடர்ந்து குத்துச்சண்டை என்றாலே முகமது அலி என்று சொல்லும் அளவுக்கு புகழ்பெற்றார். குத்துச்சண்டை களத்தில் மட்டுமின்றி அமெரிக்காவில் அக்காலத்தில் தீவிரமாக பரவியிருந்த இனவெறிக்கு எதிராகவும் அவர் போராடினார். அவர் குவிக்கும் வெற்றிகள் கறுப்பின மக்களிடையே புதிய எழுச்சியை ஏற்படுத்தின.
1960-ல் இருந்து 1981 வரை முகமது அலி குத்துச்சண்டை உலகின் முடிசூடா மன்னனாக இருந்தார். 61 தொழில்முறை குத்துச்சண்டை போட்டிகளில் 56-ல் வெற்றி பெற்று அனைவரையும் ஆச்சரியத்தில் ஆழ்த்தினார். இதில் 37 போட்டிகளில் நாக் அவுட் முறையில் வென்றதால் ‘நாக் அவுட் நாயகன்’ என்று அழைக்கப்பட்டார். 3 முறை உலக குத்துச்சண்டை சாம்பியன் பட்டத்தை வென்றார்.
ஒரு தேனீயைப் போல களத்தில் வேகமாக செயலாற்றி கண்ணிமைக்கும் நேரத்தில் சரமாரியான குத்துகளை விட்டு எதிரிகளை நிலைகுலையச் செய்வது அவரது பாணியாக இருந்தது. இதனாலேயே தனது நாடான அமெரிக்காவில் மட்டுமின்றி உலகம் முழுவதும் அவர் புகழ்பெற்றார்.
குத்துச்சண்டை களத்தில் இருந்து ஓய்வுபெற்ற அவரை 1980-களின் தொடக்கத்தில் பார்கின்சன் நோய் தாக்கியது. பார்கின்சன் என்பது மத்திய நரம்பு மண்டலத்தில் பாதிப்பை ஏற்படுத்தி அதன்மூலம் மனிதனின் இயக்கத்தை முடக்கக்கூடிய ஒருவிதமான வாத நோயாகும். குத்துச்சண்டை போட்டி களுக்காக கடுமையான பயிற்சிகளை மேற்கொண்டதால் அவரை இந்த நோய் தாக்கியதாக கூறப்படுகிறது.
30 ஆண்டுகளுக்கும் மேலாக பார்கின்சன் நோயுடன் போராடி வந்த அவர் கடந்த ஆண்டு மூச்சுத்திணறல் மற்றும் சிறுநீரகத் தொற்று உள்ளிட்ட உபாதைகளால் பாதிக்கப்பட்டார். இந்நிலையில் சுவாசப் பிரச்சினை காரணமாக பீனிக்ஸில் உள்ள மருத்துவமனையில் அனுமதிக்கப்பட்டார்.
முகமது அலி அனுமதிக்கப்பட்டதைத் தொடர்ந்து அவரது ரசிகர்கள் மருத்துவ மனையைச் சூழ்ந்தனர். அவர் நலம் பெற்று வர வேண்டும் என்பதற்காக பிரார்த் தனைகளிலும் ஈடுபட்டனர்.
இந்நிலையில் நேற்று முன் தினம் இரவு அவர் மருத்துவ மனையில் காலமானார். இது குறித்து அவரது குடும்பத்தினர் வெளியிட்டுள்ள அறிக்கையில் சுவாசப் பிரச்சினை காரணமாக அவர் மரணமடைந்ததாக கூறப்பட்டுள்ளது.
முகமது அலிக்கு 9 குழந் தைகள். அவரது மகள் லைலா அலி குத்துச்சண்டையில் உலக சாம்பியன் பட்டத்தை வென்றவர். முகமது அலியின் உடல் அடக்கம் சொந்த நகரான லூயிவிலியில் நடைபெற உள்ளது. அவரது மறைவுக்கு பிரதமர் மோடி இரங்கல் தெரிவித்துள்ளார்.
    """

    # Create a SummaryTool object
    st = SummaryTool()

    # Build the sentences dictionary
    sentences_dic = st.get_sentences_ranks(content)

    # Build the summary with the sentences dictionary
    summary = st.get_summary(title, content, sentences_dic)

    # Print the summary
    print summary

    # Print the ratio between the summary length and the original length
    print ""
    print "Original Length %s" % (len(title) + len(content))
    print "Summary Length %s" % len(summary)
    print "Summary Ratio: %s" % (100 - (100 * (len(summary) / (len(title) + len(content)))))


if __name__ == '__main__':
    main()