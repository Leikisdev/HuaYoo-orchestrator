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

# ---------- Sentences ----------
class SentenceCreate(BaseModel):
    cardId: Optional[int] = None
    chinese: str
    pinyin: Optional[str] = None
    english: str
    source: Optional[str] = None
    isAiGenerated: Optional[bool] = False
    audioUrl: Optional[str] = None


class SentenceRead(BaseModel):
    id: int
    cardId: int
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
    cardId: int
    tagId: int


class TranslationTagRead(BaseModel):
    cardId: int
    tagId: int


# ---------- Decks ----------
class DeckCreate(BaseModel):
    userId: int
    name: str
    isAiComposed: Optional[bool] = False

class DeckRead(BaseModel):
    id: int
    userId: int
    name: str
    isAiComposed: bool
    createdAt: datetime
    lastPracticeAt: Optional[datetime] = None


# ---------- DeckTranslations (join) ----------
class DeckCardCreate(BaseModel):
    deckId: int
    cardId: int
    position: int

class DeckCardRead(BaseModel):
    deckId: int
    cardId: int
    position: int
    addedAt: datetime


# ---------- Reviews ----------
class ReviewCreate(BaseModel):
    userId: int
    cardId: int
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
    cardId: int
    deckId: Optional[int] = None
    reviewedAt: datetime
    rating: int
    intervalDays: int
    easeFactor: float
    streak: int
    lapses: int
    dueAt: Optional[datetime] = None

# ---------- Flashcards ----------
class FlashcardRegister(BaseModel):
    userId: int
    hanziSimplified: str
    hanziTraditional: Optional[str] = None
    isAiGenerated: bool = False
    pinyin: str  
    sentences: Optional[list[SentenceCreate]] = None

class FlashcardRead(BaseModel):
    cardId: int
    userId: int
    hanziSimplified: str
    hanziTraditional: Optional[str] = None
    pinyin: str
    translation: str
    sentences: list[SentenceRead]
    createdAt: datetime
    updatedAt: datetime