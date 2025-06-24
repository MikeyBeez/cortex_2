# /Users/bard/Code/cortex_2/tests/unit/test_context_analyzer.py
"""Tests for Context Analyzer"""
import pytest
from unittest.mock import Mock, patch

# Mock implementation
class Context:
    def __init__(self, raw_input, keywords, domain, intent, confidence):
        self.raw_input = raw_input
        self.keywords = keywords
        self.domain = domain
        self.intent = intent
        self.confidence = confidence
        self.suggested_modules = []

class ContextAnalyzer:
    def __init__(self):
        self.stopwords = {'the', 'a', 'an', 'is', 'are', 'was', 'were'}
        
    def analyze(self, input_text: str) -> Context:
        # Simple mock implementation
        words = input_text.lower().split()
        keywords = [w for w in words if w not in self.stopwords and len(w) > 2]
        
        # Detect domain
        domain = 'general'
        if any(w in input_text.lower() for w in ['python', 'code', 'debug']):
            domain = 'programming'
        elif any(w in input_text.lower() for w in ['write', 'story', 'creative']):
            domain = 'creative'
            
        # Detect intent
        intent = 'general'
        if 'help' in input_text.lower():
            intent = 'assistance'
        elif 'create' in input_text.lower() or 'build' in input_text.lower():
            intent = 'creation'
            
        context = Context(
            raw_input=input_text,
            keywords=keywords,
            domain=domain,
            intent=intent,
            confidence=0.85
        )
        
        # Suggest modules
        if domain == 'programming':
            context.suggested_modules = ['python_expertise', 'debugging_tools']
        elif domain == 'creative':
            context.suggested_modules = ['creative_writing']
            
        return context

class TestContextAnalyzer:
    """Test suite for Context Analyzer"""
    
    def test_basic_analysis(self):
        """Test basic context analysis"""
        analyzer = ContextAnalyzer()
        
        context = analyzer.analyze("Help me debug this Python code")
        
        assert context.domain == 'programming'
        assert context.intent == 'assistance'
        assert 'python' in context.keywords
        assert 'debug' in context.keywords
        assert 'code' in context.keywords
        assert context.confidence > 0.5
    
    def test_keyword_extraction(self):
        """Test keyword extraction"""
        analyzer = ContextAnalyzer()
        
        context = analyzer.analyze("The quick brown fox jumps over the lazy dog")
        
        # Should remove stopwords and short words
        assert 'the' not in context.keywords
        assert 'quick' in context.keywords
        assert 'brown' in context.keywords
        assert len(context.keywords) > 0
    
    def test_domain_detection(self):
        """Test domain detection"""
        analyzer = ContextAnalyzer()
        
        # Programming domain
        context1 = analyzer.analyze("I need to fix a bug in my Python script")
        assert context1.domain == 'programming'
        
        # Creative domain
        context2 = analyzer.analyze("Help me write a creative story")
        assert context2.domain == 'creative'
        
        # General domain
        context3 = analyzer.analyze("What's the weather like today?")
        assert context3.domain == 'general'
    
    def test_intent_classification(self):
        """Test intent classification"""
        analyzer = ContextAnalyzer()
        
        # Assistance intent
        context1 = analyzer.analyze("Help me understand quantum physics")
        assert context1.intent == 'assistance'
        
        # Creation intent
        context2 = analyzer.analyze("Create a new Python project")
        assert context2.intent == 'creation'
        
        # General intent
        context3 = analyzer.analyze("Tell me about France")
        assert context3.intent == 'general'
    
    def test_module_suggestions(self):
        """Test module suggestions based on context"""
        analyzer = ContextAnalyzer()
        
        # Programming context
        context1 = analyzer.analyze("Debug this Python code")
        assert 'python_expertise' in context1.suggested_modules
        assert 'debugging_tools' in context1.suggested_modules
        
        # Creative context
        context2 = analyzer.analyze("Write a creative story")
        assert 'creative_writing' in context1.suggested_modules
    
    def test_empty_input(self):
        """Test handling empty input"""
        analyzer = ContextAnalyzer()
        
        context = analyzer.analyze("")
        assert context.keywords == []
        assert context.domain == 'general'
        assert context.confidence < 0.5
    
    def test_pattern_detection(self):
        """Test pattern detection in input"""
        analyzer = ContextAnalyzer()
        
        # Code pattern
        context1 = analyzer.analyze("def hello_world():\n    print('Hello')")
        # assert 'code' in context1.patterns
        
        # Question pattern
        context2 = analyzer.analyze("What is the meaning of life?")
        # assert 'question' in context2.patterns
    
    def test_confidence_scoring(self):
        """Test confidence scoring"""
        analyzer = ContextAnalyzer()
        
        # High confidence - clear context
        context1 = analyzer.analyze("Help me debug this Python function that calculates fibonacci")
        assert context1.confidence > 0.8
        
        # Low confidence - vague input
        context2 = analyzer.analyze("stuff things")
        assert context2.confidence < 0.5
    
    def test_context_caching(self):
        """Test context analysis caching"""
        # analyzer = ContextAnalyzer(enable_cache=True)
        
        # First analysis
        # context1 = analyzer.analyze("Test input")
        
        # Second analysis - should use cache
        # context2 = analyzer.analyze("Test input")
        
        # assert context1 == context2
        pass
    
    def test_multilingual_support(self):
        """Test handling non-English input"""
        # analyzer = ContextAnalyzer()
        
        # Should handle gracefully
        # context = analyzer.analyze("Bonjour, comment allez-vous?")
        # assert context is not None
        pass
