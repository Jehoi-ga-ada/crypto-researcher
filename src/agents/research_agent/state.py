from typing import List, TypedDict

class ResearchState(TypedDict):
    question: str
    answer: str
    documents: List[str]