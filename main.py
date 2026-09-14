"""Renders the animated terminal at the top of github.com/Aiza166.

Built with x0rzavi/github-readme-terminal (pip package: github-readme-terminal).

    python main.py            # renders output-dark.gif and output-light.gif, updates the README stamp
    python main.py dark       # one variant only (used internally)

Needs ffmpeg on PATH and GITHUB_TOKEN in the environment (for live GitHub stats).
Runs daily on GitHub Actions: .github/workflows/update.yml
"""

import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).parent
FONT_BITMAP = str(HERE / "fonts" / "ter-u14n.pil")             # Terminus 14, crisp bitmap
FONT_LOGO = str(HERE / "fonts" / "vtks-blocketo.regular.ttf")  # blocky display font
FPS = 15
TZ = ZoneInfo("Asia/Karachi")
VARIANTS = {
    # name: (gifos colour scheme, terminal bg, smiley yellow)
    "dark": ("catppuccin-mocha", (30, 30, 46), (249, 226, 175)),
    "light": ("catppuccin-latte", (239, 241, 245), (223, 142, 29)),
}


def render(variant):
    scheme, bg, yellow = VARIANTS[variant]
    # gifos reads its settings at import time, so configure before importing it.
    os.environ["GIFOS_GENERAL_COLOR_SCHEME"] = scheme
    os.environ["GIFOS_GENERAL_USER_NAME"] = "aiza"
    os.environ["GIFOS_FILES_OUTPUT_GIF_NAME"] = f"output-{variant}"
    import gifos
    from PIL import Image, ImageFont

    R = "\x1b[0m"

    def c(code, s):
        return f"\x1b[{code}m{s}{R}"

    def pixelforge_smiley(path, px=12):
        """After examples/smiley.pf from my PixelForge compiler, rendered to a PNG.

        canvas 16x16; color YELLOW; fill_rect 2,2,12,12; eyes at (5,5),(10,5);
        mouth: a symmetric smile across columns 4..11.
        """
        img = Image.new("RGB", (16, 16), bg)
        for y in range(2, 14):
            for x in range(2, 14):
                img.putpixel((x, y), yellow)
        for x, y in [(5, 5), (10, 5)] + [(i, 11 - abs(2 * i - 15) // 2) for i in range(4, 12)]:
            img.putpixel((x, y), bg)
        img.resize((16 * px, 16 * px), Image.NEAREST).save(path)

    t = gifos.Terminal(800, 540, 15, 15, FONT_BITMAP, 15)
    t.set_fps(FPS)
    t.set_prompt("\x1b[0;91maiza\x1b[0m@\x1b[0;93mgithub ~> \x1b[0m")
    now = datetime.now(TZ)
    year = now.strftime("%Y")

    # ---- 1. BIOS -----------------------------------------------------------
    t.gen_text("", 1, count=8)
    t.toggle_show_cursor(False)
    t.gen_text("AIZA BIOS (C) " + year + ", " + c("91", "Gazyani Systems"), 1)
    t.gen_text(c("94", "GitHub Profile ReadMe Terminal, Rev 2027"), 3)
    t.gen_text("CPU: Karachi(tm) Student Processor @ 3.0 coffees/hr", 5)
    t.gen_text("Press " + c("94", "DEL") + " to enter SETUP, " + c("94", "ESC") + " to skip memory test", t.num_rows)
    for i in range(0, 65536 + 1, 16384):
        t.delete_row(7)
        t.gen_text(f"Memory Test: {i}K", 7, count=2, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64K " + c("92", "OK"), 7, count=6, contin=True)
    t.gen_text("Detecting drives ... " + c("92", "OK"), 8, count=3, contin=True)
    t.gen_text("Loading " + c("93", "aiza.os") + " ...", 9, count=8, contin=True)

    # ---- 2. Logo reveal -----------------------------------------------------
    t.clear_frame()
    t.set_font(FONT_LOGO, 96)
    logo = "AIZA"
    text_w = ImageFont.truetype(FONT_LOGO, 96).getlength(logo)
    cell_w = t._Terminal__font_width
    mid_row = (t.num_rows + 1) // 2
    mid_col = max(1, round(((800 - text_w) / 2 - 15) / cell_w) + 1)
    for line in gifos.effects.text_scramble_effect_lines(logo, 4, only_upper=True, include_special=False):
        t.delete_row(mid_row)
        t.gen_text(c("95", line), mid_row, mid_col)
    t.delete_row(mid_row)
    t.gen_text(c("95", logo), mid_row, mid_col, count=18)

    # ---- 3. Login -----------------------------------------------------------
    t.set_font(FONT_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(3)
    t.gen_text(c("93", "aiza.os 2027.1 (tty1)"), 1, count=4)
    t.gen_text("login: ", 3, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text("aiza", 3, contin=True)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text("********", 4, contin=True)
    t.toggle_show_cursor(False)
    t.gen_text(f"Last login: {now.strftime('%a %b %d %H:%M %Y')} PKT on tty1", 6, count=4)

    # ---- 4. fetch -----------------------------------------------------------
    stats = gifos.utils.fetch_github_stats("Aiza166")
    top_langs = ", ".join(lang for lang, _ in stats.languages_sorted[:5])

    t.gen_prompt(8)
    col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text(c("91", "fetch.s"), 8, contin=True)
    t.delete_row(8, col)
    t.gen_text(c("92", "fetch.sh"), 8, contin=True)
    t.gen_typing_text(" -u Aiza166", 8, contin=True)
    t.toggle_show_cursor(False)
    t.gen_text("", 9, count=3)

    t.clear_frame()
    t.gen_prompt(1)
    t.gen_text(c("92", "fetch.sh") + " -u Aiza166", 1, contin=True)

    smiley = HERE / f".smiley-{variant}.png"
    pixelforge_smiley(smiley)
    t.paste_image(str(smiley), 4, 4)
    smiley.unlink()

    L, V, H = "96", "93", "30;105"  # label, value, header
    details = [
        c(H, " aiza@github "),
        "-------------",
        c(L, "OS:       ") + c(V, "Windows 11, Linux"),
        c(L, "Host:     ") + c(V, "FAST NUCES, Karachi"),
        c(L, "Kernel:   ") + c(V, "BS Computer Science, class of 2027"),
        c(L, "Shell:    ") + c(V, "bash"),
        c(L, "Builds:   ") + c(V, "LLM-powered tools, end to end"),
        c(L, "Also:     ") + c(V, "kernel modules, compilers, ML pipelines"),
        c(L, "Latest:   ") + c(V, "SWE Intern @ AlphaVenture, summer " + year),
        "",
        c(H, " contact "),
        "-------------",
        c(L, "Email:    ") + c(V, "aizagazyani16@gmail.com"),
        c(L, "LinkedIn: ") + c(V, "in/aiza-gazyani"),
        c(L, "Web:      ") + c(V, "aiza-gazyani.vercel.app"),
        "",
        c(H, " github "),
        "-------------",
        c(L, "Rank:         ") + c(V, stats.user_rank.level),
        c(L, "Stars:        ") + c(V, str(stats.total_stargazers)),
        c(L, "Commits (1y): ") + c(V, str(stats.total_commits_last_year)),
        c(L, "PRs:          ") + c(V, str(stats.total_pull_requests_made)),
        c(L, "Followers:    ") + c(V, str(stats.total_followers)),
        c(L, "Languages:    ") + c(V, top_langs),
    ]
    t.gen_text(details, 3, 38, count=75, contin=True)

    # ---- 5. projects --------------------------------------------------------
    t.clear_frame()
    t.gen_prompt(1)
    col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text(c("91", "l"), 1, contin=True)
    t.delete_row(1, col)
    t.gen_text(c("92", "ls"), 1, contin=True)
    t.gen_typing_text(" -l ~/projects", 1, contin=True)
    t.toggle_show_cursor(False)
    t.gen_text("", 2, count=2)
    D = "94"  # directory colour
    projects = [
        c(D, "baymax.app/          ") + "multi-agent career copilot (team). my agent: CSP-validated 90-day roadmaps",
        c(D, "NeuroDetect/         ") + "Parkinson's classifier -> leakage audit. published the honest 0.53 AUC",
        c(D, "PixelForge-Compiler/ ") + "pixel-art language: lexer -> parser -> IR -> bytecode -> stack VM",
        c(D, "kernel-module/       ") + "1 producer, 4 consumer kthreads, 3-priority ring buffer " + c("90", "(private)"),
        c(D, "alphaventure-ai/     ") + "chat over 5,998 YC startups via an MCP server, PHP + JS " + c("90", "(private)"),
    ]
    t.gen_text(projects, 2, count=30)

    t.gen_prompt(t.curr_row + 1)
    t.toggle_show_cursor(True)
    t.gen_typing_text(c("92", "# thanks for stopping by :)"), t.curr_row, contin=True)
    t.gen_text("", t.curr_row, count=75, contin=True)

    # gifos.gen_gif() shells out with single quotes, which breaks on Windows; do it ourselves.
    frames = list(Path("frames").glob("frame_*.png"))
    subprocess.run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-r", str(FPS), "-i", "frames/frame_%d.png",
        "-filter_complex", "[0:v] split [a][b];[a] palettegen [p];[b][p] paletteuse",
        f"output-{variant}.gif",
    ], check=True)
    print(f"INFO: output-{variant}.gif written, {len(frames)} frames, ~{len(frames) / FPS:.1f}s")


def stamp_readme():
    readme = HERE / "README.md"
    text = readme.read_text(encoding="utf-8")
    when = datetime.now(TZ).strftime("%d %b %Y, %H:%M PKT")
    new = re.sub(r"(<!-- STAMP -->).*?(<!-- /STAMP -->)", rf"\g<1>last rendered {when}\g<2>", text, flags=re.S)
    if new != text:
        readme.write_text(new, encoding="utf-8", newline="\n")
        print("INFO: README stamp updated")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        render(sys.argv[1])
    else:
        for v in VARIANTS:
            subprocess.run([sys.executable, __file__, v], check=True, cwd=HERE)
        stamp_readme()
