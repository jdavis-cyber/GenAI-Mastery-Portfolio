# 🗺️ GenAI Engineering Master Plan (The 10-Project Gauntlet)

**Status:** 🏗️ In Progress  
**Architecture:** 3-Layer Governance (Directives → Orchestration → Execution)  
**Stack:** Antigravity (VS Code), Python, Gemini 1.5, Streamlit, Local Filesystem.

---

## 🎓 Phase 1: The "Vibe Coding" Foundation

*Goal: Learn to delegate to AI to build UIs and Logic fast.*

### ✅ Project 1: The Security Risk Register (Completed)

* **Concept:** A "Lovable-style" rapid application build.
* **What we built:** A Streamlit app to log, categorize, and view security risks.
* **Compounding Skill:** **Deterministic Execution.** Learned to use an Agent to write code that performs specific, repeatable actions (logging data) without "hallucinating."
* **Career Signal:** "Can build functional internal tools in minutes, not days."

### ⏳ Project 2: The Resource Manager (Data & State)

* **Concept:** A "Claude Code" style complex backend tool.
* **The Build:** A **Personal Knowledge Graph**. Manage bookmarks, PDF links, and notes with tagging and search.
* **New Challenge:** CRUD operations (Create, Read, Update, Delete), Persistent State (SQLite), and Search Logic.
* **Career Signal:** "Understands data persistence and backend complexity."

### ⏳ Project 3: The Receipt/Document Intelligence Pipeline

* **Concept:** Adapting the "Mobile App" project for Systems Engineering.
* **The Build:** A folder watcher that detects new PDFs/Images (receipts/invoices), uses **Gemini Vision** to extract data (Merchant, Date, Total), and saves it to a CSV/Database.
* **New Challenge:** Multimodal AI (Vision), File System Events, Automated Pipelines.
* **Career Signal:** "Can build automated pipelines that process unstructured data."

---

## 🧠 Phase 2: AI Integration & RAG

*Goal: Moving from 'Code' to 'Cognition'.*

### 🚀 Project 4: The Transcript Sanitizer (Current Focus)

* **Concept:** The "First LLM Integration."
* **The Build:** A privacy tool for **PLAUD/Wispr** recordings. Reads a raw transcript, uses Gemini to identify and redact PII (Names, IPs, Orgs), and outputs a clean file.
* **New Challenge:** Token Economics, Privacy Engineering, Structured Output.
* **Career Signal:** "Understands the security implications of sending data to LLMs."

### ⏳ Project 5: The Policy RAG (Talk-to-your-Docs)

* **Concept:** Retrieval Augmented Generation.
* **The Build:** A "Compliance Officer" bot. Upload a NIST/ISO PDF. Ask: "Does Project 1 comply with Section 5?"
* **New Challenge:** Embeddings, Vector Search (ChromaDB), Chunking Strategies, Citations.
* **Career Signal:** "Can build systems that ground AI answers in company truth."

---

## 🤖 Phase 3: Agent Architecture (The Deep Work)

*Goal: Understanding the 'Why', not just the 'How'.*

### ⏳ Project 6: The ReAct Loop (From Scratch)

* **Concept:** No Frameworks. Pure Python.
* **The Build:** A raw script that implements `Thought -> Action -> Observation`. We will build a "Competitive Research Agent" that can search the web (or mock search) and synthesize answers.
* **New Challenge:** Parsing LLM output, managing loops, stopping conditions.
* **Career Signal:** "Understands Agentic Reasoning deeply. Doesn't just rely on LangChain magic."

### ⏳ Project 7: The Local MCP Server

* **Concept:** Model Context Protocol (The 2026 Standard).
* **The Build:** An MCP Server that exposes your **Project 2 Database** to the AI.
* **New Challenge:** Building standard interfaces that *any* agent can talk to.
* **Career Signal:** "Is ready for the future of interoperable AI agents."

---

## ⚡ Phase 4: Autonomous Systems

*Goal: Agents that act without you.*

### ⏳ Project 8: The Calendar/Email Assistant

* **Concept:** "Human-in-the-Loop" Actions.
* **The Build:** An agent that reads your calendar (Google API) and drafts emails to decline/accept meetings based on your rules.
* **New Challenge:** OAuth, Dangerous Actions (Sending Emails), Approval Workflows.
* **Career Signal:** "Trusted to build agents that interact with the real world."

### ⏳ Project 9: The Proactive "Inbox Concierge"

* **Concept:** Triggers and Background Jobs.
* **The Build:** A script that wakes up every hour, classifies new emails/files, and moves them to folders based on urgency.
* **New Challenge:** Cron Jobs, Error Recovery (what if API is down?), Logging.
* **Career Signal:** "Builds systems that run 24/7."

---

## 🛡️ Phase 5: Production Engineering

*Goal: Making it bulletproof.*

### ⏳ Project 10: The Observability Suite

* **Concept:** Production Readiness.
* **The Build:** Adding **Tracing** (LangSmith or Local Logs) to your previous agents. Visualizing cost, latency, and errors.
* **New Challenge:** Telemetry, Cost Optimization, Debugging Live Systems.
* **Career Signal:** "Writes production-grade code, not just demos."

---

## 📚 The 100-Hour Rule

* **Hours 1-20 (We are here):** Vibe Coding & Basic Apps.
* **Hours 21-40:** LLM Integration & RAG.
* **Hours 41-60:** Agent Fundamentals (ReAct/MCP).
* **Hours 61-80:** Autonomous Systems.
* **Hours 81-100:** Production Engineering.

> "The best AI engineers aren't the best coders—they're the best at working with AI."
