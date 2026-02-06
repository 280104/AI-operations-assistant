"""
AI Operations Assistant - Main Orchestrator
Coordinates Planner, Executor, and Verifier agents
"""
import json
from typing import Dict, Any
from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.verifier import verifier_agent


class AIOperationsAssistant:
    def __init__(self):
        self.planner = planner_agent
        self.executor = executor_agent
        self.verifier = verifier_agent
    
    def process_task(self, user_task: str, verbose: bool = False) -> Dict[str, Any]:
        """
        Process a user task through the multi-agent pipeline
        
        Args:
            user_task: Natural language task description
            verbose: Print intermediate steps
        
        Returns:
            Final structured result
        """
        if verbose:
            print(f"\n{'='*60}")
            print(f"TASK: {user_task}")
            print(f"{'='*60}\n")
        
        # Step 1: Planning
        if verbose:
            print("📋 PLANNER: Creating execution plan...")
        
        try:
            plan = self.planner.create_plan(user_task)
            if verbose:
                print(f"✓ Plan created with {len(plan.get('steps', []))} steps\n")
                print(json.dumps(plan, indent=2))
                print()
        except Exception as e:
            return {
                "status": "error",
                "stage": "planning",
                "error": str(e)
            }
        
        # Step 2: Execution
        if verbose:
            print("⚙️  EXECUTOR: Running plan steps...")
        
        try:
            execution_results = self.executor.execute_plan(plan)
            if verbose:
                print(f"✓ Executed {len(execution_results['steps_executed'])} steps\n")
        except Exception as e:
            return {
                "status": "error",
                "stage": "execution",
                "error": str(e),
                "plan": plan
            }
        
        # Step 3: Verification
        if verbose:
            print("✅ VERIFIER: Validating results...")
        
        try:
            final_result = self.verifier.verify_and_format(user_task, execution_results)
            if verbose:
                print(f"✓ Verification complete\n")
                print(f"{'='*60}")
                print("FINAL RESULT:")
                print(f"{'='*60}\n")
                print(json.dumps(final_result, indent=2))
        except Exception as e:
            return {
                "status": "error",
                "stage": "verification",
                "error": str(e),
                "execution_results": execution_results
            }
        
        return final_result


def main():
    """CLI Interface"""
    print("""
    ╔═══════════════════════════════════════════════╗
    ║   AI Operations Assistant                     ║
    ║   Multi-Agent Task Automation System          ║
    ╚═══════════════════════════════════════════════╝
    """)
    
    assistant = AIOperationsAssistant()
    
    # Example tasks
    example_tasks = [
        "Find the top 3 Python repositories on GitHub and get the current weather in San Francisco",
        "Search for machine learning repositories and tell me the weather in London",
        "Get information about the tensorflow/tensorflow repository"
    ]
    
    print("Example tasks:")
    for i, task in enumerate(example_tasks, 1):
        print(f"{i}. {task}")
    
    print("\nOr enter your own task (or 'quit' to exit)\n")
    
    while True:
        try:
            user_input = input("Enter task number or custom task: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            # Check if input is a number for example tasks
            if user_input.isdigit():
                task_num = int(user_input)
                if 1 <= task_num <= len(example_tasks):
                    task = example_tasks[task_num - 1]
                else:
                    print("Invalid task number")
                    continue
            else:
                task = user_input
            
            if not task:
                continue
            
            # Process the task
            result = assistant.process_task(task, verbose=True)
            
            print("\n" + "="*60)
            print("Want to try another task? (or 'quit' to exit)")
            print("="*60 + "\n")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()
