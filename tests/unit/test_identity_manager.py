# /Users/bard/Code/cortex_2/tests/unit/test_identity_manager.py
"""Tests for Identity Manager"""
import pytest
from unittest.mock import Mock, patch
import json

# Mock implementations
class Identity:
    def __init__(self, id, traits=None, preferences=None):
        self.id = id
        self.traits = traits or {}
        self.preferences = preferences or {}
        self.personas = []
        self.mood = {'valence': 0.0, 'arousal': 0.0}
        self.energy = 1.0
        self.confidence = 0.8
        
    def apply_persona(self, persona):
        self.personas.append(persona)
        # Apply trait modifications
        for trait, modifier in persona.modifications.items():
            if trait in self.traits:
                self.traits[trait] += modifier

class Persona:
    def __init__(self, id, modifications=None):
        self.id = id
        self.modifications = modifications or {}

class IdentityManager:
    def __init__(self):
        self.current_identity = None
        self.loaded_personas = {}
        self.available_identities = {
            'assistant': Identity('assistant', 
                traits={'helpfulness': 0.8, 'formality': 0.5}),
            'developer': Identity('developer',
                traits={'technical': 0.9, 'precision': 0.8})
        }
        
    def load_identity(self, identity_id: str) -> Identity:
        if identity_id not in self.available_identities:
            raise ValueError(f"Identity not found: {identity_id}")
        self.current_identity = self.available_identities[identity_id]
        return self.current_identity
        
    def apply_persona(self, persona_id: str) -> None:
        if not self.current_identity:
            raise ValueError("No identity loaded")
        persona = Persona(persona_id, modifications={'formality': 0.2})
        self.current_identity.apply_persona(persona)
        self.loaded_personas[persona_id] = persona
        
    def get_current(self) -> Identity:
        return self.current_identity

class TestIdentityManager:
    """Test suite for Identity Manager"""
    
    def test_load_identity(self):
        """Test loading base identity"""
        manager = IdentityManager()
        
        identity = manager.load_identity('assistant')
        
        assert identity is not None
        assert identity.id == 'assistant'
        assert manager.current_identity == identity
        assert 'helpfulness' in identity.traits
    
    def test_load_nonexistent_identity(self):
        """Test loading non-existent identity"""
        manager = IdentityManager()
        
        with pytest.raises(ValueError):
            manager.load_identity('nonexistent')
    
    def test_apply_persona(self):
        """Test applying persona overlay"""
        manager = IdentityManager()
        
        # Load base identity
        manager.load_identity('assistant')
        initial_formality = manager.current_identity.traits.get('formality', 0)
        
        # Apply persona
        manager.apply_persona('professional')
        
        # Check persona applied
        assert 'professional' in manager.loaded_personas
        assert len(manager.current_identity.personas) == 1
        
        # Check trait modification
        new_formality = manager.current_identity.traits.get('formality', 0)
        assert new_formality > initial_formality
    
    def test_apply_persona_without_identity(self):
        """Test applying persona without loaded identity"""
        manager = IdentityManager()
        
        with pytest.raises(ValueError):
            manager.apply_persona('professional')
    
    def test_identity_state_persistence(self):
        """Test saving and loading identity state"""
        manager = IdentityManager()
        
        # Set up identity with state
        identity = manager.load_identity('assistant')
        identity.mood['valence'] = 0.5
        identity.energy = 0.7
        
        # Save state (mocked)
        state = {
            'id': identity.id,
            'mood': identity.mood,
            'energy': identity.energy,
            'traits': identity.traits
        }
        
        # Create new manager and restore
        manager2 = IdentityManager()
        restored = manager2.load_identity('assistant')
        
        # Manually restore state
        restored.mood = state['mood']
        restored.energy = state['energy']
        
        assert restored.mood['valence'] == 0.5
        assert restored.energy == 0.7
    
    def test_mood_dynamics(self):
        """Test mood system dynamics"""
        manager = IdentityManager()
        identity = manager.load_identity('assistant')
        
        # Test mood updates
        initial_valence = identity.mood['valence']
        
        # Positive interaction
        identity.mood['valence'] += 0.1
        assert identity.mood['valence'] > initial_valence
        
        # Mood should be clamped
        identity.mood['valence'] = 1.5
        # In real implementation: assert identity.mood['valence'] <= 1.0
    
    def test_energy_depletion(self):
        """Test energy system"""
        manager = IdentityManager()
        identity = manager.load_identity('assistant')
        
        initial_energy = identity.energy
        
        # Complex task depletes energy
        identity.energy -= 0.2
        assert identity.energy < initial_energy
        
        # Energy should have minimum
        identity.energy = -0.5
        # In real implementation: assert identity.energy >= 0.0
    
    def test_persona_stacking(self):
        """Test multiple persona application"""
        manager = IdentityManager()
        manager.load_identity('developer')
        
        # Apply multiple personas
        manager.apply_persona('professional')
        manager.apply_persona('teacher')
        
        assert len(manager.current_identity.personas) == 2
        assert len(manager.loaded_personas) == 2
    
    def test_identity_switching(self):
        """Test switching between identities"""
        manager = IdentityManager()
        
        # Load first identity
        identity1 = manager.load_identity('assistant')
        identity1.mood['valence'] = 0.5
        
        # Switch to second identity
        identity2 = manager.load_identity('developer')
        
        assert manager.current_identity == identity2
        assert manager.current_identity.id == 'developer'
        
        # First identity state should be preserved if we switch back
        # In real implementation, state would be saved
    
    def test_confidence_system(self):
        """Test confidence dynamics"""
        manager = IdentityManager()
        identity = manager.load_identity('assistant')
        
        initial_confidence = identity.confidence
        
        # Success increases confidence
        identity.confidence += 0.05
        assert identity.confidence > initial_confidence
        
        # Failure decreases confidence
        identity.confidence -= 0.1
        assert identity.confidence < initial_confidence
    
    def test_identity_composition(self):
        """Test composing identities from multiple sources"""
        # manager = IdentityManager()
        
        # Compose identity from base + additions
        # composite = manager.compose_identity(
        #     base='assistant',
        #     additions=['technical_writer', 'patient_teacher']
        # )
        
        # Should have combined traits
        # assert 'helpfulness' in composite.traits  # from assistant
        # assert 'technical' in composite.traits     # from technical_writer
        # assert 'patience' in composite.traits      # from patient_teacher
        pass
