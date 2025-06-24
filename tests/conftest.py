# /Users/bard/Code/cortex_2/tests/conftest.py
"""Pytest configuration and shared fixtures"""
import pytest
from pathlib import Path
import tempfile
import shutil
from typing import Generator

@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for tests"""
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    shutil.rmtree(temp_path)

@pytest.fixture
def mock_module_dir(temp_dir: Path) -> Path:
    """Create a mock module directory structure"""
    module_dir = temp_dir / "test_module"
    module_dir.mkdir()
    
    # Create manifest
    manifest = module_dir / "manifest.yaml"
    manifest.write_text("""
id: test_module
version: 1.0.0
type: knowledge
metadata:
  name: Test Module
  description: A test module
  size_tokens: 1000
triggers:
  keywords: [test, demo]
content:
  knowledge_files:
    - content/knowledge.json
""")
    
    # Create content directory
    content_dir = module_dir / "content"
    content_dir.mkdir()
    
    # Create knowledge file
    knowledge = content_dir / "knowledge.json"
    knowledge.write_text('{"test": "data"}')
    
    return module_dir

@pytest.fixture
def mock_event_bus():
    """Create a mock event bus"""
    class MockEventBus:
        def __init__(self):
            self.events = []
            
        def emit(self, event: str, data: any = None):
            self.events.append((event, data))
            
        def on(self, event: str, callback):
            pass
            
        def get_events(self):
            return self.events
            
    return MockEventBus()

@pytest.fixture
def mock_config():
    """Create mock configuration"""
    return {
        'memory': {
            'limit': 100000,
            'buffer': 5000
        },
        'storage': {
            'hot_size': 50000,
            'warm_directory': './storage/warm',
            'cold_directory': './storage/cold'
        },
        'learning': {
            'enabled': True,
            'exploration_rate': 0.1
        }
    }
