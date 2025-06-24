---
title: "Helping My Daughter Learn French with Films"
date: 2025-05-27
description: "From Disney to documentaries — how we use films, subtitles, and a bit of tech to make French fun at home."
tags: ["language learning", "french", "movies", "cartoons", "plex", "subtitles", "home server"]
categories: ["Blog"]
category: "Blog"
ShowToc: true
comments: true
showBreadcrumbs: true
cover:
  image: "/images/french-films-cover.png"  # <- путь к картинке
  alt: "French learning with movies"
  hidden: false
---

## Introduction

We’re a family from Ukraine who has been living in France for the past three years. My daughter is 9 years old and already speaks French quite well — she attends school here and communicates confidently with her classmates.

Still, I wanted to immerse her even deeper into the language in a way that feels natural and fun. That's how I came up with a simple idea: learning French through watching movies, cartoons, and TV series together.

<code>But there’s a catch.</code> In France, even when you find the film you want — say, Avatar — it’s often impossible to get Ukrainian or Russian subtitles. Sometimes even Japanese subs are available, but not ours. As a bilingual Ukrainian family, we mostly use Russian or Ukrainian at home, and having subtitles in those languages would make it much easier for our daughter to follow along.

Watching animated films like The Lion King with French subtitles already helps a lot — when she doesn't understand something by ear, she can still read it. But with more complex movies, full of new vocabulary and fast dialogue, it's much harder to follow — so I needed to find a better solution.

## The Solution I Came Up With

After some experimenting, I found a practical and flexible way to make movies and cartoons a true part of our language learning routine — even with subtitle limitations in France.

The idea was simple: get a Blu-ray drive that could read both Blu-ray and DVD discs, and use it to back up the films we own onto our PC. Once a movie is saved locally, I can look for subtitles — in French, Ukrainian, or Russian — and either embed them directly into the video or keep them as separate `.srt` files.

From there, we have two options:
- **Option 1:** Use [Plex](https://www.plex.tv/) on the PC to stream the movie over our local network to the TV or any Android TV box.
- **Option 2:** Copy the final movie file (with subtitles or not) to a USB stick and watch it directly through a media player like [VLC](https://www.videolan.org/vlc/) on the TV.


In most cases, I don’t even need to embed the subtitles permanently — just placing the `.srt` file next to the movie works fine. VLC and other media players can pick it up automatically or let us choose which subtitles to load.

This method gives us full control:
- We can use any subtitles we find or create
- We can switch languages on the fly
- We can pause, rewind, or rewatch tricky parts
- And best of all — it doesn’t rely on internet streaming platforms or region-specific limitations

## Equipment You’ll Need

💼 To set up this workflow, you’ll need the following hardware and software:

### External Blu-ray Drive

We’re using the **USB 3.0 External Blu-ray Drive Portable 3D BD-Combo** — a budget-friendly external drive that supports Blu-ray, DVD, and CD reading. It works on both Windows and Mac and is one of the most affordable options we could find.
➡️ [View it on AliExpress](https://www.aliexpress.com/item/1005007633897719.html?spm=a2g0o.order_list.order_list_main.5.56771802grrM2E)

If you prefer something from a more well-known brand, you can look into models on Amazon, but be prepared to pay 2–3× more.

### Software Tools

- [**MakeMKV**](https://www.makemkv.com/) — to rip Blu-ray or DVD content to your PC in high quality. Simple, powerful, and often free in beta.
- [**VLC Media Player**](https://www.videolan.org/vlc/) — to test and play back videos with external or embedded subtitles.
- [**MKVToolNix**](https://mkvtoolnix.download/) — to add or edit subtitle tracks inside MKV files.
- [**OpenSubtitles**](https://www.opensubtitles.org/){ target="_blank" rel="noopener" } — to search and download subtitles in languages like French, Ukrainian, and Russian.

This toolkit gives you complete control over your film library and helps tailor content for a rich, multilingual learning experience.



## How to Add Subtitles (Step-by-Step)

🎞️ Let’s walk through the full process of adding subtitles to a movie — from finding them to embedding them — using *Man of Steel (Zack Snyder)* as an example.

### 1. Find the Right Subtitles

To start, you’ll need subtitle files that match the **exact version** of your movie (resolution, frame rate, extended/director’s cut, etc.). The most common format is `.srt`.

🗂️ Here are reliable subtitle sources:

- [**OpenSubtitles.org**](https://www.opensubtitles.org/)
- [**Subscene.com**](https://subscene.com/)
- [**Addic7ed.com**](https://www.addic7ed.com/)

💡 **Tip:** Search by full movie title and year. For our example:


---

### 2. Test with VLC Media Player

Before embedding, make sure the subtitle file syncs well with the video.

1. Open the video in [**VLC**](https://www.videolan.org/vlc/).
2. Drag the `.srt` file into the playing video window.
3. Use `Shift + H/J` to sync the subtitles if needed.

💡 If you don’t want to permanently embed subtitles, just keeping the `.srt` file in the same folder (with the same name as the video file) will often be enough — especially when using VLC or Plex.

---

### 3. Embed Subtitles with MKVToolNix

If you want your subtitles to always stay with the movie (e.g., for use on TVs, USB sticks, Plex), you can embed them directly into the video file using [**MKVToolNix**](https://mkvtoolnix.download/).

Here’s how:

1. Open `MKVToolNix GUI`.
2. Drag your `.mkv` movie into the window.
3. Drag your `.srt` file into the same window — it will appear as a new track.
4. (Optional) Set language metadata (e.g., "fre" for French, "ukr" for Ukrainian).
5. (Optional) Check the “Default track” box if you want this subtitle to appear by default.
6. Choose output filename and click **Start multiplexing**.

💡 Your new `.mkv` file will now include the subtitle track.

---

### 4. Watch with Plex or VLC

Now that your movie has subtitles embedded (or placed next to it), you can enjoy it on almost any device.

🖥️ On PC: use **VLC** to play locally — it will show embedded or external subtitles.

📺 On TV: copy the movie to a USB stick or stream via **[Plex](https://www.plex.tv/)**. Plex supports both embedded and external subtitle files and is great for browsing your library with metadata.

---

## Conclusion: Learn Languages Through Movies

🌍 This method isn’t limited to French — you can use it to expose your child (or yourself) to almost **any language**. Just find subtitles in the language you want to learn and pair them with high-quality, engaging content.

🎬 **Animated movies** from studios like **Disney**, **Pixar**, **DreamWorks**, or **Studio Ghibli** are especially effective for younger learners. The language is simpler, more expressive, and visually supported.

✅ Whether you embed the subtitles or keep them as separate files, this setup allows you to:

- Learn vocabulary and sentence structure from native content.
- Read along while listening, boosting comprehension.
- Watch together as a family, combining fun with education.

💬 **Have questions or want help with subtitles?** Feel free to leave a comment below — I’ll try to help!


