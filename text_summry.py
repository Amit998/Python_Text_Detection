import spacy
from  spacy.lang.en.stop_words import  STOP_WORDS

from heapq import nlargest

class Text_Summarization:
    stopWords=list(STOP_WORDS)
    nlp=spacy.load('en_core_web_sm')
    def __init__(self,doc,size=0.3):


        self.doc=self.nlp(doc)
        self.size=size

    def get_punctuation(self):
        from string import punctuation
        punctuation=list(punctuation)
        punctuation.append('\n')

        return punctuation

    
    def tokenize(self):
        
        docs=self.doc
        tokens=[ token.text for token in docs ]


        punctuation=self.get_punctuation()
        tokens=[ token for token in tokens if token not in punctuation ]

        return tokens

    def word_frequencey_couter(self):
        punctuation=self.get_punctuation()
        word_frequency={}
        for word in self.doc:
            if word.text.lower() not in self.stopWords:
                if (word.text.lower() not in punctuation ):
                    if word.text not in word_frequency.keys():
                        word_frequency[word.text] = 1
                    else:
                        word_frequency[word.text] +=1
        
        max_frequency=max(word_frequency.values())    

        for word in word_frequency.keys():
            word_frequency[word]=word_frequency[word]/max_frequency
        
        return word_frequency,max_frequency
    

    def sentence_tokenize(self):
        sentence_tokens=[sent for sent in self.doc.sents]
        return sentence_tokens
    
    def sentence_tokenize_score(self):
        word_frequency,_=self.word_frequencey_couter()
        sentence_tokens=self.sentence_tokenize()
    
        sentence_score={}
        
        for sent in sentence_tokens:
            for word in sent:
                if (word.text.lower() in word_frequency.keys()):
                    if(sent not in sentence_score.keys()):
                        sentence_score[sent]=word_frequency[word.text.lower()]
                    else:
                        sentence_score[sent] +=word_frequency[word.text.lower()]
        return sentence_score
    
    def summarize_text(self):
        sentence_score= self.sentence_tokenize_score()
        sentence_tokens=self.sentence_tokenize()
        select_length=int(len(sentence_tokens) * self.size)
        # print(self.size)
        get_summary=nlargest(select_length,sentence_score,key=sentence_score.get)
        # print(get_summary)

        final_summary=[word.text for word in get_summary]
        summary=' '.join(final_summary)

        return summary

        
    def print_text(self):
        i=self.summarize_text()
        print(i)



text="""
On September 3, 2019, Abdul Samad Amiri, the acting head of the Afghanistan Independent Human Rights Commission’s office in his home province of Ghor, posted a reflective message on Facebook. He was just shy of thirty. He had grown up amid “the trauma of more than 40 years’ civil war and feel wholeheartedly the affliction imposed on my people,” he wrote. Yet he was optimistic. “I can’t ignore or forget the dreams for Afghanistan’s future and her place as a part of this world. . . . Despite the difficulties, I owe my life to this land and will work for its betterment so long as I live.”

Later that day, while Amiri was travelling by car from Kabul to Ghor, Taliban militants kidnapped and then, two days later, murdered him—one more death among hundreds of assassinations targeting rights advocates, journalists, civil servants, and other unarmed, younger Afghans who had seized the opportunities created by the American-led invasion of their country, in 2001. Nine months after Amiri’s murder, Fatima Khalil, a commission employee who was twenty-four, and a driver, Ahmad Jawid Folad, forty-one, were killed when unknown assailants placed a bomb on the road, targeting their vehicle; the explosive detonated as they drove through Kabul.

“The loss of my colleagues really broke me in ways that I had never thought about before,” Shaharzad Akbar, the chairwoman of the commission, told me recently. Akbar, who is thirty-four, was appointed to her position about two years ago. “Dealing with the anxiety of all this, for all of us in the leadership team—we feel responsible, but there is very little we can do to keep people safe,” she said. Colleagues sleep in the office for weeks on end, and it is an all but full-time job to sift through and evaluate the threats.

As the Biden Administration withdraws the last American troops from Afghanistan, the Independent Human Rights Commission is one of the many civil institutions now left to confront a new era of insecurity and uncertainty. The commission was created by a provision of the Bonn Agreement of December, 2001, when, immediately following the Taliban’s overthrow, the United States, European allies, Iran, and Pakistan met with anti-Taliban Afghan leaders, exiles, and regional strongmen to work out an accord for an interim government. The Bonn conference selected Hamid Karzai to lead the new government; the creation of the commission was also a provision of the accord. Since the Taliban have mounted a comeback, starting in 2006, the commission has been a regular target of threats and violence.

Akbar is one of the Bonn generation of Afghans who did not join the war that spread as the Taliban seized control of rural areas and sent death squads into cities, but who sought to build a revived society, at once traditional and modernizing—a society that nato aspired to enable through security and investment. She forged a career that would have been unimaginable during the years of Taliban rule. Her father, a leftist journalist, had edited several publications before leaving with his family for Pakistan, in 1999, to escape the civil war and the rising influence of the Taliban. He introduced his daughter to “prominent women and their lives, through books,” she said. It was “very important to him that I was aware of feminism.”

The family returned to Afghanistan in February, 2002. Akbar, who had honed her study of English in Pakistan, enrolled at Kabul University, and then was accepted as a transfer student to Smith College, where she studied anthropology and graduated cum laude. Later, she earned a master’s degree in international development at the University of Oxford.

She returned to Kabul during the first term of the Obama Administration, a time when the U.S. was investing heavily in its state-building ambitions, pouring hundreds of millions of dollars annually into agriculture, drug eradication, education, and other sectors. But Akbar and her friends—who were, she said, “very young and idealistic”—became disillusioned with the way that some of the groups involved were using the money. “I could see that a lot of these organizations were very detached from local realities,” she said. “I felt that Afghans should have a greater say.”

She was the kind of well-educated, next-generation Afghan that President Ashraf Ghani sought to lure into government after he was elected, in 2014. Akbar served on his National Security Council, working on the peace process, an initially fitful and fractured effort to develop talks between Taliban leaders and Afghans associated with the Kabul government. From the start, negotiators aligned with Kabul were divided over how far to go to accommodate the Taliban’s extremist views, particularly about the role of women. In 2019, Akbar participated in discussions with the Taliban in Doha, Qatar, concerning victims’ rights, human rights, women’s rights, and freedom of expression. “They had some prepared statements, and they didn’t want to go deeper,” she recalled. The international community “did the same,” offering gestural statements about protecting rights that elided hard questions about what accommodating the Taliban would require.

"""
summ=Text_Summarization(text,size=0.3)
summ.print_text()