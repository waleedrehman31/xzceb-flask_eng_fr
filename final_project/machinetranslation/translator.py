import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['API_KEY']
URL = os.environ['URL']

authenticator = IAMAuthenticator(API_KEY)

languageTranslator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

languageTranslator.set_service_url(URL)


def english_to_french(english_text):
    # write the code here
    french_text = languageTranslator.translate(
        text=english_text,
        model_id="en-fr"
    ).get_result().get("translations")[0].get("translation")
    return french_text


print(english_to_french("Hello"))


def french_to_english(french_text):
    # write the code here
    english_text = languageTranslator.translate(
        text=french_text,
        model_id="fr-en"
    ).get_result().get("translations")[0].get("translation")
    return english_text


print(french_to_english("Bonjour"))
