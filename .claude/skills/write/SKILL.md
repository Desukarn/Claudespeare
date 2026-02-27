---
name: write
description: Commands for creative writing workflow - story development from initialization through drafting and revision. Supports both quick-start (YOLO) and detailed planning (In-Depth) modes, with adaptive templates for different story lengths. Tracks full story context across chapters with style matching, consistency checking, pacing guidance, and manuscript export features.
---

# Write - Story Development Skill

Commands for structured creative writing workflow with context-aware chapter generation.

## Commands

### `/write:init`
Initialize new story project

Creates project directory structure and captures foundational story information (title, genre, premise, story length, workflow mode).

See: init-project.md

### `/write:expand`
Expand YOLO project from vague idea to structured premise

For YOLO mode projects: transforms fuzzy concepts into workable premises with basic character sketches and simple plot structure. Enables rapid transition to writing.

See: yolo-expand.md

### `/write:style`
Analyze writing samples and define voice (STYLE.md)

Define your writing style through sample analysis and voice configuration. Analyzes 2-3 sample paragraphs for measurable patterns (sentence length, vocabulary level, tone markers) and combines with explicit voice preferences (POV, tense, formality, narrative distance). Creates STYLE.md profile for use in chapter generation.

See: style-seed.md

### `/write:chapter`
Generate chapters and scenes with story context (chapters/*.md)

Write chapters with full story awareness - matches your style seed, maintains character voices, tracks plot threads, and adapts output length to story type. Loads STYLE.md, CHARACTERS.md, OUTLINE.md, ARCS.md, WORLD.md, and existing chapters for consistency. Generates prose scene-by-scene for long chapters or single-pass for short chapters.

See: write-chapter.md

### `/write:detect`
Scan prose for AI language patterns (AI-DETECTION-REPORT.md)

Analyze your chapters for 10 common AI language patterns including 'delve', 'tapestry', 'navigate', 'testament to', 'juxtaposition', overly formal academic language, "it's worth noting" phrases, and purple prose excess. Get concrete replacement suggestions (3-5 alternatives per match) with context. Add custom phrases to watch for via AI-PATTERNS.md customization.

See: ai-detect.md

### `/write:check`

Scan your story for consistency violations across all chapters. Checks character details (appearance, voice, personality), timeline continuity, world rule adherence, and POV consistency. Loads CHARACTERS.md, WORLD.md, and all chapters to detect contradictions. Generates CONSISTENCY-REPORT.md with flagged issues, locations, and suggestions. Run after writing 3-5 chapters or before major revisions to catch plot holes and continuity errors.

**Checks:** Character appearance/voice consistency, timeline/event order, world rule violations, POV shifts, personality contradictions
**Input:** Story project directory
**Output:** CONSISTENCY-REPORT.md with detailed findings
**Duration:** 5-15 minutes depending on chapter count

See: check-consistency.md

### Future Commands

<!-- Placeholder for future commands -->
<!-- `/write:plan` - Complete In-Depth story planning (Phase 1 Plan 03) -->
<!-- `/write:chapter` - Draft new chapter -->
<!-- `/write:revise` - Revision workflow -->
<!-- `/write:detect-ai` - Detect and highlight AI language patterns -->

## When to use this skill

- Starting a new story project (short story, novella, or novel)
- Developing characters, plot, and world-building
- Defining your unique writing style through sample analysis
- Drafting chapters with consistent voice and style matching
- Detecting and removing AI-generated language patterns
- Revising to ensure authentic human voice
- Maintaining story consistency across chapters

## Workflow modes

**YOLO mode:** Quick start from vague ideas, minimal upfront planning, discover story through writing
**In-Depth mode:** Comprehensive planning before drafting, detailed character/plot/world development
