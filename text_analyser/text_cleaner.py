from string import punctuation
import re

class Cleaner:
    def __init__(self, text: str):
        self.text = text

    def __clean_punctuation(self):
        # for sign in punctuation:
        #     self.text = self.text.replace(sign, " ")
        self.text = re.sub(f"[{punctuation}]", " ", self.text)
        

    def __clean_crlf(self):
        self.text = " ".join(self.text.splitlines())

    def __clean_spaces(self):
        self.text = re.sub(" +", " ", self.text)

    def __little_words(self, min_len: int):
        self.text = " ".join(
            filter(lambda w: len(w) > min_len, 
            self.text.split()
        ))
        # words = []
        # for word in self.text.split():
        #     if len(word) > 3:
        #         words.append(word)
        # self.text = " ".join(words)

    def clean(self, min_len: int=3) -> str:
        self.__clean_punctuation()
        self.__clean_crlf()
        self.__clean_spaces()
        self.__little_words(min_len)

        return self.text.lower()