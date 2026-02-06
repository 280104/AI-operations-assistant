"""
Verifier Agent: Validates execution results and ensures completeness
"""
from typing import Dict, Any
from llm.llm_client import llm_client


class VerifierAgent:
    def __init__(self):
        self.llm = llm_client
    
    def verify_and_format(
        self, 
        original_task: str,
        execution_results: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Verify execution results and format final output
        
        Args:
            original_task: Original user task
            execution_results: Results from Executor Agent
        
        Returns:
            Verified and formatted final output
        """
        # Check for errors
        has_errors = any(
            step.get("status") == "error" 
            for step in execution_results.get("steps_executed", [])
        )
        
        # Extract successful data
        successful_data = []
        errors = []
        
        for step in execution_results.get("steps_executed", []):
            if step.get("status") == "success":
                successful_data.append({
                    "step": step["step_number"],
                    "action": step["action"],
                    "data": step["data"]
                })
            else:
                errors.append({
                    "step": step["step_number"],
                    "action": step["action"],
                    "error": step["error"]
                })
        
        # Use LLM to verify completeness and format output
        verification = self._llm_verify(
            original_task, 
            successful_data, 
            errors
        )
        
        return {
            "task": original_task,
            "status": "partial_success" if has_errors else "success",
            "verification": verification,
            "data": successful_data,
            "errors": errors if errors else None
        }
    
    def _llm_verify(
        self, 
        task: str, 
        data: list, 
        errors: list
    ) -> Dict[str, Any]:
        """
        Use LLM to verify if results are complete and format them
        
        Args:
            task: Original task
            data: Successful step data
            errors: Any errors encountered
        
        Returns:
            Verification assessment
        """
        system_prompt = """You are a verification agent. Analyze execution results and assess:
1. Were all required steps completed?
2. Is the data sufficient to answer the user's task?
3. What information is missing (if any)?
4. Provide a human-readable summary

Output ONLY valid JSON with this schema:
{
    "is_complete": true/false,
    "missing_items": ["item1", "item2"] or [],
    "summary": "Human-readable summary of results",
    "confidence": "high/medium/low"
}"""

        user_prompt = f"""Original Task: {task}

Successful Data:
{data}

Errors (if any):
{errors}

Verify if the execution successfully accomplished the task."""

        try:
            verification = self.llm.generate_json(user_prompt, system_prompt)
            return verification
        except Exception as e:
            # Fallback verification if LLM fails
            return {
                "is_complete": len(errors) == 0,
                "missing_items": [],
                "summary": "Verification completed with errors" if errors else "Task executed successfully",
                "confidence": "low"
            }


# Singleton instance
verifier_agent = VerifierAgent()
