#!/usr/bin/env python3
"""
Simple test script to validate the converter output.
"""

import json
import sys
from pathlib import Path


def test_tools_json(tools_path: Path):
    """Validate tools.json structure."""
    print("🧪 Testing tools.json...")
    
    with open(tools_path) as f:
        api = json.load(f)
    
    # Check required top-level fields
    assert 'api_name' in api, "Missing api_name"
    assert 'version' in api, "Missing version"
    assert 'servers' in api, "Missing servers"
    assert 'auth' in api, "Missing auth"
    assert 'tools' in api, "Missing tools"
    assert 'components' in api, "Missing components"
    
    print(f"  ✓ API: {api['api_name']} v{api['version']}")
    print(f"  ✓ Servers: {len(api['servers'])} server(s)")
    print(f"  ✓ Auth type: {api['auth']['type']}")
    print(f"  ✓ Tools: {len(api['tools'])} endpoint(s)")
    
    # Check each tool
    for tool in api['tools']:
        assert 'name' in tool, f"Tool missing name"
        assert 'description' in tool, f"Tool {tool.get('name')} missing description"
        assert 'parameters' in tool, f"Tool {tool['name']} missing parameters"
        assert 'returns' in tool, f"Tool {tool['name']} missing returns"
        assert 'x-http' in tool, f"Tool {tool['name']} missing x-http"
        assert 'examples' in tool, f"Tool {tool['name']} missing examples"
        
        # Validate x-http
        x_http = tool['x-http']
        assert 'method' in x_http, f"Tool {tool['name']} missing method"
        assert 'path_template' in x_http, f"Tool {tool['name']} missing path_template"
        assert 'arg_mapping' in x_http, f"Tool {tool['name']} missing arg_mapping"
        assert 'auth_required' in x_http, f"Tool {tool['name']} missing auth_required"
        
        # Validate parameters schema
        params = tool['parameters']
        assert params.get('type') == 'object', f"Tool {tool['name']} parameters must be object type"
        assert '$schema' in params, f"Tool {tool['name']} parameters missing $schema"
        
        # Check that all required params are in properties
        required = params.get('required', [])
        properties = params.get('properties', {})
        for req in required:
            assert req in properties, f"Tool {tool['name']}: required param '{req}' not in properties"
        
        # Check that all path params are in arg_mapping
        path = x_http['path_template']
        import re
        path_params = re.findall(r'\{(\w+)\}', path)
        for param in path_params:
            assert param in x_http['arg_mapping'], f"Tool {tool['name']}: path param '{param}' not in arg_mapping"
            assert x_http['arg_mapping'][param]['in'] == 'path', f"Tool {tool['name']}: path param '{param}' should be in 'path'"
    
    print(f"  ✓ All {len(api['tools'])} tools validated")
    print("")


def test_docs_md(docs_path: Path):
    """Validate docs.md structure."""
    print("🧪 Testing docs.md...")
    
    with open(docs_path) as f:
        content = f.read()
    
    # Check key sections exist
    assert '# ' in content, "Missing title"
    assert '## Base URLs' in content, "Missing Base URLs section"
    assert '## Authentication' in content, "Missing Authentication section"
    assert '## Endpoints' in content, "Missing Endpoints section"
    
    # Check for curl examples
    assert '```bash' in content, "Missing bash code blocks"
    assert 'curl' in content, "Missing curl examples"
    
    print(f"  ✓ Document size: {len(content):,} characters")
    print(f"  ✓ Contains curl examples")
    print(f"  ✓ All required sections present")
    print("")


def test_chunks_jsonl(chunks_path: Path):
    """Validate chunks.jsonl structure."""
    print("🧪 Testing chunks.jsonl...")
    
    chunks = []
    with open(chunks_path) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            
            try:
                chunk = json.loads(line)
                chunks.append(chunk)
                
                # Validate chunk structure
                assert 'id' in chunk, f"Line {line_num}: missing id"
                assert 'tag' in chunk, f"Line {line_num}: missing tag"
                assert 'method' in chunk, f"Line {line_num}: missing method"
                assert 'path' in chunk, f"Line {line_num}: missing path"
                assert 'text' in chunk, f"Line {line_num}: missing text"
                assert 'meta' in chunk, f"Line {line_num}: missing meta"
                
                # Check text size
                text_len = len(chunk['text'])
                assert text_len > 0, f"Line {line_num}: empty text"
                assert text_len <= 800, f"Line {line_num}: text too long ({text_len} > 800)"
                
            except json.JSONDecodeError as e:
                raise AssertionError(f"Line {line_num}: invalid JSON - {e}")
    
    print(f"  ✓ Total chunks: {len(chunks)}")
    print(f"  ✓ All chunks are valid JSON")
    print(f"  ✓ Text sizes: {min(len(c['text']) for c in chunks)}-{max(len(c['text']) for c in chunks)} chars")
    print("")


def main():
    """Run all tests."""
    if len(sys.argv) < 2:
        print("Usage: python3 test.py <output-directory>")
        print("\nExample:")
        print("  python3 test.py example-output")
        sys.exit(1)
    
    output_dir = Path(sys.argv[1])
    
    if not output_dir.exists():
        print(f"❌ Output directory not found: {output_dir}")
        sys.exit(1)
    
    print(f"Testing output in: {output_dir}\n")
    
    try:
        # Test each artifact
        test_tools_json(output_dir / "tools.json")
        test_docs_md(output_dir / "docs.md")
        test_chunks_jsonl(output_dir / "chunks.jsonl")
        
        print("✅ All tests passed!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"\n❌ File not found: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

