#!/usr/bin/env python3
"""Cortex CLI interface"""
import click

@click.group()
def cli():
    """Cortex_2 Cognitive Operating System"""
    pass

@cli.command()
def module():
    """Module management commands"""
    click.echo("Module commands coming soon...")

@cli.command()
def server():
    """Start Cortex server"""
    click.echo("Starting Cortex server...")

def main():
    cli()

if __name__ == "__main__":
    main()
