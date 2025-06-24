#!/bin/bash
# /Users/bard/Code/cortex_2/migrate_to_cortex2.sh

echo "=== Stopping all old services (Anna organs, Nexus, old Cortex) ==="

# List current services before stopping
echo "Current running services:"
launchctl list | grep -E "(cortex|nexus|anna)" | grep -v grep
echo ""

# Unload all Anna organ services
echo "Stopping Anna organs (O1-O5)..."
launchctl unload ~/Library/LaunchAgents/com.anna.o1.plist 2>/dev/null
launchctl unload ~/Library/LaunchAgents/com.anna.o2.plist 2>/dev/null
launchctl unload ~/Library/LaunchAgents/com.anna.o3.plist 2>/dev/null
launchctl unload ~/Library/LaunchAgents/com.anna.o4.plist 2>/dev/null
launchctl unload ~/Library/LaunchAgents/com.anna.o5.plist 2>/dev/null

# Unload Anna control center
echo "Stopping Anna control center..."
launchctl unload ~/Library/LaunchAgents/com.anna.control-center.plist 2>/dev/null

# Unload Anna startup
echo "Stopping Anna startup..."
launchctl unload ~/Library/LaunchAgents/com.mikeyb.anna.startup.plist 2>/dev/null

# Unload Nexus queue
echo "Stopping Nexus queue..."
launchctl unload ~/Library/LaunchAgents/com.nexus.queue.plist 2>/dev/null

# Remove all old plist files
echo ""
echo "Removing old plist files..."
rm -f ~/Library/LaunchAgents/com.anna.*.plist
rm -f ~/Library/LaunchAgents/com.mikeyb.anna.startup.plist
rm -f ~/Library/LaunchAgents/com.nexus.*.plist
rm -f ~/Library/LaunchAgents/com.mikeybee.cortex.plist

# Kill any remaining processes
echo ""
echo "Killing any remaining processes..."
pkill -f "anna" 2>/dev/null
pkill -f "nexus" 2>/dev/null
pkill -f "cortex" 2>/dev/null

# Wait for processes to stop
sleep 3

# Verify everything is stopped
echo ""
echo "Verifying all services are stopped..."
REMAINING=$(launchctl list | grep -E "(cortex|nexus|anna)" | grep -v "grep\|apple.nexusd" | wc -l)
if [ $REMAINING -eq 0 ]; then
    echo "✅ All old services successfully stopped"
else
    echo "⚠️  Warning: Some services may still be running:"
    launchctl list | grep -E "(cortex|nexus|anna)" | grep -v "grep\|apple.nexusd"
fi

echo ""
echo "=== Starting new Cortex_2 service ==="

# Go to cortex_2 directory
cd /Users/bard/Code/cortex_2

# Make scripts executable
chmod +x manage_service.sh

# Create logs directory
mkdir -p logs

# Install new service
echo "Installing Cortex_2 service..."
./manage_service.sh install

# Wait a moment for service to start
sleep 2

# Check status
echo ""
echo "Cortex_2 service status:"
./manage_service.sh status

echo ""
echo "=== Migration Complete! ==="
echo ""
echo "Old services stopped:"
echo "  - Anna organs (O1-O5)"
echo "  - Anna control center"
echo "  - Anna startup"
echo "  - Nexus queue"
echo ""
echo "New service started:"
echo "  - Cortex_2 (com.mikeybee.cortex2)"
echo ""
echo "Check logs with:"
echo "  tail -f /Users/bard/Code/cortex_2/logs/cortex.log"
echo ""
echo "Manage service with:"
echo "  make service-status"
echo "  make service-stop"
echo "  make service-start"
echo "  make service-logs"
