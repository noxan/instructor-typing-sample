import instructor
from langfuse.openai import openai
from pydantic import BaseModel

client = instructor.from_openai(openai.Client())


class SampleSchema(BaseModel):
    poem: str
    number: int


result = client.completions.chat.create(
    messages=[],
    model="gpt-3.5-turbo",
    response_model=SampleSchema,
)
