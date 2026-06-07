# HEXAGONAL BLUEPRINT
Node Validation & Mapping Document
Creative OS — Standalone Implementation
Version 0.6 — Ruling 6.7 (Hum-Compelled Disclosure) | Ch.4–5 traces corrected | Trace 006 added

**Changes from v0.5:**
Ruling 6.7 issued: Hum-compelled disclosure is physics-consistent; physics checks conviction not concealment | τ agency requirement added: Hum-compelled transitions are not τ | Traces 004–005 corrected (Z anchors, manuscript defects 5.1/5.2 logged, Miller terminal Z) | Trace 006 added (Ch.6 — D persists across POV, no new nodes, Ruling 6.7 clean) | Sustained α at 2 instances; Z variant watch at 2 instances

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
| Sustained α — distinct marker? | Open. Two instances (Ch.4 City Hall, Ch.6 technician cascade). One more = ruling. |
| Z variant — thematic statements? | Open. Two instances (Ch.3 tunnel close, Ch.5 close). One more = ruling. |
| D deactivation in non-Veritas projects? | Open. Only confirmed at G/F. Other deactivation conditions may emerge. |
| Terminal Z sub-mode? | Open. One instance (Miller, Ch.5). Two more instances needed before ruling. |
| Hum-compelled disclosure vs. physics? | Resolved — Ruling 6.7. Compelled = disclosure not conviction. τ requires agency. |
| D composition changes? | Open. One event (Miller exits, Ch.5). Does D require minimum membership? |

---

## Next Steps

- ~~Traces 001–003 complete, prototype running~~ **DONE**
- ~~Trace 004 (Ch.4) — revised v0.6: Z Complete (Valeria), Defects 5.1/5.2 logged~~ **DONE**
- ~~Trace 005 (Ch.5) — revised v0.6: Miller terminal Z, D-composition event, Z variant 2/3~~ **DONE**
- ~~Trace 006 (Ch.6) — D persists across POV, Ruling 6.7 confirmed, no new nodes~~ **DONE**
- **Trace 007 — Ch.7 (Power, Parse, Path).** Tribune Building, Rachel Díaz, consortium files decrypted. Watch: F activation (story approaching resolution)? Z for Cassie (Z-free since Ch.2)? Third τ instance (hunt for non-approach)? Third sustained α instance (ruling threshold)?
- **Trace 008 — Ch.8 (The Consortium).** Aegis Suite confrontation. A(Valeria+Thorne) activates. Deferred Valeria Z (Truncated, Ch.3) resolves here — Ruling 6.4 deferral clause. Watch Thorne's confession under Ruling 6.7.
- **Traces 009–014** — Ch.9 through Ch.14 (Judgment, Spread, Adaptation, Remaining Names, New Order, Living with Truth). G and F activation, A(Cassie+Valeria) maturation arc, extended aftermath.
- **Grammar encoding** — after all chapter traces complete and prototype validates the full arc.
