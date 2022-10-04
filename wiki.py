import wikipedia
from PyDictionary import PyDictionary
import joblib
# import os
# from tensorflow.keras.models import Sequential, load_model

# class SmallTalkPredictor:
#     def __init__(self, model_dir):
#         self.tokenizer = joblib.load(os.path.join(model_dir,"tokenizer.joblib"))
#         self.label_encoder = joblib.load(os.path.join(model_dir,"label_encoder.joblib"))
#         self.model_params = joblib.load(os.path.join(model_dir,"model_params.joblib"))
#         self.model = load_model(os.path.join(model_dir,"model.h5"))
#         self.intents = json.load(open('intents.json','r'))
#     def preprocess(self, text):
#         text = [text]
#         text = self.tokenizer.texts_to_sequences(text)
#         text = pad_sequences(text,truncating = 'post', maxlen = self.model_params['max_len'])
#         return text
#     def predict(self,text):
#         text = self.preprocess(text)
#         probabilities = self.model.predict(text)
#         intent_id = np.argmax(probabilities)
#         intent_name = self.label_encoder.inverse_transform([intent_id.view()])
#         intent = self.intents[intent_name[0]]
#         return {"response":np.random.choice(intent['responses']), "confidence":np.max(probabilities)}

# predictor = SmallTalkPredictor("model_data")



class Solution:
    def __init__(self):
        self.dictionary=PyDictionary()


    def getAnswer(self, question):
        return wikipedia.summary(question, sentences = 2)

    def getDefinition(self, question):
        return self.dictionary.meaning(question)


if __name__ == "__main__":
    obj = Solution()
    while True:
        question = input(f'Question: ')
        # print(f'question.isspace(): {question.isspace()}')
        # if (' ' in question == False):
        #     print(f'Answer from PyDictionary: {obj.getDefinition(question)}')
        # else:
        #     print(f'Answer from Wikipedia: {obj.getAnswer(question)}')

        print(f'Answer from PyDictionary: {obj.getDefinition(question)}')
        print(f'Answer from Wikipedia: {obj.getAnswer(question)}')
        # predictor.predict("What does 'noble cause' corruption mean?")