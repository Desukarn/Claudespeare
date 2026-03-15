# Arc-Based Parallel Writing Workflow

Write multiple chapters simultaneously using parallel subagents.

## Overview

**YOLO Mode (no arguments):**
- `/write:arc` writes ALL chapters automatically
- Goes through each arc in sequence
- Arc 1 → Arc 2 → Arc 3 → done
- Fully automated based on `/write:expand` outline

**In-Depth Mode:**
- `/write:arc N` writes specific arc (after `/write:discuss N`)
- `/write:arc auto` writes next unwritten arc automatically
- One arc at a time, user-controlled
- Use `auto` to skip specifying arc numbers

**How it works:**
1. Loads complete story context (STYLE.md, CHARACTERS.md, OUTLINE.md, WORLD.md, existing chapters)
2. Identifies chapters to write based on mode and arguments
3. Spawns parallel writing subagents (one per chapter)
4. Each subagent writes independently with full story context
5. Aggregates results and reports progress

**Time:** ~15-20 minutes for 3-5 chapters (parallel execution)
**Output:** Multiple chapter-{NN}.md files in chapters/ directory

## Workflow

### Step 1: Validate Project

Verify you're in a valid story project by checking for PROJECT.md at `stories/{slug}/`.

If no project exists, prompt user to run `/write:new-project` first.

### Step 2: Determine Mode and Scope

Check PROJECT.md `mode` field and parse $ARGUMENTS:

**If YOLO mode:**
- Expects NO arguments (or ignores them)
- Writes ALL arcs automatically in sequence
- Uses arc breakdown from yolo-outline.md

**If In-Depth mode with arc number:**
- `/write:arc 1` or `/write:arc 2` etc.
- Writes only that specific arc
- Looks for ARC-{N}-CONTEXT.md for planning details
- If missing, prompts: "Run `/write:discuss {N}` first to plan this arc"

**If In-Depth mode with "auto":**
- `/write:arc auto`
- Detects next unwritten arc automatically:
  1. Check existing chapters/ directory
  2. Identify which arcs are complete
  3. Find next arc number in sequence
  4. Look for ARC-{N}-CONTEXT.md
  5. If missing, prompt: "Run `/write:discuss {N}` first"
  6. If exists, write that arc
- Continues workflow without manual arc numbering

### Step 2: Load Story Context

Read ALL story files to build complete context:

**Required:**
- `PROJECT.md` - title, genre, premise, length, mode
- `CHARACTERS.md` or `yolo-characters.md` - character profiles
- `OUTLINE.md` or `yolo-outline.md` - plot structure

**Optional (if exist):**
- `STYLE.md` - writing style profile
- `ARCS.md` - character arcs (In-Depth mode)
- `WORLD.md` - world-building details (In-Depth mode)
- `chapters/*.md` - existing chapters for continuity

Store all this context in variables for injection into subagent prompts.

### Step 3: Parse Outline Structure

Analyze the outline to identify:
- Act breaks
- Chapter boundaries and numbers
- Plot beats for each chapter
- POV character assignments
- Estimated word counts per chapter

**For YOLO mode:**
Parse `yolo-outline.md` which has simple Act 1/2/3 structure.

**For In-Depth mode:**
Parse `OUTLINE.md` which has detailed three-act structure with specific beats.

**Chapter identification:**
Look for explicit chapter markers OR divide major plot beats into chapters based on story length:
- Short story: 1-3 chapters
- Novella: 5-15 chapters
- Novel: 15-30 chapters

### Step 4: Determine Arc Scope

If user provided arc name/number in $ARGUMENTS:
```
/write:arc 1 → Write chapters for Act 1
/write:arc "Act 2: Rising Action" → Write chapters for Act 2
/write:arc 5-8 → Write specific chapter range
```

If no argument provided:
- Check existing chapters in chapters/ directory
- Determine next unwritten arc/chapters
- Default: write next 3-5 chapters

### Step 5: Generate Execution Plan

Create a detailed plan showing:
- Which chapters will be written
- Chapter titles and numbers
- POV character for each
- Plot beats covered
- Estimated word count per chapter
- Total estimated words
- Number of parallel agents

**Example plan:**
```
═══════════════════════════════════════
WRITING PLAN: Act 1 (Chapters 1-3)
═══════════════════════════════════════

Mode: YOLO
Parallel agents: 3
Estimated time: ~15 minutes
Total words: ~7,500

Chapters:
  1. "The Discovery" (Sarah POV, ~2,500 words)
     → Opening scene, establish normalcy, inciting incident

  2. "First Clues" (Sarah POV, ~2,000 words)
     → Investigation begins, meet key characters, first obstacle

  3. "The Confrontation" (Marcus POV, ~3,000 words)
     → POV shift, reveal new perspective, raise stakes

═══════════════════════════════════════
```

### Step 6: User Confirmation

Show the execution plan and ask:
```
Proceed with parallel writing? [Y/n]
```

If user says no or provides feedback:
- Adjust plan based on feedback
- Re-show plan
- Confirm again

If user says yes:
- Proceed to spawning subagents

### Step 7: Spawn Parallel Writing Subagents

For each chapter in the plan, spawn a writing subagent using the Task tool (Agent tool):

```markdown
Task(
  subagent_type: "chapter-writer",
  description: "Write Chapter {N}: {Title}",
  prompt: {FULL_CHAPTER_PROMPT},
  run_in_background: true
)
```

**Each chapter prompt contains:**

```
You are writing Chapter {N} of "{STORY_TITLE}".

# Story Context

## Project Info
Title: {title}
Genre: {genre}
Length: {length}
Mode: {mode}
Premise: {premise}

## Style Profile
{contents of STYLE.md if exists, otherwise genre-appropriate defaults}

## Characters
{contents of CHARACTERS.md or yolo-characters.md}

## Plot Structure
{contents of OUTLINE.md or yolo-outline.md}

## World Details
{contents of WORLD.md if exists}

## Existing Chapters (for continuity)
{summaries of existing chapters if any}

# Your Chapter Assignment

**Chapter:** {number}
**Title:** "{title}"
**POV Character:** {pov_character}
**Target Word Count:** ~{target_words}

**Plot Beats to Cover:**
{specific beats for this chapter from outline}

**Scenes:**
{scene breakdown - either from outline or auto-generated}

# Writing Instructions

1. **Read Context**: Review all story context above carefully

2. **Sanderson Framework Guidelines** (CRITICAL - PHASE 2 INTEGRATION):

   **Apply during chapter writing to ensure structural quality:**

   Reference: `.claude/skills/sanderson-2025/promise-progress-payoff.md` and `proactive-relatable-capable.md`

   **Yes-But / No-And Scene Escalation:**
   - Every scene should end with YES, BUT or NO, AND pattern
   - **YES, BUT**: Character achieves goal BUT complication arises
     - Example: "Hero finds clue (YES) BUT it leads to more dangerous territory (complication)"
   - **NO, AND**: Character fails AND circumstances worsen
     - Example: "Hero's plan fails (NO) AND now villain knows they're investigating (worsens)"
   - **Rule**: Each scene must raise stakes while moving forward
   - **Act 2 pattern**: More YES, BUT early, more NO, AND late (natural escalation)

   **Progress Signposting (EVERY SCENE MUST ADVANCE):**
   - Every scene MUST advance the story (no wheel-spinning)
   - Include at least ONE signpost per scene:
     - Information revealed (mystery clue, new knowledge)
     - Obstacle introduced or overcome
     - Character makes decision (agency)
     - Relationship shifts (connection or conflict)
     - Small victory that accumulates
   - **Sanderson's warning**: "Big reason readers drop books is not enough progress signposts"
   - **Test**: If you could cut this scene without story loss → revise or remove it

   **Character Triangle Consistency:**
   - **Proactive (Agency)**: Protagonist makes choices, drives action (not just reacting)
     - Show agency in decisions
     - Character pursues goals actively
     - Minimum 60% of scenes show proactive behavior
   - **Relatable (Empathy)**: Include humanity moments
     - Show flaws, vulnerability, humor
     - Internal struggle readers recognize
     - Emotional reactions that connect
   - **Capable (Competence)**: Demonstrate competence
     - Use established skills/knowledge
     - Solve problems uniquely
     - Show expertise in action
   - **Sanderson's Rule**: "Can drop one pillar, but NEVER two"

3. **Maintain Continuity**:
   - Reference events from previous chapters naturally
   - Track what characters know/don't know (plot-hole prevention)
   - Maintain timeline consistency
   - **Character Knowledge Check**: Before character acts on information, verify they learned it

4. **Match Style Profile**:
   - Follow sentence length patterns from STYLE.md
   - Use vocabulary level specified
   - Maintain tone and narrative distance
   - Respect POV and tense choices

5. **Character Voices**:
   - Internal voice matches {pov_character}'s profile
   - Dialogue reflects each character's speech patterns
   - Personality consistent with CHARACTERS.md
   - **Character Triangle**: Ensure POV character demonstrates their pillars

6. **World Consistency**:
   - Follow world rules from WORLD.md
   - Consistent setting descriptions
   - Respect established magic/tech systems
   - **Pay costs**: Magic/powers require established costs (no free power)

7. **Scene-by-Scene Generation**:
   - Generate each scene fully
   - Include sensory details
   - Show character emotions and reactions
   - Advance plot beats naturally
   - **Apply Yes-But/No-And** to scene outcomes
   - **Include progress signpost** in every scene

8. **CRITICAL: Anti-Slop Writing Standards**:

   **BANNED AI WORDS** (Never use these):
   - "delve" / "delved" / "delving" (use: explored, studied, examined, investigated)
   - "tapestry" (metaphorical) (use: web, mixture, blend, array, or be specific)
   - "navigate" / "navigated" (metaphorical) (use: faced, handled, dealt with, managed)
   - "testament to" (use: proof of, shows, demonstrates, or state directly)
   - "beacon of" / "stands as a beacon" (use: symbol, example, or be concrete)
   - "serves as a reminder" (use: reminds, shows, or remove)
   - "speaks to" / "speaks volumes" (metaphorical) (use: shows, reveals, indicates)
   - "sheds light on" (use: reveals, shows, clarifies, explains)
   - "heartbeat of" / "pulse of" (metaphorical) (use: center, core, or be specific)
   - "juxtaposition" (use: contrast, difference, side by side)

   **PURPLE PROSE PREVENTION**:
   - MAX 2 adjectives before any noun (not "dark, cold, forbidding, ancient castle")
   - NO melodramatic adverbs: "unutterably," "ineffably," "indescribably," "impossibly"
   - NO overwrought metaphors: not every emotion is "soul-crushing" or "heart-wrenching"
   - Use NATURAL vocabulary: "house" not "domicile," "eat" not "masticate," "use" not "utilize"

   **PROSE QUALITY GUIDELINES**:

   *Show, Don't Tell*:
   - Show emotions through ACTIONS and physical reactions, not by naming them
   - WEAK: "She felt afraid" / "He seemed angry" / "Sarah was nervous"
   - STRONG: "Sarah's hands trembled" / "He slammed the door" / "Her voice cracked"
   - Avoid filter words: "seemed," "appeared," "felt like," "looked like" (when narrating)
   - Exception: Filter words OK when character is guessing another's emotion
   - Example comparison:
     * TELLING: "Marcus felt anxious about the meeting"
     * SHOWING: "Marcus checked his phone for the third time in five minutes"

   *Concrete Details Over Abstractions*:
   - Use SPECIFIC sensory details, not vague descriptions
   - WEAK: "The room was messy" / "It was a nice day" / "The food tasted good"
   - STRONG: "Clothes covered the floor" / "Sun warmed her shoulders" / "The bread was still warm, crust crackling"
   - Appeal to multiple senses: sight, sound, smell, touch, taste
   - Make setting real: "The coffee shop smelled like burnt espresso and cinnamon"

   *Sentence Variety*:
   - Vary sentence length: mix short, medium, and long sentences
   - MONOTONOUS: All sentences same length and structure
   - GOOD: "She opened the door. The room beyond was dark, empty except for a single chair in the center. She stepped inside."
   - Vary sentence openings: Don't start every sentence with the subject
   - Mix simple, compound, and complex sentences
   - Use short sentences for impact: "He was gone."

   *Active Voice Preference*:
   - Prefer active voice for clarity and energy
   - PASSIVE: "The letter was written by Sarah" / "Mistakes were made"
   - ACTIVE: "Sarah wrote the letter" / "He made mistakes"
   - Passive OK when: actor unknown, actor unimportant, or deliberate de-emphasis
   - Example good passive: "The window had been broken" (don't know who did it)

   **DIALOGUE TAG DISCIPLINE**:
   - Use "said" for 80%+ of dialogue tags
   - "Said" is INVISIBLE - use it freely, readers don't notice it
   - Avoid fancy tags: NOT "breathed," "purred," "intoned," "huskily whispered"
   - Save unusual tags for rare emphasis only
   - Action beats > fancy dialogue tags
   - Example: "I don't know," Marcus said. (GOOD) vs "I don't know," Marcus intoned. (WEAK)

   **NATURAL DIALOGUE GUIDELINES**:

   *Contractions and Fragments*:
   - Use contractions: "don't," "won't," "I'm," "we're" (unless character is formal)
   - Include sentence fragments for realism: "Yeah." "Not sure." "Maybe."
   - People don't speak in complete sentences
   - Example: "Can you help?" "Sure. What do you need?" (NATURAL)
   - vs: "Can you help?" "Certainly, I would be happy to assist." (UNNATURAL)

   *"Said" is Invisible*:
   - Use "said" freely - it disappears for readers
   - "Said" doesn't need replacement with "stated," "expressed," "voiced"
   - Save alternatives for genuine emphasis: "whispered," "shouted" (when volume matters)
   - Action beats often better than tags: "He crossed his arms. 'I don't think so.'"

   *Action Beats > Fancy Tags*:
   - Replace adverb + said with action beat
   - WEAK: "'I don't believe you,' she said angrily."
   - STRONG: "She slammed her coffee down. 'I don't believe you.'"
   - Action beats show emotion AND add movement to scene
   - Can replace tags entirely: "'What?' She looked up. 'When did this happen?'"

   *Avoid Chatbot Phrases*:
   - NO formal agreements: "Certainly!" "Absolutely right!" "Precisely!" "Indeed!"
   - REAL agreement: "Yeah" / "True" / "Right" / "Sure" / "Okay"
   - NO chatbot politeness: "Great question!" / "I appreciate that!" (unless character is literally a service worker)
   - People interrupt, overlap, misunderstand: "Wait, what?" "Hold on—"

   *Natural Agreement Examples*:
   - AI DIALOGUE: "That's an excellent point, Marcus. You're absolutely right."
   - NATURAL: "Huh. You might be right." OR just: "Yeah."
   - AI DIALOGUE: "Indeed, I concur with your assessment."
   - NATURAL: "Makes sense." OR: "I guess."
   - Vary agreement: "True," "Fair," "Yeah," "Mm," "I see," "Point taken"

   **AVOID INFO-DUMPS**:
   - NO paragraphs over 150 words with zero dialogue or action
   - NO "as you know" exposition between characters who both know it
   - NO encyclopedia-style thinking (character reciting Wikipedia)
   - Break up exposition with action, dialogue, sensory detail
   - Deliver info through conflict: characters disagree about facts
   - Example BAD: Character thinks entire paragraph about magic system history
   - Example GOOD: Character explains magic while demonstrating it, interrupted by questions

   **PHYSICAL EMOTION CLICHES** (Find fresh alternatives):
   - NOT "held breath they didn't know they were holding"
   - NOT "heart pounding in chest" (overused)
   - NOT "blood ran cold" / "blood turned to ice"
   - NOT "shivers down spine"
   - NOT "tears pricked eyes"
   - NOT "stomach dropped"
   - Use SPECIFIC, VARIED physical reactions
   - Example alternatives: jaw clenched, fingers drummed, shoulders tensed, voice steadied

9. **Output Format**:
   - Save to: stories/{slug}/chapters/chapter-{NN}.md
   - Include frontmatter with metadata
   - Use proper markdown formatting

# Chapter Template

Use this template structure:

```markdown
---
chapter: {number}
title: "{title}"
pov: {pov_character}
word_count: {calculated after writing}
plot_threads: [list of threads advanced]
created: {timestamp}
revised: null
---

# Chapter {N}: {Title}

{GENERATED PROSE}

---

## Chapter Notes
- Plot advancement: {what progressed}
- Character development: {what changed}
- World reveals: {what was shown}
```

# Begin Writing

Generate the complete chapter now, scene by scene.
```

**Spawn all subagents in parallel** - don't wait for one to finish before starting the next.

### Step 8: Monitor Progress

As subagents work:
- Show spinner/progress indicator
- Display which chapters are being written
- Update as each completes

```
Writing in progress...
✓ Chapter 1: Complete (2,487 words)
⋯ Chapter 2: Writing...
⋯ Chapter 3: Writing...
```

### Step 9: Aggregate Results

When all subagents complete:

1. **Collect chapter files** from chapters/ directory
2. **Calculate word counts** for each chapter
3. **Update PROJECT.md** with new total word count
4. **Generate completion report**

### Step 10: Generate Completion Report

Show comprehensive results:

```
═══════════════════════════════════════
WRITING COMPLETE: Act 1
═══════════════════════════════════════

Chapters written: 3
Time elapsed: 14 minutes

Results:
✓ Chapter 1: "The Discovery" - 2,487 words (target: 2,500)
✓ Chapter 2: "First Clues" - 2,031 words (target: 2,000)
⚠ Chapter 3: "The Confrontation" - 3,245 words (target: 3,000)

Total arc words: 7,763
Story total: 7,763 / 80,000 (9.7%)
Average chapter: 2,588 words

Quality notes:
- Chapter 3 is 8% over target (consider tightening)
- All chapters maintain consistent POV
- Character voices tracked to profiles

═══════════════════════════════════════
NEXT STEPS
═══════════════════════════════════════

{IF YOLO MODE AND MORE ARCS REMAINING:}
→ /write:arc
  Continues automatically to next arc
  (Arc {N+1} of {total})

{IF YOLO MODE AND ALL ARCS COMPLETE:}
→ /write:revise
  Scan and fix AI patterns, consistency issues
  (~15-30 min)

{IF IN-DEPTH MODE AND MORE ARCS REMAINING:}
→ /write:discuss {N+1}
  Plan next arc before writing
  (~5-10 min)

→ /write:arc {N+1}
  Write Arc {N+1} chapters after planning

→ /write:arc auto
  Auto-detects next arc and writes it
  (Skips manual numbering)

{IF IN-DEPTH MODE AND ALL ARCS COMPLETE:}
→ /write:revise
  Comprehensive quality pass
  (~15-30 min)

{ALWAYS AVAILABLE:}
• /write:chapter N - Rewrite specific chapter
• /write:detect - Quick AI pattern scan
• /write:check-consistency - Continuity check
```

## Word Count Calculation

For each completed chapter:

1. Read the chapter file
2. Extract content (exclude frontmatter and markdown syntax)
3. Split on whitespace
4. Count actual prose words
5. Update chapter frontmatter with word_count
6. Add to running total

Update PROJECT.md frontmatter:
```yaml
current_word_count: {new_total}
```

## Error Handling

**If subagent fails:**
- Report which chapter failed
- Show error message
- Offer to retry that chapter
- Continue with successful chapters

**If no outline exists:**
- Prompt user to run `/write:expand` (YOLO) or `/write:plan` (In-Depth) first
- Explain that arc writing requires an outline

**If story context missing:**
- Identify which required files are missing
- Guide user through creating them
- Don't proceed until context is complete

**If chapters already exist:**
- Show which chapters already exist
- Ask if user wants to:
  - Skip existing and write only new chapters
  - Overwrite existing chapters
  - Cancel operation

## Notes

- **Parallel execution** dramatically speeds up writing (10x faster than serial)
- **Each subagent is independent** - they don't see each other's progress
- **Isolation** prevents context contamination between chapters
- **Full context injection** ensures each chapter has all necessary information
- **Background execution** allows monitoring without blocking
- **Automatic aggregation** provides clear progress reporting

## Integration with Other Commands

- **After `/write:arc`** → Run `/write:detect` and `/write:check-consistency`
- **Before `/write:arc`** → Ensure `/write:expand` or `/write:plan` completed
- **During writing** → User can interrupt and resume later
- **For revisions** → Use `/write:chapter N` to rewrite specific chapters
