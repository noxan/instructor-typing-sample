# https://python.useinstructor.com/concepts/parallel/

from __future__ import annotations

import openai
import instructor

from typing import Iterable, Literal
from pydantic import BaseModel


class Weather(BaseModel):
    location: str
    units: Literal["imperial", "metric"]


class GoogleSearch(BaseModel):
    query: str


client = instructor.from_openai(openai.OpenAI(), mode=instructor.Mode.PARALLEL_TOOLS)

function_calls = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": "You must always use tools"},
        {
            "role": "user",
            "content": "What is the weather in toronto and dallas and who won the super bowl?",
        },
    ],
    response_model=Iterable[Weather | GoogleSearch],
)

for fc in function_calls:
    print(fc)
    # > location='Toronto' units='metric'
    # > location='Dallas' units='imperial'
    # > query='super bowl winner'
