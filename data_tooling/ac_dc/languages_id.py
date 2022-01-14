import pandas as pd


langs_id = [
    {
        "lang": "Afrikaans",
        "dataset_id": "af",
        "stopwords_id": "af",
        "badwords_id": None,
        "fasttext_id": "af",
        "sentencepiece_id": "af",
        "kenlm_id": "af",
    },
    {
        "lang": "Arabic",
        "dataset_id": "ar",
        "stopwords_id": "ar",
        "badwords_id": "ar",
        "fasttext_id": "ar",
        "sentencepiece_id": "ar",
        "kenlm_id": "ar",
    },
    {
        "lang": "Egyptian Arabic",
        "dataset_id": "arz",
        "stopwords_id": None,
        "badwords_id": None,
        "fasttext_id": "arz",
        "sentencepiece_id": None,
        "kenlm_id": None,
    },
    {
        "lang": "Assamese",
        "dataset_id": "as",
        "stopwords_id": None,
        "badwords_id": None,
        "fasttext_id": "as",
        "sentencepiece_id": None,
        "kenlm_id": None,
    },
    {
        "lang": "Bengali",
        "dataset_id": "bn",
        "stopwords_id": "bn",
        "badwords_id": None,
        "fasttext_id": "bn",
        "sentencepiece_id": "bn",
        "kenlm_id": "bn",
    },
    {
        "lang": "Catalan",
        "dataset_id": "ca",
        "stopwords_id": "ca",
        "badwords_id": "ca",
        "fasttext_id": "ca",
        "sentencepiece_id": "ca",
        "kenlm_id": "ca",
    },
    {
        "lang": "English",
        "dataset_id": "en",
        "stopwords_id": "en",
        "badwords_id": "en",
        "fasttext_id": "en",
        "sentencepiece_id": "en",
        "kenlm_id": "en",
    },
    {
        "lang": "Spanish",
        "dataset_id": "es",
        "stopwords_id": "es",
        "badwords_id": "es",
        "fasttext_id": "es",
        "sentencepiece_id": "es",
        "kenlm_id": "es",
    },
    {
        "lang": "Basque",
        "dataset_id": "eu",
        "stopwords_id": "eu",
        "badwords_id": "eu",
        "fasttext_id": "eu",
        "sentencepiece_id": None,
        "kenlm_id": None,
    },
    {
        "lang": "French",
        "dataset_id": "fr",
        "stopwords_id": "fr",
        "badwords_id": "fr",
        "fasttext_id": "fr",
        "sentencepiece_id": "fr",
        "kenlm_id": "fr",
    },
    {
        "lang": "Gujarati",
        "dataset_id": "gu",
        "stopwords_id": None,
        "badwords_id": None,
        "fasttext_id": "gu",
        "sentencepiece_id": "gu",
        "kenlm_id": "gu",
    },
    {
        "lang": "Hindi",
        "dataset_id": "hi",
        "stopwords_id": "hi",
        "badwords_id": "hi",
        "fasttext_id": "hi",
        "sentencepiece_id": "hi",
        "kenlm_id": "hi",
    },
    {
        "lang": "Indonesian",
        "dataset_id": "id",
        "stopwords_id": "id",
        "badwords_id": "id",
        "fasttext_id": "id",
        "sentencepiece_id": "id",
        "kenlm_id": "id",
    },
    {
        "lang": "Kannada",
        "dataset_id": "kn",
        "stopwords_id": None,
        "badwords_id": "kn",
        "fasttext_id": "kn",
        "sentencepiece_id": "kn",
        "kenlm_id": "kn",
    },
    {
        "lang": "Malayalam",
        "dataset_id": "ml",
        "stopwords_id": None,
        "badwords_id": "ml",
        "fasttext_id": "ml",
        "sentencepiece_id": "ml",
        "kenlm_id": "ml",
    },
    {
        "lang": "Marathi",
        "dataset_id": "mr",
        "stopwords_id": "mr",
        "badwords_id": "mr",
        "fasttext_id": "mr",
        "sentencepiece_id": "mr",
        "kenlm_id": "mr",
    },
    {
        "lang": "Portuguese",
        "dataset_id": "pt",
        "stopwords_id": "pt",
        "badwords_id": "pt",
        "fasttext_id": "pt",
        "sentencepiece_id": "pt",
        "kenlm_id": "pt",
    },
    {
        "lang": "Somali",
        "dataset_id": "so",
        "stopwords_id": "so",
        "badwords_id": None,
        "fasttext_id": "so",
        "sentencepiece_id": None,
        "kenlm_id": None,
    },
    {
        "lang": "Swahili",
        "dataset_id": "sw",
        "stopwords_id": "sw",
        "badwords_id": None,
        "fasttext_id": "sw",
        "sentencepiece_id": None,
        "kenlm_id": None,
    },
    {
        "lang": "Tamil",
        "dataset_id": "ta",
        "stopwords_id": None,
        "badwords_id": None,
        "fasttext_id": "ta",
        "sentencepiece_id": None,
        "kenlm_id": None,
    },
    {
        "lang": "Telugu",
        "dataset_id": "te",
        "stopwords_id": None,
        "badwords_id": "te",
        "fasttext_id": "te",
        "sentencepiece_id": None,
        "kenlm_id": None,
    },
    {
        "lang": "Urdu",
        "dataset_id": "ur",
        "stopwords_id": "ur",
        "badwords_id": None,
        "fasttext_id": "ur",
        "sentencepiece_id": None,
        "kenlm_id": None,
    },
    {
        "lang": "Vietnamese",
        "dataset_id": "vi",
        "stopwords_id": "vi",
        "badwords_id": "vi",
        "fasttext_id": "vi",
        "sentencepiece_id": None,
        "kenlm_id": None,
    },
    {
        "lang": "Yoruba",
        "dataset_id": "yo",
        "stopwords_id": "yo",
        "badwords_id": None,
        "fasttext_id": "yo",
        "sentencepiece_id": None,
        "kenlm_id": None,
    },
    {
        "lang": "Chinese",
        "dataset_id": "zh",
        "stopwords_id": "zh",
        "badwords_id": "zh",
        "fasttext_id": "zh",
        "sentencepiece_id": "zh",
        "kenlm_id": "zh",
    },
]
langs_id = pd.DataFrame(langs_id)
