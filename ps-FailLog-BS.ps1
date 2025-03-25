# ISS 212 CS Scripting - WK 8 TD 6- PowerShell - Event Log Monitoring
# PS script using Regex -- Redacting data using pattern matching
#

'''
.DESCRIPTION
Add Lauren Mathews and 3/24/25 to the first comment line.
ISS 212 - CS Scripting - PowerShell Script: ps-FailLog.ps1
Citations: Jen Moody

.PURPOSE
Week 8 PS script using Regex to match IP data using regex.

.USAGE
Run script from file with command or from terminal. | .\ps-FailLog.ps1
'''

# Week 8 PS script using Regex -- extracting data using regex

# Looking for any failed log in attempts  in the log file and matches the IP address to the failed attempt
$logFile = "security.log"
$failedAttempts = Select-String -Path $logFile -Pattern "Login attempt failed from IP (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" -AllMatches

# Counts the number of failed attempts from the IP addresses it finds and adds up the attempts
$ipCounts = @{}
foreach ($match in $failedAttempts) {
    $ip = $match.Matches.Groups[1].Value
    if ($ipCounts.ContainsKey($ip)) {
        $ipCounts[$ip] += 1
    } else {
        $ipCounts[$ip] = 1
    }
}

# Counts the number of attempts and if there are more than 3 attempts it tells you there is a potentially malicious IP
Write-Host "Potentially Malicious IPs:"
foreach ($ip in $ipCounts.Keys) {
    if ($ipCounts[$ip] -gt 3) {
        Write-Host "$ip has $($ipCounts[$ip]) failed login attempts"
    }
}