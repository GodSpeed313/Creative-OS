# Creative OS

**A narrative governance framework for writers.**

Creative OS keeps your original intent alive throughout the entire creative process.
Built on the All-Lanes Architectural Framework for Narrative Design.

---

## What It Does

Every feature points back to one objective — preserving the creator's North Star:

| Tool | Question It Answers |
| --- | --- |
| **Wander Alarm** | Is the story still going where it was supposed to go? |
| **Motion Calculus** | Is this character still who they were supposed to be? |
| **Sandbox Simulation** | Can I test this detour without losing the original thread? |
| **Zero-Complaint Standard** | No drift. No exceptions. |

---

## Architecture

### Module I — The Architect (Planning)

Formalizes creative intent before execution begins. Houses the **Living Graph Database** — the story bible and declared truth — alongside **Motion Calculus**, which initializes frequency mapping for character dynamics and internal physics.

### Module II — The Pilot (Drafting)

Real-time drafting suite. Monitors active prose against the structural specifications defined in The Architect.

- **Live Vibe-Checks** — real-time tonal and atmospheric analysis
- **Intent-Based Drafting** — monitors prose against predefined narrative benchmarks
- **Adaptive Vocabulary** — keeps word choice consistent with world and character voice
- **Sandbox Simulation** — non-destructive environment for testing alternative plot paths

### Module III — The Editor (Review)

Multi-stage synthesis from macro-structural integrity to micro-level precision.

- **Developmental Analysis** — audits for plot holes and pacing irregularities
- **Voice/Style Audit** — verifies the prose has not degraded into generic AI syntax
- **Precision Mode** — grammatical refinement with why-based explanations (creator retains full agency)

---

## AI Discernment Layers

```text
Technical Layer   →  grammar, punctuation, structural standards
Narrative Layer   →  Wander Alarm monitors live energy against declared anchors
Discernment Layer →  evaluates subtext and emotional stakes at scene level
```

---

## Core Concepts

**North Star** — The project's original thesis and structural anchors. Everything the system measures against.

**Zero-Complaint Standard** — Any deviation from the declared truth is a violation. No thresholds. No partial credit.

**Lore Creep** — When world-building expands so far it overshadows the core plot. The Wander Alarm's primary target.

**Internal Physics** — The logical framework and behavioral rules established in the story bible for each character. Actions must remain rigorous and logically sound relative to these rules at all times.

**Motion Calculus** — Frequency mapping engine that tracks character dynamics and behavioral synchronicity over time.

**Kinetic Tracking** — Heat-map visualization of story tension and energy. Makes the North Star measurable as a predefined tension curve.

---

## The `.cos` DSL

Creative OS uses a custom declarative language (`.cos`) to encode a project's declared truth. The compiler parses it into an IR dict; the Wander Engine evaluates draft snapshots against that IR.

### M1 — Named tension levels (backward compatible)

```cos
domain narrative_governance {
    project:  "Your Project Title"
    standard: zero_complaint
}

north_star {
    thesis: "Your core objective — what this story is fundamentally about."

    tension_curve {
        baseline: high
        floor:    elevated
    }
}

entity Character "CharacterName" {
    logic: "behavioral rule one"
    logic: "behavioral rule two"
    sync:  "how their behavior relates to scene and lore context"
}

constraint PhysicsIntegrity {
    target:   "CharacterName"
    rule:     behavior must match logic
    weight:   anchor
    on_drift: flag + alert
}

constraint TensionAlignment {
    rule:     tension_level must not drop below north_star.tension_curve.floor
    weight:   core
    on_drift: flag + alert
}

constraint LoreBalance {
    rule:     lore_expansion must not overshadow core_plot
    weight:   anchor
    on_drift: flag + alert
}

enforce {
    north_star:  active
    constraints: [PhysicsIntegrity, TensionAlignment, LoreBalance]
}
```

### M2 — Float tension + IDP + Sandbox Commit

M2 replaces named tension levels with a float system (`0.0–1.0`) and adds two new block types.

**Tension alias table:**

| Alias | Float |
| --- | --- |
| `low` | 0.10 |
| `elevated` | 0.25 |
| `medium` | 0.37 |
| `high` | 0.50 |
| `heavy` | 0.75 |
| `extreme` | 1.00 |

**`intent_parameters` block** (replaces `tension_curve` in M2):

```cos
north_star {
    original_thesis: "Your thesis."

    intent_parameters {
        tension_baseline:         0.75
        physics_integrity:        strict
        lore_balance:             restrained
        behavioral_synchronicity: high
    }
}
```

Variance threshold: `±0.05`. Any scene deviating beyond this fires `WANDER_ALARM_KINETIC_DEVIATION`.

**Intentional Deviation Protocol (IDP)** — formally authorize a planned departure from declared truth:

```cos
intentional_deviation {
    target:        Character.CharacterName.behavior
    intent:        "Why this deviation is authorized and what it accomplishes"
    scope:         scene.act2_turning_point..chapter.arc_resolution
    sync_override: [Character.CharacterName.physics, Lore.WorldRule]
    resolution:    evolve { evolved_to: "Updated physics post-deviation" }
}
```

**Sandbox Commit** — merge a tested alternate path into the main North Star:

```cos
sandbox_commit {
    source_sandbox:          "sandbox_id"
    commit_deltas:           [Character.Name.arc, Plot.MainConflict]
    reanchor_north_star:     { new_thesis: "Revised thesis." new_tension_floor: 0.65 }
    vibe_check_verification: passed
}
```

**Authorized delta path categories:** `Character`, `Lore`, `Tension`, `World_Physics`, `Plot`

### Constraint Weights

| Weight | Meaning |
| --- | --- |
| `anchor` | Non-negotiable. Character physics and thesis alignment. |
| `core` | Structural integrity. Tension and pacing. |
| `tone` | Atmospheric consistency. |

---

## Running the Wander Engine

```bash
# Install dependencies
pip install -r requirements.txt

# Compile a .cos file to IR
python compile_cos.py m1/north_star.cos m1/ir.json

# Run against the default M1 snapshot
python run_wander.py

# Run against any project
python run_wander.py veritas/ir.json veritas/snapshot_ch11_drift.json
```

### Alert output — drift detected

```text
VIBE-CONSTRAINT ALERT
════════════════════════════════════════════════════════════
...
├── CONSTRAINT: TensionAlignment [weight: core]
│   ├── Evaluation : tension=0.42, baseline=0.75, Δ=0.33
│   ├── ✗ DRIFT DETECTED
│   ├── Finding    : WANDER_ALARM_KINETIC_DEVIATION — variance 0.33 exceeds ±0.05 threshold
│   └── Action     : flag + alert
│
└── RESOLUTION
    ├── System state : DRIFTING
    ├── Drift count  : 3 violation(s) detected
    └── The Wander Alarm has triggered. Review flagged constraints before continuing.
```

### Alert output — aligned

```text
NARRATIVE ALIGNMENT CHECK
════════════════════════════════════════════════════════════
...
└── RESOLUTION
    ├── System state : ALIGNED
    └── All constraints satisfied. North Star holding. No drift detected.
```

### M2 alert codes

| Code | Trigger |
| --- | --- |
| `WANDER_ALARM_KINETIC_DEVIATION` | Scene tension variance exceeds ±0.05 of declared baseline |
| `WANDER_ALARM_PHYSICS_VIOLATION` | Character action flagged `physics_match: false` |
| `WANDER_ALARM_LORE_CREEP` | `lore_expansion_ratio` exceeds 0.5 |

---

## Dogfood Test Cases

### One Piece — M1 fixture (`m1/`)

North Star: Luffy becomes King of the Pirates through willpower and bonds, never raw power.

- Clean test: Wano rooftop scene — **ALIGNED** (3/3 constraints)
- Drift test: Egghead Nika awakening — **DRIFTING** (PhysicsIntegrity + LoreBalance)

### Veritas — M2 fixture (`veritas/`)

Thesis: *"Truth without mercy is just another form of violence — the line between a lie that saves and a lie that enslaves is consent."*
Characters: Cassie Monroe, Valeria Knox, Commander Elias Thorne. Tension baseline: 0.75.

- Clean test: Chapter 1 — **ALIGNED** (5/5 constraints)
- Drift test: Chapter 11 hunt arc — **DRIFTING** (ThornePhysics + TensionAlignment + LoreBalance)

---

## Hexagonal Blueprint — Node State System

The Hexagonal Blueprint is a second architectural layer above the constraint engine. Where the Wander Alarm is reactive (fires when something goes wrong), the node system is positional — it tracks *where the story is* at any given moment.

Seven narrative states, Greek markers for transitions between them, and hard rules about how many states can be active simultaneously.

### The 7 Nodes

| Node | Creative OS Name | Active When |
| --- | --- | --- |
| G | Narrative Coherence | All threads resolve; arcs land; thematic intent fulfilled |
| F | Near-Coherence | One thread unresolved; story approaching resolution |
| W | Narrative Equilibrium | Story stable; no active tension toward resolution or collapse |
| A | Thematic Symmetry | Two opposing narrative forces in balance; neither dominating |
| Z | Story Checkpoint | Narrative pauses to confirm its own coherence before continuing |
| H | Narrative Boundary | Outermost reach of story world; no defined structure beyond this point |
| S | Thread Convergence | Multiple threads actively merging toward a single resolution point |

### Greek Flow Markers

| Marker | Role | Fires When |
| --- | --- | --- |
| π | Ground State Anchor | Always — structural floor of the entire system |
| α | Transition Begins | A node state transition is initiated |
| δ | State Shifts | A node state has changed; the shift is being marked |
| τ | Duration-Dependent Transition | The state change requires a full scene duration to complete |
| σ | Pressure / Conflict Path | A path is under active narrative pressure |
| γ | Generative Marker | Something new enters the system; a new state is being created |

### Rules

- **Adjacency:** every node must have at least one defined adjacent node before it can fire
- **Simultaneous activation limit:** maximum 3 nodes active at once without Z (Checkpoint) firing first — exceeding this triggers Lore Creep (auto-detected from the slot count)
- **Floor nodes:** π is always present and does not consume an activation slot; H may be elevated to floor status when a story's premise permanently dissolves structural bounds (see `spec/hexagonal_blueprint_v03.md`)
- **Physics violations:** does a character's core conviction change without being earned on the page (Ruling 6.7)? Unlike Lore Creep, this isn't auto-detected — it's a judgment call the trace-writer records via `flag_physics_violation()`. First real instance caught in the v0.10 dogfood stress test (`spec/hexagonal_blueprint_v05.md`, Section 9).

### Validation

The node system was traced against Veritas Prologue + Chapter 1 (Trace 001). All 7 node definitions held against real story material without requiring any changes. Z fired naturally in the GlobalHarvest boardroom scene — the strongest validation: it confirmed itself without being engineered.

Two architectural rulings issued from the trace:

- **H Persistence Ruling:** When a story's premise makes the Narrative Boundary permanent, H is elevated to floor status and does not consume an activation slot. Applies to Veritas.
- **A Granularity Ruling:** Thematic Symmetry tracks per-entity (institutional, personal, relational), not per-story. Multiple instances are independent — one can deactivate while others persist.

Full spec: [`spec/hexagonal_blueprint_v04.md`](spec/hexagonal_blueprint_v04.md)

---

## Roadmap

| Milestone | Feature | Status |
| --- | --- | --- |
| M1 | Wander Alarm — North Star declaration + violation detection | ✅ Complete |
| M2 | Float tension system, IDP, Sandbox Commit Logic | ✅ Complete |
| Hex v0.3 | Hexagonal Blueprint — node definitions locked, Ch.1 trace validated | ✅ Complete |
| Hex v0.4 | Ch.2 + Ch.3 traced — S/Z/A definitions refined, 6 rulings issued | ✅ Complete |
| Hex v0.12 | Node transition prototype (Jupyter → code) — Traces 001-008 complete (Ch.1-8) + Trace 009 Part 1 (Ch.9, in progress), 10 rulings issued, alternate-branch dogfood stress test complete through its actual ending — first PHYSICS_VIOLATION caught, zero Lore Creep with a traceable reason why, G correctly does not fire at a deliberately-ambiguous ending | In Progress — Ch.9 manuscript incomplete |
| M3 | Living Graph Database — story bible integration (The Architect) | Planned |
| M4 | Real-time drafting monitor — Live Vibe-Checks (The Pilot) | Planned |
| M5 | Developmental Analysis + Voice Audit (The Editor) | Planned |

---

## Cognitive Extension Principle

Creative OS does not automate creativity. It functions as a high-fidelity coach — a peer-to-peer cognitive parity model that preserves the creator's unique voice and prevents the linguistic homogenization typical of standard LLM outputs. Every correction, every flag, every alert is designed to keep the creator in full intellectual agency over their work.
