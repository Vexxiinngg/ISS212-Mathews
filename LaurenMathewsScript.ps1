# SP25 - ISS 212 Week 4 Tool Dev 2
# Works Cited - Jenn Moody
# Tool Dev Scenario 3

Write-Host "Current Execution Policy: $(Get-ExecutionPolicy)"
if ((Get-ExecutionPolicy) -in "Unrestricted", "Bypass") {
    Write-Host "WARNING: Your execution policy allows all scripts to run. Ensure you trust the source."
} elseif ((Get-ExecutionPolicy) -eq "Restricted") {
    Write-Host "Scripts cannot be executed on this system."
}

# SP25 - ISS 212 Week 4 Tool Dev 2
# Works Cited - Jenn Moody
# Tool Dev Scenario 4

if (([System.Security.Principal.WindowsIdentity]::GetCurrent()).Groups -contains "S-1-5-32-544") {
    Write-Host "Administrator Privileges: Yes"
} else {
    Write-Host "Administrator Privileges: No"
}

# SP25 - ISS 212 Week 4 Tool Dev 2
# Works Cited - Jen Moody
# Tool Dev Scenario 5

Write-Host "Username: $env:USERNAME"
Write-Host "User Domain: $env:USERDOMAIN"
Write-Host "Computer Name: $env:COMPUTERNAME"
Write-Host "System Path: $env:Path"

# SP25 - ISS 212 Week 4 Tool Dev 2
# Works Cited - Jenn Moody
# Tool Dev Scenario 6

$ip = Read-Host "Enter IP Address"
$ports = @(22, 80, 443)
foreach ($port in $ports) {
    $result = Test-NetConnection -ComputerName $ip -Port $port -WarningAction SilentlyContinue
    if ($result.TcpTestSucceeded) {
        Write-Host "Port $($port): OPEN"
    } else {
        Write-Host "Port $($port): CLOSED"
    }
}