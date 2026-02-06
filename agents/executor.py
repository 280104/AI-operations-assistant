"""
Executor Agent: Executes the plan by calling appropriate tools
"""
from typing import Dict, Any, List
from tools.github_tool import github_tool
from tools.weather_tool import weather_tool


class ExecutorAgent:
    def __init__(self):
        self.tool_map = {
            "github_search": self._github_search,
            "github_info": self._github_info,
            "weather_current": self._weather_current,
            "weather_forecast": self._weather_forecast
        }
    
    def execute_plan(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the plan by running each step
        
        Args:
            plan: Plan dictionary from Planner Agent
        
        Returns:
            Dictionary with execution results
        """
        results = {
            "task_summary": plan.get("task_summary", ""),
            "steps_executed": [],
            "errors": []
        }
        
        steps = plan.get("steps", [])
        
        for step in steps:
            step_result = self._execute_step(step)
            results["steps_executed"].append(step_result)
        
        return results
    
    def _execute_step(self, step: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a single step
        
        Args:
            step: Step dictionary with action and parameters
        
        Returns:
            Step result with data or error
        """
        step_number = step.get("step_number", 0)
        action = step.get("action", "")
        parameters = step.get("parameters", {})
        reasoning = step.get("reasoning", "")
        
        result = {
            "step_number": step_number,
            "action": action,
            "reasoning": reasoning,
            "status": "success",
            "data": None,
            "error": None
        }
        
        try:
            if action in self.tool_map:
                tool_function = self.tool_map[action]
                data = tool_function(parameters)
                result["data"] = data
            else:
                result["status"] = "error"
                result["error"] = f"Unknown tool: {action}"
        
        except Exception as e:
            result["status"] = "error"
            result["error"] = str(e)
        
        return result
    
    # Tool wrapper methods
    def _github_search(self, params: Dict[str, Any]) -> Any:
        """Execute GitHub search"""
        query = params.get("query", "")
        limit = params.get("limit", 5)
        sort = params.get("sort", "stars")
        return github_tool.search_repositories(query, sort, limit)
    
    def _github_info(self, params: Dict[str, Any]) -> Any:
        """Execute GitHub repo info fetch"""
        owner = params.get("owner", "")
        repo = params.get("repo", "")
        return github_tool.get_repository_info(owner, repo)
    
    def _weather_current(self, params: Dict[str, Any]) -> Any:
        """Execute current weather fetch"""
        city = params.get("city", "")
        units = params.get("units", "metric")
        return weather_tool.get_current_weather(city, units)
    
    def _weather_forecast(self, params: Dict[str, Any]) -> Any:
        """Execute weather forecast fetch"""
        city = params.get("city", "")
        units = params.get("units", "metric")
        return weather_tool.get_forecast(city, units)


# Singleton instance
executor_agent = ExecutorAgent()
