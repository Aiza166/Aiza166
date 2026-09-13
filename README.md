<div align="center">

# Aiza Gazyani

**Final-year BSCS student @ FAST NUCES, Karachi · Class of 2027**

I build LLM-powered tools end to end, from the database and backend through to the browser, with a background in systems programming and machine learning.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aiza-gazyani/)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://aiza-gazyani.vercel.app/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aizagazyani16@gmail.com)
[![Resume](https://img.shields.io/badge/Resume-FFA500?style=for-the-badge&logo=google-drive&logoColor=white)](https://drive.google.com/file/d/1mMadEwz5CTcw6OPjF4S7lOBRSDro6GJ7/view?usp=sharing)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/aizagazyani16/)

</div>

---

## 💼 Experience

**Software Engineering Intern · AlphaVenture** — Karachi, on-site · June – July 2026
- Built the AI analyst for the company's Y Combinator startup product: a chat tool that answers plain-English questions about 5,998 startups from a live MariaDB database and streams tables, charts, and full reports to the browser as the model writes them. PHP 8.3 and plain JavaScript, no framework.
- Designed a Model Context Protocol (MCP) server as the model's only path to the database: read-only queries, size caps, and low-permission accounts, so a model-written query cannot alter or overload the data.
- Cut the wait on a user's first message from 61 s to 24 s by tracing the delay to startup work deferred until the first request, then moving it to server boot.
- Shipped the same chat as an embeddable widget on the public site, served from one shared copy of the code so the widget and the standalone app cannot drift.
- Handed off to AlphaVenture's engineers at the end of the internship; currently being deployed to production.

**AI & Web Development Intern · Nexium** — Remote · July 2025
- Built and deployed three full-stack apps end to end ([Mental Health Tracker](https://github.com/Aiza166/Mental-Health-Tracker), [Quote Generator](https://github.com/Aiza166/Quote-Generator-Web-App), [Blog Summariser](https://github.com/Aiza166/blog-summariser)) with Next.js, Supabase, MongoDB, ShadCN UI, Vercel, and n8n workflows.
- Set up CI/CD pipelines, authentication, and database integrations for each.

**Software Development Fellow · Dev Weekends** — Remote · June – August 2025
- Mentor-led fellowship: 30+ DSA sessions and 12 engineering sessions (JavaScript, React, Node.js, system design). Solved 300+ algorithm problems and contributed to the open-source capstone.

---

## 🚀 Featured Projects

| Project | What it is | Stack |
|---|---|---|
| **[Baymax.app](https://github.com/Aiza166/baymax.app)** · [live](https://baymax-app-alpha.vercel.app/) | Multi-agent AI career copilot built by a team for the AI Mustaqbil 2.0 Hackathon, later extended for the Women in AI Accelerator Build Challenge. **My part: Abigail, the career-roadmap agent.** It models a 90-day learning plan as a constraint-satisfaction problem (AC-3 arc consistency + backtracking search) to enforce prerequisites and realistic weekly time budgets *before* an LLM turns the validated plan into readable guidance. Also added responsible-AI guardrails: per-IP rate limiting, PII-free logging, explainable scores, and output fallbacks. 17-endpoint API. | Python · FastAPI · React · TypeScript · Groq LLaMA 3.3-70B · Whisper · Mem0 |
| **[NeuroDetect](https://github.com/Aiza166/NeuroDetect)** | Parkinson's classification pipeline that turned into a leakage audit. Trained a TensorFlow/Keras classifier, then found 3 of 32 features were clinical assessments of Parkinson's itself. Retraining without them dropped ROC-AUC from 0.91 to 0.74; removing motor-symptom flags too collapsed it to 0.53, no better than chance. Identified the dataset as synthetic (uniform marginals, max inter-feature correlation 0.08) and published the honest numbers instead of the headline one. Not a screening tool. | Python · TensorFlow · Keras · Scikit-learn · Pandas |
| **Advanced Producer-Consumer Kernel Module** *(coursework, not public)* | Linux kernel module running 1 producer and 4 consumer kernel threads over a 20-slot circular buffer with 3 priority levels, drained highest-priority first. Shared-IRQ top half queues a workqueue bottom half so the buffer fill can safely take a mutex; synchronized with counting semaphores, a mutex, and bounded wait queues. 6 userspace interfaces across procfs, sysfs, debugfs, and three misc character devices. ~600 lines of C, team of 4. | C · Linux kernel |
| **[PixelForge](https://github.com/Aiza166/PixelForge-Compiler)** | A domain-specific language for pixel art with a full compiler pipeline: handwritten DFA lexer → recursive-descent LL(1) parser → semantic analysis → three-address-code IR → custom bytecode → stack-based virtual machine that renders to PNG or ANSI terminal. Supports variables, loops, conditionals, subroutines, and palettes. Includes a Flask web UI with live canvas preview. Compiler Construction course, team of 2. | Python · Flask |
| **[YC Company Detail ETL](https://github.com/Aiza166/yc-scraping)** | ETL pipeline for Y Combinator company pages. Reads the Inertia.js `data-page` JSON straight out of the HTML (no headless browser, no API key), caches raw responses and images, and upserts into a 9-table normalized MariaDB schema. Idempotent re-runs, PyMySQL fallback driver, hermetic pytest suite. | Python · BeautifulSoup · MariaDB |
| **[Mental Health Tracker](https://github.com/Aiza166/Mental-Health-Tracker)** · [live](https://mental-health-tracker-snowy.vercel.app) | Mood, energy, sleep, and stress logging with AI-generated insights. Magic-link auth via Supabase, mood data in MongoDB, insights produced by an n8n workflow calling OpenAI, charts with Recharts. | Next.js 14 · TypeScript · Supabase · MongoDB · n8n · Tailwind |

---

## 🧩 More Projects

| Project | Description | Stack |
|---|---|---|
| [Blog Summariser](https://github.com/Aiza166/blog-summariser) · [live](https://blog-summariser-five.vercel.app) | Paste a blog URL, get the article extracted with Mozilla Readability, a short summary, and a dictionary-based Urdu translation. Summaries stored in Supabase, full text in MongoDB. | Next.js 15 · TypeScript · Supabase · MongoDB |
| [Quote Generator](https://github.com/Aiza166/Quote-Generator-Web-App) · [live](https://nexium-aiza.vercel.app) | Topic-based quote generator. | Next.js 15 · ShadCN UI · Tailwind |
| [Draftly](https://github.com/Aiza166/Draftly-React-Blog-App) · [live](https://draftly-react-blog-app.vercel.app) | Blog app with authentication and post CRUD on Appwrite, Redux Toolkit state, TinyMCE rich-text editor. | React · Appwrite · Redux · Tailwind |
| [Personal Portfolio](https://github.com/Aiza166/personal-portfolio) · [live](https://aiza-gazyani.vercel.app) | Source for my portfolio site. | React · Vite · TypeScript |
| [Regular Grammar Parser](https://github.com/Aiza166/regular-grammar-parser) | CLI that takes right-linear grammar rules, derives a symbolic regular expression, builds a transition table, and simulates the finite automaton to test string acceptance. Automata theory coursework. | Python |
| [Social Networking Platform Simulator](https://github.com/Aiza166/Social-Networking-Platform-Simulator) | CLI social network with accounts, posts, stories, likes, comments, following, and file-based persistence. OOP coursework. | C++ |
| [CryptoView](https://github.com/Aiza166/Cryptocurrency-website) · [live](https://cryptocurrency-website-rust.vercel.app) | Live BTC/ETH/DOGE prices from the CoinGecko API. | HTML · CSS · JavaScript |
| [Snake Game](https://github.com/Aiza166/Snake-Game) · [QR Code Generator](https://github.com/Aiza166/QR-Code-Generator) · [To-Do List](https://github.com/Aiza166/To-Do-List) | Vanilla JS mini-projects from the Dev Weekends fellowship. | HTML · CSS · JavaScript |
| [SQL 50](https://github.com/Aiza166/SQL-50-LeetCode) · [30 Days of JavaScript](https://github.com/Aiza166/LeetCode-30-Days-Of-JavaScript) | LeetCode study-plan solutions. | SQL · JavaScript |

---

## ⚙️ Skills

**Languages:** C/C++ · Python · PHP · SQL · JavaScript · TypeScript · Bash · Assembly

**Web & backend:** React · Next.js · FastAPI · Node.js · Apache · Server-Sent Events · ShadCN UI · Chart.js

**Data & AI:** MariaDB/MySQL · MongoDB · Supabase · Model Context Protocol (MCP) · TensorFlow · Scikit-learn · NumPy · Pandas

**Systems & tools:** Linux · Git/GitHub · Claude Code

---

## 🎓 Education & Leadership

**BS Computer Science** — National University of Computer and Emerging Sciences (FAST NUCES), Karachi · 2023 – 2027

- Head of Marketing & Co-Head of Graphic Design, Robotics and Automation Society
- Co-Head of Content, Developer Student Club
- Co-Head of Marketing, FAST Entrepreneurship Society

Off the keyboard: chess, graphic design, cycling.

---

## 📊 GitHub Stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=Aiza166&show_icons=true&theme=radical&hide_border=true&cache_seconds=1800" alt="GitHub stats" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Aiza166&layout=compact&theme=radical&hide_border=true&cache_seconds=1800" alt="Top languages" />

<img height="165" src="https://streak-stats.demolab.com/?user=Aiza166&theme=radical&hide_border=true" alt="Contribution streak" />

</div>
