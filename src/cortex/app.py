"""Cortex_2 FastAPI Application"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from .api import health, modules, knowledge_graph, context, identity, resources
from .api.models import RootResponse

# Try to import settings, fall back to simple version if needed
try:
    from .core.config import settings
except ImportError:
    # Create minimal settings if config fails
    class Settings:
        app_name = "Cortex_2"
        version = "0.1.0"
    settings = Settings()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifecycle"""
    logger.info("Starting Cortex_2 API server...")
    yield
    logger.info("Shutting down Cortex_2 API server...")

# Create FastAPI app
app = FastAPI(
    title="Cortex_2 API",
    description="Cognitive Operating System - Dynamic module loading and knowledge management",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/health", tags=["System"])
app.include_router(modules.router, prefix="/modules", tags=["Modules"])
app.include_router(knowledge_graph.router, prefix="/knowledge-graph", tags=["Knowledge Graph"])
app.include_router(context.router, prefix="/context", tags=["Context"])
app.include_router(identity.router, prefix="/identity", tags=["Identity"])
app.include_router(resources.router, prefix="/resources", tags=["Resources"])

@app.get("/", response_model=RootResponse)
async def root() -> RootResponse:
    """Root endpoint with API information"""
    return RootResponse(
        name="Cortex_2 API",
        version="0.1.0",
        description="Cognitive Operating System with dynamic module loading",
        docs_url="/docs",
        health_url="/health",
        modules_url="/modules",
        knowledge_graph_url="/knowledge-graph"
    )
