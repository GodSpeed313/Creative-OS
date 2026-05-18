# Creative OS

**A narrative governance framework for writers.**

Creative OS keeps your original intent alive throughout the entire creative process.
Built on the All-Lanes Architectural Framework for Narrative Design.

---

## What It Does

Every feature points back to one objective — preserving the creator's North Star:

| Tool | Question It Answers |
|---|---|
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

Technical Layer   →  grammar, punctuation, structural standards
Narrative Layer   →  Wander Alarm monitors live energy against declared anchors
Discernment Layer →  evaluates subtext and emotional stakes at scene level



---

## Core Concepts

**North Star** — The project's original thesis and structural anchors. Everything the system measures against.

**Zero-Complaint Standard** — Any deviation from the declared truth is a violation. No thresholds. No partial credit.

**Lore Creep** — When world-building expands so far it overshadows the core plot. The Wander Alarm's primary target.

**Internal Physics** — The logical framework and behavioral rules established in the story bible for each character. Actions must remain rigorous and logically sound relative to these rules at all times.

**Motion Calculus** — Frequency mapping engine that tracks character dynamics and behavioral synchronicity over time.

**Kinetic Tracking** — Heat-map visualization of story tension and energy. Makes the North Star measurable as a predefined tension curve.

---

## M1 — The Wander Alarm

The first milestone. Everything else depends on it working first.

The Wander Alarm constantly compares the live draft against the declared North Star. When narrative movement strays beyond the project's core objectives, it triggers a **VIBE-CONSTRAINT ALERT** identifying the exact nature and location of the drift.

### North Star Declaration (`.cos` syntax)

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



### Constraint Weights

| Weight | Meaning |
|---|---|
| `anchor` | Non-negotiable. Character physics and thesis alignment. |
| `core` | Structural integrity. Tension and pacing. |
| `tone` | Atmospheric consistency. |

### Running the Wander Engine

```bash
# Install dependencies
pip install -r requirements.txt

# Compile your .cos file to IR
python compile_cos.py m1/north_star.cos m1/ir.json

# Run the engine against a draft snapshot
python run_wander.py
Alert Output
Drift detected:


VIBE-CONSTRAINT ALERT
════════════════════════════════════════════════════════════
...
└── RESOLUTION
    ├── System state : DRIFTING
    ├── Drift count  : 2 violation(s) detected
    └── The Wander Alarm has triggered. Review flagged constraints before continuing.
No drift:


NARRATIVE ALIGNMENT CHECK
════════════════════════════════════════════════════════════
...
└── RESOLUTION
    ├── System state : ALIGNED
    └── All constraints satisfied. North Star holding. No drift detected.
Roadmap
Milestone	Feature	Status
M1	Wander Alarm — North Star declaration + violation detection	✅ Complete
M2	Motion Calculus — character physics frequency mapping	Planned
M3	Living Graph Database — story bible integration	Planned
M4	Sandbox Simulation — non-destructive plot path testing	Planned
Cognitive Extension Principle
Creative OS does not automate creativity. It functions as a high-fidelity coach — a peer-to-peer cognitive parity model that preserves the creator's unique voice and prevents the linguistic homogenization typical of standard LLM outputs. Every correction, every flag, every alert is designed to keep the creator in full intellectual agency over their work.

