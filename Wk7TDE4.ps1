# Lauren Mathews
# Resources: ISS212 Week 7 Tool Development Exercise 4 walkthrough, Jen Moody, ChatGPT
#Week 7 Assignment Exercise 4

# Define the log file path if your log file is not in same folder as PS script.
[string]$logFilePath = "WK7LOG.txt"


# Check if the log file exists
if (-Not (Test-Path $logFilePath)) {
    Write-Host "Log file not found!"
    exit
}

# Read the log entries from the file
[string[]]$logEntries = Get-Content $logFilePath

# A Regular expression pattern for parsing logs
$logPattern = '^(?<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?<level>[A-Z]+)\] (?<ip>\d{1,3}(?:\.\d{1,3}){3}) - (?<message>.+)$'

# Initialize collections for data of the Log Level Breakdown
$logStats = @{ "INFO" = 0; "WARNING" = 0; "ERROR" = 0; "CRITICAL" = 0 }
$failedLogins = @()
$suspiciousActivity = @()

# Process each log entry with the timestamp, level, ip and message
foreach ($entry in $logEntries) {
    if ($entry -match $logPattern) {
        $timestamp = $matches['timestamp']
        $logLevel = $matches['level']
        $ipAddress = $matches['ip']
        $message = $matches['message']

        # Log Level Analysis
        if ($logStats.ContainsKey($logLevel)) {
            $logStats[$logLevel]++
        }

        # Promps script for A Suspicious Activity Report
        if ($message -match "brute force|permission denied|security alert") {
            $suspiciousActivity += "$timestamp | $ipAddress | $message"
        }
    }
}

# Output  the Log Level Analysis (Breakdown)
Write-Host "`n[Log Level Breakdown]"
$logStats.GetEnumerator() | Sort-Object Key | ForEach-Object { Write-Host "$($_.Key): $($_.Value)" }


# Recent Activity Extraction: Last 15 logs
Write-Host "`n[Last 35 Log Entries]"
if ($logEntries.Count -gt 0) {
    $logEntries | Select-Object -Last 35 | ForEach-Object { Write-Host $_ }
} else {
    Write-Host "No log entries found."
}

