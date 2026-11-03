# BizAI Hub - GitHub Push & Pages Helper Script
# Usage in PowerShell: .\push_to_github.ps1 -RepoUrl "https://github.com/<your-username>/bizai-hub.git"

param (
    [Parameter(Mandatory=$false)]
    [string]$RepoUrl = ""
)

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  BizAI Hub - GitHub Push & Pages Automation" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

# 1. Run local validation first
Write-Host "`n[Step 1] Running automated tests before push..." -ForegroundColor Yellow
python tools/validate_site.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "`n[ERROR] Automated validation failed! Please fix issues before pushing." -ForegroundColor Red
    exit 1
}

# 2. Rename branch to main
git branch -M main

# 3. Check / prompt for remote URL
$existingRemote = git remote get-url origin 2>$null
if (-not $RepoUrl) {
    if ($existingRemote) {
        $RepoUrl = $existingRemote
        Write-Host "`nFound existing origin remote: $RepoUrl" -ForegroundColor Green
    } else {
        $RepoUrl = Read-Host "`nEnter your GitHub Repository URL (e.g., https://github.com/<username>/bizai-hub.git)"
    }
}

if (-not $RepoUrl) {
    Write-Host "[ERROR] Repository URL is required to push to GitHub." -ForegroundColor Red
    exit 1
}

# Set remote origin
if ($existingRemote) {
    git remote set-url origin $RepoUrl
} else {
    git remote add origin $RepoUrl
}

# 4. Push to GitHub
Write-Host "`n[Step 2] Pushing code to GitHub ($RepoUrl)..." -ForegroundColor Yellow
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n============================================================" -ForegroundColor Green
    Write-Host "  SUCCESS! Code pushed to GitHub." -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host "`nTo enable GitHub Pages:" -ForegroundColor Cyan
    Write-Host "1. Go to your GitHub repo Settings -> Pages"
    Write-Host "2. Under 'Build and deployment', set Source to 'Deploy from a branch'"
    Write-Host "3. Set Branch to 'main' and folder to '/ (root)', then click Save."
    Write-Host "4. Your site will be live at: https://<username>.github.io/<repo-name>/" -ForegroundColor Yellow
} else {
    Write-Host "`n[ERROR] Git push failed. Please check your GitHub permissions or token." -ForegroundColor Red
}
