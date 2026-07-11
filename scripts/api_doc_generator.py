#!/usr/bin/env python3
"""CLI: api-doc-generator

Api Doc Generator
"""
import sys, json, argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Api Doc Generator")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()
    result = {"tool": "api-doc-generator", "description": "Api Doc Generator", "version": "1.0.0", "author": "Jose Zuma", "timestamp": datetime.utcnow().isoformat() + "Z"}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result[chr(39)+chr(39)+chr(39)+chr(39)+chr(39)+chr(39)+chr(39)+chr(39)]}")

if __name__ == "__main__":
    main()
