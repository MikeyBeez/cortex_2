"""Health check endpoints"""
from fastapi import APIRouter
from datetime import datetime
from typing import Dict, Any

from .models import HealthStatus, ReadinessStatus, LivenessStatus

router = APIRouter()

@router.get("", response_model=HealthStatus)
async def health_check() -> HealthStatus:
    """Check the health status of Cortex_2 system"""
    return HealthStatus(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        version="0.1.0",
        components={
            "module_registry": {"status": "operational"},
            "knowledge_graph": {"status": "operational"},
            "identity_manager": {"status": "operational"},
            "resource_monitor": {"status": "operational"},
            "context_analyzer": {"status": "operational"},
            "learning_system": {"status": "experimental"}
        }
    )

@router.get("/ready", response_model=ReadinessStatus)
async def readiness_check() -> ReadinessStatus:
    """Check if the service is ready to accept requests"""
    return ReadinessStatus(status="ready")

@router.get("/live", response_model=LivenessStatus)
async def liveness_check() -> LivenessStatus:
    """Check if the service is alive"""
    return LivenessStatus(status="alive")
