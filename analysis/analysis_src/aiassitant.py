import os
from pyexpat import model
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

class ai_assistant:
    def __init__(self):
        pass

    def api_key(self):
        groq_api_key= os.getenv("GROQ_API")
        return groq_api_key
    
    def set_model(self):
        model=ChatGroq(model='gemma2-9b-it',groq_api_key=self.api_key())
        return model
    
    def set_prompt(self):
        prompt=ChatPromptTemplate.from_messages(
            [
                SystemMessage(content="""You are a professional data analyst with strong domain expertise and critical thinking skills. Your role is to:
                        Analyze any dataset, data summary, or data info provided to you.
                        Give clear, logical, and concise insights that go beyond surface-level observations.
                        Detect and explain any blunders, inconsistencies, or anomalies in the data (e.g., suspicious values, mismatched data types, missing data, redundant columns, or outliers).
                        Suggest possible root causes, business implications, and next steps or fixes.
                        Always respond like a professional analyst speaking to a data science team or a decision-making stakeholder.
                        When interpreting data, focus on:
                        Data quality and structure
                        Statistical distribution
                        Logical coherence
                        Potential issues or red flags
                        Actionable insights
                        Never make vague statements—always back your points with specific evidence from the data."""),
                HumanMessage(content="{question}")
            ]
        )
        return prompt
    
    def set_output_parser(self):
        output_parser=StrOutputParser()
        return output_parser
    
class AiAssistant(ai_assistant):
    def __init__(self):
        super().__init__()
        self.model=self.set_model()
        self.prompt=self.set_prompt()
        self.output_parser=self.set_output_parser()

    def get_response(self, question):
        """ 
        Takes a question as input and returns the response from the AI model.
        
        :param question: str - The question to be answered by the AI model.
        :return: str - The response from the AI model.
        """
        prompt_with_question=self.prompt.format_prompt(question=question)
        response=self.model.invoke(prompt_with_question)
        return self.output_parser.parse(response.content)