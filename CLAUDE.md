# SamsChosen — Project Context & Standing Instructions

## Standing permissions (AUTO MODE — durable)
- **DO NOT ask for permission** to write/modify/refactor files, commit, or push within this repository. Permission is granted for all file modifications, commits, and Git pushes to the working branch. Make changes directly and continue without seeking confirmation.
- Work stays **inside this repo** on branch `claude/chat-session-lGiWH`. No PRs, no other repos, no external publishing unless explicitly asked.
- Commit and push **incrementally** (container is ephemeral — anything uncommitted can be lost).

## The mission
Build the deepest possible research base of **under-the-radar "hidden gem" stocks** for a long-term (3–10yr+) concentrated quality-compounder portfolio. The target profile:
- **"Behind-the-scenes, indispensable, Micron/AMD-years-early"** — businesses that are picks-and-shovels into structural/future waves, before the crowd knows.
- Real moats, real economics, founder/family alignment preferred. No geographic limits.
- **This is a research-accumulation mission, not a decision mission yet.** Keep ADDING — more picks, more gems, more finder-lanes, more rankings. Pick decisions come *later*.
- **"Next Vista" sub-theme:** alongside quality compounders, hunt the *early-stage asymmetric* pattern — Vista Energy (VIST) is up ~3000% because it was a real, low-cost, cash-generating, founder-led operator bought small before the crowd. We want that **at the $10/5-years-early stage**: real business + structural wave + genuine 10x with a real downside floor (NOT pre-revenue lottery tickets).

## HARD CONSTRAINT — UK Stocks & Shares ISA buyability (Trading 212)
Every recommendable name MUST be buyable in the owner's **UK Trading 212 Stocks & Shares ISA**. Confirmed empirically:
- **US-listed ADRs are often "VIEW ONLY"** (UK PRIIPs/KID rule) — e.g. **ICICI Bank (IBN)** and **Kaspi (KSPI)** are view-only / NOT buyable. Treat ADR-only EM names as likely unavailable; flag, don't recommend.
- **US-domiciled ETFs are "view only"** in a UK ISA (no KID). Use UCITS versions (LSE) instead.
- **Individual common stocks are generally fine** on NYSE/Nasdaq, LSE, Euronext, Xetra, Borsa Italiana, Oslo, Nasdaq Nordic, SIX (where T212 supports). Vista (VIST, NYSE common) IS buyable.
- Still excluded: NSE/BSE India, most Tokyo-only, Korea-only, Taiwan-only, TSX/TSXV-only, OTC/pink.
- Consequence: the India slot stays the **iShares MSCI India UCITS ETF** (buyable) — the IBN "upgrade" is blocked by view-only status. Polycab/CDSL (NSE) also unavailable.

## Current portfolio (the 15)
Constellation Software 12%, ATOSS Software 9%, Topicus 9%, Bachem 9%, Veralto 8%, EXOR 8%, Investor AB 7%, Vitec 6%, Sartorius Stedim 6%, iShares MSCI India 6%, Eckert & Ziegler 5%, Secunet 4%, Bioventix 4%, VinaCapital Vietnam 4%, Sofina 3%. (Keep exactly 15; any new pick must be good enough to replace one — but that's a *later* decision.)

## Repo structure
- `portfolio.md` — the holdings.
- `research/portfolio-synthesis.md`, `portfolio-the-honest-read.md` — diagnosis of the book.
- `research/disputed-figures-verification.md` — primary-source fact-checks.
- `research/concentration-correlation-stress-test.md` — effective-bets analysis.
- `research/ai-vs-vertical-software-moat-tripwires.md` — the 36%-of-book AI/VMS monitoring framework.
- `research/per-holding-data-refresh.md` — per-holding data table.
- `research/best-15-synthesis.md` — keep/replace menu (informational, not a verdict).
- `research/gems/00-gem-candidates-master.md` — MASTER INDEX of all candidates + cross-lane signals + swap thesis.
- `research/gems/NN-<lane>.md` — one detailed report per finder-lane (full moat/economics/risks/sources). Numbered sequentially; **keep appending new lanes**.

## How to run a research wave (the repeatable playbook)
1. Launch many parallel sub-agents (general-purpose, **model: opus** for depth, `run_in_background: true`), each on a distinct non-overlapping finder-lane / theme.
2. Agent brief: hunt 3–5 gems in the lane; for each give Name|ticker|country|~mktcap|stage, the structural/future wave + why under-covered, moat, founder/insider ownership, sourced economics (growth/margins/FCF/ROIC/balance sheet — flag unverified, never fabricate), valuation, 10-yr bull case + top risks, which of the 15 it could replace / which blind spot it fills, conviction 1–5, plus a rejected list. **Agents must NOT write files** — return the report as their final message (they otherwise save to the wrong path).
3. As each completes, save its full report to `research/gems/NN-<lane>.md`, append a condensed row-set to the master index, commit, and push.
4. Note cross-lane corroboration (a name surfaced by 2+ lanes = strong signal).

## Lanes already covered (01–20) — do not re-hunt; find NEW names
Nordic/EU serial acquirers · Japan niche leaders · Korea/Taiwan supply chain · US small/mid compounders · AI/compute picks-and-shovels · grid/electrification · energy/real-asset royalties · critical minerals/mining · defense/sovereignty · aerospace/space · semicap equipment/materials · radiopharma/isotopes · life-science tools/CDMO · medtech/vet/dental · water/TIC/environmental · cybersecurity/identity · financial infrastructure · India single-name · SE Asia/frontier/LatAm · automation/robotics.

## Framing
All outputs are **informational research synthesis, not financial advice.** Decisions are the owner's.
