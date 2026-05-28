# Unit Economics

The math that tells you whether the business can work at scale. Not financial modeling — that's later. **Unit economics is the back-of-envelope sanity check** that prevents you from building a business where the math is structurally broken.

A startup with great unit economics can be patient about growth. A startup with broken unit economics scales the breakage and runs out of money.

## The five numbers

You need these on the back of an envelope. Order of magnitude is enough.

### 1. Average Revenue Per User (ARPU)

What does a customer pay you, on average, per period (month or year)?

- For SaaS, the per-month subscription
- For marketplace, the take rate × GMV per active user per month
- For consumer, the average revenue from active user activity per period

### 2. Gross Margin %

For each dollar of revenue, what fraction is left after the direct cost of delivering the product?

```
Gross Margin % = (Revenue − COGS) / Revenue
```

COGS = Cost of Goods Sold = direct cost of delivering the product. For software: hosting, API costs, payment processing, customer support cost per customer. For physical: materials, manufacturing, fulfillment.

**Rules of thumb:**
- SaaS gross margin: 70–85%+ at scale
- Marketplace: 50–80%
- Physical good: 20–60%
- Service: 30–60%

### 3. Churn Rate

% of customers (or revenue) lost per period.

```
Monthly churn % = Customers lost in month / Customers at start of month
```

For SaaS: anything under 5% monthly is reasonable; under 2% is great; under 1% is exceptional.
For consumer subscription: depends on category; media subs 5–10%, fitness 5–15%, etc.

### 4. Customer Acquisition Cost (CAC)

Total cost to acquire one customer.

```
CAC = (Sales & Marketing spend in period) / (Customers acquired in period)
```

Include: ad spend, sales rep cost (loaded), marketing software, travel, paid content, the loaded cost of customer-facing time you spend.

**CAC distinctions:**
- **Blended CAC** — total spend / total new customers, regardless of channel
- **Paid CAC** — only paid-acquired customers
- **Organic CAC** — for free / referral channels, often ~0 marginal cost (but there's still time/content cost)

For PMF assessment, look at all three.

### 5. Lifetime Value (LTV)

The total profit a customer generates over their lifetime.

```
LTV = ARPU × Gross Margin % × (1 / Churn Rate)
```

Or equivalently:

```
LTV = ARPU × Gross Margin % × Average Customer Lifetime (months)
where: Average Customer Lifetime (months) = 1 / Monthly Churn %
```

## The two diagnostic ratios

### LTV / CAC

The single most useful number in pre-PMF unit economics.

```
LTV / CAC > 3:1 = healthy
LTV / CAC > 5:1 = great
LTV / CAC ≈ 1 = breakeven
LTV / CAC < 1 = you lose money on every customer
```

**Why 3:1?** Empirical rule of thumb. The 3 buffers for: future cost increases, future competition lowering pricing power, operational costs not in COGS, capital cost of waiting for LTV to accrue, and uncertainty in your own estimates. At 3:1 you have margin to absorb things going wrong.

### CAC Payback Period

How long does it take to recover the cost of acquiring a customer?

```
Payback (months) = CAC / (ARPU × Gross Margin %)
```

```
< 12 months = excellent
12–18 months = healthy
18–24 months = capital-intensive but workable
> 24 months = either you have massive scale capital, or the model is broken
```

Why payback matters even with healthy LTV/CAC: it determines **how much capital you need to grow**. Long payback = you need a lot of cash to grow because you're financing each customer for many months before they pay back.

## Worked example

A pre-PMF SaaS startup:

- **ARPU** = $200/month = $2,400/year
- **Gross Margin** = 75% (after hosting, API, support)
- **Monthly Churn** = 4% (high — pre-PMF)
- **CAC** = $2,000 (founder-led sales + paid + content)

Compute:

```
Customer lifetime = 1 / 0.04 = 25 months
LTV = $200 × 0.75 × 25 = $3,750
LTV / CAC = $3,750 / $2,000 = 1.88
Payback = $2,000 / ($200 × 0.75) = 13.3 months
```

**Diagnosis:** LTV/CAC is below the 3:1 threshold. The business is structurally weak at scale.

**Levers:**
- **Improve retention** (reduce churn from 4% to 2% → LTV doubles → LTV/CAC = 3.75)
- **Improve ARPU** (raise pricing 25% → LTV climbs 25%)
- **Improve gross margin** (move some support to self-serve → 75% → 85% → LTV climbs 13%)
- **Improve CAC** (organic % rising, founder time more leveraged → CAC drops 30%)

Most successful improvements come from **retention** (reducing churn) because it compounds. A 50% reduction in churn means the customer stays twice as long, which doubles LTV.

## Why pre-PMF unit economics are unreliable

A note of intellectual honesty.

Pre-PMF unit economics are **estimates from a tiny sample** — usually fewer than 50 customers, with low statistical confidence. The numbers will move dramatically as you scale and the *who* sharpens.

Specifically:
- **Churn** in early cohorts is high partly because you're selling to non-desperate customers; once the *who* narrows, churn drops. Don't extrapolate early churn to scale.
- **CAC** in early days is misleading because the founder is doing the selling for free. A real CAC at scale needs to include the loaded cost of a sales rep — which can be 5–10× higher than founder-time.
- **ARPU** in early days is often discounted to get any deals; real ARPU at scale is higher (or lower, depending on whether you stay narrow).
- **Gross margin** in early days is bad because you don't have scale economics yet.

So treat pre-PMF unit economics as **directional** — *can the math plausibly work at scale?* — not as accurate predictions.

The directional check: **if your back-of-envelope at reasonable scale assumptions doesn't show LTV/CAC > 3 and payback < 24 months, the model is structurally broken.** Fixing it requires changing pricing, channel, or *who* — not just executing harder.

## The "rule of 40"

A widely-used metric for evaluating SaaS businesses after PMF:

```
Rule of 40: Revenue Growth Rate % + Profit Margin % ≥ 40%
```

A SaaS company growing 60% per year with -20% profit margin scores 40. A SaaS company growing 20% with +20% margin also scores 40. Below 40 = the business is not financially attractive. Above 40 = healthy growth-margin tradeoff.

For pre-PMF this is irrelevant. For post-PMF it becomes a useful benchmark.

## The traps

| Trap | What it looks like | Why it kills you |
|---|---|---|
| Counting paid acquisition as "growth" | "We added 1,000 customers!" | If LTV/CAC < 3 you're scaling losses |
| Free-tier acquisition in CAC | Reports CAC as $0 (just signups) | True CAC includes activation/conversion cost |
| Excluded support costs in COGS | "Gross margin is 95%" | Support cost per customer at scale is significant |
| Ignoring expansion revenue | LTV underestimates upsell value | Real SaaS LTV often 1.3–2× the base LTV after expansion |
| Using blended numbers when channels differ | One channel is 10× more profitable | Diluted optimization; you're not seeing the seam |
| Treating early numbers as ground truth | "At our CAC of $50…" (founder-led) | Won't survive scaling; need to model loaded-cost CAC |
| Optimistic churn | "5% monthly churn is fine" | Compounds; 5% monthly = ~46% annual = LTV halves |

## Where this lives in the journey

- [Stage 03 — Problem-Solution Fit](../stages/03_problem_solution_fit.md) — the structural unit-economics sanity check before building
- [Stage 04 — Value Hypothesis](../stages/04_value_hypothesis.md) — pricing model in the *how*
- [Stage 06 — PMF Measurement](../stages/06_pmf_measurement.md) — verifying that the math works at the actual customer base

## Source

Standard SaaS literature: David Skok's "For Entrepreneurs" blog. Brad Feld's *Startup Communities*. SaaStr (Jason Lemkin). Bessemer Venture Partners' "State of the Cloud" reports. The unit-economics math is standard; the discipline of using it as a *sanity check rather than a forecast* is what early-stage methodology emphasizes.
