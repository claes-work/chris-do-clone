# Download English captions (manual preferred, auto fallback) for a video into raw/youtube/.
# Usage: .\tools\fetch_captions.ps1 -VideoUrl "https://www.youtube.com/watch?v=..." -Channel "channelhandle"
# Produces raw/youtube/<channel>/<upload_date>-<id>.<lang>.vtt — convert with tools/vtt_to_text.py.
param(
    [Parameter(Mandatory = $true)][string]$VideoUrl,
    [Parameter(Mandatory = $true)][string]$Channel
)

yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs 'en.*' --sub-format vtt `
    -o "raw/youtube/$Channel/%(upload_date>%Y-%m-%d)s-%(id)s.%(ext)s" $VideoUrl
