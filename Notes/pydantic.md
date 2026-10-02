Pydantic: Source and AgentResponse
1. What is Pydantic?
A library for making forms with fixed fields.
It makes the agent reply in an organized shape, not free text.
Each form is a class that inherits from BaseModel.
2. What is a class?
A template (a blank form).
You design it once, then fill it in many times.
3. The two classes

Source = ONE website

python
class Source(BaseModel):
    """A source of information."""
    url: str = Field(description="The URL of the source.")

AgentResponse = the WHOLE reply

python
class AgentResponse(BaseModel):
    """Agent response with answer and sources"""
    answer: str = Field(description="The agent answer")
    sources: List[Source] = Field(default_factory=list, description="Sources used")
4. Key parts explained
Part	Meaning
"""..."""	Docstring: a note the AI reads
url: str	A field named url that must be text
Field(description=...)	An instruction telling the AI what to put there
List[Source]	A list of many Source forms
default_factory=list	If there are no sources, use an empty list []
5. Picture to remember
AgentResponse   (the folder)
├── answer: "..."
└── sources:
      ├── Source(url="weather.com")
      └── Source(url="indeed.com")
6. Rules to remember
One Source per website. The list can hold as many as needed.
Two classes are not required. sources: list[str] also works.
Two classes are used because they're cleaner and easy to expand.
To add details to each website (title, topic), edit only Source.
To add something to the whole reply (summary, confidence), edit AgentResponse.
7. How to use it
python
agent = create_agent(model=llm, tools=[...], response_format=AgentResponse)

result = agent.invoke({"messages": [HumanMessage(content="...")]})
response = result["structured_response"]

print(response.answer)
for s in response.sources:
    print(s.url)

whether you need to change the Source class to fit a second website (one for weather, one for jobs). You don't.

1. Is each class written only once?

Yes. Source is written once, and AgentResponse is written once. That's all the class code you need, however many questions you ask.

2. Do you need to add another website to Source?

No. Keep only one url field. Don't write anything like this:

python
class Source(BaseModel):
    url: str
    url2: str        # ✗ not needed

IMPORTANT : Source describes one website. When the agent uses two websites, it simply makes two Source items.

What happens when you ask your question:

"What is the weather in Tokyo, and search for AI engineer jobs in Tokyo?"

The agent searches for the weather and finds weather.com.
The agent searches for jobs and finds indeed.com.
It creates 2 Source items from the same one class.
AgentResponse
├── answer: "Tokyo is 18°C. Here are some AI engineer jobs..."
└── sources:
      ├── Source(url="weather.com")    ← weather website
      └── Source(url="indeed.com")     ← jobs website

If it uses 5 websites, it makes 5 Source items, still from the same class.

The rule to remember:

Write the class once, and the agent makes as many items as it needs.

The only time you'd change Source is to add a new kind of detail for every website, such as a title or a topic. Not to add more websites.