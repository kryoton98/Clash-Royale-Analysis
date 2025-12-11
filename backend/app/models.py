from sqlalchemy import Column, Integer, String, Float, JSON, DateTime, ForeignKey, Table, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

group_members = Table(
    'group_members',
    Base.metadata,
    Column('group_id', Integer, ForeignKey('groups.id')),
    Column('player_id', Integer, ForeignKey('players.id'))
)

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    card_id = Column(String, unique=True, index=True)
    name = Column(String)
    elixir_cost = Column(Integer)
    rarity = Column(String)
    card_type = Column(String)
    role_tags = Column(JSON, default=[])

class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    deck_id = Column(String, unique=True, index=True)
    card_ids = Column(JSON)
    avg_elixir = Column(Float)
    card_type_counts = Column(JSON)
    card_rarity_counts = Column(JSON)
    has_win_condition = Column(Boolean, default=False)
    meta_stats = relationship("DeckMeta", back_populates="deck")

class DeckMeta(Base):
    __tablename__ = "deck_meta"
    id = Column(Integer, primary_key=True)
    deck_id = Column(Integer, ForeignKey("decks.id"), index=True)
    trophy_range = Column(String)
    games_played = Column(Integer)
    wins = Column(Integer)
    win_rate = Column(Float)
    archetype = Column(String, nullable=True)
    deck = relationship("Deck", back_populates="meta_stats")

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    player_tag = Column(String, unique=True, index=True)
    name = Column(String, nullable=True)
    trophies = Column(Integer, nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow)
    decks = relationship("PlayerDeck", back_populates="player", cascade="all, delete-orphan")
    groups = relationship("Group", secondary=group_members, back_populates="players")

class PlayerDeck(Base):
    __tablename__ = "player_decks"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"), index=True)
    deck_id = Column(Integer, ForeignKey("decks.id"))
    games_played = Column(Integer, default=0)
    wins = Column(Integer, default=0)
    is_main = Column(Boolean, default=False)
    player = relationship("Player", back_populates="decks")

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    players = relationship("Player", secondary=group_members, back_populates="groups")
