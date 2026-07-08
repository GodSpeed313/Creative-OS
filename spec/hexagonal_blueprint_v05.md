# HEXAGONAL BLUEPRINT
Node Validation & Mapping Document
Creative OS — Standalone Implementation
Version 0.12 — Dogfood stress test complete through the alt-branch's actual ending (Section 9)

**Changes from v0.11:**
Traced the rest of the alt-branch: Ch.13's remainder, all of Ch.14, and its epilogue — the manuscript's actual ending. Cassie fires her first Z in either branch (ends her Z-free-since-Ch.2 streak). Tested whether G fires at the literal last page of a finished 14-chapter-plus-epilogue story — it does not, because the ending is deliberately ambiguous rather than resolved; logged as a new open question (the node set may not yet cover thematically-open endings). Also self-caught and corrected a trace-authoring mistake: Valeria's Ch.12 Z was mistagged `Truncated` instead of `Complete`, which left it stuck open in the deferred-Z list since `deactivate()` doesn't clear deferrals — fixed and re-traced, noted rather than quietly patched.

**Changes from v0.9 → v0.11 (Section 9, first two passes):**
Engine extended with `flag_physics_violation()` on `NodeEngine`, mirroring the existing auto-detected Lore Creep mechanism — Ruling 6.7 defined a conviction-change test in prose from the start, but nothing before now let the engine formally *record* a violation of it. Used it once, for real: the other manuscript draft's own Ch.7–8 ("The Fallout of Angels" / "Doctrine of Silence"), forked at the shared Ch.6, reintroduces Thorne in a fully-recommanded, cold operational state with no on-page event earning a reversion from the confessor state Ch.6 (already traced, shared, committed as Trace 006) left him in. First formally-recorded PHYSICS_VIOLATION in the corpus. Stress test then continued through this branch's own Ch.9–13, including its Ch.12 climax (the densest scene in either draft) — still zero Lore Creep, with a traceable reason why (Z brackets neatly around the decisive-action beat, never overlapping another node-level event). A(Valeria+Thorne) activates in Ch.12 and structurally deactivates in Ch.13 — contrast the canonical branch, where it's left open through Ch.9. See Section 9.

**Changes from v0.8 → v0.9 (Trace 009 Part 1):**
Trace 009 Part 1 added: Diane Foster (the Ch.7/Ch.8 checkpoint woman) named; Thorne's Ch.8 ambiguous fate resolves to CONFIRMED ALIVE, sentenced as a permanent witness/pariah rather than killed by the crowd — closes that half of the open question, but A(Valeria+Thorne) itself stays active/unresolved (a crowd verdict about Thorne isn't a personal resolution between him and Valeria). F still does not fire. The manuscript itself cuts off mid-scene, before Thorne answers whether the Hum's spread is permanent — no node fires on an answer that doesn't exist yet. Awaiting Part 2 before this trace or the corpus summary can be called complete for Ch.9.

**Changes from v0.7 → v0.8 (Trace 008):**
Ruling 6.10 issued: τ confirmed to fire on a non-approach, agency-driven transition (Thorne's confession arc, Ch.8) — resolves the hunt open since Ch.5 | Trace 008 added (Ch.8 — A(Valeria+Thorne) finally activates on physical co-location; Thorne's first personal Z fires, Complete but fate left ambiguous, not terminal; Valeria's Truncated Z from Ch.3 resolves via Ruling 6.4's deferral clause; D-composition event #3 — a split, not exit or addition; F still does not fire; Manuscript Defect 8.1 logged — Cassie present in the Aegis Suite with no described entry, contradicting Ch.7's stated headcount)

---

## Status Legend

- 🔒 Locked — validated and confirmed, do not change without a story scenario that breaks it
- ✅ Validated — confirmed through source material or cross-reference
- 🔒 Assigned — defined by spec author, flagged for story-scenario promotion
- ❌ Undefined or Redundant — cannot be used until resolved

---

## Section 1: Creative OS Node Definitions

Node set expanded from 7 to 8 based on 3-scenario evidence confirmation (Ruling 6.6).

| Node | Creative OS Name | Active When | Inactive When | Status |
| --- | --- | --- | --- | --- |
| G | Narrative Coherence | All active story threads resolve; character arcs land; thematic intent fulfilled | Any thread unresolved or arc incomplete | 🔒 Locked |
| F | Near-Coherence | One thread unresolved or one arc incomplete; story approaching resolution | More than one thread unresolved; or G is already active | 🔒 Locked |
| W | Narrative Equilibrium | Story is stable; no active tension pulling toward resolution or collapse | Active tension detected; story is in motion toward G or H | 🔒 Locked |
| A | Thematic Symmetry | Two opposing narrative forces enter into staged tension at the entity level | One force structurally resolves the other; the tension is no longer generative | 🔒 Locked |
| Z | Story Checkpoint | Narrative pauses and confirms its own coherence before continuing | Narrative is in active motion; no pause required | 🔒 Locked |
| H | Narrative Boundary | Outermost reach of story world; no defined structure exists beyond this point | Story is operating within defined structural bounds | 🔒 Locked |
| S | Thread Convergence | Multiple story threads actively merging toward a point of unification | Thread-unification completes; external events may force completion but do not constitute it | 🔒 Locked |
| D | Unified Pursuit | The merged narrative unit moves forward together toward a defined shared goal — S has completed but G and F have not fired | G fires (full resolution); F fires (resolution approaching); or shared goal is abandoned | 🔒 Locked |

↳ Adjacency rule: every node must have at least one defined adjacent node before it can fire. No isolated activations.
↳ Simultaneous activation limit: maximum 3 nodes active at once without Z (Checkpoint) firing first. Exceeding this triggers Lore Creep.
↳ Floor nodes (π and any project-elevated H per Ruling 6.1) do not consume an activation slot.
↳ D auto-activates when S deactivates with a shared goal still active. This is a deterministic engine rule, not a manual trace event.

### Node Notes — A *(from v0.4)*

A can activate in a tilted state. Activation and balance are separate events. Record pole, register, and armor status at activation. Track A maturation across instances.

### Node Notes — Z *(from v0.4)*

Z fires in three modes: **Complete**, **Truncated**, **Partial/External**. See Ruling 6.4 for deferral-resolution clause.

**Z variant watch (updated in v0.6):** Thematic chapter-close beats logged as δ — two confirmed instances: Ch.3 tunnel close and Ch.5 (*"the truth didn't just hurt. It cleansed."*). Pattern: narration landing thesis before story continues. Z fires at character-level identity-collapse, not at thematic-statement moments. One more instance = ruling threshold met. Watch Ch.7–13.

### Node Notes — D

D is the structural state between convergence and resolution. S tracks the act of merging; D tracks the merged unit in motion; G/F track the approach to and arrival at resolution.

D activation is deterministic: when S completes with a shared goal still active, D fires. There is no story scenario in which S completes with a live goal and D does not fire — the merged unit must be in some structural state, and that state is D.

D deactivates when G fires (all threads resolved) or F fires (resolution in sight). Do not deactivate D based on external pressure — that is a forcing function, not a cause.

**Veritas evidence (3 appearances):**
- Ch.3 mob_invades: D activates (S completed, Shadow Ledger + Thorne still the shared goal)
- Ch.4 throughout: D persists (no resolution in sight; unified pursuit is the structural engine)
- Ch.5 throughout: D persists (Truth Bomb is a step, not the resolution; Thorne still operational)

---

## Section 2: Greek Flow Markers

| Marker | Creative OS Role | Fires When | Source | Status |
| --- | --- | --- | --- | --- |
| π | Ground State Anchor | Always present — structural floor of the entire system | Extracted | 🔒 Locked |
| α | Transition Begins | A node state transition is initiated | Extracted | 🔒 Locked |
| δ | State Shifts | A node state has changed; the shift itself is being marked | Extracted | 🔒 Locked |
| τ | Duration-Dependent Transition | A transition is timebound; state change requires full scene duration to complete | Assigned | 🔒 Locked |
| σ | Pressure / Conflict Path | A path is under active narrative pressure or conflict | Assigned | 🔒 Assigned |
| γ | Generative Marker | A new state is being created rather than transitioned into | Assigned | 🔒 Assigned |

↳ τ promoted to 🔒 Locked: two independent confirmations (Ch.1 boardroom — professional confrontation; Ch.3 drive — kinetic action sequence). Both were approach sequences; watch for τ in retreat or aftermath contexts to confirm the definition is general.

**τ agency note (new in v0.6):** τ requires character agency. Hum-compelled state transitions do not qualify — the character lacks agency in the transition. Thorne's commander→confessor shift (Ch.6) is the test case: real and timebound, but compelled not earned. It does not falsify the τ–approach-sequence coupling. τ remains at 4/4 approach sequences. The hunt for a non-approach earned transition continues through Ch.7–13.

**Sustained α observation (new in v0.5):** Ch.4 stealth/escape sequence is the longest sustained α in the traces — multiple scene beats with no δ landing. If this pattern appears again, it may warrant marker distinction. Not a ruling yet; one instance.

---

## Sections 3–5 *(unchanged from v0.4)*

See `spec/hexagonal_blueprint_v04.md` for Constraint Map, Failure Mode, and Physics Node Reference.

---

## Section 6: Rulings

### Ruling 6.1 — H Persistence *(confirmed v0.3)*
H becomes floor status when premise permanently dissolves structural bounds. Applies to Veritas.

### Ruling 6.2 — A Granularity *(confirmed v0.3)*
A tracks per-entity. Multiple instances independent. Slot count tracks node type, not instance count.

### Ruling 6.3 — S Deactivation *(confirmed v0.4)*
S deactivates on merge-completion. Forcing function and completion are separate events. Annotate both.

### Ruling 6.4 — Z States *(confirmed v0.4)*
Z fires in three modes: Complete, Truncated, Partial/External. Deferral-resolution clause: sealed scene + self-confessed + no interruption available = completion fires.

### Ruling 6.5 — A Activation vs Balance *(confirmed v0.4)*
A can activate tilted. Tilt carries armor-status information. Track maturation across instances.

### Ruling 6.6 — Unified Pursuit: D Node (Resolved in v0.5)

**Issued:** Veritas Ch.3 trace (v0.4 — open flag)
**Resolved:** Veritas Ch.5 trace (v0.5 — formalized)

**Ruling:** D (Unified Pursuit) is a defined node in the Creative OS node set. It is the structural state in which a merged narrative unit (post-S) moves forward together toward a defined shared goal before resolution is in sight (pre-F/pre-G).

**Activation rule (deterministic):** D auto-activates when S deactivates with a shared goal still active. This is a consequence rule — it does not require manual trace annotation. The engine fires D when the S-deactivation condition is met.

**Deactivation rule:** D deactivates when G fires (full resolution) or F fires (resolution approaching). Do not deactivate on external pressure.

**Evidence:** Three consecutive chapters (Ch.3, Ch.4, Ch.5) where unified pursuit was the structural engine of the narrative and no existing node tracked it. The null-gap was load-bearing across the middle act of Veritas, not incidental.

**Null-gap approach (from v0.4):** The engine's post_s_gap logging is replaced by D auto-activation. The gap was the evidence base; D is the formalization.

### Ruling 6.7 — Hum-Compelled Disclosure *(confirmed v0.6)*

**Issued:** Veritas Ch.6 trace

**Ruling:** The Hum compels **disclosure**, not **conviction**. Physics-integrity checks whether a character's values and operative belief hold — not whether hidden facts, costs, or fears surface. A character who reveals motivations, regrets, or costs under Hum compulsion is not in physics violation if their underlying conviction remains intact. Drift fires only when values soften; not when concealment fails.

**Test:** Does the character's core thesis — what they believe they would do and why — change? If yes: PHYSICS_VIOLATION or IDP. If no: forced disclosure, physics-consistent.

**Evidence:** Thorne's Ch.6 confession to Chen. He names Marcus Reeves, admits fear as his motivation, discloses the full cost of the trials. Conviction intact throughout: *"the Hum is finally doing what I wanted it to do"* / *"I knew it would hurt them. I did it anyway."* He walks into the hallway to face consequence — not to recant the act. Disclosure of cost ≠ change of conviction. Ch.6 is clean under this ruling.

**Corollary for τ:** Hum-compelled state transitions do not qualify as τ. τ marks duration-dependent earned transitions — state changes requiring character agency across a full scene. Compelled transitions are a distinct category: forced disclosure events. They are neither τ nor PHYSICS_VIOLATION.

**M3 pre-load:** The Thorne shelter letter (*"reads too kind relative to physics ceiling"*) is the other pole. Ch.6 confession = forced disclosure (physics-consistent). If the shelter letter shows softened conviction — recanting the act, not naming costs — that is value-drift (IDP territory). Ruling 6.7 settles the test before M3.

**Evidence (extended, v0.7):** Ch.7 subway checkpoint — the Purified force Cassie to disclose "Cassandra Monroe, founder of Monroe Consulting" under Hum compulsion. Her core thesis (already committed to exposure since Ch.3) does not change; this is compelled disclosure of already-implicit complicity, not a conviction collapse. Confirms the test generalizes across characters, not just Thorne. Cassie remains Z-free since Ch.2.

### Ruling 6.8 — Sustained α as Distinct Marker *(confirmed v0.7)*

**Issued:** Veritas Ch.4 trace (v0.5 — one instance flagged)
**Resolved:** Veritas Ch.7 trace (v0.7 — third instance confirmed)

**Ruling:** Sustained α — a chain of multiple scene beats accumulating narrative pressure with no δ landing between them — is a distinct trace-worthy pattern, not merely repeated ordinary α firings. It marks an extended transition sequence (typically travel/montage structure) where tension accrues across several discrete beats before a single δ resolves the whole chain at once.

**Evidence:** Three confirmed instances — Ch.4 City Hall Station sequence (stealth/escape, δ lands at Thorne.pdf), Ch.6 technician cascade (headsets off/confessions, δ lands at "commander → confessor"), Ch.7 city-crossing montage to Tribune Building (church/pharmacy/patrol/Cassie-spiral/suicide beats, δ lands at TV sighting of Thorne). A fourth instance appears in the same chapter (march to Federal Building, δ lands at "Let them pass"), reinforcing rather than founding the pattern.

**Encoding note:** Sustained α does not consume an additional slot and is not itself a node — it is a marker-chain annotation on top of whatever nodes are already active (here, A/D throughout). Trace it as a bracketed span from first beat to landing δ.

### Ruling 6.9 — Z-Variant: Thematic Chapter-Close *(confirmed v0.7)*

**Issued:** Veritas Ch.3 trace (v0.4 — one instance flagged)
**Resolved:** Veritas Ch.7 trace (v0.7 — third instance confirmed)

**Ruling:** A narration-voice thematic statement landing at a chapter's close is its own trace-worthy variant, distinct from character-level identity-collapse Z. No character pauses to confirm their own coherence; the narrative itself states its thesis before continuing. Do not conflate with true Z — Z remains reserved for character-level identity-collapse per Ruling 6.4.

**Evidence:** Three confirmed instances — Ch.3 tunnel close (α fired toward Ch.4, darkness), Ch.5 close (*"the truth didn't just hurt. It cleansed."*), Ch.7 close (*"It wasn't just pressure anymore. It was anticipation. The reckoning had begun. And this time, there would be no spin."*).

**Encoding note:** Tag as δ(thematic) at chapter-close. Does not consume a node slot, does not fire Z.

### Ruling 6.10 — τ Beyond Approach Sequences *(confirmed v0.8)*

**Issued:** Veritas Ch.5 trace (v0.6 — hunt opened after 4/4 approach instances)
**Resolved:** Veritas Ch.8 trace (v0.8 — non-approach instance confirmed)

**Ruling:** τ is not limited to physical approach sequences. It fires on any duration-dependent, agency-driven transition — the defining features are (1) the state change requires the full span of the scene to complete, and (2) the character has genuine agency in it. Physical approach (boardroom walk-up, drive, chandelier escape, crane climb) was simply the first shape τ happened to take in this manuscript; it is not part of the definition.

**Test against Ruling 6.7's corollary:** Ruling 6.7 disqualified Thorne's Ch.6 commander→confessor shift from τ because it was Hum-*compelled* — no agency. Thorne's Ch.8 confession arc is different in kind: he chooses what to reveal, chooses the frame ("this was policy, not one man"), and chooses to walk out and face the crowd rather than flee via the Cleaners (explicitly available, explicitly declined). Compulsion (can't lie) and agency (what to do about it) are not mutually exclusive — Ch.8 is the proof.

**Evidence:** Spans `ch8.thorne_badge_i_was_wrong` (the transition begins — "I was wrong. Not about the goal. About the cost.") through `ch8.thorne_public_confession_oncamera` (the transition lands — full on-camera confession, Z fires in the same beat). Duration: the greater part of the chapter. Fifth τ instance overall; first non-approach.

**Co-occurrence with Z:** τ and Z fired together once before (Ch.1 boardroom). Ch.8 repeats the pattern — a duration-dependent transition landing exactly at the moment a character's identity-collapse completes is not a coincidence, it's the expected shape when τ marks earned change rather than forced disclosure.

---

## Section 7: Story Scenario Traces

### Trace 001 — Veritas, Prologue + Chapter 1 *(v0.3)*

All 7 node definitions held. Z fired naturally in boardroom. H Persistence and A Granularity rulings issued.

### Trace 002 — Veritas, Chapter 2 *(v0.4)*

Z fired naturally in apartment (personal coherence check). No Z in office (no false self to confirm). S α fired at chapter close.

### Trace 003 — Veritas, Chapter 3 *(v0.4)*

S fully activated and deactivated. Z truncated at bank confrontation (mob invades mid-confirmation). D auto-fires at ch3.mob_invades. A(Cassie+Valeria) activates tilted in tunnel. 3-node limit at bank held.

### Trace 004 — Veritas, Chapter 4 *(revised v0.6)*

**Date:** 2026-06-06
**Result:** Z Complete (Valeria) fires in-scene at foreman's trailer — Thorne identity collapse. Peak slot 3. Sustained α through City Hall Station sequence (first sustained-α instance). τ at chandelier escape (3rd approach instance). Manuscript Defect 5.1 noted: acoustic maps + St. Jude's also staged in Ch.5 (stitch artifact); traced as-written.

| Scene | Nodes Active | Markers | Slots |
| --- | --- | --- | --- |
| Tunnel — PSH confession | A, D | α, σ | 2 |
| City Hall Station — catatonic victims, Cleaners | A, D | σ peak, sustained α | 2 |
| Chandelier escape | A, D | τ (3rd instance — approach) | 2 |
| Foreman's trailer — Thorne.pdf | A, D, Z | Z fires (Complete, entity=Valeria) | 3 |
| Z resolves in-scene | A, D | δ | 2 |
| Iron door breached — flee | A, D | σ | 2 |

**Manuscript defects logged:** Defect 5.1 (scene duplication — acoustic maps + St. Jude's also staged in Ch.5 as-written); Defect 5.2 (kinetic break at Ch.4→Ch.5 seam — WANDER_ALARM_KINETIC_DEVIATION-class). Recommended fix: collapse dual Toughbook staging into Ch.4.

### Trace 005 — Veritas, Chapter 5 *(revised v0.6)*

**Date:** 2026-06-06
**Result:** Miller Z Complete/terminal at crane — first terminal Z in corpus. D-composition event (Miller exits merged unit; D persists with Valeria+Cassie). Acoustic maps γ and St. Jude's δ in Ch.5 as-written (Defect 5.1). γ fires at Truth Bomb. Z variant watch: 2nd instance at chapter close.

| Scene | Nodes Active | Markers | Slots |
| --- | --- | --- | --- |
| Construction site exterior | A, D | σ | 2 |
| Acoustic maps [Defect 5.1 — as-written] | A, D | γ | 2 |
| St. Jude's logs [Defect 5.1 — as-written] | A, D | δ | 2 |
| Helicopter — flashbangs | A, D | σ peak | 2 |
| Crane climb | A, D | τ (4th instance — approach) | 2 |
| Crane — Miller Z fires (Complete, terminal) | A, D, Z | Z fires | 3 |
| Miller falls — Z resolves | A, D | δ (terminal) | 2 |
| Truth Bomb | A, D | γ | 2 |
| Chapter close | A, D | δ | 2 |

**Z variant watch note:** 2nd instance (Ch.3 tunnel close + Ch.5 close). One more = ruling threshold.
**Terminal Z flag:** First in corpus (entity=Miller). Sub-mode ruling held — two more instances needed.
**D-composition event #1:** Miller exits merged unit. D persists with Valeria+Cassie.

### Trace 006 — Veritas, Chapter 6 *(v0.6)*

**Date:** 2026-06-06
**Result:** D persists across Thorne POV shift — confirmed. A(Valeria+Thorne) deferred to Ch.8 (phone call is α, not A — entity-level co-location not met). No Z for Thorne — St. Jude's memory is flashback/contextualization, not in-scene identity collapse. F does not fire. No new nodes. Slot count 2 throughout. Ruling 6.7 applied: Thorne confession = forced disclosure, physics-consistent.

| Scene | Nodes Active | Markers | Slots |
| --- | --- | --- | --- |
| Aegis Suite opens — Thorne POV | A, D | δ (POV shift) | 2 |
| Knox badge + Shadow Ledger broadcast | A, D | δ | 2 |
| Chen refuses Omega-Seven | A, D | δ (command structure fractures) | 2 |
| Technician cascade — headsets off, confessions | A, D | sustained α (2nd instance) | 2 |
| St. Jude's memory — Marcus Reeves | A, D | σ | 2 |
| Valeria's call (breached channel) | A, D | α (toward A(Valeria+Thorne)) | 2 |
| Thorne steps into hallway | A, D | δ (commander → confessor, Hum-compelled) | 2 |

**Key rulings confirmed:** D persists across POV shift. A(Valeria+Thorne) fires at Ch.8. Thorne's confession is forced disclosure (Ruling 6.7) — not PHYSICS_VIOLATION. Commander→confessor shift is Hum-compelled, not τ (Ruling 6.7 corollary). Sustained α: 2nd instance — one more = ruling watch.

### Trace 007 — Veritas, Chapter 7: Power, Parse, Path *(v0.7)*

**Date:** 2026-07-08
**Result:** F does not fire — the Shadow Ledger decryption widens scope (25-year, $8B, 12-city consortium) rather than approaching resolution. Cassie's forced disclosure at the Purified checkpoint (identity as Monroe Consulting's founder) extends Ruling 6.7 to a second character — disclosure of complicity without conviction-change; Cassie remains Z-free since Ch.2. D-composition event #2: Rachel Díaz + camera crew join the merged unit at Tribune Building (an addition, contrasting with Miller's Ch.5 exit). γ fires at Shadow Ledger decryption (new state: the consortium map didn't exist in the narrative before). Sustained α hits its 3rd confirmed instance (city-crossing montage to Tribune) — Ruling 6.8 issued; a 4th instance (march to Federal Building) reinforces it in the same chapter. Z-variant thematic chapter-close hits its 3rd confirmed instance ("no spin") — Ruling 6.9 issued. τ: no new instance, remains 4/4 approach sequences; hunt continues to Ch.8+. Valeria's Truncated Z (Ch.3) remains open, still deferred to Ch.8. No Lore Creep violations — slots held at 2 (A, D) throughout.

| Scene | Nodes Active | Markers | Slots |
| --- | --- | --- | --- |
| Tunnel crawl (Ch.6 aftermath, Miller grief) | A, D | σ | 2 |
| Subway checkpoint — Cassie compelled disclosure (Monroe Consulting) | A, D | δ (Ruling 6.7 extended — disclosure, not Z) | 2 |
| Surface — burning city, Truth Hangover victims | A, D | σ | 2 |
| City-crossing montage to Tribune (church/pharmacy/patrol/Cassie spiral/suicide) | A, D | sustained α (3rd instance — Ruling 6.8) | 2 |
| TV sighting — Thorne hasn't fled | A, D | δ (lands the sustained-α chain) | 2 |
| Tribune Building — Rachel Díaz + crew join | A, D | δ (D-composition addition #2) | 2 |
| Shadow Ledger decryption (Marcus Chen) | A, D | γ (new state: consortium map) | 2 |
| Strategic pivot — confession before broadcast | A, D | α | 2 |
| March to Federal Building (patrol, crowd, "let them pass") | A, D | sustained α (4th instance — reinforcing) | 2 |
| Federal Building doors — Valeria's identity-callout, Thorne's cryptic reply | A, D | σ | 2 |
| Elevator rising — chapter close | A, D | δ (thematic — 3rd instance, Ruling 6.9) | 2 |

**Key rulings confirmed/issued:** Ruling 6.8 (sustained α, 3rd instance). Ruling 6.9 (Z-variant thematic close, 3rd instance). Ruling 6.7 extended to Cassie. F does not fire. τ hunt continues. Deferred Valeria Z remains open to Ch.8.

### Trace 008 — Veritas, Chapter 8: The Consortium *(v0.8)*

**Date:** 2026-07-08
**Manuscript Defect 8.1 logged:** Ch.7 closes with only Valeria, Rachel, and the camera operator entering the Federal Building ("Valeria, Rachel, and the camera operator stepped inside. The door locked behind them"). Ch.8 has Cassie present and speaking in the Aegis Suite with no described entry. Traced as-written; the gap is flagged, not silently patched.

**Result:** A(Valeria+Thorne) activates — physical co-location finally met, deferred since Ch.6 ("phone call is α, not A"). Not tilted; direct adversarial confrontation. Thorne undergoes his first personal Z (Complete) — an earned, agency-driven identity collapse spanning most of the chapter, distinct from Ch.6's Hum-compelled disclosure. His fate is left ambiguous at chapter close (crowd erupts in confusion, not consensus) — **not** confirmed terminal, unlike Miller's Ch.5 Z; does not count toward the terminal-Z sub-mode ruling. A(Valeria+Thorne) remains active and unresolved at chapter close — an open thread into Ch.9. Valeria's Truncated Z from Ch.3 **resolves** here via Ruling 6.4's deferral clause (sealed scene + self-confessed + uninterrupted, once Rachel and Cassie depart) — no deferred Z remain open in the corpus. τ fires its 5th instance here, and it is the first **non-approach** instance — Ruling 6.10 issued, resolving the hunt open since Ch.5. γ fires at the consortium naming (new state: full authorization network on record), but F still does not fire — this confirms scale already known from Ch.7's decryption rather than narrowing toward resolution; six chapters of aftermath remain untouched. D gains a third composition event: a **split** (Rachel + Cassie depart for the broadcast, Valeria stays with Thorne) — D persists across both branches, new evidence that D tolerates separated membership without deactivating. No Lore Creep violations across the full corpus; peak slot count 3 (A+D+Z, at Thorne's confession).

| Scene | Nodes Active | Markers | Slots |
| --- | --- | --- | --- |
| Elevator ascent — dialogue on Thorne, her father, certainty vs. truth | A, D | σ | 2 |
| Aegis Suite — Thorne confronted, A(Valeria+Thorne) activates | A, D | δ (co-location finally met) | 2 |
| Cassie confronts the casualty-rate lie | A, D | δ (Ruling 6.7 pattern continues) | 2 |
| Thorne, badge in hand — "I was wrong. Not the goal. The cost." | A, D | τ begins (5th instance — non-approach) | 2 |
| Full consortium named on camera | A, D | γ (new state: authorization network) | 2 |
| Hard drive handed to Cassie | A, D | δ | 2 |
| Broadcast-before-confession deadline set (8:30 PM) | A, D | α | 2 |
| Rachel + Cassie depart; Valeria stays | A, D | δ (D-composition event #3 — split) | 2 |
| Valeria's uninterrupted confession to Thorne | A, D | δ (deferred Z resolves — Ruling 6.4) | 2 |
| Thorne recounts the final call with Thomas Knox | A, D | τ continues, σ | 2 |
| Public on-camera confession — full consortium testimony | A, D, Z | Z fires (Complete, entity=Thorne); τ lands (Ruling 6.10) | 3 |
| Purified mark him — fate left ambiguous | A, D | δ (Z resolves, not terminal) | 2 |
| Three Purified confront Valeria; she explains, they leave | A, D | σ | 2 |
| Broadcast confirmed — chapter close | A, D | δ (thematic — 4th instance, reinforcing Ruling 6.9) | 2 |

**Key rulings confirmed/issued:** Ruling 6.10 (τ beyond approach sequences — hunt resolved). A(Valeria+Thorne) activates. Thorne's first Z — Complete, not terminal, fate ambiguous. Valeria's Ch.3 deferred Z resolves — zero deferred Z remain. D-composition event #3 (split). F still does not fire. Manuscript Defect 8.1 logged.

### Trace 009 (Part 1) — Veritas, Chapter 9: The Judgment *(v0.9 — MANUSCRIPT INCOMPLETE)*

**Date:** 2026-07-08
**Status:** Traced fragment only. The chapter as provided ends mid-scene — "Thorne looked at the man for a long moment before he answered, and Valeria understood... that whatever came out of his mouth next was going to matter more than everything he'd already confessed." No text exists past this point. Do not treat Ch.9 as complete or fold it into a Ch.1–9 corpus summary until Part 2 arrives.

**Result:** D confirmed fully reconsolidated entering this chapter (Rachel + Cassie returned to the Aegis Suite window by Ch.8's actual close). The Ch.7/Ch.8 checkpoint woman is named for the first time — **Diane Foster**, a former public defender. Diane rules on Thorne's fate before the crowd: he lives, becomes a mandatory witness against the rest of the consortium, and is released once exhausted of value — "not forgiveness... a sentence with no end date." This **confirms Thorne's Ch.8 ambiguous fate as non-terminal** (he is explicitly not killed), closing half of the open "A(Valeria+Thorne) resolution" question — but the activation itself does not deactivate: a crowd verdict about Thorne is a structural judgment, not a personal resolution between him and Valeria, so the tension stays open. F does not fire — Thorne's individual fate resolves as its own plot thread, but the global Hum-spread scale and the rest of the consortium remain untouched, and the fragment's own final beat is an unanswered question about whether the Hum is even permanent. No new node types activate or deactivate; slots hold at 2 throughout.

| Scene | Nodes Active | Markers | Slots |
| --- | --- | --- | --- |
| Window — decision to descend via stairs | A, D | δ/σ | 2 |
| Plaza — Diane Foster named (recurring Ch.7/Ch.8 checkpoint woman) | A, D | σ | 2 |
| Diane frames the question: what do we do with a confessed man? | A, D | σ | 2 |
| Crowd splits — "Kill him!" vs. "We're not murderers!" | A, D | σ (peak) | 2 |
| Diane's ruling — Thorne lives as permanent witness/pariah | A, D | δ (Thorne's fate confirmed non-terminal) | 2 |
| Permanence question posed to Thorne — **manuscript cuts off** | A, D | σ (unresolved cliffhanger) | 2 |

**Key findings:** Diane Foster named. Thorne's fate confirmed alive/non-terminal (not killed) — A(Valeria+Thorne) itself remains open regardless. F still does not fire. No manuscript text exists past the permanence question — Trace 009 needs Part 2 before it or a Ch.1–9 summary can be finalized.

---

## Section 8: Open Questions

| Question | Status |
| --- | --- |
| All 7 nodes distinct? | Resolved — confirmed across 5 traces. Now 8 nodes. |
| τ, σ, γ encoding? | τ Locked. σ and γ Assigned — need scenarios as primary marker. |
| Z states and deferral? | Resolved — Ruling 6.4. Z variant watch open (thematic chapter-close). |
| A activation vs balance? | Resolved — Ruling 6.5. |
| S deactivation | Resolved — Ruling 6.3. |
| Unified pursuit / post-S gap? | Resolved — Ruling 6.6. Node D formalized. |
| Sustained α — distinct marker? | Resolved — Ruling 6.8. Three instances confirmed (Ch.4, Ch.6, Ch.7×2). |
| Z variant — thematic statements? | Resolved — Ruling 6.9. Three instances confirmed (Ch.3, Ch.5, Ch.7). |
| D deactivation in non-Veritas projects? | Open. Only confirmed at G/F. Other deactivation conditions may emerge. |
| Terminal Z sub-mode? | Open. One instance (Miller, Ch.5). Thorne's Ch.8 Z is Complete but ambiguous/non-terminal — does not count. Two more terminal instances still needed before ruling. |
| Hum-compelled disclosure vs. physics? | Resolved — Ruling 6.7. Compelled = disclosure not conviction. τ requires agency. Confirmed across 2 characters (Thorne Ch.6, Cassie Ch.7). |
| D composition changes? | Open. One exit (Miller, Ch.5) + one addition (Rachel Díaz + crew, Ch.7) + one split (Rachel+Cassie depart, Valeria stays, Ch.8 — D persists across both branches). Does D require minimum/maximum membership, or a single location? Ch.8 says location isn't required. |
| τ — non-approach earned transition? | Resolved — Ruling 6.10. Confirmed via Thorne's Ch.8 confession arc. |
| A(Valeria+Thorne) resolution? | Open. Thorne's fate is confirmed (alive, permanent witness) as of Ch.9 Part 1 — a structural/crowd verdict, not a personal resolution. The tension between Valeria and Thorne specifically remains unaddressed. Still watching. |
| Is the Hum's spread permanent? | Open — this is the exact question Ch.9 cuts off on. Thorne told Valeria/Rachel privately in Ch.7 that it's self-sustaining/uncontrollable; whether he says so publicly here is unwritten. |
| Does the node set cover a deliberately-ambiguous ending? | Open — new, from Section 9. Neither F nor G fits a story that is fully finished but ends on irresolution as its own narrative choice (the alt-branch's actual ending). May need a 9th node, or a ruling on tracing thematically-open endings. |
| Cassie's Z-free streak | Ended in the alt-branch (Ch.13, first Z — "it stayed"), held through Ch.9 in the canonical branch. Branch-specific, not a contradiction — different manuscripts, different outcomes are expected. |

---

## Section 9: Alternate Branch — Dogfood Stress Test

**Context.** Every trace through Ch.9 had zero Lore Creep violations and zero physics
violations. That's good evidence the manuscript we traced is disciplined, but it left an
open question about the *tool*: does `NodeEngine` actually catch a real mistake, or has it
only ever been asked to confirm that nothing went wrong? Lore Creep is auto-detected from
the 3-slot count, so that mechanism is self-testing by construction. Ruling 6.7's
conviction-change test is not — it's a prose definition applied by judgment each time, with
no formal record of a violation ever having been logged.

**The manuscript has a second draft to test it against.** A second file
("Veritas Expanded Full Story.txt") shares Ch.1–6 verbatim with the traced corpus, then
forks into its own continuation — different Ch.7 ("The Fallout of Angels"), different Ch.8
("Doctrine of Silence"), different weapon-program name ("Project CORDELIA" vs. "PSH"),
different faction name ("Silence Seekers" vs. "the Purified"), and a fully-written arc
through to an epilogue (Ch.14). Read in full — see below — its own internal Ch.7–14 holds
together on its own terms; the interesting seam is the fork point itself.

**Engine change required.** Added `flag_physics_violation(scene, entity, description,
contradicts)` to `NodeEngine`, alongside a `self.physics_violations` list and a summary
line reporting it — same shape as the existing `self.violations` (Lore Creep) list. This
does not make conviction-change detection automatic (the engine still can't read prose or
infer psychology); it gives the trace-writer a formal place to record the call once made,
the same way Manuscript Defects already get logged in prose but Lore Creep gets logged
mechanically. The gap being closed is that Ruling 6.7 had a test but no instance.

**Result — one real violation, formally recorded.** Traced this branch's own Ch.7
("Fallout of Angels") against the forked engine state: clean, no violations — Thorne never
appears on-page, so nothing there can yet contradict his Ch.6 exit-state. Ch.8 ("Doctrine
of Silence") reintroduces him directly: fully recommanded, cold, ordering Phase 5 (a
deafening weapon) and "Lethal Extraction" on Valeria, with no scene between Ch.6's close
and this one showing how or why he reverted from "a man with a confession" back to a
still-scheming commander. Per Ruling 6.7's own test — does the character's core thesis
change without being earned on the page? — this is exactly the failure case the ruling was
written to catch. Logged as the corpus's first `PHYSICS_VIOLATION`:

```
entity: Thorne
scene: ch8alt.aegis_suite_thorne_recommands
description: Reappears fully in command -- cold, operational, giving orders --
  with no on-page event explaining a reversion from the confessor state Ch.6
  left him in.
contradicts: ch6.thorne_into_hallway (Trace 006) -- commander-to-confessor
  shift, Ruling 6.7. Declared state: guilt-ridden, moving toward surrender.
```

**Secondary finding (manuscript defect, not physics).** The weapon program is named
"Project CORDELIA" in this branch vs. "PSH" in the traced canonical branch — a
worldbuilding/naming inconsistency, logged separately since it's not a character-conviction
question.

**Continued through the Ch.12 climax — still zero Lore Creep, and now we know why.**
Extended the same fork through this branch's own Ch.9 (a bystander vignette, no tracked
entity on-page — skipped cleanly), Ch.10–11 (build toward the Federal Building, two
chapter-closes explicitly logged as *not* matching the Ruling 6.9 thematic pattern, keeping
that ruling's evidence honest), and Ch.12 ("The Heart of the Well") — the densest scene in
either branch. A(Valeria+Thorne) activates here for the first time in this branch (physical
co-location finally met), stacked with Z firing mid-scene for Valeria (Truncated — Thorne
psychologically manipulating her into a spiral, surfacing a previously-unestablished secret
about a boy she killed and never reported — logged as a soft manuscript observation,
distinct from the Thorne reversal). Peak slot count hit exactly 3 (A+D+Z) — the same
ceiling as every other Z-firing scene in the whole corpus — and never exceeded.

Traced *why* rather than assuming it: Z activates when Thorne's manipulation begins and
deactivates the instant Valeria acts (she shoots the acoustic dampeners, not Thorne —
rejecting his manipulation through a chosen action rather than being resolved by an
external cutoff). Nothing else asks for a node-level slot while Z is open. Even under
deliberate stress-testing at the densest scene either draft contains, the 3-slot discipline
holds — because the author sequenced the identity-crisis to resolve before anything else
needed the room. A genuine Lore Creep may require a scene where two node-level events
overlap *without* an intervening resolution — which this climax, dense as it is, does not
actually contain. That is a real finding, not a null result.

A(Valeria+Thorne) later **deactivates** in this branch's Ch.13 — Thorne defeated, sitting
in the wreckage, Valeria and Cassie simply walk away ("nothing left to say to a man who
had been outlived by his own atrocity"). Structural resolution, tension no longer
generative. Contrast the canonical branch, where this same node is explicitly left open
through Ch.9.

**F candidacy, still not fired.** This climax is the strongest F candidate encountered in
either branch — the central pursuit-thread (stop Thorne, stop Phase 5, expose the truth)
resolves in one scene. Not firing it: F requires being down to exactly *one* remaining
thread, and per this branch's own Ch.13–14, multiple threads stay open past this point
(Thorne's ultimate moral reckoning, the global-scale aftermath, a "living with truth"
thematic arc). Logged as an open note rather than forced.

**Self-caught modeling error, corrected.** The first pass of this trace activated
Valeria's Ch.12 Z as `Truncated` (implying deferral, like her Ch.3 bank Z). That was wrong:
Truncated means cut short by an *external* interruption, but this one plays out fully
in-scene and resolves through her own decisive action (firing at the dampeners) rather
than being cut off. Because `deactivate()` doesn't clear the deferred-Z list — only
`resolve_deferred_z()` does — the mistagged Truncated entry sat open forever, surfacing as
a second permanently-open deferred Z in the corpus summary. Caught on review, corrected to
`Complete` (the accurate mode), re-traced. Noted here rather than quietly fixed, since a
trace-authoring mistake is exactly the kind of thing this whole project exists to catch —
including in its own trace-writer.

**Through Ch.13's remainder and all of Ch.14 + its epilogue — the manuscript's actual
ending.** Backfilled two Ch.13 beats that precede the already-traced "they leave" moment:
the local Hum going silent (γ — but local only; Ch.14 confirms the global spread
continues), and Cassie's own reaction to what the collision did to her ("I can still see
them... it stayed") — read as her **first Z in either branch**, ending the Z-free-since-
Ch.2 streak that had held all the way through the canonical branch's Ch.9. Valeria herself
becomes permanently "skinless" (feels others' guilt/fear directly) — tagged δ, not Z: this
is an external condition imposed on her, not a pause to confirm her own coherence, and
conflating the two would blur a distinction the framework depends on. Ch.14 shows the
global spread directly on-page for the first time in either branch (a London newsroom,
live) and introduces "the Vow" — a worldwide faction of the permanently self-silenced.
Two more chapter-closes land the same thematic-statement pattern from Ruling 6.9, this
time as **cross-branch corroboration** — a pattern confirmed independently in two
different continuations of the same manuscript is stronger evidence than repeated
instances within just one.

**Does G fire at the actual ending?** This is the literal last page of a complete,
14-chapter-plus-epilogue manuscript — a nameless child born after the Inversion finds
Thomas Knox's badge, feels nothing from it (to him it's an inert relic of an incomprehensible
old world), and the story closes on a distant, solitary figure (almost certainly Valeria)
where "the air seemed to shimmer... as if the truth was trying to find a way to become a
lie again." If G (Narrative Coherence — all threads resolve, arcs land, thematic intent
fulfilled) were ever going to fire, it would be here. **It does not.** Thorne's ultimate
fate is never revisited past Ch.13. The Vow/Silent Colonies social order is explicitly
*ongoing and adapting*, not landed ("a civilization of the Wary... learning to live in the
Light... building new masks, new distances" — a process, not a resolution). And the final
image is deliberately ambiguous — the text itself calls that ambiguity "the only hope
left," not a resolved thesis.

**New open question for the framework itself** (not a manuscript defect — a gap in node
coverage): neither F nor G describes a story that is fully *finished* but deliberately ends
on irresolution as its own narrative choice, rather than approaching or reaching coherence.
Logged in Section 8 below rather than forced into an ill-fitting node.

**Conclusion.** This is the dogfood-gate evidence that was missing: not "the manuscript
stayed clean," but "the tool caught something wrong when given something wrong to catch"
(the physics violation), *and* "the tool correctly did not manufacture a violation where
none existed, with a traceable reason why" (the Ch.12 climax). Both results used the
system's own already-established rules, applied mechanically rather than only narrated
about.

---

## Next Steps

- ~~Traces 001–003 complete, prototype running~~ **DONE**
- ~~Trace 004 (Ch.4) — revised v0.6: Z Complete (Valeria), Defects 5.1/5.2 logged~~ **DONE**
- ~~Trace 005 (Ch.5) — revised v0.6: Miller terminal Z, D-composition event, Z variant 2/3~~ **DONE**
- ~~Trace 006 (Ch.6) — D persists across POV, Ruling 6.7 confirmed, no new nodes~~ **DONE**
- ~~Trace 007 (Ch.7) — F does not fire, D-composition addition #2 (Rachel Díaz + crew), Ruling 6.7 extended to Cassie, Rulings 6.8 + 6.9 issued~~ **DONE**
- ~~Trace 008 (Ch.8) — A(Valeria+Thorne) activates, Thorne's first Z (Complete, non-terminal, ambiguous fate), Valeria's Ch.3 deferred Z resolves, D-composition split event #3, Ruling 6.10 issued (τ hunt resolved), Manuscript Defect 8.1 logged~~ **DONE**
- **Trace 009 (Part 1) — Ch.9 (The Judgment).** Diane Foster named. Thorne's fate confirmed alive/non-terminal via crowd verdict (permanent witness, released once exhausted of use). F still does not fire. **MANUSCRIPT INCOMPLETE** — cuts off before Thorne answers whether the Hum's spread is permanent. Two earlier Ch.9 candidates ("The Anatomy of the Quiet" — an unrelated bystander vignette from the old superseded draft branch; "Chapter Nine: Echoes" — a mystical secret-society narrative sharing only the title) were checked and rejected as not continuing this storyline.
- **Trace 009 (Part 2) — needed to complete Ch.9.** Awaiting Thorne's answer to the permanence question. Watch: does this finally give F a real approach-to-resolution signal, or does confirming permanence widen scope further (consistent with every prior "reveal" in this manuscript)? Does A(Valeria+Thorne) get any closer to structural resolution?
- **Traces 009–014** — Ch.9 through Ch.14 (Judgment, Spread, Adaptation, Remaining Names, New Order, Living with Truth). G and F activation, A(Cassie+Valeria) maturation arc, extended aftermath.
- **Grammar encoding** — after all chapter traces complete and prototype validates the full arc.
