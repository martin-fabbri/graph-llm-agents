from datetime import datetime

from pydantic import BaseModel, EmailStr, PositiveInt, field_validator


class User(BaseModel):
    id: int
    source: str
    name: str = "John Doe"
    email: EmailStr
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]

    @field_validator("source")
    @classmethod
    def source_must_start_with_prefix(cls, v: str) -> str:
        if not v.startswith("XYZ"):
            raise ValueError("must start with 'XYZ'")
        return v.title


external_data = {
    "id": 123,
    "source": "XYZ7000",
    "signup_ts": "2019-06-01 12:22",
    "email": "john@doe.com",
    "tastes": {
        "wine": 9,
        "cheese": 7,
        "cabbage": 1,
    },
}

user = User(**external_data)

print(user.id)
print(user.model_dump())

user_098_dump = """{
    "id": 098, 
    "source": "XYZ0000", 
    "name": "John Doe", 
    "email": "john@doe.com", 
    "signup_ts": datetime.datetime(2019, 6, 1, 12, 22), 
    "tastes": {"wine": 9, "cheese": 7, "cabbage": 1},
}"""

user_098 = User.parse_raw(user_098_dump.replace("\n", ""))

invalid_external_data = {
    "id": 123,
    "source": "XYZ007",
    "signup_ts": "2019-06-01 12:22",
    "email": "john@doe.com",
    "tastes": {
        "wine": 9,
        "cheese": 7,
        "cabbage": 1,
    },
}

invalid_user = User(**invalid_external_data)

# print(invalid_user.model_dump_json())
