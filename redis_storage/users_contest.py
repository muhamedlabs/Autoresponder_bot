from dataclasses import dataclass
from ashredis import RecordBase, MISSING
from typing import Optional

@dataclass
class UsersСontest(RecordBase):
    user_id: str 
    first_name: Optional[int] = MISSING
    language: Optional[int] = MISSING
    first_message_1: Optional[int] = MISSING
    first_message_2: Optional[int] = MISSING
    first_message_3: Optional[int] = MISSING
