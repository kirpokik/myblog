---
title: "Hugo Site Deployment with GitHub Actions"
date: 2025-06-24
description: "Learn how to automate the deployment of your Hugo static site to an FTP hosting provider using GitHub Actions"
tags: ["hugo", "deployment", "github", "ftp", "automation", "web dev"]
categories: ["build-log", "project-journal"]
category: "Code Notes"
comments: true
ShowToc: true
---

Deploying a static site manually every time can be a boring and error-prone task. If you're using [Hugo](https://gohugo.io/), a static site generator, and host your site with a provider like [Hostinger](https://www.hostinger.com/), you might be used to generating the site with `hugo` and dragging the contents of the `public/` folder into a file manager or FTP client.

Let’s change that.

In this guide, I’ll show you how to automate this process using **GitHub Actions**. Every time you push to your `main` branch, your site will be automatically built and uploaded to your server via FTP.

### What You Need

- A Hugo project
- GitHub repository
- FTP access to your server (e.g. Hostinger)
- GitHub Actions enabled

###  Initialize a GitHub Repository

Create a new GitHub repository and push your Hugo project to it.

Make sure to exclude the `/public` folder from version control. Create a `.gitignore` file with this content:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Add GitHub Secrets

Go to your GitHub repository:

`Settings → Secrets and variables → Actions → New repository secret`

Add the following secrets related to your FTP connection:

| Secret Name       | Description                     | Example                        |
|-------------------|---------------------------------|-------------------------------|
| `FTP_SERVER`      | Your FTP server address          | `ftp.yourhost.com`             |
| `FTP_USERNAME`    | Your FTP username                | `user123`                     |
| `FTP_PASSWORD`    | Your FTP password                | `yourpassword`                |
| `FTP_PORT`        | FTP port (optional, default 21) | `21`                          |
| `FTP_REMOTE_PATH` | Remote path to upload files      | `/public_html/your-site/`      |

You can find these credentials in your hosting control panel (Hostinger: Hosting → FTP Accounts).

### Create GitHub Action Workflow
Create a new workflow file in your Hugo project:

```bash
mkdir -p .github/workflows
touch .github/workflows/deploy.yml
```
Then, open the `deploy.yml` file and paste the following configuration:

```bash
name: Deploy Hugo site to FTP

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.146.0'

      - name: Build site
        run: hugo --minify

      - name: Upload to FTP
        uses: SamKirkland/FTP-Deploy-Action@v4.3.4
        with:
          server: ${{ secrets.FTP_SERVER }}
          username: ${{ secrets.FTP_USERNAME }}
          password: ${{ secrets.FTP_PASSWORD }}
          local-dir: ./public
```

> ✅ Now, whenever you push changes to the `main` branch, GitHub will build your site and upload it to your server via FTP — fully automated.

### Update and Deploy with One Command

Any time you update your site locally — whether it's fixing a typo or publishing a new post — just run:

```bash
git add .
git commit -m "Update: new article"
git push origin main
```
<p align="center">
  <img src="/images/build-hugo.png" alt="Subtitle delay example in VLC" style="max-width: 100%;">
  <img src="/images/build-hugo-2.png" alt="Subtitle delay example in VLC" style="max-width: 100%;">
</p>

GitHub will take care of the rest: build, FTP upload, and you're live.

### Conclusion
The deployment process usually takes just a couple of minutes. Any changes you make locally — whether editing code or adding a new post — will automatically be uploaded after running a single command. It’s fast and convenient.

Another benefit is that your website’s source code is safely stored on GitHub. If your computer crashes or you need to recover your project, everything is backed up and easily accessible.

This setup is ideal if you're hosting your site on [Hostinger](https://www.hostinger.com/) or a similar provider. If you're using [Vercel](https://vercel.com/), the process is different — Vercel handles deployments automatically without any extra configuration. I’ll cover the full migration from Hostinger to Vercel in my next article.
And the main reason for switching? Cost. While Hostinger’s most basic plan costs around €4–5 per month, Vercel is completely free and perfectly suited for small projects like a personal blog, portfolio, or simple landing page.
