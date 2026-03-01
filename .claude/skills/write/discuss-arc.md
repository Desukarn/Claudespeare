# Discuss Arc (In-Depth Mode)

Interactive discussion to plan a specific arc before writing chapters.

## Overview

For In-Depth mode projects, this command helps clarify arc-specific details through targeted questions before writing. Creates ARC-{N}-CONTEXT.md capturing decisions.

**Time:** 5-10 minutes per arc
**Output:** ARC-{N}-CONTEXT.md with planning details
**Next step:** `/write:arc {N}` to write that arc's chapters
**Mode:** In-Depth only (YOLO uses `/write:expand` for all arcs at once)

## Workflow

### Step 1: Validate In-Depth Mode

Check PROJECT.md confirms `mode: indepth`.

If YOLO mode, explain: "YOLO mode doesn't use arc-by-arc discussion. Run `/write:expand` to set up all arcs, then `/write:arc` to write everything."

### Step 2: Require Arc Number

Arc number must be provided in $ARGUMENTS.

**If no arc number:**
```
Error: Arc number required for /write:discuss

Usage: /write:discuss N

Examples:
  /write:discuss 1  - Discuss Arc 1 details
  /write:discuss 2  - Discuss Arc 2 details

For In-Depth mode, discuss each arc before writing it.
```

### Step 3: Load Story Context

Read all available story context:
- PROJECT.md
- CHARACTERS.md
- OUTLINE.md
- ARCS.md (character arcs)
- WORLD.md (world-building)
- Existing ARC-*-CONTEXT.md files (previous arc discussions)
- Existing chapters/*.md (if any arcs already written)

### Step 4: Identify Arc Scope

From OUTLINE.md, identify what Arc {N} covers:
- Which act or act portion
- Which plot beats
- Estimated chapter range
- Key events to include

**Example for Arc 2:**
```
Arc 2 (from OUTLINE.md):
- Act 2, Rising Action (first half)
- Chapters 5-9 (estimated)
- Plot beats:
  • Investigation deepens
  • Meet informant
  • First major obstacle
  • Relationship develops
  • Midpoint twist begins
```

### Step 5: Ask Clarifying Questions

Ask 3-5 targeted questions about this arc:

**Question 1: Chapter Focus**
```
Arc {N} covers {X} major plot beats. How many chapters should this be?

Recommendation: {estimate} chapters (~{words} words each)

Your choice: ___
```

**Question 2: POV Distribution**
```
Which characters have POV in this arc?

Available POV characters:
{list from CHARACTERS.md}

For each chapter in arc, specify POV or use pattern:
- All {character}: Stick with one POV
- Alternate: Rotate between characters
- Specify per chapter: Ch5:{char}, Ch6:{char}, etc.

Your choice: ___
```

**Question 3: Emphasis**
```
What should Arc {N} emphasize?

Options:
- Plot advancement (fast pacing, action focus)
- Character development (internal growth, relationships)
- World-building (reveal setting details, establish rules)
- Balanced (mix of all three)

Your choice: ___
```

**Question 4: Tone Shift (if applicable)**
```
Does this arc have different tone than previous?

Arc {N-1} was: {previous_tone if exists, otherwise skip question}

Arc {N} tone:
- Same as before
- Darker / more serious
- Lighter / more hopeful
- Tense / suspenseful
- Other: ___

Your choice: ___
```

**Question 5: Specific Concerns**
```
Any specific concerns or requirements for this arc?

Examples:
- "Make sure to foreshadow the betrayal in Chapter 7"
- "Keep the magic system rules consistent"
- "Don't resolve the mystery yet, just deepen it"
- "Include backstory for Marcus"

Your input: ___
```

### Step 6: Generate Arc Plan

Based on answers, create detailed arc plan:

```markdown
# Arc {N} Planning Context

## Arc Scope
- Act: {act_name}
- Chapters: {start}-{end} ({count} chapters)
- Estimated words: ~{total_words}
- Plot beats: {list_from_outline}

## Chapter Breakdown

### Chapter {X}: {title_from_beat}
- POV: {character}
- Plot: {main_beat_for_this_chapter}
- Emphasis: {plot/character/world/balanced}
- Target words: ~{estimate}
- Key elements: {any_specific_requirements}

### Chapter {X+1}: {title}
- POV: {character}
- Plot: {beat}
- Emphasis: {emphasis}
- Target words: ~{estimate}
- Key elements: {requirements}

[... repeat for all chapters in arc]

## Arc Goals
- Plot advancement: {what_progresses}
- Character development: {what_grows}
- World reveals: {what_shown}
- Tone: {tone_choice}

## Special Considerations
{any_specific_concerns_from_Q5}

## Continuity Notes
- References to previous arcs: {what_to_reference}
- Setup for future arcs: {what_to_foreshadow}

## Next Step
Ready for `/write:arc {N}` to write these chapters with this planning context.
```

### Step 7: Save Arc Context

Write to `stories/{slug}/ARC-{N}-CONTEXT.md`.

### Step 8: Confirmation Message

```
✓ ARC {N} PLANNING COMPLETE
═══════════════════════════════════════

Arc {N}: {act_name}
Chapters: {start}-{end} ({count} chapters)
Estimated: ~{words} words
POV: {pov_pattern}
Emphasis: {emphasis}

Saved to: ARC-{N}-CONTEXT.md

═══════════════════════════════════════
READY TO WRITE
═══════════════════════════════════════

Next step:
→ /write:arc {N}
  Write this arc's chapters in parallel
  (~{time_estimate})

OR
→ /write:arc auto
  Auto-detects and writes this arc
  (Same result, skips manual numbering)

Continue planning:
• /write:discuss {N+1} - Plan next arc first
• Edit ARC-{N}-CONTEXT.md - Refine details
```

## Examples

**Example 1: First arc discussion**
```
User: /write:discuss 1

→ Questions about Act 1 setup
→ How many chapters? (suggests 3-4)
→ POV pattern? (suggests protagonist)
→ Emphasis? (suggests balanced)
→ Specific concerns? (user notes foreshadowing)
→ Creates ARC-1-CONTEXT.md
→ Ready for /write:arc 1
```

**Example 2: Mid-story arc**
```
User: /write:discuss 3

→ Reviews previous arcs (1-2 already written)
→ Questions about Act 2 complications
→ How many chapters? (suggests 5-6)
→ POV pattern? (suggests alternating Sarah/Marcus)
→ Tone shift? (user chooses "darker/more serious")
→ Creates ARC-3-CONTEXT.md with continuity notes
→ Ready for /write:arc 3
```

## Integration with /write:arc

When `/write:arc {N}` runs in In-Depth mode:
1. Checks for ARC-{N}-CONTEXT.md
2. If exists: Uses planning context for chapter generation
3. If missing: Prompts to run `/write:discuss {N}` first

## Notes

- **In-Depth mode only**: YOLO doesn't need arc-by-arc discussion
- **One arc at a time**: Discuss → write → discuss → write rhythm
- **Context carries forward**: Each discussion references previous arcs
- **Flexible**: Can edit ARC-{N}-CONTEXT.md before writing
- **Optional but recommended**: Can skip and let `/write:arc {N}` ask questions

## Comparison

**YOLO:** `/write:expand` plans ALL arcs at once → `/write:arc` writes everything
**In-Depth:** `/write:discuss 1` → `/write:arc 1` → `/write:discuss 2` → `/write:arc 2` → etc.
