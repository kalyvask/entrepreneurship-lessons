# Systematic Ideation — Breaking Functional Fixedness

Most product innovation fails not because people can't generate ideas, but because of **functional fixedness**: the cognitive bias where we see objects and products only in their current form and use. We take things "as they are" and can't imagine alternatives. It is the single biggest barrier to product innovation.

The counterintuitive fix is **structure**. Rather than "think outside the box" (which produces random, hard-to-execute ideas), you "think inside the box" — apply a small set of transformation templates to the components you already have. Function follows form: you make a structural change first, then ask what need it could serve.

The process is two-phase: **Diverge** (create choices — don't evaluate) then **Converge** (make choices). The cardinal rule: *do not evaluate during diverge.* Judging ideas as they appear kills the generative process.

This complements the discovery-driven, problem-first approach in the rest of this repo. Use it when you have an insight and a space, and you're generating candidate product concepts to test — or when you're stuck and your ideas all look the same.

## The five templates

Each template takes the components of an existing product (or workflow, or service) and applies one transformation. For each: list the components → apply the transformation → visualize the result → *then* ask "what need would this serve, and for whom?"

### 1. Subtraction — remove an essential component

Take something the product obviously "needs" and remove it. Then ask what the stripped-down version could be good for.

- **iCloud** removed local storage. The "essential" hard drive is gone; the file lives in the cloud.
- **Google Docs** removed the desktop application. The "essential" installed software is gone.
- Discount airlines removed meals, assigned seats, and free baggage.

The insight: removing what seems essential often reveals a simpler, cheaper, more convenient product for a segment that was overserved by the full version. (This connects to low-end disruption — see [`frameworks/disruption_theory.md`](disruption_theory.md).)

### 2. Task Unification — give a new task to an existing component

Assign a function to a component that wasn't designed for it. Often: make an internal component do external work, or vice versa.

- **reCAPTCHA** unified "prove you're human" with "digitize old books / label training data." The security check does double duty.
- The **Yerka bike** uses the bike's own frame as the lock — the structure that holds the bike together also secures it.
- Loyalty programs make the *customer* do the marketing (referrals).

The insight: components you already have can carry additional jobs, often eliminating the need for a separate product or step.

### 3. Division — separate a component (physically, functionally, or preserving)

Split the product or one of its components and rearrange.

- **Physical division:** foam puzzle-mat tiles (one mat → many connectable pieces). Modular furniture.
- **Functional division:** a washer/dryer stack (one appliance's functions, separated and recombined). Separating the "control" from the "device" (remote controls, then apps).
- **Preserving division:** divide into smaller copies of the whole (a concentrate you dilute; single-serve packaging).

The insight: dividing creates flexibility, modularity, and new usage contexts.

### 4. Multiplication — copy a component, then change it

Duplicate a component and give the copy a different property.

- **Multi-blade razors** (copy the blade, angle each differently).
- **Duraflame log variants** (copy the log, change the burn profile / scent / duration).
- Dual-camera phones (copy the lens, change the focal length).

The insight: a modified copy often unlocks a capability the single original couldn't deliver.

### 5. Attribute Dependency — create a dependency between two attributes

Make one attribute change as a function of another. "As X changes, Y changes."

- **Transition lenses** — tint depends on ambient light.
- A gym that charges you *more if you don't show up* — price depends on attendance (inverting the normal dependency).
- Surge pricing — price depends on demand.

The insight: dependencies that didn't exist before create products that adapt, personalize, or align incentives in new ways.

## The diverge → converge discipline

**Diverge (generate):**
- Apply each template to your product's components, one at a time.
- Generate without judging. "Bad" ideas are fuel; an impractical first form often contains a workable kernel.
- Aim for volume. The 20th application of a template is often where the surprising idea appears.
- Capture everything.

**Converge (select):**
- *Now* evaluate. Which generated concepts map to a real, severe customer need? (Cross-reference your customer discovery and value-prop canvas.)
- Which are painkillers, not vitamins? (See [`frameworks/value_dimensions.md`](value_dimensions.md).)
- Which can you actually build and test cheaply?
- Take the survivors into the validation sequence (see [`playbooks/validation_sequence.md`](../playbooks/validation_sequence.md)).

## When to use this — and when not to

**Use it when:**
- You have an insight and a space but your candidate product concepts all look the same
- You're early in solution-shaping (Stage 03) and want a wider set of options before committing
- You're stuck — every idea is an incremental version of the obvious one
- You're looking at an existing product/workflow and asking "what else could this be?"

**Don't use it:**
- As a substitute for customer discovery. These templates generate *candidate solutions*; whether anyone is desperate for them is still an empirical question you answer in the market.
- To "brainstorm your way to an idea" before doing the research. The repo's whole thesis (see [`frameworks/rdi.md`](rdi.md)) is that ideas should be harvested from research, not manufactured at a whiteboard. Use these templates to *expand the solution space around a researched insight* — not to replace the insight.

## How it fits the repo's philosophy

The rest of this library is problem-first: find a desperate customer, then build. These templates are a *solution-generation* aid for the moment when you have the problem and need a wider set of candidate solutions to test. They produce options; the market picks the winner.

The danger is using ideation as procrastination — generating clever product concepts instead of talking to customers. Hold the discipline: **generate concepts with templates, then immediately test them against real desperate customers.** The template gives you the *what* to test; the customer tells you if it's right.

## Where this lives in the journey

- [Stage 01 — Insight and Idea](../stages/01_insight_and_idea.md) — expanding the solution space around an insight
- [Stage 03 — Problem-Solution Fit](../stages/03_problem_solution_fit.md) — generating candidate solution shapes
- [`frameworks/disruption_theory.md`](disruption_theory.md) — Subtraction maps to low-end disruption
- [`frameworks/value_dimensions.md`](value_dimensions.md) — converge on painkillers, not vitamins

## Source

The "Thinking Inside the Box" / Systematic Inventive Thinking templates (Subtraction, Task Unification, Division, Multiplication, Attribute Dependency) are from Drew Boyd and Jacob Goldenberg's *Inside the Box* (2013), grounded in Genrich Altshuller's TRIZ. The functional-fixedness framing is standard cognitive psychology (Duncker). Taught in product launch and innovation curricula.
