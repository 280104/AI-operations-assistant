"""
Planner Agent: Converts user input into actionable step-by-step plan
"""
from typing import Dict, Any, List
from llm.llm_client import llm_client


class PlannerAgent:
    def __init__(self):
        self.llm = llm_client
        self.available_tools = {
            "github_search": "Search GitHub repositories by query, returns top repositories with stars and info",
            "weather_current": "Get current weather for a city",
            "weather_forecast": "Get 5-day weather forecast for a city"
        }
    
    def create_plan(self, user_task: str) -> Dict[str, Any]:
        """
        Create a structured plan from user's natural language task
        
        Args:
            user_task: Natural language description of task
        
        Returns:
            Dictionary with plan structure
        """
        system_prompt = f"""You are a planning agent. Your job is to break down user tasks into step-by-step plans.

Available tools:
{self._format_tools()}

Rules:
1. Output ONLY valid JSON
2. Each step must specify a tool and parameters
3. Do NOT create steps that depend on results from other steps
4. Use github_search with limit parameter instead of multiple github_info calls
5. Be specific with parameters

JSON Schema:
{{
    "task_summary": "Brief summary of the task",
    "steps": [
        {{
            "step_number": 1,
            "action": "tool_name",
            "parameters": {{"param": "value"}},
            "reasoning": "Why this step is needed"
        }}
    ]
}}"""

        user_prompt = f"""Task: {user_task}

Create a step-by-step plan to accomplish this task using the available tools."""

        try:
            plan = self.llm.generate_json(user_prompt, system_prompt)
            return plan
        except Exception as e:
            raise Exception(f"Planner Agent Error: {str(e)}")
    
    def _format_tools(self) -> str:
        """Format available tools for prompt"""
        tools_list = []
        for name, description in self.available_tools.items():
            tools_list.append(f"- {name}: {description}")
        return "\n".join(tools_list)


# Singleton instance
planner_agent = PlannerAgent()
