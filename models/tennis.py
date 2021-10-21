
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class TennisModel(BaseModel):
    _id: Optional[str] = None
    ATP: Optional[str] = None
    Location: Optional[str] = None
    Tournament: Optional[str] = None
    Date: Optional[str] = None
    Series: Optional[str] = None
    Court: Optional[str] = None
    Surface: Optional[str] = None
    Round: Optional[str] = None
    Best_of: Optional[str] = Field(None, alias='Best of')
    Winner: Optional[str] = None
    Loser: Optional[str] = None
    WRank: Optional[str] = None
    LRank: Optional[str] = None
    WPts: Optional[str] = None
    LPts: Optional[str] = None
    W1: Optional[str] = None
    L1: Optional[str] = None
    W2: Optional[str] = None
    L2: Optional[str] = None
    W3: Optional[str] = None
    L3: Optional[str] = None
    W4: Optional[str] = None
    L4: Optional[str] = None
    W5: Optional[str] = None
    L5: Optional[str] = None
    Wsets: Optional[str] = None
    Lsets: Optional[str] = None
    Comment: Optional[str] = None
    B365W: Optional[str] = None
    B365L: Optional[str] = None
    EXW: Optional[str] = None
    EXL: Optional[str] = None
    LBW: Optional[str] = None
    LBL: Optional[str] = None
    PSW: Optional[str] = None
    PSL: Optional[str] = None
    SJW: Optional[str] = None
    SJL: Optional[str] = None
    MaxW: Optional[str] = None
    MaxL: Optional[str] = None
    AvgW: Optional[str] = None
    AvgL: Optional[str] = None
