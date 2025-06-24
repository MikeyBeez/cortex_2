"""Context management endpoints"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

from .models import ContextPushResponse, ContextAnalysisResponse

router = APIRouter()

class ContextPushRequest(BaseModel):
    domain: str
    intent: str
    keywords: List[str] = []

class ContextAnalyzeRequest(BaseModel):
    text: str

@router.post("/push", response_model=ContextPushResponse)
async def push_context(request: ContextPushRequest) -> ContextPushResponse:
    """Push context information"""
    return ContextPushResponse(
        status="context_updated",
        domain=request.domain,
        intent=request.intent,
        keywords=request.keywords,
        suggested_modules=["python_expertise"] if "python" in request.keywords else []
    )

@router.post("/analyze", response_model=ContextAnalysisResponse)
async def analyze_context(request: ContextAnalyzeRequest) -> ContextAnalysisResponse:
    """Analyze text to determine context"""
    keywords = request.text.lower().split()[:10]  # Simple keyword extraction
    domain = "programming" if any(word in request.text.lower() for word in ["python", "code", "debug"]) else "general"
    
    return ContextAnalysisResponse(
        keywords=keywords,
        domain=domain,
        intent="unknown",
        confidence=0.75,
        suggested_modules=[]
    )
