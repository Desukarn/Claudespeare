# Chapter Generation Workflow

Write a single chapter with full story context - matches your style, maintains character voices, tracks plot threads.

## Overview

This workflow generates chapters that match YOUR writing style. It loads all story context (style profile, character voices, plot structure, world details) and produces prose that maintains consistency.

**Time:** 15-30 minutes per chapter
**Output:** chapter-{NN}.md in chapters/ directory
**When to use:** Write or rewrite a specific chapter

## Smart Context Detection

The command automatically detects chapter information from your outline when possible:

**If you provide a chapter number** (e.g., `/write:chapter 5` or arguments like "5"):
- Auto-loads chapter 5 details from OUTLINE.md
- Detects POV character, plot beats, scenes
- Non-interactive generation

**If you provide no arguments** (just `/write:chapter`):
- Suggests next unwritten chapter
- Interactive mode if context unclear
- Asks for chapter specifics

## The Workflow

### Step 1: Validate Story Project

Verify you're in a valid story project by reading `PROJECT.md` from `stories/{slug}/`.

If no project exists, prompt to run `/write:new-project` first.

### Step 2: Load Story Context

Load ALL available story files:

**Required:**
- `PROJECT.md` - title, length, mode, genre, premise
- `CHARACTERS.md` or `yolo-characters.md` - character profiles with voice notes
- `OUTLINE.md` or `yolo-outline.md` - plot structure with beats

**Optional (if exist):**
- `STYLE.md` - writing style profile (from `/write:style-seed`)
- `ARCS.md` - character transformation tracking (In-Depth mode)
- `WORLD.md` - setting and world-building details (In-Depth mode)
- `chapters/*.md` - existing chapters for continuity

### Step 3: Determine Chapter Details

**If chapter number provided in $ARGUMENTS:**

1. Parse outline to find chapter {N} details
2. Extract:
   - Chapter title
   - Plot beats for this chapter
   - POV character (from outline or pattern from existing chapters)
   - Scene breakdown (from outline or auto-generate based on beats)
   - Target word count (based on story length and chapter count)

3. If all details found → proceed to Step 4 automatically
4. If details missing → ask user for clarification

**If no arguments provided:**

1. Check existing chapters/ directory
2. Identify next unwritten chapter number
3. Suggest: "Write Chapter {N} next?"
4. Ask for:
   - Chapter number (confirm or override)
   - Plot beat/focus
   - POV character
   - Scene breakdown (optional)

### Step 4: Generate Chapter

Build complete chapter prompt with all story context:

```
You are writing Chapter {N} of "{TITLE}".

# Story Context

{FULL_CONTENT_OF_PROJECT_MD}

{FULL_CONTENT_OF_STYLE_MD_OR_GENRE_DEFAULTS}

{FULL_CONTENT_OF_CHARACTERS_MD}

{FULL_CONTENT_OF_OUTLINE_MD}

{FULL_CONTENT_OF_WORLD_MD_IF_EXISTS}

{SUMMARIES_OF_EXISTING_CHAPTERS}

# Chapter Assignment

Chapter: {number}
Title: "{title}"
POV: {pov_character}
Target words: ~{target}

Plot beats:
{beats_for_this_chapter}

Scenes:
{scene_breakdown}

# Writing Instructions

Generate the complete chapter following these guidelines:

**Style Matching:**
- Match sentence length patterns from style profile
- Use vocabulary level specified
- Follow tone markers and narrative distance
- Respect POV and tense

**Character Voices:**
- POV character's internal voice matches profile
- Each character's dialogue reflects speech patterns
- Personality consistent across chapters

**Story Continuity:**
- Reference previous chapters naturally
- Track character knowledge
- Maintain timeline
- Follow world rules

**Scene Structure:**
- Generate scene-by-scene
- Include sensory details
- Show emotions and reactions
- Advance plot organically

**Output Format:**

Use this template:

```markdown
---
chapter: {number}
title: "{title}"
pov: {pov_character}
word_count: {calculate_after_writing}
plot_threads: [{threads_advanced}]
created: {timestamp}
revised: null
---

# Chapter {N}: {Title}

{GENERATED_PROSE}

---

## Chapter Notes
- Plot advancement: {summary}
- Character development: {changes}
- World reveals: {new_info}
```

Save to: stories/{slug}/chapters/chapter-{NN}.md
```

Generate the chapter now.

### Step 5: Calculate Word Count

After generation:

1. Read the generated chapter file
2. Extract prose content (exclude frontmatter and markdown formatting)
3. Split on whitespace and count words
4. Update chapter frontmatter with word_count field

### Step 6: Update Story Progress

Update PROJECT.md:

1. Read current `current_word_count` from PROJECT.md frontmatter
2. Add new chapter word count to total
3. Update PROJECT.md frontmatter with new total
4. If `word_count_goal` exists, calculate percentage

### Step 7: Report Completion

Show chapter summary:

```
═══════════════════════════════════════
CHAPTER COMPLETE
═══════════════════════════════════════

Chapter {N}: "{Title}"
Words: {count} (target: {target})
POV: {character}
Status: {under/on/over target}

Story Progress:
Total: {total} / {goal} words ({percent}%)
Chapters: {count}
Average: {avg} words/chapter

═══════════════════════════════════════
NEXT STEPS
═══════════════════════════════════════

{IF MORE CHAPTERS IN OUTLINE:}
Continue writing:
→ /write:chapter {N+1}
  Write next chapter ({title_from_outline})

→ /write:arc
  Write remaining chapters in parallel
  (Faster than one-by-one)

{IF ALL CHAPTERS COMPLETE:}
→ /write:revise
  Scan and fix quality issues
  (~15-30 min for full story)

{ALWAYS AVAILABLE:}
• /write:detect - Check this chapter for AI patterns
• /write:check-consistency - Verify continuity
• /write:revisions chapter-{NN} - View edit history
```

## Context-Aware Examples

**Example 1: With chapter number**
```
User: /write:chapter 3
→ Loads chapter 3 from outline automatically
→ Detects POV, beats, scenes
→ Generates immediately
```

**Example 2: Without arguments**
```
User: /write:chapter
→ Checks chapters/, sees chapters 1-2 exist
→ Suggests: "Write Chapter 3 next?"
→ Shows what chapter 3 covers (from outline)
→ Confirms and generates
```

**Example 3: Rewriting existing**
```
User: /write:chapter 2
→ Detects chapter-02.md already exists
→ Asks: "Chapter 2 exists. Overwrite? [y/N]"
→ If yes: backs up old version, generates new
→ If no: cancels
```

## Integration with Arc Writing

`/write:chapter` is designed for:
- Writing single chapters one at a time
- Rewriting specific chapters after review
- Filling gaps in partial drafts

For writing multiple chapters at once, use `/write:arc` which spawns parallel subagents.

## Error Handling

**No outline exists:**
- Prompt to run `/write:expand` (YOLO) or `/write:plan` (In-Depth)
- Explain chapter generation needs plot structure

**Chapter number invalid:**
- If user requests chapter 50 but outline only has 30 chapters
- Ask if they want to extend outline or write a different chapter

**Missing required context:**
- Identify which files are missing
- Guide user to create them
- Don't proceed until basics exist (project, characters, outline)

## Notes

- Automatically uses STYLE.md if exists, otherwise genre defaults
- Scene-by-scene generation for chapters over 1500 words
- Single-pass generation for shorter chapters
- Saves version history automatically (see `/write:revisions`)
- Word count excludes frontmatter and markdown syntax
