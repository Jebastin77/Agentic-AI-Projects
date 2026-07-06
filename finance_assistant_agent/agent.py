from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from investment_plan_agent.agent import investment_plan_agent
from typing import Dict


def get_user_personal_details() -> Dict:
    """
    Gets users personal finance details like salary, expenses and savings capacity.
    """

    return {
        "salary": 50000,
        "expense": {
            "EMI_Expense": 25000,
            "Essentials": 5000,
            "Entertainment": 5000,
            "Shopping and Travel": 5000
        },
        "savings": 10000
    }


finance_assistant_agent = LlmAgent(
    name="finance_assistant_agent",
    model="gemini-2.5-flash",
    description="A simple finance assistant that helps users with their finance goals.",
    instruction="""
You are a friendly finance assistant.

You have two tools to use to complete your task.

1. get_user_personal_details - This tool will give you the user's current financial details.

2. investment_plan_agent - This tool can perform Google Search to get any latest information from websites and will be able to ask more details from the user and plan their savings goal.

You can answer users' generic finance questions and help them plan their financial goals.
Be friendly, positive, and provide clear explanations.
""",
    tools=[
        AgentTool(investment_plan_agent),
        get_user_personal_details,
    ],
)

root_agent = finance_assistant_agent