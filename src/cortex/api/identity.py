"""Identity management endpoints"""
from fastapi import APIRouter, HTTPException, status

from .models import IdentityInfo, IdentityLoadResponse

router = APIRouter()

@router.get("/current", response_model=IdentityInfo)
async def get_current_identity() -> IdentityInfo:
    """Get current identity configuration"""
    return IdentityInfo(
        identity_id="default",
        traits=["helpful", "analytical"],
        communication_style={
            "tone": "professional",
            "complexity": "adaptive"
        },
        active_personas=[]
    )

@router.post("/load/{identity_id}", response_model=IdentityLoadResponse)
async def load_identity(identity_id: str) -> IdentityLoadResponse:
    """Load an identity configuration"""
    known_identities = ["default", "developer", "teacher", "mikey_bee_core"]
    
    if identity_id not in known_identities:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Identity {identity_id} not found"
        )
    
    return IdentityLoadResponse(
        status="loaded",
        identity_id=identity_id,
        message=f"Identity {identity_id} loaded successfully"
    )
