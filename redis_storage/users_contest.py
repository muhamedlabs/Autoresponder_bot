from dataclasses import dataclass
from ashredis import RecordBase, MISSING
from typing import Optional

@dataclass
class UsersContest(RecordBase):
    user_id: str
    first_name: Optional[str] = MISSING
    language: Optional[str] = MISSING
    first_message_1: Optional[str] = MISSING
    first_message_2: Optional[str] = MISSING
    first_message_3: Optional[str] = MISSING
    first_message_4: Optional[str] = MISSING
    first_message_5: Optional[str] = MISSING
