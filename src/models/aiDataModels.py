from typing import Optional
from pydantic import BaseModel, Field

class WordGuessingResponse(BaseModel):
    hanzi: str
    pinyin: str
    meaning: str

class SentenceResponse(BaseModel):
    hanzi: str
    pinyin: str
    english: str

class TranslationResponse(BaseModel):
    translation: str
    sentences: list[SentenceResponse]

class WordGuessingRequest(BaseModel):
    pinyin: str
    context: Optional[str] = None

class TranslationRequest(BaseModel):
    word: str
    context: Optional[str] = None