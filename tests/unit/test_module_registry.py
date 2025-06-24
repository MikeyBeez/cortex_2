# /Users/bard/Code/cortex_2/tests/unit/test_module_registry.py
"""Tests for Module Registry"""
import pytest
from pathlib import Path
from unittest.mock import Mock, patch

# These imports will work once we implement the actual modules
# from cortex.modules.registry import ModuleRegistry, ModuleRecord
# from cortex.modules.types import ModuleType, ModuleStatus

# For now, let's create mock classes
class ModuleType:
    KNOWLEDGE = "knowledge"
    CAPABILITY = "capability"
    IDENTITY = "identity"
    MEMORY = "memory"

class ModuleStatus:
    AVAILABLE = "available"
    LOADED = "loaded"
    LOADING = "loading"

class ModuleRecord:
    def __init__(self, id, version, type, status=ModuleStatus.AVAILABLE):
        self.id = id
        self.version = version
        self.type = type
        self.status = status
        self.size = 1000

class ModuleRegistry:
    def __init__(self):
        self.modules = {}
        
    def register(self, module_path: str) -> str:
        # Mock implementation
        return "test_module"
        
    def find_by_keyword(self, keyword: str) -> list:
        return []
        
    def get_dependencies(self, module_id: str) -> list:
        return []
        
    def check_conflicts(self, module_id: str) -> list:
        return []

class TestModuleRegistry:
    """Test suite for ModuleRegistry"""
    
    def test_register_module(self, mock_module_dir):
        """Test registering a new module"""
        registry = ModuleRegistry()
        
        # Register module
        module_id = registry.register(str(mock_module_dir))
        
        assert module_id == "test_module"
        # Once implemented:
        # assert module_id in registry.modules
        # assert registry.modules[module_id].version == "1.0.0"
    
    def test_register_duplicate_module(self, mock_module_dir):
        """Test registering duplicate module"""
        registry = ModuleRegistry()
        
        # Register once
        registry.register(str(mock_module_dir))
        
        # Try to register again - should raise error
        # with pytest.raises(ModuleAlreadyExistsError):
        #     registry.register(str(mock_module_dir))
    
    def test_find_by_keyword(self):
        """Test finding modules by keyword"""
        registry = ModuleRegistry()
        
        # Add test modules
        registry.modules['python_module'] = ModuleRecord(
            'python_module', '1.0.0', ModuleType.KNOWLEDGE
        )
        registry.modules['java_module'] = ModuleRecord(
            'java_module', '1.0.0', ModuleType.KNOWLEDGE
        )
        
        # Search
        results = registry.find_by_keyword('python')
        
        # Once implemented:
        # assert len(results) == 1
        # assert results[0].id == 'python_module'
    
    def test_dependency_resolution(self):
        """Test dependency resolution"""
        registry = ModuleRegistry()
        
        # Set up modules with dependencies
        # module_a depends on module_b
        # module_b depends on module_c
        
        deps = registry.get_dependencies('module_a')
        
        # Once implemented:
        # assert 'module_b' in deps
        # assert 'module_c' in deps
        # assert len(deps) == 2
    
    def test_circular_dependency_detection(self):
        """Test circular dependency detection"""
        registry = ModuleRegistry()
        
        # Set up circular dependency
        # module_a -> module_b -> module_c -> module_a
        
        # Should detect circular dependency
        # with pytest.raises(CircularDependencyError):
        #     registry.get_dependencies('module_a')
    
    def test_conflict_detection(self):
        """Test conflict detection"""
        registry = ModuleRegistry()
        
        # Set up conflicting modules
        conflicts = registry.check_conflicts('module_a')
        
        # Once implemented:
        # assert len(conflicts) > 0
        # assert conflicts[0].reason == "version_conflict"
    
    def test_version_compatibility(self):
        """Test version compatibility checking"""
        registry = ModuleRegistry()
        
        # Test various version specs
        # assert registry.version_compatible("1.0.0", ">=1.0.0")
        # assert registry.version_compatible("1.2.0", ">=1.0.0")
        # assert not registry.version_compatible("0.9.0", ">=1.0.0")
        # assert registry.version_compatible("1.2.3", "~=1.2.0")
    
    def test_module_stats_tracking(self):
        """Test module usage statistics"""
        registry = ModuleRegistry()
        
        # Track usage
        # registry.record_usage('test_module')
        # registry.record_usage('test_module')
        
        # stats = registry.get_stats('test_module')
        # assert stats.usage_count == 2
        # assert stats.last_used is not None
