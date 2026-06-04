# HEXAGONAL BLUEPRINT
Node Validation & Mapping Document
Creative OS — Standalone Implementation
Version 0.5 — Node D Formalized — Ruling 6.6 Resolved

**Changes from v0.4:**
Node D (Unified Pursuit) added — 8th node, confirmed across 3 scenarios | Ruling 6.6 closed as formalized | Engine auto-activates D at S-deactivation-with-active-goal | δ logged (not Z) for thematic chapter-close beats — Z variant watch opened | Traces 004 and 005 added

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

**Z variant watch (new in v0.5):** At the close of Ch.5 (*"the truth didn't just hurt. It cleansed."*), the beat felt structurally adjacent to Z but was logged as δ. Reason: Z fires at character-level identity-collapse, not at thematic-statement moments. A thematic Z would require its own definition, rules, and firing conditions — one instance does not earn a new mode. Logged as δ. Watch for two more appearances of the same pattern (narration landing thesis before the story continues) in Ch.6–8. If it appears twice more in the same way, this becomes a ruling.

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

---

## Section 7: Story Scenario Traces

### Trace 001 — Veritas, Prologue + Chapter 1 *(v0.3)*

All 7 node definitions held. Z fired naturally in boardroom. H Persistence and A Granularity rulings issued.

### Trace 002 — Veritas, Chapter 2 *(v0.4)*

Z fired naturally in apartment (personal coherence check). No Z in office (no false self to confirm). S α fired at chapter close.

### Trace 003 — Veritas, Chapter 3 *(v0.4)*

S fully activated and deactivated. Z truncated at bank confrontation (mob invades mid-confirmation). D auto-fires at ch3.mob_invades. A(Cassie+Valeria) activates tilted in tunnel. 3-node limit at bank held.

### Trace 004 — Veritas, Chapter 4 *(v0.5)*

**Date:** 2026-06-04
**Result:** Corridor chapter. Slot count 2 throughout (A + D). No Z fired. No new nodes activated. Longest sustained α in traces (stealth/escape sequence). Thorne named — α fires toward Ch.5, not Z. Post-S D persists as structural engine.

| Scene | Nodes Active | Markers | Slots |
| --- | --- | --- | --- |
| All scenes | A, D | α, δ, σ (variable) | 2 |

### Trace 005 — Veritas, Chapter 5 *(v0.5)*

**Date:** 2026-06-04
**Result:** Z Partial/External fires and completes in-scene at trailer (Toughbook). One deferred Z (Ch.3 Truncated, Valeria) still open. γ fires at Truth Bomb. Chapter close logged as δ (not Z — thematic statement, not character-level collapse). D persists throughout.

| Scene | Nodes Active | Markers | Slots |
| --- | --- | --- | --- |
| Miller breakdown + trailer found | A, D | σ | 2 |
| Toughbook — Z fires (Partial/External) | A, D, Z | α | 3 |
| Z completes in-scene | A, D | δ, Z resolves | 2 |
| Helicopter — flashbangs | A, D | σ peak | 2 |
| Crane — Miller's death | A, D | δ | 2 |
| Truth Bomb | A, D | γ, δ | 2 |
| Chapter close | A, D | δ | 2 |

**Z variant watch note:** Chapter close beat logged as δ. One instance of thematic-level coherence-statement. Watching for pattern.

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
| Sustained α — distinct marker? | Open. One instance (Ch.4 stealth). Watch for second. |
| Z variant — thematic statements? | Open. One instance (Ch.5 close). Two more needed for ruling. |
| D deactivation in non-Veritas projects? | Open. Only confirmed at G/F. Other deactivation conditions may emerge. |

---

## Next Steps

- ~~Traces 001–003 complete, prototype running~~ **DONE**
- ~~Trace 004 (Ch.4) — corridor chapter confirmed~~ **DONE**
- ~~Trace 005 (Ch.5) — Partial/External Z, D persists, γ at Truth Bomb~~ **DONE**
- **Trace 006 — Ch.6 (Eye of the Storm, Thorne POV).** First chapter primarily from Thorne's perspective. Watch: does D persist without Valeria/Cassie as POV characters? Does A(Valeria+Thorne) activate here or only in Ch.8?
- **Trace 007 — Ch.7 (Fallout of Angels).** Truth Bomb aftermath. Watch: does F activate as threads approach resolution? Does Z fire for Cassie (she's been Z-free since Ch.2)?
- **Trace 008 — Ch.8 (Doctrine of Silence).** The deferred Valeria Z resolves here. Confirm Ruling 6.4 deferral-resolution clause fires correctly. Watch A(Valeria+Thorne) → balanced.
- **Grammar encoding** — after all chapter traces complete and prototype validates the full arc.
