import instructor
from instructor.client import T
from langfuse.openai import openai
from pydantic import BaseModel

client = instructor.from_openai(openai.Client(api_key=""))


class SampleSchema(BaseModel):
    poem: str
    number: int


result = client.completions.chat.create(
    messages=[],
    model="gpt-3.5-turbo",
    response_model=SampleSchema,
)

result2 = client.completions.chat.create(
    messages=[],
    model="gpt-3.5-turbo",
    response_model=None,
)


def wrapped_create(response_model: type[T] | None) -> T | str:
    result = client.create(
        messages=[],
        model="gpt-3.5-turbo",
        response_model=response_model,
    )
    if response_model is None:
        return result.choices[0].message.content or ""

    return result
