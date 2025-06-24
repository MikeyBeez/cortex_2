# Context Analyzer

The Context Analyzer understands the current situation and determines what kind of help is needed. It's the sensory system of Cortex_2.

## Purpose

- Analyze input to understand context
- Extract keywords, patterns, and intent
- Classify the type of interaction
- Detect domain and complexity
- Trigger appropriate module loading

## Core Structure

```python
class ContextAnalyzer:
    """Analyzes input to understand context"""
    
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.keyword_extractor = KeywordExtractor()
        self.pattern_detector = PatternDetector()
        self.intent_classifier = IntentClassifier()
        self.domain_identifier = DomainIdentifier()
```

## Context Model

```python
@dataclass
class Context:
    raw_input: str
    tokens: List[Token]
    keywords: List[Keyword]
    patterns: List[Pattern]
    intent: Intent
    domain: Domain
    complexity: float
    confidence: float
    metadata: Dict[str, Any]
```

## Analysis Pipeline

### 1. Tokenization
```python
def tokenize(self, input_text: str) -> List[Token]:
    """Break input into tokens"""
    tokens = []
    
    # Basic tokenization
    words = self.tokenizer.split(input_text)
    
    for word in words:
        token = Token(
            text=word,
            type=self.classify_token(word),
            position=self.get_position(word, input_text),
            features=self.extract_features(word)
        )
        tokens.append(token)
        
    return tokens
```

### 2. Keyword Extraction
```python
def extract_keywords(self, tokens: List[Token]) -> List[Keyword]:
    """Extract significant keywords"""
    keywords = []
    
    for token in tokens:
        # Skip common words
        if token.text in self.stopwords:
            continue
            
        # Calculate significance
        significance = self.calculate_significance(token)
        
        if significance > KEYWORD_THRESHOLD:
            keyword = Keyword(
                text=token.text,
                significance=significance,
                type=self.classify_keyword(token)
            )
            keywords.append(keyword)
            
    return keywords
```

### 3. Pattern Detection
```python
def detect_patterns(self, tokens: List[Token]) -> List[Pattern]:
    """Detect patterns in input"""
    patterns = []
    
    # Code patterns
    if self.is_code_pattern(tokens):
        patterns.append(Pattern(
            type=PatternType.CODE,
            confidence=self.code_detector.confidence(tokens)
        ))
    
    # Question patterns
    if self.is_question_pattern(tokens):
        patterns.append(Pattern(
            type=PatternType.QUESTION,
            subtype=self.classify_question(tokens)
        ))
    
    # Command patterns
    if self.is_command_pattern(tokens):
        patterns.append(Pattern(
            type=PatternType.COMMAND,
            action=self.extract_command(tokens)
        ))
        
    return patterns
```

### 4. Intent Classification
```python
def classify_intent(self, context: PartialContext) -> Intent:
    """Determine user intent"""
    features = self.extract_intent_features(context)
    
    # Use learned classifier
    intent_scores = self.intent_model.predict(features)
    
    # Get top intent
    top_intent = max(intent_scores.items(), key=lambda x: x[1])
    
    return Intent(
        type=top_intent[0],
        confidence=top_intent[1],
        sub_intents=self.extract_sub_intents(context)
    )
```

### 5. Domain Identification
```python
def identify_domain(self, context: PartialContext) -> Domain:
    """Identify the domain of discourse"""
    domain_scores = {}
    
    # Check keywords against domain vocabularies
    for domain, vocabulary in self.domain_vocabularies.items():
        score = self.calculate_domain_score(context.keywords, vocabulary)
        domain_scores[domain] = score
    
    # Get best matching domain
    best_domain = max(domain_scores.items(), key=lambda x: x[1])
    
    return Domain(
        name=best_domain[0],
        confidence=best_domain[1],
        sub_domains=self.identify_sub_domains(context, best_domain[0])
    )
```

## Complete Analysis

```python
def analyze(self, input_text: str) -> Context:
    """Complete context analysis"""
    # Tokenize
    tokens = self.tokenize(input_text)
    
    # Extract features
    keywords = self.extract_keywords(tokens)
    patterns = self.detect_patterns(tokens)
    
    # Build partial context
    partial = PartialContext(
        raw_input=input_text,
        tokens=tokens,
        keywords=keywords,
        patterns=patterns
    )
    
    # Classify
    intent = self.classify_intent(partial)
    domain = self.identify_domain(partial)
    
    # Calculate complexity
    complexity = self.calculate_complexity(partial)
    
    # Build complete context
    return Context(
        raw_input=input_text,
        tokens=tokens,
        keywords=keywords,
        patterns=patterns,
        intent=intent,
        domain=domain,
        complexity=complexity,
        confidence=self.calculate_confidence(partial),
        metadata=self.extract_metadata(partial)
    )
```

## Learning Component

The Context Analyzer learns from usage:

```python
class ContextLearner:
    """Learn to better analyze context"""
    
    def learn_from_feedback(self, context: Context, feedback: Feedback):
        """Update models based on feedback"""
        if feedback.intent_correct:
            self.intent_model.reinforce(context, context.intent)
        else:
            self.intent_model.correct(context, feedback.correct_intent)
            
        if feedback.domain_correct:
            self.domain_model.reinforce(context, context.domain)
        else:
            self.domain_model.correct(context, feedback.correct_domain)
```

## Configuration

```yaml
context_analyzer:
  keyword_threshold: 0.5
  pattern_confidence_threshold: 0.7
  max_keywords: 20
  stopwords_file: "config/stopwords.txt"
  domain_vocabularies: "config/domains/"
  intent_model: "models/intent_classifier.pkl"
```

## Context Types

Common context types detected:

- **Programming**: Code questions, debugging, architecture
- **Creative**: Writing, brainstorming, ideation
- **Technical Support**: Troubleshooting, how-to questions
- **Conversation**: Casual chat, discussions
- **Learning**: Explanations, tutorials, concepts
- **Analysis**: Data analysis, research, investigation

## Events

Context Analyzer emits:
- `context_analyzed` - Analysis complete
- `domain_detected` - Domain identified
- `intent_classified` - Intent determined
- `pattern_found` - Significant pattern detected

## Integration

- **Cognitive Controller** uses context for decisions
- **Module Registry** finds modules for context
- **Identity Manager** adapts behavior to context
- **Learning System** improves analysis over time

## Next Steps

- See [Pattern Detector](pattern_detector.md) for pattern details
- See [Intent Classifier](intent_classifier.md) for intent classification
- See [Domain Identifier](domain_identifier.md) for domain detection
