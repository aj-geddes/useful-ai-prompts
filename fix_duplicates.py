#!/usr/bin/env python3
"""
Script to remove duplicate headings from converted files
"""
import os
import re
from pathlib import Path

def fix_duplicate_headings(file_path):
    """Remove duplicate headings from converted files"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find duplicate headings like:
    # # Title
    # ## Metadata
    # ...
    # 
    # # Title (duplicate)
    pattern = r'(# [^\n]+)\n\n## Metadata.*?\n\n## Description[^\n]*\n\n\n# \1'
    
    # More specific pattern for our case
    lines = content.split('\n')
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # If we find a heading that starts with #
        if line.startswith('# ') and new_lines:
            # Check if this is a duplicate of the first heading
            first_heading = None
            for prev_line in new_lines:
                if prev_line.startswith('# '):
                    first_heading = prev_line
                    break
            
            # If we found the same heading again, skip it and the empty line after
            if first_heading and line == first_heading:
                i += 1  # Skip the duplicate heading
                # Skip the empty line after if it exists
                if i < len(lines) and lines[i] == '':
                    i += 1
                continue
        
        new_lines.append(line)
        i += 1
    
    new_content = '\n'.join(new_lines)
    
    # Write back if content changed
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, "Fixed duplicate heading"
    
    return False, "No changes needed"

def main():
    """Fix duplicate headings in converted files"""
    converted_files = [
        # Space economy files that were converted
        'prompts/space-economy/satellite-constellation-operations-manager.md',
        'prompts/space-economy/launch-campaign-management-expert.md',
        'prompts/space-economy/spacecraft-development-and-payload-integration-expert.md',
        'prompts/space-economy/commercial-space-mission-architecture-expert.md',
        'prompts/space-economy/space-technology-development-innovation-manager.md',
        
        # Supply chain files
        'prompts/supply-chain/sustainable-supply-chain-management-expert.md',
        'prompts/supply-chain/digital-supply-chain-transformation-expert.md',
        'prompts/supply-chain/supply-chain-excellence-director.md',
        'prompts/supply-chain/supply-chain-resilience-strategy-expert.md',
        
        # Blockchain files
        'prompts/blockchain/enterprise-blockchain-integration-expert.md',
        'prompts/blockchain/defi-protocol-development-expert.md',
        'prompts/blockchain/decentralized-autonomous-organization-expert.md',
        'prompts/blockchain/cross-chain-interoperability-expert.md',
        'prompts/blockchain/smart-contract-security-audit-expert.md',
        
        # Government files
        'prompts/government/digital-government-transformation-expert.md',
        'prompts/government/citizen-service-experience-designer.md',
        'prompts/government/smart-city-platform-development-expert.md',
        'prompts/government/digital-identity-platform-architect.md',
        'prompts/government/government-api-strategy-expert.md',
        
        # Healthcare digital files
        'prompts/healthcare-digital/healthcare-ai-implementation-expert.md',
        'prompts/healthcare-digital/medical-device-ai-integration-expert.md',
        'prompts/healthcare-digital/telehealth-platform-development-expert.md',
        'prompts/healthcare-digital/patient-data-analytics-expert.md',
        'prompts/healthcare-digital/digital-health-transformation-strategist.md',
        
        # Quantum computing files
        'prompts/quantum-computing/quantum-hardware-characterization-expert.md',
        'prompts/quantum-computing/quantum-algorithm-development-expert.md',
        'prompts/quantum-computing/quantum-cryptography-protocol-expert.md',
        'prompts/quantum-computing/fault-tolerant-quantum-computing-expert.md',
        'prompts/quantum-computing/quantum-machine-learning-development-expert.md'
    ]
    
    for file_path in converted_files:
        if os.path.exists(file_path):
            changed, message = fix_duplicate_headings(file_path)
            print(f"{file_path}: {message}")
        else:
            print(f"{file_path}: File not found")

if __name__ == '__main__':
    main()