from dataclasses import dataclass
from typing import Optional
from ashredis import RecordBase, MISSING

@dataclass
class UsersInfo(RecordBase):
    user_id: str
    username: Optional[str] = MISSING
    first_name: Optional[str] = MISSING
    last_name: Optional[str] = MISSING
    phone: Optional[str] = MISSING
    chat_id: Optional[str] = MISSING
    link: Optional[str] = MISSING
    timestamp: Optional[str] = MISSING
