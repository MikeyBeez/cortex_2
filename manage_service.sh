#!/bin/bash
# /Users/bard/Code/cortex_2/manage_service.sh

PLIST_NAME="com.mikeybee.cortex2"
PLIST_FILE="/Users/bard/Code/cortex_2/com.mikeybee.cortex2.plist"
LAUNCHD_PATH="$HOME/Library/LaunchAgents/$PLIST_NAME.plist"

case "$1" in
    install)
        echo "Installing Cortex_2 service..."
        # Create logs directory
        mkdir -p /Users/bard/Code/cortex_2/logs
        
        # Copy plist to LaunchAgents
        cp "$PLIST_FILE" "$LAUNCHD_PATH"
        
        # Load the service
        launchctl load "$LAUNCHD_PATH"
        echo "Service installed and started"
        ;;
        
    uninstall)
        echo "Uninstalling Cortex_2 service..."
        # Unload the service
        launchctl unload "$LAUNCHD_PATH"
        
        # Remove plist
        rm -f "$LAUNCHD_PATH"
        echo "Service uninstalled"
        ;;
        
    start)
        echo "Starting Cortex_2 service..."
        launchctl start "$PLIST_NAME"
        ;;
        
    stop)
        echo "Stopping Cortex_2 service..."
        launchctl stop "$PLIST_NAME"
        ;;
        
    restart)
        echo "Restarting Cortex_2 service..."
        launchctl stop "$PLIST_NAME"
        sleep 2
        launchctl start "$PLIST_NAME"
        ;;
        
    status)
        echo "Cortex_2 service status:"
        launchctl list | grep "$PLIST_NAME"
        ;;
        
    logs)
        echo "=== Cortex_2 Logs ==="
        tail -f /Users/bard/Code/cortex_2/logs/cortex.log
        ;;
        
    errors)
        echo "=== Cortex_2 Error Logs ==="
        tail -f /Users/bard/Code/cortex_2/logs/cortex-error.log
        ;;
        
    *)
        echo "Usage: $0 {install|uninstall|start|stop|restart|status|logs|errors}"
        exit 1
        ;;
esac
