# Enumerate all videos of a YouTube channel/playlist into ledger-shaped CSV rows.
# Usage: .\tools\fetch_channel.ps1 -Url "https://www.youtube.com/@ChannelHandle/videos" -Out "pipeline\staging-channelhandle.csv"
# Review the staging file, then merge into pipeline/ledger.csv (dedup by id).
# Note: flat-playlist listings may lack upload_date on some channels; refine per
# channel in Phase 3 (fallback: a second metadata pass on the video IDs).
param(
    [Parameter(Mandatory = $true)][string]$Url,
    [Parameter(Mandatory = $true)][string]$Out
)

# Non-ASCII in titles (curly quotes, em dashes, emoji) must survive the yt-dlp -> pipe
# -> PowerShell hop. Two ends to fix: (1) yt-dlp's own `--encoding utf-8` forces it to
# WRITE UTF-8 instead of the lossy Windows console codepage (PYTHONIOENCODING/PYTHONUTF8
# are NOT honored here — verified: they still emit U+FFFD for U+2019); (2) make
# PowerShell DECODE the native stdout as UTF-8.
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

$today = Get-Date -Format 'yyyy-MM-dd'
$rows = yt-dlp --encoding utf-8 --flat-playlist --print '%(id)s;%(title)s;%(upload_date>%Y-%m-%d|NA)s;%(duration|0)s;%(view_count|0)s;%(channel|NA)s' $Url

$csv = foreach ($r in $rows) {
    $p = $r -split ';', 6
    $title = $p[1] -replace '"', "'"
    $dur = 0; [void][int]::TryParse($p[3], [ref]$dur)  # duration may be "NA"; treat as 0
    $isShort = if ($dur -gt 0 -and $dur -le 62) { 'short' } else { 'video' }
    # id,type,title,channel_or_publisher,url,published,discovered,status,priority,domains,notes
    "yt-$($p[0]),$isShort,""$title"",$($p[5]),https://www.youtube.com/watch?v=$($p[0]),$($p[2]),$today,L0-discovered,3,,views=$($p[4])"
}

@('id,type,title,channel_or_publisher,url,published,discovered,status,priority,domains,notes') + $csv |
    Set-Content -Path $Out -Encoding utf8
Write-Host "$($csv.Count) items -> $Out"
