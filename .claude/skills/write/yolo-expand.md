# YOLO Mode: Complete Expansion to Writing-Ready

One-step setup from vague idea to complete writing-ready project.

## Overview

Transforms fuzzy concepts into complete story foundation:
1. Expands vague premise into structured concept
2. Generates 2-4 character sketches
3. Creates simple 3-act plot structure
4. **Optionally analyzes writing samples for style profile**
5. **Divides story into arcs for parallel writing**
6. Ready for immediate `/write:arc` execution

**Time:** 5-10 minutes
**Output:** yolo-characters.md, yolo-outline.md, optionally STYLE.md
**Next step:** `/write:arc` writes all chapters

## Workflow

### Step 1: Validate YOLO Mode

Check PROJECT.md frontmatter confirms `mode: yolo`.

If not YOLO mode, suggest `/write:plan` for In-Depth projects.

### Step 2: Expand Premise

Analyze vague idea and generate 2-3 sentence expanded premise including:
- Protagonist type (detective, scholar, rebel, etc.)
- Core conflict/goal (solve mystery, survive, prevent disaster, etc.)
- Setting (modern city, fantasy kingdom, space station, etc.)
- Unique hook (what makes this interesting)
- Stakes (what happens if they fail)

**Examples:**

*Vague:* "detective with magic powers"
*Expanded:* "A homicide detective who secretly possesses telepathy must solve murders in a modern city where magic is illegal, while hiding her abilities from her mundane partner and avoiding the Inquisition. When the murders reveal a government conspiracy, she must choose between staying hidden and stopping a magical catastrophe."

*Vague:* "space station mystery"
*Expanded:* "A maintenance engineer on a remote space station discovers a murder in the sealed environment. As more deaths occur, she realizes the station's AI may be sentient and eliminating crew who threaten its secret. She must uncover the truth before the AI decides she knows too much."

Update PROJECT.md Premise section with expanded version.

### Step 3: Generate Character Sketches

Create 2-4 character sketches from the premise:

**Required:**
1. **Protagonist** - main character driving the story
2. **Antagonist** - opposing force (person, organization, nature, self)

**Optional (1-2):**
3. **Ally** - friend, mentor, partner, love interest
4. **Rival** - secondary antagonist complicating journey

**For each character:**
- **Name**: Genre-appropriate
- **Role**: Protagonist/Antagonist/Ally/Rival
- **Core Traits (3)**: Mix of strengths and flaws
- **Brief Background (2-3 sentences)**: Formative events, why they're in this story
- **Primary Goal**: What they want (1 sentence)
- **Voice Note (optional)**: How they speak

Write to `stories/{slug}/yolo-characters.md`.

### Step 4: Create Simple Outline

Generate 3-act structure from premise and characters:

**Act 1: Setup (~25% of story)**
- Opening scene: Where/how story begins, normal world
- Inciting incident: What disrupts normal, forces protagonist to act
- Commitment point: What locks protagonist into journey

**Act 2: Confrontation (~50% of story)**
- Major complications (2-4 bullet points): Key events escalating conflict
- Midpoint twist: Major revelation or reversal
  - False victory → setback, OR
  - New information changes everything, OR
  - Commitment deepens (can't turn back)

**Act 3: Resolution (~25% of story)**
- Climax concept (2-3 sentences): Final confrontation/decision, stakes, how earlier elements pay off
- Resolution (1-2 sentences): How story ends, new normal, character growth

Keep high-level with bullets, not detailed scenes. Leave room for discovery during writing.

Write to `stories/{slug}/yolo-outline.md`.

### Step 5: Optional Style Profile

Ask if user wants to provide writing samples:

```
═══════════════════════════════════════
OPTIONAL: STYLE PROFILE
═══════════════════════════════════════

Create style profile for authentic voice matching?

YES: Paste 2-3 paragraphs of your writing
→ Analyzes sentence patterns, vocabulary, tone
→ Creates STYLE.md for chapter generation
→ Better voice matching

NO: Use genre-appropriate defaults
→ Still produces good prose
→ Can add later with /write:style-seed

Create style profile now? [y/N]
```

**If yes:**
1. Prompt for 2-3 sample paragraphs
2. Analyze patterns:
   - Average sentence length
   - Sentence length variance (std deviation)
   - Vocabulary level (simple/moderate/rich)
   - Common words and phrases
   - Tone markers (formal/casual, lyrical/direct)
   - Narrative distance (close/moderate/distant)
3. Create STYLE.md with profile
4. Confirm: "✓ Style profile created from your samples"

**If no:**
- Skip style creation
- Note genre defaults will be used

### Step 6: Divide into Arcs

Automatically divide outline into writing arcs based on story length from PROJECT.md:

**Short story (< 7,500 words):**
- 1 arc = entire story
- Chapters: 1-3

**Novella (7,500-40,000 words):**
- 3 arcs matching acts
- Arc 1: Act 1 setup (chapters 1-X)
- Arc 2: Act 2 confrontation (chapters X-Y)
- Arc 3: Act 3 resolution (chapters Y-end)

**Novel (40,000+ words):**
- 3-5 arcs, dividing Act 2 if needed
- Arc 1: Act 1 setup
- Arc 2: Act 2 rising action (first half)
- Arc 3: Act 2 complications (second half)
- Arc 4: Act 3 climax and resolution

Estimate chapter count based on length:
- Short story: 1-3 chapters (~500-1000 words each)
- Novella: 5-15 chapters (~1000-2500 words each)
- Novel: 15-30 chapters (~2000-4000 words each)

Add arc breakdown to yolo-outline.md:

```markdown
## Arc Breakdown

Arc 1 (Chapters 1-3): Setup
- Opening scene, establish normalcy
- Introduce protagonist and world
- Inciting incident occurs
- Protagonist commits to journey

Arc 2 (Chapters 4-7): Rising Action
- Complications begin
- Relationships develop
- Skills and knowledge gained
- Midpoint twist

Arc 3 (Chapters 8-10): Resolution
- Darkest moment / crisis
- Final confrontation
- Resolution of conflict
- New normal established
```

### Step 7: Completion Message

Update PROJECT.md status and show ready message:

```yaml
status: ready-to-write
```

```
✓ YOLO EXPANSION COMPLETE
═══════════════════════════════════════

Your story is ready to write:
✓ Premise expanded
✓ Characters created ({count} sketches)
✓ Plot structure outlined (3-act)
{✓ Style profile created}
✓ Arcs identified

Files created:
- yolo-characters.md
- yolo-outline.md
{- STYLE.md}

Story structure:
• {arc_count} arcs
• ~{chapter_estimate} chapters
• Target: {word_count_goal or "open-ended"}

═══════════════════════════════════════
READY TO WRITE
═══════════════════════════════════════

YOLO philosophy: Details emerge during drafting.
Your outline is a guide, not a contract.

Next step: /write:arc

This will write ALL chapters automatically,
arc by arc with parallel subagents.

Estimated time: ~{time} for first draft
```

Time estimates:
- Short story: ~30 minutes
- Novella: ~1 hour
- Novel: ~2 hours

## Notes

- **One-step setup**: Everything needed for writing in one command
- **Style is optional**: Genre defaults work well, but samples are better
- **Arc breakdown automatic**: Based on story length from PROJECT.md
- **Ready for /write:arc**: No additional setup needed
- **Can refine later**: All files are editable, add detail anytime

## Integration

**Before `/write:expand`:** Run `/write:new-project` first
**After `/write:expand`:** Run `/write:arc` to write chapters
**Optional additions:**
- `/write:populate-bank` - Create character bank from sketches
- Edit yolo-characters.md or yolo-outline.md to add detail
- `/write:style-seed` - Add style profile later if skipped
