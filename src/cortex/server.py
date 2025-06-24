# /Users/bard/Code/cortex_2/src/cortex/server.py
"""Cortex_2 Server - Main service entry point"""
import asyncio
import signal
import sys
from pathlib import Path
import logging
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('cortex.server')

class CortexServer:
    """Main Cortex_2 server"""
    
    def __init__(self):
        self.running = False
        self.tasks = []
        
    async def start(self):
        """Start the server"""
        logger.info("Starting Cortex_2 server...")
        self.running = True
        
        # TODO: Initialize components
        # - Module Registry
        # - Context Analyzer
        # - Identity Manager
        # - Resource Monitor
        # - Learning System
        
        logger.info("Cortex_2 server started successfully")
        
        # Keep server running
        while self.running:
            await asyncio.sleep(1)
            
    async def stop(self):
        """Stop the server"""
        logger.info("Stopping Cortex_2 server...")
        self.running = False
        
        # Cancel all tasks
        for task in self.tasks:
            task.cancel()
            
        # Wait for tasks to complete
        await asyncio.gather(*self.tasks, return_exceptions=True)
        
        logger.info("Cortex_2 server stopped")
        
    def handle_signal(self, sig, frame):
        """Handle shutdown signals"""
        logger.info(f"Received signal {sig}")
        asyncio.create_task(self.stop())
        

async def main():
    """Main entry point"""
    server = CortexServer()
    
    # Set up signal handlers
    signal.signal(signal.SIGINT, server.handle_signal)
    signal.signal(signal.SIGTERM, server.handle_signal)
    
    try:
        await server.start()
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
    finally:
        await server.stop()

if __name__ == "__main__":
    # Ensure logs directory exists
    Path("/Users/bard/Code/cortex_2/logs").mkdir(exist_ok=True)
    
    # Run the server
    asyncio.run(main())
