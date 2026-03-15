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

## CRITICAL: Anti-Slop Writing Standards

**NAMING RULES - ABSOLUTE REQUIREMENT**:

**For NEW minor characters introduced in this chapter:**
- ❌ NEVER generate names spontaneously (AI slop risk)
- ✅ ALWAYS draw from name pools in CHARACTERS.md
- Location: See "Name Pools for Minor Characters" section
- Track used names to avoid repeats within same chapter
- Examples: Guards, shopkeepers, servants, passersby

**For NEW locations introduced in this chapter:**
- ❌ NEVER generate place names spontaneously
- ✅ ALWAYS follow naming conventions documented in WORLD.md
- Location: See "Naming Conventions" section
- Match established phonetic patterns exactly
- Example: If existing cities are "Eisenheim, Rotenburg" (Germanic), new city should be "Grünwald" (Germanic pattern), NOT "Shadowkeep" (AI slop)

**BANNED CHARACTER NAMES (AI Slop):**
- Kael, Kaelin, Kylar, Kain
- Elara, Elora, Elysia, Elira
- Lyra, Lira, Liora
- Aria, Arya, Ariana
- Theron, Talon, Zara, Zyra
- Seraphina, Celestia
- Any name ending in -ael, -ara, -lyn

**BANNED PLACE NAMES (AI Slop):**
- Shadow + [anything]: Shadowmere, Shadowkeep, Shadowfen
- Dark + [anything]: Darkwood, Darkhaven, Darkwater
- Storm + [anything]: Stormkeep, Stormreach, Stormhaven
- [Color] + [Generic]: Redwood, Blackwater, Greenmoor
- Generic fantasy: The Fallen Kingdom, The Lost City

**When in doubt about names:**
- Use descriptive terms: "the guard," "the innkeeper," "the old woman"
- Note in chapter summary that element needs naming
- User will provide authentic name in revision pass
- BETTER to use descriptor than AI slop name

**Note new named elements in chapter summary:**
- List any new minor characters introduced (with temporary descriptors if unnamed)
- List any new locations mentioned
- User will verify naming authenticity during revision

---

**BANNED AI WORDS** (Never use these):
- "delve" / "delved" / "delving" → Use: explored, studied, examined, investigated
- "tapestry" (metaphorical) → Use: web, mixture, blend, array, or be specific
- "navigate" / "navigated" (metaphorical) → Use: faced, handled, dealt with, managed
- "testament to" → Use: proof of, shows, demonstrates, or state directly
- "beacon of" / "stands as a beacon" → Use: symbol, example, or be concrete
- "serves as a reminder" → Use: reminds, shows, or remove
- "speaks to" / "speaks volumes" (metaphorical) → Use: shows, reveals, indicates
- "sheds light on" → Use: reveals, shows, clarifies, explains
- "heartbeat of" / "pulse of" (metaphorical) → Use: center, core, or be specific
- "juxtaposition" → Use: contrast, difference, side by side

**PURPLE PROSE PREVENTION**:
- MAX 2 adjectives before any noun (not "dark, cold, forbidding, ancient castle")
- NO melodramatic adverbs: "unutterably," "ineffably," "indescribably," "impossibly"
- NO overwrought metaphors: not every emotion is "soul-crushing" or "heart-wrenching"
- Use NATURAL vocabulary: "house" not "domicile," "eat" not "masticate," "use" not "utilize"

**DIALOGUE TAG DISCIPLINE**:
- Use "said" for 80%+ of dialogue tags
- "Said" is INVISIBLE - use it freely
- Avoid fancy tags: NOT "breathed," "purred," "intoned," "huskily whispered"
- Save unusual tags for rare emphasis only
- Action beats > fancy dialogue tags

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

**DIALOGUE QUALITY GUIDELINES**:

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
- Match each character's voice from their profile

**AVOID INFO-DUMPS**:
- NO paragraphs over 150 words with zero dialogue or action
- NO "as you know" exposition between characters who both know it
- NO encyclopedia-style thinking (character reciting Wikipedia entries)
- Break up exposition with action, dialogue, sensory detail
- Deliver world-building through conflict and discovery

**PHYSICAL EMOTION CLICHES** (Find fresh alternatives):
- NOT "held breath they didn't know they were holding"
- NOT "heart pounding in chest" (overused - find specific variations)
- NOT "blood ran cold" / "blood turned to ice"
- NOT "shivers down spine"
- NOT "tears pricked eyes"
- NOT "stomach dropped"
- Use SPECIFIC, VARIED physical reactions unique to your characters

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
