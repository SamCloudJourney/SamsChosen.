# Lane 21 — Edge-AI Inference Silicon & IP Enablers

_Research date: 2026-06-01. Informational synthesis, not financial advice. All figures sourced from SEC filings, press releases, and aggregator data; flagged where unverified._

---

## Lane thesis

On-device / edge inference is the next trillion-dollar deployment layer: cloud AI trained the models; now **billions of endpoints need to run them locally** — in vehicles, factories, MCUs, smartphones, wearables, smart cameras, and industrial robots. The picks-and-shovels into this wave are not Nvidia or AMD. They are the **IP licensors, chiplet-interconnect IP vendors, semiconductor analytics platforms, and test handlers** that sit underneath every edge AI chip, invisible to the market, collecting royalties or software subscriptions with compounding moat.

The structural wave:
- Edge AI silicon market growing >30% CAGR through 2030 (GrandView Research, 2025 report).
- TinyML chipset shipments projected to hit $5.9B by 2030 (Nordic Semi press release, June 2025).
- AI chip complexity (chiplets, 3D packaging, HBM) creates geometric demand for interconnect IP, yield analytics, and thermal test infrastructure.

**Why under-covered:** Most analyst attention is on Nvidia, Broadcom, Marvell (data-center inference). The edge layer — lower power, lower ASP per chip, but shipped in billions of units — is covered by fewer than 10 analysts on average for each of the names below.

---

## The 4 Gems

---

### GEM 1: CEVA Inc

**Name:** CEVA, Inc.
**Ticker / Venue:** CEVA, Nasdaq (common stock — ISA buyable YES)
**Country:** US (HQ Israel R&D)
**~Market Cap (2026-05-29):** ~$1.11B
**Stage:** Revenue-generating royalty engine; AI inflection phase

#### The structural wave + why early/under-covered

CEVA is the **ARM of wireless and edge-AI connectivity IP**. It licenses silicon IP — DSPs, connectivity cores (Bluetooth, Wi-Fi, 5G cellular IoT), and crucially its **NeuPro NPU family** — to chip makers who pay an upfront licence fee and then a per-unit royalty on every chip shipped. CEVA holds **68% wireless connectivity IP market share** — confirmed by IPnest 2024 annual report (cited in CEVA press release, August 2024), more than 10x its nearest peer. The AI NPU (NeuPro) business is the new, higher-royalty layer being added on top.

Why under-covered: Only ~8 sell-side analysts cover CEVA. The royalty lag (design win to silicon to volume royalty = 2-4 year cycle) means today's NPU wins only hit the P&L in 2026-2028. Consensus is underpricing the royalty ramp because it is not visible yet.

#### Moat / why indispensable

1. **IP lock-in:** Once a chip is designed around CEVA's DSP or NPU core, switching costs are enormous — the chip must be completely re-taped. CEVA cores are inside ~2 billion units shipped per year (2024 actuals).
2. **68% wireless market share:** Near-monopoly in Bluetooth and Wi-Fi IP. Cellular IoT growing +41% YoY (Q3 2025 data).
3. **NeuPro NPU cross-sell:** The same 400+ licensees who use CEVA's wireless IP are now being upsold NPU blocks. 10 NeuPro agreements signed in 2025; AI >20% of 2025 licensing revenue (CEVA press release, 2026-01).
4. **NeuPro-Nano Award:** Won Embedded World 2026 Artificial Intelligence Award — validator of technical leadership (PR Newswire, 2026-03-11).
5. **Physical AI platform:** Positioning CEVA as the complete "sense, connect, infer" substrate for autonomous/edge AI devices.

#### Founder / insider ownership

Institutional ownership ~77%. Insider ownership modest (~$13M in named-insider holdings per 2025 data). CEO and CFO engaged in cluster buying post-earnings (Fintool News, sourced). Not a founder-led story — but the royalty model means management does not need to be the moat; the IP architecture is.

Flagged: insider % is low — a relative weakness vs. the portfolio DNA. Partially offset by the structural nature of the royalty moat.

#### Sourced economics

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Revenue ($M) | 113.8 | 120.6 | 97.4 | 106.9 | 109.6 |
| Revenue growth | n/a | +6% | -19% | +10% | +2% |
| Gross margin | 91% | 87% | 88% | 88% | 87% |
| Operating income ($M) | +7.0 | +3.9 | -13.5 | -7.6 | -11.4 |
| Net income ($M) | +0.4 | -23.2 | -11.9 | -8.8 | -10.6 |
| FCF ($M) | +23.6 | +3.4 | -9.2 | +0.5 | -6.3 |

Sources: StockAnalysis.com income statement; Telecompaper revenue confirmation.

Revenue mix FY2025: Licensing $63.6M (+6% YoY); Royalties $46.0M. Total $109.6M.
Units shipped FY2024: ~1.98 billion. Implied royalty per unit: ~$0.024 (2.4 cents/unit). [Calculated from public data; treat as indicative.]
Cash/debt (Sep 2025 post-offering): ~$204M total liquidity (cash + marketable securities); zero long-term debt. (SEC 424B5 filing, Nov 2025.)
Dilution note: CEVA raised $58.5M in a Nov 2025 public offering at $19.50/share adding ~3M shares.

#### Valuation (2026-05-29)

- Market cap: ~$1.11B
- TTM revenue: ~$112M; P/S ~9.9x
- EV: ~$910M (adjusting for ~$200M net cash) -> EV/Revenue ~8.1x
- No GAAP profits. No debt.
- Analyst consensus: 8 analysts, Strong Buy, avg target $43.13 (StockAnalysis).
- Peer context: ARM Holdings trades ~30x revenue. CEVA at ~9-10x EV/revenue is materially cheaper.

#### 10-year bull case + asymmetric math

Base case: NPU AI royalties layer onto existing wireless base. By 2028, 6 NeuPro customers reach silicon volume. Royalty per AI unit = $0.05-$0.15 (company states "typically higher royalty potential" for AI). If 500M AI-enabled units ship in 2030 at $0.10/unit = $50M incremental AI royalties on top of growing wireless base. Total revenue $250-350M by 2030-2032. At 15-18x EV/Revenue -> EV of $4-6B -> 4-6x from current.

Bull case (AI chips ubiquitous, NPU wins compound): 2B+ AI-enabled edge units by 2033. $0.08 average NPU royalty = $160M AI royalties alone. Total revenue $400M+ at 80%+ gross margins -> EBIT $120M+ -> 30x EBIT = $3.6B+ EBIT value. Bull case = 3-5x from today.

Asymmetric floor: 68% market share wireless IP + $200M net cash + zero debt. Even in a bear scenario (no AI monetisation), CEVA is worth 6-8x revenue on wireless royalties alone ~= current price. Downside limited to slow growth, not implosion.

#### Top 3 risks

1. Royalty ramp delay: NPU design wins take 3-5 years from licence to meaningful royalty. If AI chips deploy slower, or if major OEMs design proprietary NPUs (Apple, Qualcomm already do), CEVA's AI royalty thesis stalls.
2. ARM / Synopsys / Cadence encroachment: ARM's Ethos NPU is a direct competitor. CEVA's only protection is price/power efficiency differentiation and existing customer relationships.
3. Dilution: FCF-negative; issues stock regularly. Continued dilution suppresses per-share value accretion.

#### UK ISA buyability

CEVA is a US-domiciled common stock on Nasdaq. Confirmed buyable YES (not an ADR, not a US-domiciled ETF).

#### Portfolio fit

Could replace: iShares MSCI India ETF or VinaCapital Vietnam (fills AI/compute IP blind spot with a genuinely indispensable royalty tollbooth). Does not overlap with any current 15.

**Conviction: 3.5/5** — moat is real and wide, royalty ramp credible, valuation reasonable. Held back by low insider alignment, FCF-negative, dilutive capital needs, ARM competition. Best framing: a watchlist name with a 2026-2027 entry trigger (evidence of royalty ramp inflecting).

---

### GEM 2: Arteris IP (Network-on-Chip IP)

**Name:** Arteris, Inc.
**Ticker / Venue:** AIP, Nasdaq (common stock — ISA buyable YES)
**Country:** US
**~Market Cap (2026-05-29):** ~$1.66B
**Stage:** SaaS-like IP licensor; inflecting toward profitability

#### The structural wave + why early/under-covered

Arteris is the **dominant independent vendor of Network-on-Chip (NoC) interconnect IP** — the internal highway system of every modern AI chip, SoC, and chiplet. Every complex chip needs a NoC to route data between CPU clusters, NPU blocks, memory controllers, and I/O. As chips grow more complex (chiplets, 3D-ICs, multi-die AI accelerators), NoC complexity explodes: AMD's AI chiplets use 5-20 internal networks per device.

Why under-covered: ~$1.66B market cap, fewer than 10 analysts. NoC IP is a critical but invisible sub-component — the market does not know what a NoC is, let alone who the monopolist is.

#### Moat / why indispensable

1. Pioneered NoC IP commercialisation — 20+ year head start, 4+ billion chips shipped using Arteris technology (milestone Feb 2026, cited in StockTitan).
2. Design-in switching costs: Replacing a NoC mid-design requires a complete re-architecture. Once licensed, the customer is locked in for the chip lifetime (5-10+ years).
3. AMD FlexGen win: AMD selected Arteris FlexGen Smart NoC IP for next-generation AI chiplet designs (StockTitan, 2025). Marquee validator.
4. Renesas R-Car automotive: Arteris NoC IP inside Renesas' next-gen automotive SoC for ADAS. Auto content = high-ASP, long-design-cycle, sticky.
5. Cycuity acquisition (Jan 2026): Semiconductor security verification software — natural adjacent moat extension.
6. CEO Karel Janac owns ~22-32% of shares (range reflects measurement dates); has been CEO since 2005 (21 years). Fully aligned.

#### Founder / insider ownership

Karel Janac, CEO since 2005, is the largest shareholder. Most recent sourced data: insiders own 33-44% of shares (Nasdaq articles); Janac personally holds $126M+ of stock value. Institutional ownership ~57% (Yahoo Finance). Strongest insider alignment in the lane.

#### Sourced economics

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Revenue ($M) | 37.9 | 50.4 | 53.7 | 57.7 | 70.6 |
| Revenue growth | n/a | +33% | +6.5% | +7.5% | +22% |
| Gross margin | 90% | 91.5% | 90.5% | 89.7% | 90.2% |
| Operating loss ($M) | -21.8 | -28.9 | -35.1 | -31.6 | -33.1 |
| FCF ($M) | -1.6 | -7.8 | -17.2 | -1.0 | +5.4 |

Sources: StockAnalysis.com; Arteris 8-K FY2026 (SEC EDGAR).

Q1 2026 (most recent): Revenue $22.9M +39% YoY. ACV + royalties $92.8M +39% YoY. Variable royalties $7.9M +67% YoY. RPO $118.3M +33% YoY. (Arteris Q1 2026 press release.)

FY2026 guidance: Revenue $91-95M; ACV + royalties $102-106M; Non-GAAP operating loss -$4.5 to -$8.5M; Positive FCF $5-9M. (Q1 2026 earnings call.)

Balance sheet: Minimal long-term debt pre-Cycuity. Flagged: verify post-acquisition in latest 10-Q.

#### Valuation (2026-05-29)

- Market cap: ~$1.66B
- TTM revenue: ~$77M; P/S ~21.5x — premium
- ACV + royalties (forward midpoint): ~$104M -> EV/ACV ~16x
- FCF turned positive in 2025 ($5.4M), guided positive in 2026
- Stock up ~426% over past year (StockAnalysis) — entry valuation is demanding

#### 10-year bull case

Compounding revenue 25-30% through 2030 -> $500-700M by 2030 with 88-90% gross margins and 30%+ operating margins -> $150-200M EBIT. At 30-40x EBIT (IP licensor premium) = $4.5-8B market cap = 3-5x from today.

Asymmetric floor: High switching costs mean ACV churn is structurally low. $90M+ ACV at 90% gross margins with long-tenured founder CEO creates a hard floor even at flat growth.

#### Top 3 risks

1. Premium valuation demands execution: At 21x P/S, any revenue shortfall triggers multiple compression. The +39% Q1 2026 run-rate must be sustained.
2. Synopsys competition: ~$85B market cap Synopsys offers competing interconnect IP as part of broader EDA bundle. Could undercut on price for bundled deals.
3. Concentration: ADAS/auto and AI chiplet customers are large but few. Loss of AMD or Renesas design wins would be material.

#### UK ISA buyability

AIP is a US-domiciled common stock on Nasdaq. Confirmed buyable YES.

#### Portfolio fit

Could replace: iShares MSCI India ETF. Fills hard-tech/semi-IP blind spot; highest insider alignment of all lane candidates; unique NoC IP moat not represented in current 15.

**Conviction: 4/5** — deepest moat in the lane (4B chips, design-in lock-in, AMD win, 21-year aligned CEO). Only friction is current valuation (21x P/S) after a 4x run. Best entry: pullback to 15-17x P/S (~$25-30 stock price), or staged accumulation.

---

### GEM 3: PDF Solutions (Semiconductor AI Analytics Platform)

**Name:** PDF Solutions, Inc.
**Ticker / Venue:** PDFS, Nasdaq (common stock — ISA buyable YES)
**Country:** US
**~Market Cap (2026-05-29):** ~$2.06B
**Stage:** Transitioning from niche yield-management to industry-wide AI data platform

#### The structural wave + why early/under-covered

PDF Solutions provides **AI-driven yield analytics and secure manufacturing data collaboration** for the semiconductor industry. Its Exensio platform ingests petabytes of fab data (FDC, test, assembly, packaging) and uses AI/ML to improve yield and quality. As AI chips get more complex (3D packaging, chiplets, sub-3nm nodes), manufacturing data complexity explodes non-linearly — a structural tailwind for exactly this analytics layer.

The SecureWISE acquisition ($130M, 2025) adds a secure multi-party data collaboration network connecting fabs, equipment makers, and fabless customers — creating network effects across the supply chain (management Q3 2025 earnings call).

Why under-covered: Only 8 analysts cover PDFS. The company sits at the intersection of semiconductor manufacturing and enterprise SaaS — a non-obvious niche that semiconductor analysts skip and software analysts don't understand. Customer base expanded from 150 pre-2020 to 370+ by 2025 (multiple press releases confirmed).

#### Moat / why indispensable

1. Exensio data stickiness: Fabs invest years integrating manufacturing data flows into Exensio. Switching to a competitor means re-integrating petabytes of proprietary process data. Switching costs approach capital-equipment levels.
2. SecureWISE network effect: As more fabs and equipment OEMs join the secure-collaboration network, the value compounds. 8-figure contract with large equipment OEM in Q3 2025 validates model (PDF Solutions Q3 2025 earnings call).
3. eProbe hardware-software integration: Non-contact electron-beam inspection tool with "defect detection capabilities that are very hard or nearly impossible to see with other systems" — creates hardware-anchored software moat inside leading-edge fabs.
4. Intel Tiber AI Studio partnership: Integrating Intel's AI platform into Exensio Studio AI positions PDFS as the AI analytics infrastructure layer for advanced semiconductor manufacturing.
5. TSMC / Intel / Samsung customers: Deep integration with world's most critical fabs creates reference moats.
6. CEO John Kibarian is the third-largest shareholder; insiders own ~19% in aggregate, ~9.37% of shares. Aligned.

#### Sourced economics

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Revenue ($M) | 111.1 | 148.6 | 165.8 | 179.5 | 219.0 |
| Revenue growth | n/a | +34% | +12% | +8% | +22% |
| Gross margin | 60% | 64% | 69% | 71% | 72% |
| Operating income ($M) | -19.0 | -2.1 | -0.2 | +0.9 | +5.9 |
| Net income ($M) | -21.5 | -3.4 | +3.1 | +4.1 | -0.6 |
| FCF ($M) | +0.2 | +23.9 | +3.3 | -8.1 | -8.8 |

Sources: StockAnalysis.com income statement.

Q1 2026: Revenue $60.1M vs $47.8M Q1 2025 (+26% YoY). Company reaffirms 20% revenue growth guidance for FY2026 (Seeking Alpha, May 2026).

Backlog: $292M (+25% QoQ, +22% YoY) as of Q3 2025. >50% expected to convert within 2 years. (Q3 2025 earnings call / EverTicker analysis.)

Balance sheet: Debt-to-equity 0.28x. ~$70M bank debt from SecureWISE acquisition. Conservative.

Customer concentration risk: Customer A = 38% of Q3 revenue, 35% of receivables. Significant concentration. [Flagged: plausibly Intel given the Tiber AI partnership — verify.]

#### Valuation (2026-05-29)

- Market cap: ~$2.06B
- EV/Revenue: ~5.9x on FY2025 actuals; ~5x on FY2026E (~$260M+)
- Analyst targets: Rosenblatt $52, DA Davidson $56 (May 2026)
- Operating margin inflecting: -17% (2021) to +2.7% (2025); management targets 20% long-term
- Peer comparison: Synopsys ~15.8x EV/Rev, Cadence ~17.6x, KLA ~12.9x. PDFS at ~5x is substantial discount despite being fastest-growing.

#### 10-year bull case

Revenue compounding 20% through 2031 -> ~$540M. Operating margins reaching 20% = $108M EBIT. At 20-25x EBIT (below Synopsys/Cadence) -> market cap $2.2-2.7B from EBIT layer alone. Re-rating catalyst: if Exensio is recognised as "the SAP of semiconductor manufacturing analytics" it warrants 10-12x revenue -> $5-6B market cap = 2.5-3x from today.

Asymmetric element: At 5x EV/Revenue with 22% growth and growing backlog, even the downside scenario (growth slows to 10%) looks cheap vs. peers.

#### Top 3 risks

1. Customer A concentration: Loss or renegotiation of the 38%-revenue customer would be material.
2. eProbe qualification delays: Only 5-10 potential customers globally. If qualifications slip, 2026 profitability targets move out.
3. Geopolitical / export control: 47% international revenue with China-adjacent fab exposure. US-China trade tensions and export controls create regulatory tail risk.

#### UK ISA buyability

PDFS is a US-domiciled common stock on Nasdaq. Confirmed buyable YES.

#### Portfolio fit

Could replace: iShares MSCI India ETF (fills hard-tech/semiconductor-analytics slot). Alternatively could replace VinaCapital Vietnam. PDFS is semi-adjacent to Veralto (process quality analytics) — complementary to current portfolio, not overlapping.

**Conviction: 3.5/5** — genuine moat (Exensio data lock-in + SecureWISE network), real revenue growth, cheap vs. peers. Flagged for customer concentration and eProbe execution risk. Strong watchlist candidate; accumulate on pullbacks.

---

### GEM 4: Cohu Inc (AI Accelerator Test Handlers)

**Name:** Cohu, Inc.
**Ticker / Venue:** COHU, Nasdaq (common stock — ISA buyable YES)
**Country:** US
**~Market Cap (2026-05-29):** ~$2.55B
**Stage:** Established; entering structural AI-test-handler supercycle

#### The structural wave + why early/under-covered

Cohu is a **test handler and inspection specialist** — the machines that physically handle and thermally stress semiconductor chips during testing. AI accelerator chips (GPUs, custom ASICs, HBM memory) run hotter and at higher power than traditional chips, requiring **new classes of thermal-control test handlers** that incumbents Teradyne and Advantest do not supply directly. Cohu's Eclipse handler with Active Thermal Control is purpose-built for high-power AI accelerators.

$750M pipeline: Cohu identified a $750M AI-related test-handler and HBM inspection pipeline across 12 customers — 5 in qualification, 7 in early engagement (Q4 2025 earnings). None had converted to revenue as of late 2025. Classic hockey-stick setup: pipeline is real but not yet in the P&L.

Why under-covered: Handler companies are seen as commodity automation, not strategic. The AI handler thesis is specific and not widely appreciated. Fewer than 10 analysts cover COHU.

#### Moat / why indispensable

1. Active Thermal Control (ATC) Eclipse handler: High-power AI chips require precise thermal testing. This is engineering-intensive IP, not a commodity product. First high-power thermal Eclipse order booked for an AI accelerator roadmap (Q4 2025 earnings).
2. Installed base / OSAT relationships: Recurring revenue (services, spares, interface solutions) up 25% YoY in Q4 2025. Installed base creates re-order momentum.
3. Neon HBM inspection platform: Forecasting 80% revenue growth YoY to ~$20M in 2026, targeting HBM3, HBM4, and HBM5 final inspection. HBM inspection is mandatory for every AI accelerator.
4. $484M cash position (end Q4 2025) + $287.5M convertible notes. Strong balance sheet to invest in AI handler ramp.

Note: Cohu is NOT a founder-led story. CEO Luis Muller sold ~45K shares in May 2026 (Quiver Quantitative). Insider ownership ~2.7-4.8%. Flagged: alignment is weak.

#### Sourced economics

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Revenue ($M) | 887 | 813 | 636 | 402 | 453 |
| Gross margin | 44% | n/a | n/a | n/a | 43% |
| Operating income ($M) | +60 | +126 | +43 | -72 | -70 |
| Net income ($M) | +26 | +97 | +28 | -70 | -74 |
| FCF ($M) | +86 | +98 | +85 | -7.9 | +10.7 |

Sources: StockAnalysis.com.

Recovery underway: Q4 2025 revenue $122M (+30% YoY); Q1 2026 revenue $125.1M (+29% YoY). Wall Street consensus: FY2026 revenue ~$558M (+23%).

FY2026 HPC guidance raised: AI/HPC segment revenue guidance $80-100M for FY2026 (Q1 2026 earnings call).

Balance sheet: $488.7M total cash/investments (Q1 2026). $287.5M convertible notes due 2031 at 1.5%. Net cash positive.

#### Valuation

- Market cap: ~$2.55B (May 2026)
- 2026E revenue ~$558M consensus -> P/S ~4.6x
- P/E and EV/EBITDA not sourced — flagged, verify before acting.

#### 10-year bull case

If the $750M AI handler pipeline converts over 2026-2029, and HBM inspection grows with each HBM generation, revenue base could sustainably reach $1B+. At normalised 12-18% operating margins -> $120-180M EBIT. At 12-15x EBIT = $1.4-2.7B EBIT value + $500M cash. Bull case (full cycle upturn + AI handler leadership = 20% margins): modest upside from $2.55B today. The AI handler pipeline optionality is essentially "free" at current valuation.

#### Top 3 risks

1. Pipeline-to-revenue conversion risk: 12 customers, 5 in qualification, 7 in early engagement = none yet in volume revenue. Qualification delays or losses to Teradyne/Advantest who could build handlers in-house would delay the thesis by years.
2. Duopoly shadow: Teradyne and Advantest spend as much on R&D as Cohu generates in total revenue. If either vertically integrates high-power handlers, Cohu is outgunned.
3. Cycle sensitivity: Revenue dropped from $887M (2021) to $402M (2024) — a 55% decline in a downcycle. Not a quality-compounder in the traditional sense.

#### UK ISA buyability

COHU is a US-domiciled common stock on Nasdaq. Confirmed buyable YES.

#### Portfolio fit

Could replace: India ETF (fills hard-tech/semiconductor cycle blind spot). However, the lack of founder alignment and cyclical nature are a poor fit for the portfolio's compounder DNA.

**Conviction: 3/5** — real structural tailwind, real pipeline, real handler IP, real cash balance. But: no founder alignment (CEO selling), cyclical business model, duopoly competition, pipeline-to-revenue uncertain. Best framing: watchlist / opportunistic name for the AI-test supercycle if the pipeline converts. Not a core compounder.

---

## Rejected / Eliminated Names

| Name | Reason |
|---|---|
| Alphawave Semi (AWE, LSE) | Acquired by Qualcomm December 2025 for ~$2.4B — now a wholly-owned Qualcomm subsidiary. Not investable as standalone. |
| Indie Semiconductor (INDI, Nasdaq) | Revenue flat since 2023 (~$217M both FY2023 and FY2025). Operating loss -$154M on $217M revenue (-71% margin). FCF -$71M. No path to profitability. Low gross margin (~40%) for a chip designer. Eliminated. |
| Semtech (SMTC, Nasdaq) | Recovered well but ~$14B market cap — too large for hidden-gem classification. LoRa is a genuine moat but the scale and the debt from Sierra Wireless acquisition make this a mid-cap macro trade, not a quality compounder. |
| Lattice Semiconductor (LSCC, Nasdaq) | High-quality FPGA business but already widely covered and richly valued. The $1.65B AMI acquisition announced May 2026 is a material integration risk at scale. Watchlist not gem. |
| Silicon Motion (SIMO, Nasdaq) | ADR — likely view-only in UK ISA (same PRIIPs/KID rule as KSPI/IBN). ISA-blocked. Eliminated. |
| Canaan Inc | Bitcoin mining ASIC maker. Speculative, pre-profit, China-domiciled. Not a quality compounder. Eliminated. |
| Cambricon Technologies (688256.SS) | STAR Market China — not accessible to UK ISA via Trading 212. Eliminated. |
| MaxLinear (MXL, Nasdaq) | Revenue collapsed from $1B (2022) to ~$350M (2024) — broadband-chip downcycle. Operating loss -$500M+ in 2024. High debt. Too much execution risk. Eliminated. |
| SiFive (RISC-V IP) | Still private (pre-IPO). Raised $400M Series G at $3.65B in April 2026. Not buyable yet. Watch for IPO in 2026 — would be the most exciting RISC-V edge AI IP play if it comes to market at a reasonable price. |
| Hailo, Kneron, Axelera AI, Mythic | All private. Not investable in ISA. Axelera raised $250M+ Series C (BlackRock) Feb 2026; Mythic raised $125M Dec 2025. Watch for IPOs. |
| Flex Logix, Expedera, Aspinity, Syntiant, Perceive, Eta Compute, Sima.ai | All private. Not investable. |

---

## Cross-signal notes

- CEVA + Arteris together = the IP licensor duo for edge AI. CEVA is the wireless/NPU layer; Arteris is the NoC interconnect. They are complementary, not competing. If adding one from this lane, Arteris (higher alignment, deeper moat on chiplet complexity) is the stronger candidate.
- PDF Solutions is the closest analogue to the "hidden infrastructure platform" pattern (like Veralto in water analytics). Under-covered, compounding revenue, inflecting margins.
- Alphawave was the most exciting LSE-listed name but is now Qualcomm — cautionary tale: UK-listed semi-IP names get acquired rapidly once the moat is proven.
- SiFive IPO (2026) is one to watch. At $3.65B or below, it would be the most exciting RISC-V edge AI IP play in the public market.

---

## Sources

- CEVA 2025 AI Licensing Press Release: https://www.ceva-ip.com/press/ceva-highlights-breakthrough-year-for-ai-licensing-and-physical-ai-adoption-in-2025/
- CEVA NeuPro-Nano Embedded World 2026 AI Award: https://www.prnewswire.com/news-releases/cevas-neupro-nano-npu-wins-artificial-intelligence-award-at-embedded-world-2026-302711611.html
- CEVA $58.5M Public Offering (SEC 424B5): https://www.sec.gov/Archives/edgar/data/0001173489/000143774925035644/ceva20251118_424b5.htm
- CEVA Wireless Market Share 68% IPnest: https://www.prnewswire.com/news-releases/ceva-expands-its-market-share-leadership-in-wireless-connectivity-ip-strengthening-its-solutions-for-smart-edge-aiiot-applications-302220760.html
- CEVA AI Inflection Royalty Model Analysis: https://everyticker.com/quote/CEVA/ceva-s-ai-inflection-why-the-royalty-engine-is-just-starting-to-rev-nasdaq-ceva
- Arteris 4 Billion Chips Milestone: https://www.arteris.com/press-releases/arteris-network-on-chip-technology-achieves-deployment-milestone-of-4-billion-chips-and-chiplets/
- Arteris AMD FlexGen Win: https://www.stocktitan.net/news/AIP/arteris-to-provide-flex-gen-smart-no-c-ip-in-next-generation-amd-ai-blwksuwakkwr.html
- Arteris Q1 2026 Results (+39%): https://www.stocktitan.net/news/AIP/arteris-announces-financial-results-for-the-first-quarter-and-b8xclr4zalgp.html
- Arteris FY2025 8-K (SEC): https://www.sec.gov/Archives/edgar/data/0001667011/000162828026007669/exhibit991fy258-k.htm
- Arteris CEO Karel Janac ownership: https://www.nasdaq.com/articles/with-44-ownership-arteris-inc.-nasdaq:aip-insiders-have-a-lot-at-stake
- PDF Solutions Q1 2026 Results: https://www.globenewswire.com/news-release/2026/05/07/3290527/7239/en/PDF-Solutions-Reports-First-Quarter-2026-Financial-Results.html
- PDF Solutions 20% Growth Guidance 2026: https://seekingalpha.com/news/4551653-pdf-solutions-anticipates-20-percent-revenue-growth-in-2026-as-ai-driven-collaboration-accelerates
- PDF Solutions Exensio Studio AI / Intel Tiber: https://www.stocktitan.net/news/PDFS/pdf-solutions-announces-next-generation-of-its-exensio-ai-ml-hea0ilkok0ee.html
- PDF Solutions Deep Dive Analysis: https://beyondspx.com/quote/PDFS/pdf-solutions-building-the-semiconductor-industry-s-ai-platform-amid-an-investment-inflection-point-nasdaq-pdfs
- Cohu AI Handler Pipeline ($750M): https://www.fool.com/investing/2026/05/27/1-ai-semiconductor-stock-buy-hand-fist-wall-street/
- Cohu Q1 2026 HPC Revenue Growth: https://www.investing.com/news/company-news/cohu-q126-slides-hpc-pipeline-drives-29-revenue-growth-93CH-4651626
- Alphawave / Qualcomm Acquisition: https://awavesemi.com/press-release/alphawave-semi-reveals-suite-of-optoelectronics-silicon-products-addressing-hyperscaler-datacenter-and-ai-interconnect-market/
- SiFive $400M Series G at $3.65B: https://thenextweb.com/news/sifive-400m-series-g-risc-v-ipo
- Nordic Semiconductor / Neuton.AI acquisition: https://www.prnewswire.com/news-releases/nordic-semiconductor-accelerates-edge-ai-leadership-with-acquisition-of-neutonai-302483828.html
