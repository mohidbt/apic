#!/bin/bash
# Export current production specs to JSON for backup/migration
#
# Usage:
#   ./backend/scripts/export_specs.sh
#
# Output:
#   backup-specs-YYYYMMDD.json

# Configuration
API_URL="${API_URL:-https://api-ingest.com}"
OUTPUT_FILE="backup-specs-$(date +%Y%m%d-%H%M%S).json"

echo "Exporting specs from $API_URL..."
echo "Output file: $OUTPUT_FILE"

# Export all specs (increase limit if you have more than 1000)
curl -s "${API_URL}/api/specs?limit=1000" > "$OUTPUT_FILE"

# Check if export was successful
if [ $? -eq 0 ] && [ -s "$OUTPUT_FILE" ]; then
    SPEC_COUNT=$(grep -o '"total":[0-9]*' "$OUTPUT_FILE" | head -1 | cut -d':' -f2)
    echo "✅ Successfully exported $SPEC_COUNT specs"
    echo "📁 Saved to: $OUTPUT_FILE"
else
    echo "❌ Export failed"
    rm -f "$OUTPUT_FILE"
    exit 1
fi
