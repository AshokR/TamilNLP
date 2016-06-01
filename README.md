## தமிழ் சொல்வகை குறியீடு (POS tag) 
செய்யத் தேவையான நிரல்கள், கருவிகள் மற்றும் படைப்புகள் இங்கே உள்ளன

RDRPOSTagger என்ற கட்டற்ற சொல்வகை குறியீடு (POS tagger) செய்யும் மென்பொருளை பயன்படுத்தி நீங்கள் உங்கள் தமிழ் உரையை குறியீடு செய்யலாம்.

இந்த கருவி 30 சொல்வகைகள் கொண்ட அமிர்தா குறிச்சொல் தொகுப்பு (Amrita Tagset) படி குறியீடு செய்ய தயார் செய்யப்பட்டுள்ளது. அமிர்தா குறிச்சொல் தொகுப்பு Resource folder-ல் காண்க.

##### RDRPOSTagger பயன்படுத்தி சொல்வகை குறியீடு செய்வது எப்படி?

1. [RDRPOSTagger](http://rdrpostagger.sourceforge.net/) என்ற கட்டற்ற சொல்வகை குறியீடு (POS tagger) செய்யும் மென்பொருளை பயன்படுத்தி நீங்கள் உங்கள் தமிழ் உரையை குறியீடு செய்யலாம்.
2. இந்த தளத்தில் இருந்து குறியீடு செய்யும் விதிகள் கோப்பு (.RDR) மற்றும் அகராதி கோப்பு (.DICT) பதிவிறக்கம் செய்தல்.
3. கட்டளை வரியில் (command line) குறியீடு செய்தல்: Your tobetagged.txt file should be in the same format as the rawtest file in the data directory. Change directory to where you have installed RDRPOSTagger.py and then run this command: `python RDRPOSTagger.py tag /path/TrainedModel.RDR /path/GeneratedLexicon.DICT /path/tobetagged.txt` It will create a new file named tobetagged.txt.TAGGED in the same folder.
4. பைதான் நிரல் மூலம் குறியீடு செய்தல்: Use the POSTagRDR.py file provided to do the tagging programmatically.

##### குறிப்புகள்:

1. RDRPOSTagger பைதான் 2.7-ல் எழுதப்பட்டது. ஆகவே பைதான் 3-ல் வேலை செய்யாது.
2. இந்த ஆவணங்கள் அனைத்தும் லினக்ஸ் (உபுண்டு 14.04) அடிப்படையானவை. 
3. நீங்கள் விண்டோஸ் பயன்படுத்துகிறீர்கள் எனில், அதை அமைப்பது எப்படி என்று ஒரு சில வரிகளை எழுதினால் மற்ற விண்டோஸ் பயனர்களுக்கு மிகவும் உதவியாக இருக்கும்.

**Acknowledgement**: Many thanks to Dat Quoc Nguyen and his team at the Department of Computing, Macquarie University, Sydney, Australia for providing RDRPOSTagger software as open source. And particularly for his super fast help with resolving the issues that I ran into while trying to train this tool for Tamil tagging.

