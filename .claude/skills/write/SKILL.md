---
name: write
description: Creative writing workflow for novels, novellas, and short stories. Parallel chapter generation, automatic quality checks, style matching, and consistency tracking. YOLO mode for fast drafts, In-Depth mode for detailed planning.
---

# Write - Story Development Skill

Complete creative writing system from idea to finished manuscript.

## Quick Start

**YOLO Mode (Fast - 2 hours for first draft with quality safeguards):**
```
/write:new-project → /write:expand → /write:arc → /write:revise → /write:export
```
- `/expand` includes optional style seed
- **MANDATORY outline approval checkpoint** (prevents cookie-cutter storytelling)
- `/arc` writes ALL chapters automatically
- **Automatic pre-writing scene analysis** (catches exposition dumps)
- **Automatic post-generation review** (verifies quality)

**In-Depth Mode (Thorough - 6-8 hours for first draft):**
```
/write:new-project → /write:plan →
/write:discuss 1 → /write:arc 1 →
/write:discuss 2 → /write:arc auto → ... →
/write:revise → /write:export
```
- `/discuss N` plans each arc
- `/arc N` or `/arc auto` writes chapters
- `auto` detects next arc automatically
- **Same quality safeguards as YOLO** (scene analysis + review)

## Core Commands

### Project Setup

#### `/write:new-project`
Initialize new story with guided setup

Comprehensive project initialization. Asks about story length, workflow mode (YOLO vs In-Depth), genre, premise. Creates project directory with templates. **Start here.**

See: new-project.md

#### `/write:init`
Quick project initialization for advanced users

Direct setup for users who know their preferences. Minimal prompting.

See: init-project.md

### Planning

#### `/write:expand`
**YOLO mode:** Complete one-step expansion with quality safeguards

Transforms fuzzy concepts into writing-ready project:
- Expands premise
- Creates character sketches
- Generates 3-act outline with arc breakdown
- **Adds Goal/Conflict/Outcome analysis for EVERY chapter**
- **Automatic exposition dump detection with warnings**
- **MANDATORY outline approval checkpoint** (cannot skip)
- **Optionally creates style profile from your samples**
- Ready for `/write:arc` immediately

**New safeguards prevent:**
- Tavern/inn exposition scenes
- Passive "character learns about" chapters
- Convenient NPC explanations
- Lack of conflict in scenes
- Protagonist passivity

See: yolo-expand.md

#### `/write:plan`
**In-Depth mode:** Comprehensive story planning

Detailed character profiles, complete plot outline, character arcs, world-building, themes. Creates CHARACTERS.md, OUTLINE.md, ARCS.md, WORLD.md.

See: indepth-plan.md

#### `/write:discuss [N]`
**In-Depth mode:** Plan specific arc before writing

Interactive questions about arc {N}: chapter count, POV pattern, emphasis, tone. Creates ARC-{N}-CONTEXT.md. Run before `/write:arc N`.

See: discuss-arc.md

#### `/write:style-seed`
Add/update style profile (optional)

Analyzes 2-3 paragraphs to capture sentence patterns, vocabulary, tone. Can also be done during `/write:expand`.

See: style-seed.md

### Writing

#### `/write:arc [N|auto]`
**Main writing command.** Write chapters in parallel with quality checks

Spawns parallel writing agents. Each writes one chapter independently with full story context.

**YOLO mode:**
- `/write:arc` - Writes ALL chapters automatically
- Goes through arcs in sequence
- Fully automated

**In-Depth mode:**
- `/write:arc N` - Writes specific arc N
- `/write:arc auto` - Auto-detects next unwritten arc
- After `/write:discuss N` planning
- Use `auto` to skip manual numbering

**NEW: Automatic quality safeguards:**
1. **Pre-Writing Scene Analysis** (runs before spawning writers)
   - Verifies Goal/Conflict/Outcome for each scene
   - Detects exposition dumps in scene structure
   - Flags passive information gathering
   - Pauses if 3+ issues detected for user decision

2. **Chapter Writer Checklist** (mandatory for each writer)
   - Show vs Tell commitment
   - Exposition dump prevention
   - Active character agency
   - Prose quality standards
   - Scene structure requirements

3. **Post-Generation Structural Review** (runs after writing)
   - Scans actual prose for exposition dumps
   - Detects passive patterns that slipped through
   - Offers auto-revision if 3+ issues found
   - Pauses for user decision on quality concerns

**Time:** ~15-20 minutes per arc (3-5 chapters) + review time if issues detected

See: write-arc.md

#### `/write:chapter [N]`
Write single chapter with context awareness

Context-aware:
- With number: Auto-loads from outline, generates immediately
- Without number: Interactive mode, asks for details

Good for: Rewriting specific chapters, filling gaps

**Time:** 15-30 minutes per chapter

See: write-chapter.md

### Quality Control

#### `/write:revise [range]`
Comprehensive automatic revision

Scans for 24+ AI language patterns, checks character voice consistency, verifies world rules, analyzes style drift. Applies automatic fixes, reports manual review items.

**Time:** 15-30 minutes for full novel

See: revise.md

#### `/write:detect`
Focused AI pattern detection

Scans for common AI language ("delve", "tapestry", etc.) with replacement suggestions.

See: ai-detect.md

#### `/write:check-consistency`
Focused consistency checking

Scans for character contradictions, timeline issues, world rule violations, POV problems.

See: check-consistency.md

### Character Management

#### `/write:character <name>`
View character profile from persistent bank

See: character-bank.md

#### `/write:update-character <name>`
Update character details

See: character-bank.md

#### `/write:populate-bank`
Auto-populate character bank from CHARACTERS.md

See: character-bank.md

### Output

#### `/write:export`
Export chapters as manuscript

Individual chapters or compiled manuscript. Formats: Markdown, plain text, standard manuscript format.

See: export.md

### Version Control

#### `/write:revisions <chapter-name>`
View chapter revision history

See: chapter-versions.md

#### `/write:restore <chapter-name> <version>`
Roll back chapter to previous version

See: chapter-versions.md

#### `/write:diff <chapter-name> <v1> <v2>`
Compare two chapter versions

See: chapter-versions.md

### Utilities

#### `/write:pacing`
Get story-specific pacing recommendations

See: pacing-guide.md

## Anti-Cookie-Cutter Safeguards

**NEW (v2.0):** Comprehensive quality system prevents formulaic AI storytelling.

### Multi-Layer Prevention

**7 layers of protection against exposition dumps and passive storytelling:**

1. **Trope Research** - Avoid AI plot patterns (optional but recommended)
2. **Name Generator** - Prevent "Kael", "Elara", "Lyra" bias (mandatory)
3. **Goal/Conflict/Outcome** - Chapter-level structure analysis
4. **Exposition Detection** - Automatic pattern scanning (keywords + structure)
5. **Outline Approval** - User review before writing (YOLO mode, mandatory)
6. **Pre-Writing Analysis** - Scene verification before spawning writers
7. **Post-Writing Review** - Catch patterns that slipped through

### What Gets Detected

**Exposition Dump Patterns:**
- Tavern/inn/bar scenes where NPCs explain plot
- "Character learns about X" passive information gathering
- Convenient conversations that dump world-building
- Mentor/sage characters who know everything
- Overhearing crucial information
- "As you know" conversations

**Green Flags (GOOD patterns):**
- Character PURSUES goals actively
- Information has COST (risk, social price, effort)
- Discovery through ACTION and conflict
- Character WRONG, must correct mistakes
- Meaningful obstacles in every scene

### Quality Checkpoints

**YOLO Mode (3 mandatory):**
1. Outline approval after expansion (cannot skip)
2. Pre-writing scene analysis (pauses if 3+ issues)
3. Post-generation review (pauses if 3+ issues)

**In-Depth Mode (3 per arc):**
1. Arc planning (/write:discuss)
2. Pre-writing scene analysis (pauses if 3+ issues)
3. Post-generation review (pauses if 3+ issues)

**User can override with warnings, but safeguards always run.**

See: PROCESS-OVERVIEW.md for complete workflow details

## When to Use This Skill

- Starting a new story project
- Developing characters, plot, world-building
- Defining your unique writing style
- Drafting chapters with consistent voice
- **Preventing cookie-cutter AI storytelling**
- **Ensuring character agency and conflict**
- Detecting and removing AI language patterns
- Checking story consistency
- Tracking chapter revisions
- Exporting finished manuscripts

## Workflow Modes

**YOLO Mode:** Minimal upfront planning, discover story through writing, fast iteration
- Time to first draft: ~2 hours for 80k words

**In-Depth Mode:** Comprehensive planning before drafting, detailed foundation
- Time to first draft: ~6-8 hours for 85k words

Start with `/write:new-project` and follow the guided workflow.
