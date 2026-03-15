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

### Step 2.5: Quick Trope Inspiration Research (ANTI-SLOP)

**CRITICAL**: Even in YOLO mode, research fresh tropes to avoid cookie-cutter plots.

**YOLO Streamlined Process** (faster but still authentic):

**Prompt user**:
```
Would you like me to research story tropes for fresh inspiration?

YOLO mode = Quick research (5 tropes instead of 10)
Takes ~2 minutes but helps avoid common AI plot patterns:
- "Strength becomes weakness"
- "Final moral act"
- "Power corrupts protagonist"
- Standard chosen one narratives

I'll browse TVTropes.org to find unexpected angle combinations.

A. Yes - Quick trope research (recommended, 5 tropes)
B. No - Skip and plan directly
```

**If YES**: Launch quick trope research (Task tool with modified prompt)

**Modified prompt for YOLO speed**:
```
Research fresh story tropes for this premise: [premise]

Browse TVTropes.org and find 5 unexpected tropes (instead of 10) that could inspire unique angles.

Focus on:
- Tropes that subvert genre expectations
- Uncommon character dynamics
- Plot patterns that avoid clichés

Return 5 trope suggestions with brief explanations.
```

**Agent returns 5 trope suggestions**. Present to user, user selects 1-2 (instead of 2-3).

**Store selected tropes** in PROJECT.md:
```yaml
inspiration_tropes:
  - "Trope Name 1"
  - "Trope Name 2"
```

**Reference these during character and plot creation** to avoid formulaic choices.

**If NO**:
- Note that story may risk AI plot patterns
- Continue to character creation
- Can add trope research later if needed

**YOLO Mode Change**: 5 tropes instead of 10, select 1-2 instead of 2-3, but STILL AVAILABLE.

**NO BYPASSING**: Fast mode ≠ slop mode. Quality shortcuts, not quality elimination.

### Step 3: Generate Character Sketches

Create 2-4 character sketches from the premise:

**Required:**
1. **Protagonist** - main character driving the story
2. **Antagonist** - opposing force (person, organization, nature, self)

**Optional (1-2):**
3. **Ally** - friend, mentor, partner, love interest
4. **Rival** - secondary antagonist complicating journey

**For each character:**

#### Name Generation (ANTI-SLOP - REQUIRED)

**CRITICAL**: Even in YOLO mode, use online name generator for authenticity.

See `name-generator-requirement.md` for full details.

**YOLO Streamlined Process** (faster but still authentic):

1. Ask user for character context: "Tell me about this character (genre, culture/ethnicity, role, time period)"
2. Choose appropriate generator:
   - Fantasy: https://www.fantasynamegenerators.com/
   - Historical/Modern: https://www.behindthename.com/random/
   - Sci-Fi: https://www.fantasynamegenerators.com/sci-fi-names.php
3. Use WebFetch to get **5 name options** (instead of 10 for In-Depth mode)
4. Present options to user:
   ```
   Here are 5 authentic [context] names from [generator]:

   1. [Name]
   2. [Name]
   3. [Name]
   4. [Name]
   5. [Name]

   Pick a number (1-5), ask for more, or provide your own name.
   ```
5. User selects or requests regeneration

**YOLO Mode Change**: 5 options instead of 10, but STILL REQUIRED.

**NO BYPASSING**: Do NOT generate names directly. AI models are biased toward "Kael", "Elara", "Lyra", etc.

**If user provides their own name**: Accept it (bypasses generator requirement)

#### Character Details

- **Role**: Protagonist/Antagonist/Ally/Rival
- **Core Traits (3)**: Mix of strengths and flaws
- **Brief Background (2-3 sentences)**: Formative events, why they're in this story
- **Primary Goal**: What they want (1 sentence)
- **Voice Note (optional)**: How they speak

Write to `stories/{slug}/yolo-characters.md`.

### Step 3.5: Place Naming & Name Pools (ANTI-SLOP)

**CRITICAL:** Generate place names and minor character name pools BEFORE writing begins.

#### Part A: Major Place Naming

Ask user:
```
What cultural/linguistic feel for place names?

A. Germanic (Eisenheim, Rotenburg, Schwarzwald)
B. Celtic (Caerdun, Brynmor, Lynhaven)
C. Arabic (Al-Hazan, Qalat-al-Nur, Ishdarabad)
D. Nordic (Fjordheim, Vikingstad, Holmgard)
E. Latin/Romance (Valoris, Montclair, Bellehaven)
F. Asian-inspired (Tianzhou, Hanshan, Longcheng)
G. Mixed cultures (specify which)
H. Wikipedia random method (unique evocative names)
I. Skip for now (can add later)
```

**If user chooses A-G (Cultural Pattern):**

1. Determine what needs names:
   - How many major cities? (2-5 typical for YOLO)
   - How many regions/kingdoms? (1-3 typical)
   - Major geographic features? (optional: 1-2)

2. Use WebFetch or research cultural patterns:
   - Germanic: Suffixes -heim, -burg, -wald, -stadt
   - Celtic: Suffixes -dun, -ton, -bry, -mor
   - Arabic: Suffixes -abad, -dar, prefixes al-
   - etc. (see comprehensive-naming-guide.md)

3. Generate 8 options per major location type

4. Present to user:
   ```
   Major cities (Germanic pattern) - Pick 3:
   1. Eisenheim (Iron-home, metalworking center)
   2. Rotenburg (Red fortress)
   3. Grünwald (Green forest)
   4. Steinburg (Stone fortress)
   5. Silberhof (Silver court)
   6. Grauhaven (Gray harbor)
   7. Neustadt (New city)
   8. Altdorf (Old village)
   ```

5. User selects

6. Document in `stories/{slug}/WORLD.md`:
   ```markdown
   ## Major Locations

   ### [City Name]
   Brief description (1-2 sentences)

   ## Naming Conventions

   All places follow [culture] patterns:
   - Suffixes: [list]
   - Examples: [established names]
   - When introducing new locations, maintain this pattern
   ```

**If user chooses H (Wikipedia Random Method):**

1. Use Bash to fetch 10 random Wikipedia articles:
   ```bash
   for i in {1..10}; do
     curl -sL "https://en.wikipedia.org/api/rest_v1/page/random/summary" | \
     python3 -c "import sys, json; data=json.load(sys.stdin); \
     print(f\"Title: {data['title']}\nExtract: {data['extract'][:200]}...\")"
     sleep 0.5
   done
   ```

2. Extract evocative terms, syllables, place names

3. Adapt into 8 fantasy place names:
   ```
   From articles (Hastings, Byzantine, Coral, Mionów):

   Cities:
   1. Hastinmere (Hastings + mere/lake)
   2. Byzara (Byzantine inspired)
   3. Koralvast (Coral + vast)
   4. Mionwick (Mion + wick/bay)
   5. Rifport (Reef + port)
   6. Prudholm (Prud + holm)
   7. Hastengard (Hasten + gard)
   8. Opolen (Opole + suffix)
   ```

4. User picks 3-5

5. Document in WORLD.md with etymology notes

**If user chooses I (Skip):**
- Note that place names can be added during revision
- WARN: May need to rename AI-generated place names later
- Continue to name pools

#### Part B: Minor Character Name Pools

**CRITICAL:** Pre-generate name pools to prevent AI slop during writing.

Ask user:
```
I'll generate name pools for minor characters (guards, shopkeepers, servants).

What culture(s) for your character names?
- Match to place naming culture? [default]
- Different? (specify)
```

**For EACH culture in story:**

1. Use WebFetch with Behind the Name (appropriate cultural filter)
2. Generate:
   - 30 male names
   - 30 female names
   - 20 surnames/family names

3. Add to `stories/{slug}/CHARACTERS.md`:
   ```markdown
   ## Name Pools for Minor Characters

   ### [Culture] Names (e.g., Germanic-inspired)

   **Male Names (30):**
   [List of 30 names]

   **Female Names (30):**
   [List of 30 names]

   **Surnames (20):**
   [List of 20 names]

   **Usage:** For guards, shopkeepers, servants, background characters.
   Draw as needed. Track used names to avoid repeats in same scene.
   ```

**Time investment:** 3-5 minutes for both place naming and name pools

**Benefits:**
- Zero AI slop names (even for tiny roles)
- Instant access while writing
- Cultural consistency throughout
- Professional authenticity

**YOLO Mode Note:** This step adds 3-5 minutes but prevents hours of revision later removing AI slop names. RECOMMENDED even in YOLO mode.

---

### Step 4: Create Simple Outline with Conflict & Exposition Analysis

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

**CRITICAL: Add Chapter-Level Goal/Conflict/Outcome**

For EACH chapter in the outline, add this structure:

```markdown
Chapter {N}: "{Title}" ({POV character}, ~{words} words)
  GOAL: What does the character want this chapter?
  CONFLICT: What opposes them? What stands in their way?
  OUTCOME: What changes? How does the story progress?

  Plot beats:
  - {Beat 1}
  - {Beat 2}
```

**AUTOMATIC EXPOSITION DUMP DETECTION**

While generating chapter summaries, scan for red flag patterns and FLAG them:

**Red Flag Keywords:**
- "learns about" / "discovers that" / "finds out" / "is told"
- "overhears" / "eavesdrops" / "explained" / "describes"
- "tavern" / "bar" / "inn" (often exposition dump locations)
- "conversation reveals" / "discussion about"

**Red Flag Patterns:**
- "Character goes to [place] and learns [info]" (passive gathering)
- "NPC tells character about [lore]" (convenient exposition)
- "Character overhears [crucial info]" (lazy reveal)
- "At tavern, meets [exposition NPC]"
- "Mentor explains [system/prophecy/history]"

**When detected, add WARNING to that chapter:**

```markdown
Chapter {N}: "{Title}"
  ⚠️ POTENTIAL EXPOSITION DUMP
  Pattern: {specific pattern found}
  Problem: Information delivered passively, no conflict

  ALTERNATIVE: Reveal through conflict
  - Character NEGOTIATES for info (social cost)
  - Character STEALS/DISCOVERS info (physical risk)
  - Character DEDUCES info (intellectual challenge)
  - Info revealed DURING action (chase/fight)
  - Character WRONG, must correct (error cost)
```

**Example Comparison:**

❌ **BAD (Passive):**
```
Chapter 3: "The Tavern"
  - Sarah visits local tavern
  - Meets old sage
  - He tells her artifact history
  - She learns the prophecy
  - Returns to camp
```
*Problem: No conflict, passive listening*

✅ **GOOD (Active):**
```
Chapter 3: "The Theft"
  GOAL: Access restricted archives
  CONFLICT: Locked, guarded, unauthorized
  OUTCOME: Partial info + now hunted by guards

  - Breaks into university at night
  - Nearly caught, hides
  - Photographs partial documents
  - Alarm triggered, window escape
  - Guard sees her face
```
*Better: Active, risk, consequences*

**If any chapter lacks Goal/Conflict/Outcome: FLAG for Step 7 approval.**

Keep high-level with bullets, not detailed scenes. Leave room for discovery during writing.

Write to `stories/{slug}/yolo-outline.md`.

**Store all flagged chapters for Step 7 checkpoint.**

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

### Step 7: MANDATORY OUTLINE APPROVAL CHECKPOINT

**⚠️ CRITICAL: This prevents cookie-cutter storytelling. DO NOT SKIP. ⚠️**

Before proceeding to writing, present comprehensive outline for explicit approval.

Generate and show this detailed breakdown:

```
═══════════════════════════════════════
OUTLINE APPROVAL CHECKPOINT
═══════════════════════════════════════

⚠️ REVIEW THIS CAREFULLY ⚠️

Once approved, parallel agents will write ALL chapters
based on this outline. Fixing structural problems after
writing is 10x harder than fixing them now.

═══════════════════════════════════════
OPENING STRATEGY
═══════════════════════════════════════

{Show the opening scene/chapter strategy}

Opening type: {In medias res / Inciting incident / Character intro}
Hook: {What grabs reader immediately}
First scene summary: {Brief description}
Conflict in opening: {What tension exists immediately}

═══════════════════════════════════════
ACT STRUCTURE
═══════════════════════════════════════

Act 1: Setup (~{word_count} words, Chapters {range})
  → {Brief summary of Act 1 arc}

Act 2: Confrontation (~{word_count} words, Chapters {range})
  → {Brief summary of Act 2 arc}

Act 3: Resolution (~{word_count} words, Chapters {range})
  → {Brief summary of Act 3 arc}

Total: {total_chapters} chapters, ~{total_words} words

═══════════════════════════════════════
CHAPTER-BY-CHAPTER BREAKDOWN
═══════════════════════════════════════

{For each chapter, show full details including warnings:}

Chapter {N}: "{Title}" ({POV}, ~{words} words)
  GOAL: {What character wants}
  CONFLICT: {What opposes them}
  OUTCOME: {What changes}

  Plot beats:
  - {Beat 1}
  - {Beat 2}

  {If exposition dump flagged:}
  ⚠️ EXPOSITION DUMP WARNING
  Pattern: {Pattern detected}
  Fix: {Suggested alternative}

═══════════════════════════════════════
KEY PLOT BEATS
═══════════════════════════════════════

Inciting Incident: Ch {N} - {Description}
Midpoint Twist: Ch {N} - {Description}
Darkest Moment: Ch {N} - {Description}
Climax: Ch {N} - {Description}

═══════════════════════════════════════
CHARACTER ARCS
═══════════════════════════════════════

{For each main character:}
{Name}:
  Start: {Initial state}
  Change: {Growth/transformation}
  End: {Final state}

═══════════════════════════════════════
QUALITY CHECK QUESTIONS
═══════════════════════════════════════

Before approving, answer these:

1. OPENING HOOK
   Does the opening hook immediately?
   Is there tension/conflict in first scene?

2. EXPOSITION DUMP CHECK
   Any tavern/bar/inn exposition scenes?
   Any "character learns about" passive scenes?
   Any convenient NPC explanations?
   {List flagged chapters if any}

3. CHAPTER-LEVEL CONFLICT
   Does EVERY chapter have Goal/Conflict/Outcome?
   Can you identify what character WANTS each chapter?
   Can you identify what OPPOSES them each chapter?

4. CHARACTER AGENCY
   Is protagonist ACTIVE (drives story) or PASSIVE (reacts)?
   Do they make meaningful choices?
   Do they pursue goals or wait for things to happen?

5. STORY START POINT
   Does story start at right moment?
   Too late (too much setup)? Too early (mundane life)?
   Is inciting incident in Ch 1 or early Ch 2?

6. PLOT PROGRESSION
   Does each chapter advance meaningfully?
   Can you identify NEW info/obstacle/change in each?
   Any wheel-spinning chapters?

7. STAKES ESCALATION
   Do stakes rise throughout Act 2?
   Clear progression of tension?

═══════════════════════════════════════
APPROVAL DECISION
═══════════════════════════════════════

Type "YES" to approve and proceed to writing.
Type "NO" to revise outline.
Type chapter numbers to get detailed revision help.

⚠️ LAST CHANCE to fix structural problems before
   parallel agents write all chapters. Revising
   structure AFTER writing is 10x more work.

APPROVE OUTLINE? [YES/NO/chapter numbers]:
```

**WAIT for explicit user response. DO NOT PROCEED without it.**

**If user types "YES":**
- Proceed to Step 8 (Completion Message)
- Note approval in PROJECT.md

**If user types "NO":**
- Ask what needs revision
- Make requested changes to outline
- Re-run this checkpoint (show full breakdown again)
- Require new approval

**If user types chapter numbers (e.g., "3, 5, 7"):**
- For each flagged chapter, provide:
  - Current structure analysis
  - Specific problems (passive info-gathering, exposition, etc.)
  - Suggested revisions with Goal/Conflict/Outcome
  - Alternative approaches
- Allow user to request changes
- Update outline accordingly
- Re-run checkpoint
- Require new approval

**DO NOT proceed to Step 8 until user explicitly types "YES".**

### Step 8: Completion Message

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
✓ OUTLINE APPROVED (quality checkpoint passed)

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
