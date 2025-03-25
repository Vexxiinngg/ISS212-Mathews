#! C:\Program Files\Git\bin\sh.exe

# ISS 212 CS Scripting - WK 8 TD 6 - Bash & Regex - IP Redaction
# Bash script using Regex -- Redacting data using pattern matching
#Add Lauren Mathews and 3/24/25 to the first comment line.
#Citations: Jen Moody

# Check for redacted IPs in the access log and paste them in the redacted log
sed -E 's/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/[REDACTED]/g' access.log > access_redacted.log

echo "Redacted IP addresses in access.log and saved as access_redacted.log"
