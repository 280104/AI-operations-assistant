"""
FastAPI REST API Server for AI Operations Assistant
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from main import AIOperationsAssistant
import uvicorn


app = FastAPI(
    title="AI Operations Assistant API",
    description="Multi-agent system for task automation with LLM and API integrations",
    version="1.0.0"
)

assistant = AIOperationsAssistant()


class TaskRequest(BaseModel):
    task: str
    verbose: Optional[bool] = False


class TaskResponse(BaseModel):
    status: str
    result: dict


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "AI Operations Assistant API",
        "status": "running",
        "version": "1.0.0"
    }


@app.post("/process", response_model=TaskResponse)
async def process_task(request: TaskRequest):
    """
    Process a natural language task
    
    Args:
        request: Task request with task description
    
    Returns:
        Structured result from multi-agent processing
    """
    try:
        result = assistant.process_task(request.task, verbose=request.verbose)
        return TaskResponse(status="success", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "agents": {
            "planner": "ready",
            "executor": "ready",
            "verifier": "ready"
        },
        "tools": ["github_search", "github_info", "weather_current", "weather_forecast"]
    }


if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════╗
    ║   AI Operations Assistant API Server          ║
    ╚═══════════════════════════════════════════════╝
    
    Starting server on http://localhost:8000
    
    Endpoints:
    - POST /process - Process a task
    - GET /health  - Health check
    - GET /docs    - API documentation
    """)
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
