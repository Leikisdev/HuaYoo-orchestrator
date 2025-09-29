from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr


# ---------- Users ----------
class UserCreate(BaseModel):
    email: EmailStr
    displayName: str


class UserRead(BaseModel):
    id: int
    fedId: str
    email: EmailStr
    username: str
    createdAt: datetime
    lastModifiedAt: datetime


# ---------- Words ----------
class WordCreate(BaseModel):
    userId: int
    hanziSimplified: Optional[str] = None
    hanziTraditional: Optional[str] = None
    pinyinTone: Optional[str] = None
    frequencyRank: Optional[int] = None


class WordRead(BaseModel):
    id: int
    userId: int
    hanziSimplified: Optional[str] = None
    hanziTraditional: Optional[str] = None
    pinyinTone: Optional[str] = None
    frequencyRank: Optional[int] = None
    createdAt: datetime
    updatedAt: datetime


# ---------- Translations ----------
class TranslationCreate(BaseModel):
    wordId: int
    shortGloss: str
    definitionLong: Optional[str] = None
    usageNotes: Optional[str] = None
    register: Optional[str] = None
    partOfSpeech: Optional[str] = None
    source: Optional[str] = None
    isAiSuggested: Optional[bool] = False


class TranslationRead(BaseModel):
    id: int
    wordId: int
    shortGloss: str
    definitionLong: Optional[str] = None
    usageNotes: Optional[str] = None
    register: Optional[str] = None
    partOfSpeech: Optional[str] = None
    source: Optional[str] = None
    isAiSuggested: bool
    createdAt: datetime
    updatedAt: datetime


# ---------- Sentences ----------
class SentenceCreate(BaseModel):
    translationId: int
    chinese: str
    pinyin: Optional[str] = None
    english: Optional[str] = None
    source: Optional[str] = None
    isAiGenerated: Optional[bool] = False
    audioUrl: Optional[str] = None


class SentenceRead(BaseModel):
    id: int
    translationId: int
    chinese: str
    pinyin: Optional[str] = None
    english: Optional[str] = None
    source: Optional[str] = None
    isAiGenerated: bool
    audioUrl: Optional[str] = None
    createdAt: datetime


# ---------- Tags ----------
class TagCreate(BaseModel):
    userId: int
    value: str


class TagRead(BaseModel):
    id: int
    userId: int
    value: str
    createdAt: datetime


# ---------- TranslationTags (join) ----------
class TranslationTagCreate(BaseModel):
    translationId: int
    tagId: int


class TranslationTagRead(BaseModel):
    translationId: int
    tagId: int


# ---------- Decks ----------
class DeckCreate(BaseModel):
    userId: int
    name: str
    isAiComposed: Optional[bool] = False
    lastPracticeAt: Optional[datetime] = None


class DeckRead(BaseModel):
    id: int
    userId: int
    name: str
    isAiComposed: bool
    createdAt: datetime
    lastPracticeAt: Optional[datetime] = None


# ---------- DeckTranslations (join) ----------
class DeckTranslationCreate(BaseModel):
    deckId: int
    translationId: int
    position: int


class DeckTranslationRead(BaseModel):
    deckId: int
    translationId: int
    position: int
    addedAt: datetime


# ---------- Reviews ----------
class ReviewCreate(BaseModel):
    userId: int
    translationId: int
    deckId: Optional[int] = None
    rating: int = Field(ge=0, le=32767)
    intervalDays: Optional[int] = 0
    easeFactor: Optional[float] = 2.5
    streak: Optional[int] = 0
    lapses: Optional[int] = 0
    dueAt: Optional[datetime] = None


class ReviewRead(BaseModel):
    id: int
    userId: int
    translationId: int
    deckId: Optional[int] = None
    reviewedAt: datetime
    rating: int
    intervalDays: int
    easeFactor: float
    streak: int
    lapses: int
    dueAt: Optional[datetime] = None


# ---------- Recommendations ----------
class RecommendationCreate(BaseModel):
    userId: int
    sourceTranslationId: Optional[int] = None
    suggestedTranslationId: int
    reason: Optional[str] = None
    score: Optional[float] = 0.0


class RecommendationRead(BaseModel):
    id: int
    userId: int
    sourceTranslationId: Optional[int] = None
    suggestedTranslationId: int
    reason: Optional[str] = None
    score: float
    createdAt: datetime