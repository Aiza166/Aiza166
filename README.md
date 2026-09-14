# Aiza Gazyani

**Final-year computer science student at FAST NUCES, Karachi, graduating 2027.**

I build LLM-powered tools end to end, from the database and backend through to the browser, with a background in systems programming and machine learning.

[Portfolio](https://aiza-gazyani.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/aiza-gazyani/) · [Resume](https://drive.google.com/file/d/1mMadEwz5CTcw6OPjF4S7lOBRSDro6GJ7/view?usp=sharing) · [LeetCode](https://leetcode.com/u/aizagazyani16/) · [Email](mailto:aizagazyani16@gmail.com)

<img alt="C, C++, Python, PHP, JavaScript, TypeScript, Bash, React, Next.js, FastAPI, Node.js, MySQL, MongoDB, Supabase, TensorFlow, Scikit-learn, Linux, Git" src="https://skillicons.dev/icons?i=c,cpp,python,php,js,ts,bash,react,nextjs,fastapi,nodejs,mysql,mongodb,supabase,tensorflow,sklearn,linux,git&theme=dark&perline=9" />

## Lately

**AlphaVenture** · Software Engineering Intern, Karachi, June–July 2026. I built the AI analyst for their product for exploring Y Combinator startups: ask a plain-English question about 5,998 startups and get tables, charts and full reports streamed to the browser as the model writes them. PHP 8.3 and plain JavaScript, no framework.

- The model's only path to the live MariaDB database is a Model Context Protocol (MCP) server I designed: read-only queries, size caps, low-permission accounts.
- Moving deferred startup work to server boot cut the first-message wait from 61 s to 24 s.
- Also shipped as an embeddable widget on their public site, from the same codebase as the main chat. Handed to AlphaVenture's engineers and now being deployed to production. Private code.

Before that: three full-stack Next.js apps for **Nexium** — Mental Health Tracker ([live](https://mental-health-tracker-snowy.vercel.app) · [code](https://github.com/Aiza166/Mental-Health-Tracker)), Blog Summariser ([live](https://blog-summariser-five.vercel.app) · [code](https://github.com/Aiza166/blog-summariser)), Quote Generator ([live](https://nexium-aiza.vercel.app) · [code](https://github.com/Aiza166/Quote-Generator-Web-App)) — and a summer of 300+ algorithm problems with the **Dev Weekends** fellowship.

## Selected work

**[baymax.app](https://github.com/Aiza166/baymax.app)** — Multi-agent AI career copilot, a team project for the AI Mustaqbil 2.0 hackathon, extended for the Women in AI Accelerator Build Challenge. My part is Abigail, the roadmap agent: constraint satisfaction (AC-3 arc consistency plus backtracking search) enforces prerequisites and realistic scheduling on a 90-day learning plan *before* an LLM turns it into readable guidance, with responsible-AI guardrails (per-IP rate limiting, PII-free logging, explainable scoring, output fallbacks) on top.<br>
*Python, FastAPI, React, TypeScript, Groq LLaMA 3.3-70B* · [Live →](https://baymax-app-alpha.vercel.app/)

**[NeuroDetect](https://github.com/Aiza166/NeuroDetect)** — A Parkinson's classifier on a clinical-style dataset, and the audit that followed: 3 of its 32 features were clinical assessments of Parkinson's itself, and retraining without them dropped ROC-AUC from 0.91 to 0.74, then to 0.53 (chance) once the motor-symptom flags went too. The dataset turned out to be synthetic (uniform marginals, max inter-feature correlation 0.08), so the repo publishes the honest numbers and says plainly that it is not a screening tool.<br>
*Python, TensorFlow, Keras, Scikit-learn, Pandas*

**[PixelForge-Compiler](https://github.com/Aiza166/PixelForge-Compiler)** — A small language for drawing pixel art, with the whole pipeline: handwritten DFA lexer, recursive-descent LL(1) parser, semantic analysis, three-address IR, custom bytecode and a stack-based VM that renders to PNG or the ANSI terminal. Flask web UI with live canvas preview; Compiler Construction course, team of two.<br>
*Python, Flask*

**Producer-Consumer Kernel Module** — A Linux kernel module: one producer and four consumer kernel threads over a 20-slot circular buffer with three priority levels, drained highest-priority-first, with six userspace interfaces across procfs, sysfs, debugfs and char devices. About 600 lines of C, team of four.<br>
*C, Linux* · coursework, not on GitHub

More on the [repositories tab →](https://github.com/Aiza166?tab=repositories)

## Activity

<p>
  <img height="165" alt="GitHub stats" src="https://github-readme-stats.shion.dev/api?username=Aiza166&show_icons=true&hide_border=true&theme=tokyonight" />
  <img height="165" alt="Most used languages" src="https://github-readme-stats.shion.dev/api/top-langs/?username=Aiza166&layout=compact&langs_count=6&hide_border=true&theme=tokyonight" />
</p>

---

Off the keyboard: chess, graphic design, cycling. On campus: marketing, content and design roles at the Robotics and Automation Society, Developer Student Club and FAST Entrepreneurship Society.