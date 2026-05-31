# Concentration & Correlation Stress-Test

*Informational structural analysis — not investment advice. As of 2026-05-31.*

A 15-line portfolio looks diversified. The question this note answers is whether the **15 names are 15 bets, or a smaller number of bets wearing 15 tickers.** The conclusion, developed below, is the latter: the book is structurally closer to **4–6 independent bets**, and a large majority of it is a single stylistic wager.

---

## 0. The book at a glance

| Holding | Wt | Bucket (nominal) | Real exposure axis |
|---|---|---|---|
| Constellation Software | 12% | VMS | Serial-acquirer compounder (parent of Topicus) |
| ATOSS Software | 9% | VMS | High-multiple quality SaaS |
| Topicus | 9% | VMS | Serial-acquirer compounder (CSU-controlled) |
| Vitec Software | 6% | VMS | Serial-acquirer compounder (Nordic clone) |
| Bachem | 9% | Life-sci supply | Peptide / GLP-1 capex cycle |
| Sartorius Stedim | 6% | Life-sci supply | Bioprocessing capex cycle |
| Eckert & Ziegler | 5% | Life-sci supply | Radiopharma / isotopes |
| Bioventix | 4% | Life-sci supply | Antibody royalty (troponin/vit-D) |
| EXOR | 8% | Holdco | Family compounder, EU industrials/healthcare |
| Investor AB | 7% | Holdco | Family compounder + EQT private exposure |
| Sofina | 3% | Holdco | Private-growth / venture compounder |
| Veralto | 8% | Compliance | Water/quality "razor-blade" quality compounder |
| Secunet | 4% | Sovereignty | German state IT-security |
| iShares MSCI India | 6% | EM Asia | India beta |
| VinaCapital Vietnam VOF | 4% | EM Asia | Vietnam / frontier beta |

Nominal buckets: 5. That is the *apparent* diversification. The rest of this note is about why 5 buckets overstate the independence.

---

## 1. Correlation-cluster map — what actually moves together, and why

The portfolio resolves into a small number of **return drivers**. The clusters below are ranked by how tightly the members co-move and how concentrated the weight is.

### Cluster A — The CSU/TOI serial-acquirer ecosystem (~36% if you include all VMS; ~21% in the controlled core)
**Constellation 12% + Topicus 9%** are not two bets. CSU owns **~30% of Topicus on a fully-diluted basis** and spun it out of its own TSS group — Topicus *is* the European limb of the Constellation playbook, run by overlapping people, capital-allocation philosophy, and culture. When the market re-rates the "buy-and-hold-forever vertical software roll-up" model, these two move as one. **Vitec 6%** is a deliberate Nordic clone of the identical model. **ATOSS 9%** is a different animal mechanically (single-product organic SaaS, not a roll-up) but trades on the *same investor narrative* — German-quality, high-FCF, premium-multiple software — so it shares the multiple-compression risk even if its operations don't.
- **Shared drivers:** software-multiple regime, "quality growth" factor, EUR/CAD software sentiment, rates (long-duration cash flows).
- **Tight sub-cluster (CSU+TOI):** ownership-linked, ~21%. Effectively one company for correlation purposes.
- **Whole-cluster weight: ~36%.**

### Cluster B — The bioprocessing / GLP-1 capex cycle (~15% core, ~24% with the adjacencies)
**Bachem 9% + Sartorius Stedim 6%** ride the *same single cycle*: the build-out and subsequent digestion of biologics/peptide manufacturing capacity. Bachem is a peptide CDMO (GLP-1 tailwind and overhang); Sartorius Stedim sells the bioprocessing consumables/equipment into the same end-customers. Both already shared the 2022–2024 post-COVID destock drawdown together. This is **one wager on biomanufacturing capex**, ~15%.
**Eckert & Ziegler 5%** (radiopharma/isotopes) and **Bioventix 4%** (diagnostic antibody royalties) are *different* sub-industries — but they share the "life-sciences picks-and-shovels" factor, regulatory/reimbursement sensitivity, and the same thematic buyer base. Looser link, but not independent. **Adjacency-inclusive weight: ~24%.**

### Cluster C — Family/holdco compounders with overlapping private-market and EU-healthcare exposure (~18%)
**EXOR 8% + Investor AB 7% + Sofina 3%** are sold as three names but share a *style and look-through*:
- All three are **European family-controlled NAV-discount compounders**. They re-rate/de-rate together on the same lever: **holdco NAV-discount sentiment** (a single factor that whipsaws all three regardless of underlying assets).
- **Private-market duplication:** Investor AB's single largest "engine" exposure is its **~15% anchor stake in EQT** plus a large unlisted/Patricia Industries book; **Sofina** is essentially a fund-of-private-growth/venture vehicle. So a chunk of the "diversified holdco" sleeve is the *same* bet — private-growth/PE marks and exit windows. When private valuations and PE exit activity freeze, Investor AB *and* Sofina take the hit through the same channel.
- **EU-healthcare look-through:** EXOR (Philips, Lingotto), Investor AB (AstraZeneca, Mölnlycke), and the holdcos generally carry meaningful European healthcare — which **double-counts against Cluster B's life-sciences exposure** at the look-through level.

### Cluster D — "Defensive compliance / sovereignty" quality (~12%)
**Veralto 8% + Secunet 4%.** Thematically grouped as non-cyclical "mandated spend." Operationally unrelated (US water/quality instruments vs. German government cybersecurity), so this is the *most genuinely diversified* pair in the book — but both are still **premium-multiple quality-compounders**, so they load onto the same overarching style factor as Cluster A (see §3). Veralto also carries the same life-sciences/pharma-QC end-market that touches Cluster B.

### Cluster E — Emerging Asia beta (~10%)
**iShares MSCI India 6% + VinaCapital VOF 4%.** Genuinely the *most independent* sleeve — different macro regime, different currency (INR/VND), domestic-demand-driven, low correlation to European quality-growth. This is the one place the portfolio actually buys uncorrelated risk. But it is also the smallest conviction sleeve (10%) and India+Vietnam do share an "emerging-Asia risk-on" and USD-funding factor with each other.

### Cross-cutting overlays (the hidden, portfolio-wide correlations)

These don't live in one cluster — they cut across many holdings and are the real source of hidden concentration:

1. **Currency: EUR is the dominant exposure.** ATOSS, Bachem (CHF, EUR-linked), Sartorius Stedim, Eckert & Ziegler, Secunet, Sofina, EXOR (EUR/listed), plus Topicus' European cash flows and much of Investor AB's book are European. A rough tally puts **~55–65% of the book in EUR/CHF terms.** A EUR move, or a Europe-specific shock, hits a majority of the portfolio simultaneously. Only Veralto, the India/Vietnam sleeve, and CSU (CAD/USD) sit outside it.
2. **The "long-duration quality-growth" factor.** VMS cluster, the holdcos, Veralto/Secunet, and the high-multiple life-sci names all share sensitivity to **real long rates and the quality-growth style**. A 2022-style rate/style rotation marks down ~80% of the book through one channel.
3. **Geography: ~75%+ developed-Europe-centric** once holdco look-through is applied. The "global" feel comes mainly from two small EM lines.

---

## 2. Effective number of independent bets (vs. nominal 15)

**Approach.** The intuition: independent bets reduce risk like √N; correlated bets don't. A standard structural proxy is the **effective number of bets**

> N_eff ≈ 1 / Σ(cluster weight)²  *(a Herfindahl on independent risk clusters, the diversification analogue of HHI),*

applied **to the correlation clusters, not the line items**, because line items inside a cluster are near-redundant. I also sanity-check against a participation-ratio intuition (how the variance would actually spread if intra-cluster correlation ≈ 0.7–0.9 and cross-cluster ≈ 0.3–0.5).

**Step 1 — collapse to risk clusters (with judgment weights):**

| Cluster | Weight | Internal correlation |
|---|---|---|
| A. VMS / quality-software ecosystem | 36% | very high (CSU+TOI ~1.0; rest 0.7+) |
| B. Life-sci supply / bioprocessing | 24% | high within Bachem+Sartorius; moderate to E&Z/Bioventix |
| C. Holdco compounders | 18% | high (shared NAV-discount + private-market factor) |
| D. Compliance/sovereignty quality | 12% | low operationally, but style-linked to A |
| E. Emerging Asia | 10% | low vs. everything else (the real diversifier) |

**Step 2 — naïve HHI on these 5 clusters:**
Σw² = 0.36² + 0.24² + 0.18² + 0.12² + 0.10² = 0.1296 + 0.0576 + 0.0324 + 0.0144 + 0.0100 = **0.244**
→ N_eff ≈ 1 / 0.244 ≈ **4.1 clusters.**

**Step 3 — adjust for cross-cluster linkage (the overlays in §1).** Clusters A and D share the quality-growth style; A, B, C, D all share the EUR + long-duration-rate factor; B and C overlap on EU healthcare; C partly *is* private-growth. These positive cross-correlations mean the true N_eff is **below** the 4.1 the clean-cluster math implies. Pulling the developed-Europe-quality clusters partly together and leaving EM Asia (and, weakly, the US-listed defensives) as the only genuinely separate risk:

> **Effective independent bets ≈ 3 to 4, against a nominal 15.**

So the line-item count overstates diversification by roughly **4x**. You are paying the monitoring/complexity cost of 15 positions for the risk-spreading of ~3–4. Stated differently: of the "15," roughly **two are duplicates by ownership (CSU/TOI)**, **two more are duplicates by cycle (Bachem/Sartorius)**, **two-plus are duplicates by factor inside the holdco sleeve (Investor AB/Sofina private-markets)**, and the holdcos double-count the healthcare you already own outright.

*Assumptions shown: cluster definitions and the high/low correlation buckets are structural judgments, not estimated from a return series. The exact N_eff would shift with a real covariance matrix, but the order of magnitude — single digits, not low-teens — is robust to reasonable changes in those assumptions.*

---

## 3. The single-bet framing — how much is one wager?

Strip the labels and ask what *thesis* each holding expresses. The dominant one is:

> **"High-quality, high-return-on-capital compounders, bought at premium multiples, will keep compounding and keep their premium."**

Map the weights onto that single sentence:

- VMS ecosystem (A): **36%** — textbook expression of it.
- Holdco compounders (C): **18%** — same thesis, wrapped in a NAV discount.
- Compliance/sovereignty quality (D): **12%** — same premium-quality-compounder style.
- The high-multiple life-sci quality names (Sartorius, Bioventix, arguably Bachem): **~15% of the book** — again premium quality-growth.

That is roughly **70–80% of the portfolio expressing one stylistic wager**: *quality-compounding, in favour, at a premium multiple, financed by low long-term real rates.* The single biggest risk to the book is therefore **not** any company failing — it is the **style going out of favour** (a 2022-type quality/duration de-rating, or a sustained value/cyclical/rates regime), which would mark down ~three-quarters of the holdings *through the same mechanism, at the same time,* irrespective of business performance.

The genuinely off-thesis weight is small: **EM Asia (10%)**, plus whatever portion of the defensives/EM is truly cyclical-or-value rather than quality-growth. Call it **~10–15% of the book that is *not* the one wager.**

**Bottom line of §3: this is ~75% one bet on a single factor, dressed as five buckets.**

---

## 4. What genuine ballast would do (scenarios, not recommendations)

The portfolio is **long quality-growth, long duration, long Europe, long "things go right."** It has essentially **zero** of the asset types that historically *zig when this style zags*. The absent ballast and what each would structurally change:

**Absent entirely:**
- **Energy / real assets / broad commodities** — the natural hedge against the inflation/rates regime that is *precisely* what de-rates this book.
- **US mega-cap tech / US large-cap broad index** — the portfolio is conspicuously light on the world's largest profit pool and the USD; its "tech" is all European/Canadian small-mid software.
- **Cash / short-duration bonds** — no dry powder, no negative-beta, no convexity to buy the drawdown.
- **Gold / gold miners** — no monetary-debasement or tail hedge.
- **Broad value / cyclical equity** — nothing that *benefits* from the style rotation the book is most exposed to.

**Scenario sketches (qualitative, directional):**

- *Scenario 1 — rates/quality-growth de-rating (2022 redux).* Today: ~75% of the book marks down together through the duration channel; EM Asia (10%) provides thin offset; expect a deep, broad drawdown with little internal dispersion to cushion it. *With 10–20% ballast* (energy + short bonds + gold): the ballast is flat-to-up while equities fall, mechanically shaving the peak-to-trough by roughly its weight-times-its-divergence — turning a, say, ~35% style drawdown into something materially shallower, and crucially giving **rebalancing fuel** to buy the compounders cheap.
- *Scenario 2 — Europe-specific shock (energy, political, EUR stress).* Today: ~55–65% EUR exposure means the book takes it on the chin with few non-European offsets. *With ballast* skewed to USD assets (US tech/index, USD cash): currency and geography diversification directly dampen the hit.
- *Scenario 3 — inflation/cyclical-value regime persists for years.* Today: the book *structurally underperforms* for an extended stretch — not a crash, a grind — because its single factor is out of favour. *With ballast* in energy/real assets/value: a meaningful sleeve actively *earns* in that regime, converting a multi-year drag into something closer to flat.
- *Scenario 4 — risk-on, quality-growth rips.* Today: the book screams higher (this is the upside the concentration is buying). *With 10–20% ballast:* you give up some of that upside — that is the honest cost. Ballast is insurance; in the good state it is a drag.

The trade is explicit: **ballast lowers the ceiling a little to raise the floor a lot and to add rebalancing optionality.** Whether that trade is worth it depends on the holder's tolerance for a deep, *correlated* drawdown and a possible multi-year style winter — not on whether any company is good.

---

## 5. Blunt bottom-line — diversified or diversified-looking?

**Diversified-looking.**

- It *reads* as 15 names across 5 themes and 3 continents.
- It *behaves* as **~3–4 independent bets**, **~75% of which is a single stylistic wager** on premium-multiple quality-compounding in a benign-rates world.
- The diversification it advertises is mostly **cosmetic redundancy**: CSU/TOI are one bet by ownership (~21%); Bachem/Sartorius are one bet by cycle (~15%); the three holdcos collapse onto one NAV-discount + private-markets factor *and* double-count healthcare you already own; and ~55–65% of everything is the same EUR/long-duration trade.
- The only **genuine** diversifiers are the **~10% EM Asia sleeve** and, partially, the US-listed defensive Veralto — and they are the smallest, lowest-conviction parts of the book.

This is a **high-conviction, well-curated, single-factor portfolio.** That is a legitimate way to invest *if it is chosen on purpose* — but it should be understood as **concentration, not diversification.** The fifteen tickers are the *expression* of one view; they are not fifteen views. Anyone holding it should size it, and stress-test it, as the ~3–4-bet, ~75%-one-factor book that it actually is.

---

*Sources for factual linkages used above:*
- *Constellation Software ↔ Topicus ownership/spin-out (~30% fully-diluted): [Topicus spin-out release](https://topicus.com/news/constellation-software-inc-completes-spin-out-of-topicuscom-inc); [CSI Software](https://www.csisoftware.com/category/press-releases/2021/01/05/constellation-software-inc.-completes-spin-out-of-topicus.com-inc); [Wikipedia](https://en.wikipedia.org/wiki/Constellation_Software).*
- *Vitec as Nordic VMS serial-acquirer analogue: [Partnership Investing](https://partnershipinvesting.substack.com/p/vitec-software-vitb-ss-a-swedish).*
- *Investor AB anchor stake in EQT (~14.7%): [MarketScreener](https://www.marketscreener.com/news/anchor-shareholder-investor-ab-acquires-eqt-shares-for-sek-140-million-ce7e5edcda80f72d); [EQT AB — Wikipedia](https://en.wikipedia.org/wiki/EQT_AB).*
