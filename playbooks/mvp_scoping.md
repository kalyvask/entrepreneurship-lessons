# MVP Scoping Playbook

How to decide what's in v1 of your MVP. The most expensive mistakes are made here — overbuilding wastes months, underbuilding kills the test.

## The principle

The MVP is **the smallest possible product that lets you behave like a real business with a real customer using a real product to test the leap of faith.**

Every feature beyond what tests the leap of faith is wasted work. Every feature missing that prevents the customer from completing the value-generating workflow makes the test uninterpretable.

The two failure modes — overbuilding and underbuilding — both kill the test. The discipline is to find the threshold.

## The five-step scoping process

### Step 1 — Restate the leap of faith

Pull it from your value hypothesis (Stage 04). Write it on a sticky note. Stick it next to your screen.

The leap of faith is *the one thing that must be true.* The MVP exists to test it. Every feature decision references back to it.

Examples:

- *"Mid-market vertical farm GMs will treat scheduling optimization as a P1 problem worth a multi-thousand-dollar monthly subscription within 3 months of seeing the product work once."*
- *"Mobile teams currently using cloud LLMs will accept the build-complexity trade-off of an on-device runtime in exchange for not sending user content off-device."*

### Step 2 — List every feature you'd ideally want

In a brain dump. Don't filter yet. Include:

- Core functionality
- Polish (good UX, helpful errors, dashboards)
- Integrations
- Authentication / users / roles
- Reporting / analytics
- Onboarding flows
- Edge cases
- Support tooling

You'll typically end up with 30–60 features.

### Step 3 — Score each feature against the leap of faith

For each feature, ask: **does this directly test the leap of faith?**

Three categories:

- **IN — required to test the LOF.** Without this feature, the customer cannot complete the workflow that generates the data we need. The leap of faith cannot be tested without it.
- **OUT — not in v1.** Polish, integrations, edge cases, nice-to-haves. Goes to backlog.
- **HUMAN — can be done by a human, not built.** Concierge approach. We do the work manually behind the scenes. The customer doesn't know.

A useful rule: **start by trying to put 80% of your list in OUT.** Then bring back features that are *truly* required for the workflow.

### Step 4 — For the HUMAN features, design the concierge backstage

For every feature that could be done by a human, design how. Example:

- Feature: "Smart harvest scheduling that learns over time."
- Build path: 3+ months of ML work.
- Human path: a founder reads the customer's harvest schedule each morning and emails them an optimized version manually. 30 min/customer/day.

The human path lets you test value before you commit to the engineering. If the customer values the manual version, they'll value the automated version. If they don't value the manual version, no amount of ML will save you.

(This is also how you learn what the automation actually needs to do — by doing it manually, you discover the edge cases.)

### Step 5 — Estimate the build time

For everything in IN: estimate the build time.

Honest, realistic, allowing for the things you'll discover during the build that take longer than expected.

**The threshold:** total build time should be **< 3 months.**

If your estimate is over 3 months:

- More features should move to OUT or HUMAN
- Reduce the scope of the IN features (a "lite" version)
- Question whether you've defined the value hypothesis too broadly

If you can't get under 3 months even after cutting hard, the problem is upstream — your value hypothesis is too big. Revisit Stage 04 with a narrower *who* or simpler *what*.

## The reduction principle

A specific course-taught discipline:

> *"When an early adopter sees one benefit they want alongside two they don't, the reaction is 'this isn't for me' or 'I shouldn't pay full price for things I don't need.' Reducing features is the only permitted change to the what."*

In other words: **too many features in your MVP can be as bad as too few.** Early adopters want a sharp, specific, usable answer to their problem — not a bundle of half-built features that solves their problem 80% and adjacent problems 30%.

If you find your MVP needs to be cut down: cut features. Don't add to compensate.

## Worked example

A team building a vertical-farm scheduling tool.

**Leap of faith:** Mid-market vertical farm GMs will treat scheduling optimization as a P1 problem worth $3k/mo within 3 months.

**Brain dump (30 features):**
1. User accounts + auth
2. Multi-user permissions (manager, worker, viewer)
3. Daily harvest assignment view
4. Worker reassignment drag-drop
5. Integration with Argus growing software (data import)
6. Integration with Priva growing software (data import)
7. SMS notifications to workers
8. Email notifications to workers
9. Push notifications via mobile app
10. Mobile app for workers
11. Delivery commitment tracking
12. Waste tracking and analytics
13. Forecasting harvest yields
14. Order management for wholesale customers
15. CSV export
16. Reporting dashboard for management
17. ... (many more)

**After Step 3 categorization:**

**IN (8 features — core workflow, ~10 weeks of build):**
- Single user account (founder onboards each customer manually)
- Daily harvest assignment view (web)
- Drag-drop reassignment
- One integration: Argus only (other systems = OUT for now; manual CSV import as fallback)
- Email notifications to workers
- Delivery commitment tracking (basic)
- CSV export
- Daily debrief panel for the GM (so we can see what they did, when, why — instrumentation for learning)

**OUT (15 features — not in v1):**
- Multi-user permissions
- Priva integration
- Mobile app
- Push notifications
- SMS notifications
- Order management for wholesale
- Reporting dashboard
- Forecasting yields
- Waste analytics
- Most polish

**HUMAN (3 features — done by founder, not built):**
- Setting up the initial schedule (founder spends 2 hours with the GM)
- Resolving conflicts (founder Slack with the GM each morning for the first month)
- "Forecasting": founder eyeballs the yield numbers manually for the first 4 weeks, learns what the customer cares about

**Result:** 10–12 week build of 8 features. Plus 1–2 hours of human work per customer per day. Tests the leap of faith directly.

## Use partners where you must

For features that are necessary for the MVP but not core to your value, **use a partner.** Don't build:

- Auth → Auth0, Clerk, Magic
- Payments → Stripe, Lemon Squeezy
- Email → Postmark, SendGrid, Resend
- SMS → Twilio
- AI → OpenAI, Anthropic
- CRM → Hubspot, Pipedrive
- Analytics → PostHog, Amplitude
- File storage → S3
- Hosting → Vercel, Railway, Render

The build is not where you create value. The value is in the specific thing you're testing. Save build hours for that.

## Use code generation where you can

In 2026, AI-assisted coding (Cursor, Claude Code, Replit) means non-technical founders can ship working MVPs and technical founders can ship 3-5× faster.

- For internal tools: AI generates 70%+ of the code
- For customer-facing UX: AI scaffolds, human polishes
- For backend logic: AI scaffolds, human reviews carefully

Don't ship AI-generated code you don't understand. **Read it. Test it.** But use the leverage.

## Two-week sprint cadence

The build should run on two-week sprints with product reviews at the end. At each review:

1. **What was built?**
2. **What did we learn from customers?** (Yes — even pre-launch — through ongoing concept tests)
3. **What's the next-most-important thing to build *or learn?***
4. **Have we accumulated enough evidence to pivot, persevere, or invest further?**

The sprint cadence forces you to incorporate evidence into the build. Without it, you'll build heads-down for 3 months and miss the chance to change course at week 4.

## Common failure modes

| Failure | What it looks like | Why it kills you |
|---|---|---|
| Overbuilding | 6-month MVP with 15+ features | Too many variables; you can't interpret results |
| Underbuilding | MVP that doesn't let customer complete the workflow | You can't test the LOF |
| Polishing during MVP | Spending 2 weeks on UI polish | Polish doesn't test the LOF; ship rough |
| Building "everything around the LOF" | All the integrations, all the auth | Concierge / HUMAN for non-LOF features |
| No instrumentation | Building product but not the way to measure it | You won't have the data to interpret the test |
| Time-boxing failure | "It'll be 3 months" → it's 6 | Cut scope when you slip; don't extend |
| Multi-feature LOF | One MVP tests 5 different assumptions | Tests are uninterpretable; narrow to one LOF |
| Not using partners | Building auth, building Stripe-equivalent | Wasted time on commodity features |

## Where this lives in the journey

- [Stage 04 — Value Hypothesis](../stages/04_value_hypothesis.md) — leap of faith articulation
- [Stage 05 — MVP Build](../stages/05_mvp_build.md) — the home of MVP work
- [`frameworks/rachleff_pmf.md`](../frameworks/rachleff_pmf.md) — MVP definitions
- [`frameworks/lean_startup.md`](../frameworks/lean_startup.md) — Build-Measure-Learn

## Source

Distilled from Rachleff/Vrionis STRAMGT 514 MVP discipline; Ries's *Lean Startup*; Blank's customer development; Paul Graham's "do things that don't scale."
