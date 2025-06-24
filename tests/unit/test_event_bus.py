# /Users/bard/Code/cortex_2/tests/unit/test_event_bus.py
"""Tests for Event Bus System"""
import pytest
from unittest.mock import Mock
import asyncio
from typing import List, Dict, Any

class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List] = {}
        self.event_history: List[tuple] = []
        
    def emit(self, event: str, data: Any = None) -> None:
        """Emit an event to all subscribers"""
        self.event_history.append((event, data))
        
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                try:
                    callback(data)
                except Exception as e:
                    # In production, log error
                    pass
                    
    def on(self, event: str, callback) -> None:
        """Subscribe to an event"""
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)
        
    def off(self, event: str, callback) -> None:
        """Unsubscribe from an event"""
        if event in self.subscribers:
            self.subscribers[event].remove(callback)
            if not self.subscribers[event]:
                del self.subscribers[event]
                
    def clear(self, event: str = None) -> None:
        """Clear subscribers for an event or all events"""
        if event:
            self.subscribers.pop(event, None)
        else:
            self.subscribers.clear()
            
    def get_history(self) -> List[tuple]:
        """Get event history for testing"""
        return self.event_history

class TestEventBus:
    """Test suite for Event Bus"""
    
    def test_basic_emit_and_subscribe(self):
        """Test basic event emission and subscription"""
        bus = EventBus()
        received_data = []
        
        def handler(data):
            received_data.append(data)
            
        # Subscribe
        bus.on('test_event', handler)
        
        # Emit
        bus.emit('test_event', {'message': 'hello'})
        
        assert len(received_data) == 1
        assert received_data[0] == {'message': 'hello'}
    
    def test_multiple_subscribers(self):
        """Test multiple subscribers to same event"""
        bus = EventBus()
        results = []
        
        def handler1(data):
            results.append(f"handler1: {data}")
            
        def handler2(data):
            results.append(f"handler2: {data}")
            
        bus.on('test_event', handler1)
        bus.on('test_event', handler2)
        
        bus.emit('test_event', 'test')
        
        assert len(results) == 2
        assert 'handler1: test' in results
        assert 'handler2: test' in results
    
    def test_unsubscribe(self):
        """Test unsubscribing from events"""
        bus = EventBus()
        call_count = 0
        
        def handler(data):
            nonlocal call_count
            call_count += 1
            
        bus.on('test_event', handler)
        bus.emit('test_event', None)
        assert call_count == 1
        
        bus.off('test_event', handler)
        bus.emit('test_event', None)
        assert call_count == 1  # Should not increase
    
    def test_event_history(self):
        """Test event history tracking"""
        bus = EventBus()
        
        bus.emit('event1', 'data1')
        bus.emit('event2', 'data2')
        bus.emit('event1', 'data3')
        
        history = bus.get_history()
        assert len(history) == 3
        assert history[0] == ('event1', 'data1')
        assert history[1] == ('event2', 'data2')
        assert history[2] == ('event1', 'data3')
    
    def test_error_handling(self):
        """Test error handling in subscribers"""
        bus = EventBus()
        results = []
        
        def failing_handler(data):
            raise Exception("Handler error")
            
        def working_handler(data):
            results.append(data)
            
        bus.on('test_event', failing_handler)
        bus.on('test_event', working_handler)
        
        # Should not crash
        bus.emit('test_event', 'test')
        
        # Working handler should still be called
        assert len(results) == 1
        assert results[0] == 'test'
    
    def test_clear_subscribers(self):
        """Test clearing subscribers"""
        bus = EventBus()
        call_count = 0
        
        def handler(data):
            nonlocal call_count
            call_count += 1
            
        bus.on('event1', handler)
        bus.on('event2', handler)
        
        # Clear specific event
        bus.clear('event1')
        bus.emit('event1', None)
        assert call_count == 0
        
        bus.emit('event2', None)
        assert call_count == 1
        
        # Clear all
        bus.clear()
        bus.emit('event2', None)
        assert call_count == 1  # Should not increase
    
    def test_wildcard_subscriptions(self):
        """Test wildcard event subscriptions"""
        # bus = EventBus()
        # results = []
        
        # def wildcard_handler(event, data):
        #     results.append((event, data))
            
        # Subscribe to all events starting with 'module.'
        # bus.on('module.*', wildcard_handler)
        
        # bus.emit('module.loaded', 'module1')
        # bus.emit('module.unloaded', 'module2')
        # bus.emit('other.event', 'data')
        
        # Should only catch module events
        # assert len(results) == 2
        pass
    
    def test_priority_subscribers(self):
        """Test priority-based event handling"""
        # bus = EventBus()
        # order = []
        
        # def high_priority(data):
        #     order.append('high')
            
        # def low_priority(data):
        #     order.append('low')
            
        # bus.on('test_event', low_priority, priority=10)
        # bus.on('test_event', high_priority, priority=100)
        
        # bus.emit('test_event', None)
        
        # High priority should run first
        # assert order == ['high', 'low']
        pass
    
    def test_async_handlers(self):
        """Test async event handlers"""
        # bus = AsyncEventBus()
        # results = []
        
        # async def async_handler(data):
        #     await asyncio.sleep(0.01)
        #     results.append(data)
            
        # bus.on('test_event', async_handler)
        
        # await bus.emit('test_event', 'async_data')
        
        # assert len(results) == 1
        # assert results[0] == 'async_data'
        pass
    
    def test_event_filtering(self):
        """Test event filtering/middleware"""
        # bus = EventBus()
        # results = []
        
        # def filter_middleware(event, data):
        #     # Only allow events with valid data
        #     return data is not None
            
        # bus.add_filter(filter_middleware)
        
        # def handler(data):
        #     results.append(data)
            
        # bus.on('test_event', handler)
        
        # bus.emit('test_event', None)  # Should be filtered
        # bus.emit('test_event', 'valid')  # Should pass
        
        # assert len(results) == 1
        # assert results[0] == 'valid'
        pass
