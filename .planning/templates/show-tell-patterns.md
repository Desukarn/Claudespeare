# Show vs. Tell Detection System

This system analyzes prose for show-don't-tell balance, detecting filter words and telling language that distances readers from immediate experience.

## Overview

"Show, don't tell" is a core fiction writing principle:
- **Showing:** Presents action, dialogue, sensory details for readers to interpret
- **Telling:** Summarizes emotions, states information, filters through narrator

Some telling is necessary (transitions, setup, pacing), but too much creates flat, distant prose. AI-generated text tends toward telling because it's easier to state facts than dramatize scenes.

This system:
1. Detects filter words that signal telling
2. Calculates show/tell ratio per chapter
3. Flags excessive telling patterns
4. Suggests showing alternatives

---

## Filter Word Categories

Filter words are verbs/phrases that place narrator between reader and experience. They "filter" the action through explanation rather than presenting it directly.

### Category 1: Visual Filters

**Words that filter sight/observation:**
- saw / seen / sees
- looked / looking
- watched / watching
- noticed / noticing
- observed / observing
- appeared / appears / seemed to appear
- looked like
- seemed (visual contexts)

**Why problematic:**
Filters visual information through narrator commentary instead of showing what the character sees.

**Examples:**
- **Telling:** "She saw that he was angry."
- **Showing:** "His fists clenched. His jaw tightened."
- **Telling:** "The room looked expensive."
- **Showing:** "Marble floors. Crystal chandelier. Gold-framed paintings."

**Detection:**
- Scan for visual filter verbs
- Check if followed by "that" clause (signals telling)
- Flag patterns like "she saw that", "he noticed that", "it looked like"

---

### Category 2: Emotional/Mental Filters

**Words that filter emotions/thoughts:**
- felt / feeling / feels
- thought / thinking / thinks
- knew / knowing / knows
- wondered / wondering
- realized / realizing
- understood / understanding
- believed / believing
- remembered / remembering
- sensed / sensing

**Why problematic:**
Tells reader what character feels/thinks instead of showing through action, dialogue, physical sensation.

**Examples:**
- **Telling:** "She felt angry."
- **Showing:** "Her hands trembled. She wanted to scream."
- **Telling:** "He thought she was lying."
- **Showing:** "Her story didn't add up. The timeline was wrong."
- **Telling:** "She realized he'd betrayed her."
- **Showing:** "The email was addressed to her rival. Her stomach dropped."

**Detection:**
- Scan for emotional/mental filter verbs
- Especially flag "felt [emotion]" and "thought that" constructions
- Count per chapter

---

### Category 3: Seeming/Appearing (Hedging Filters)

**Words that hedge through appearance:**
- seemed / seems / seeming
- appeared / appears / appearing
- gave the impression
- looked as if / as though
- sounded like
- felt like (in hedging sense)

**Why problematic:**
Double-filters: tells reader something appears a certain way instead of showing the evidence.

**Examples:**
- **Telling:** "He seemed nervous."
- **Showing:** "He tapped his fingers. Shifted his weight. Avoided eye contact."
- **Telling:** "The house appeared abandoned."
- **Showing:** "Windows dark. Door hanging open. Weeds choking the porch."

**Detection:**
- Scan for seeming/appearing verbs
- Flag especially when followed by adjective: "seemed angry", "appeared tired"
- These are nearly always unnecessary

---

### Category 4: Experience Filters

**Words that filter sensory experience:**
- heard / hearing / hears
- smelled / smelling / smells
- tasted / tasting / tastes
- touched / touching
- experienced / experiencing

**Why problematic:**
Adds unnecessary layer between sensation and reader. Exception: "heard" is sometimes acceptable for off-screen sounds.

**Examples:**
- **Telling:** "She heard a crash."
- **Showing:** "Glass shattered in the next room." (acceptable: "She heard glass shatter in the next room" for POV clarity)
- **Telling:** "He smelled coffee."
- **Showing:** "Coffee. Fresh-brewed."
- **Telling:** "She tasted chocolate."
- **Showing:** "Rich, dark chocolate melted on her tongue."

**Detection:**
- Scan for sensory filter verbs
- "Heard" is most forgivable (contextual)
- Others are usually better removed

---

## Show/Tell Ratio Analysis

### Calculation Method

**Step 1: Count total verbs in chapter**
- Parse prose for main verbs
- Exclude dialogue tags ("said", "asked") from count
- Get baseline verb count

**Step 2: Count filter words**
- Sum all filter word instances (all categories)
- Include all forms (saw/seen/sees, felt/feeling/feels)

**Step 3: Calculate ratio**
```
Filter Percentage = (Filter Words / Total Verbs) × 100
```

**Step 4: Determine show/tell balance**
- Low filter % = More showing (immediate prose)
- High filter % = More telling (distant prose)

### Thresholds

**Filter word percentage guidelines:**

- **0-5%:** Excellent showing (immediate, vivid prose)
- **6-10%:** Good balance (mostly showing with necessary telling)
- **11-15%:** Warning zone (noticeable telling, still acceptable)
- **16-25%:** Excessive telling (critical - prose feels distant)
- **26%+:** Severe telling (robotic summary instead of scenes)

**Genre adjustments:**
- Literary fiction: Aim for <8%
- Thriller/Action: Aim for <6% (immediate urgency)
- Romance: <10% acceptable (internal emotions okay)
- YA: <12% acceptable (clearer emotional signposting)

### Analysis Per Chapter

Generate per-chapter report:

```
Chapter 1: "The Discovery"
  Total verbs: 847
  Filter words: 89
  Filter percentage: 10.5%
  Rating: Good balance

  Breakdown by category:
    Visual filters (saw, looked, noticed): 34 (38%)
    Emotional filters (felt, thought, knew): 41 (46%)
    Seeming/appearing (seemed, appeared): 9 (10%)
    Sensory filters (heard, smelled): 5 (6%)

  Most common: "thought" (18), "felt" (12), "saw" (11)
```

---

## Specific Pattern Detection

### Pattern 1: "Felt [Emotion]" Construction

**Detection:** "felt [emotion_adjective]"
- felt angry, felt sad, felt nervous, felt excited, etc.

**Why flagged:** Classic telling that removes reader from experience

**Examples with alternatives:**

| Telling | Showing |
|---------|---------|
| She felt angry | Her jaw clenched. She wanted to hit something. |
| He felt nervous | His hands trembled. Heart racing. |
| She felt sad | Tears burned behind her eyes. |
| He felt confused | Nothing made sense. What was happening? |
| She felt excited | She couldn't stop smiling. Finally! |

**Report format:**
```
"Felt [emotion]" instances: {count}
Examples:
  - Chapter 2: "She felt angry at his dismissal" → Show: fists clenched, voice sharp
  - Chapter 5: "He felt confused by her answer" → Show: "What? That doesn't..."
```

---

### Pattern 2: "Thought That" Construction

**Detection:** "thought that [statement]"

**Why flagged:** Tells us character's conclusion instead of showing their reasoning

**Examples with alternatives:**

| Telling | Showing |
|---------|---------|
| She thought that he was lying | His story had changed. Yesterday it was Tuesday. Now Wednesday? |
| He thought that the plan would fail | Too many variables. Too many ways it could go wrong. |
| She thought she recognized the voice | That voice. Where had she heard it before? |

**Alternatives:**
- Direct internal monologue (italics or not): *He's lying.*
- Show evidence that leads to thought: "The timeline didn't match."
- Deep POV: Treat thoughts as immediate reactions, not reported

**Report format:**
```
"Thought that" instances: {count}
Examples:
  - Chapter 3: "Marcus thought that she was hiding something"
    → Alternative: "She was hiding something. He could see it in her eyes."
```

---

### Pattern 3: "Saw That" Construction

**Detection:** "saw that [observation]"

**Why flagged:** Adds unnecessary narrator layer

**Examples with alternatives:**

| Telling | Showing |
|---------|---------|
| She saw that the door was open | The door stood open. |
| He saw that she was crying | Tears streaked her face. |
| She saw that the room was empty | Empty. No one. |

**Report format:**
```
"Saw that" instances: {count}
Examples:
  - Chapter 1: "Sarah saw that the window was broken"
    → Alternative: "The window was shattered, glass on the floor."
```

---

### Pattern 4: "Seemed/Appeared [Adjective]" Construction

**Detection:** "seemed [adjective]" or "appeared [adjective]"

**Why flagged:** Double-filter that hedges instead of showing evidence

**Examples with alternatives:**

| Telling | Showing |
|---------|---------|
| He seemed angry | His voice was sharp. Eyes hard. |
| She appeared tired | Dark circles under her eyes. Slumped shoulders. |
| The building seemed abandoned | Dark windows. Overgrown lawn. No cars. |

**Report format:**
```
"Seemed/appeared [adjective]" instances: {count}
Examples:
  - Chapter 4: "Marcus seemed distracted during the meeting"
    → Alternative: "Marcus stared out the window. He hadn't heard the question."
```

---

## Emotion Telling vs. Showing Examples

Common emotion tells with showing alternatives:

### Fear

| Telling | Showing |
|---------|---------|
| She felt afraid | Her heart hammered. Cold sweat. She couldn't breathe. |
| He was scared | Every shadow looked like a threat |
| She felt terrified | Run. She had to run. Now. |

### Anger

| Telling | Showing |
|---------|---------|
| She felt angry | Her fists clenched. She wanted to scream. |
| He was furious | "Get out." His voice was deadly quiet. |
| She felt rage | Everything went red. The vase—perfect target. |

### Sadness

| Telling | Showing |
|---------|---------|
| She felt sad | Tears burned. She looked away. |
| He was depressed | The ceiling. He'd been staring at it for hours. |
| She felt grief | The empty chair. Still empty. Always empty. |

### Love

| Telling | Showing |
|---------|---------|
| She felt love for him | When he smiled, everything else disappeared. |
| He loved her | He'd memorized the way she laughed. |
| She felt affection | She caught herself watching him. Again. |

### Confusion

| Telling | Showing |
|---------|---------|
| She felt confused | Wait. What? That didn't make sense. |
| He was bewildered | "I don't... what are you saying?" |
| She felt lost | None of this was right. Nothing fit. |

---

## Detection Workflow

### Step 1: Load Chapter Text

Read chapter prose, excluding:
- Frontmatter (YAML)
- Chapter notes section
- Comments

### Step 2: Parse for Verbs and Filters

**Extract all verbs:**
- Use basic verb detection (words that could be verbs)
- Exclude dialogue tags unless they're filter verbs

**Count filter words:**
- Scan for all filter word forms
- Categorize by type
- Track specific constructions (felt [emotion], thought that, saw that)

### Step 3: Calculate Ratios

```
Total verbs: {count}
Filter words: {count}
Filter percentage: {percentage}%

Category breakdown:
  Visual: {count} ({percentage}% of filters)
  Emotional/mental: {count} ({percentage}% of filters)
  Seeming/appearing: {count} ({percentage}% of filters)
  Sensory: {count} ({percentage}% of filters)
```

### Step 4: Flag Specific Patterns

Count instances of:
- "felt [emotion]"
- "thought that"
- "saw that"
- "seemed/appeared [adjective]"
- "realized that"
- "knew that"

### Step 5: Generate Suggestions

For each flagged instance, provide showing alternative:

```
Location: Chapter 3, estimated line 47
Telling: "She felt angry at his dismissal"
Category: Emotional filter (felt [emotion])
Suggestion alternatives:
  1. Her jaw clenched. Dismissed? After everything she'd done?
  2. "Dismissed?" Her voice was ice.
  3. She wanted to throw something. Preferably at his head.
```

---

## Report Format

### Chapter-Level Report

```markdown
## Chapter 3: Show/Tell Analysis

**Overall filter percentage:** 18% (Critical - excessive telling)
**Total verbs:** 634
**Filter words:** 114

### Breakdown by Category
- Visual filters: 41 instances (36%)
  - saw: 15, looked: 12, noticed: 8, watched: 6
- Emotional/mental filters: 52 instances (46%)
  - thought: 18, felt: 14, knew: 11, realized: 9
- Seeming/appearing: 15 instances (13%)
  - seemed: 10, appeared: 5
- Sensory filters: 6 instances (5%)
  - heard: 4, smelled: 2

### Specific Pattern Flags

**"Felt [emotion]" - 9 instances:**
1. Line ~23: "She felt angry" → Her fists clenched
2. Line ~67: "He felt nervous" → His hands trembled
3. Line ~89: "She felt relieved" → She exhaled. Finally.
[Continue...]

**"Thought that" - 12 instances:**
1. Line ~34: "Marcus thought that she was lying"
   → Alternative: She was lying. He could tell.
2. Line ~56: "She thought that the plan would work"
   → Alternative: The plan would work. It had to.
[Continue...]

### Priority Fixes

1. Replace "felt [emotion]" constructions (9 instances - easy wins)
2. Convert "thought that" to direct internal monologue (12 instances)
3. Remove "seemed/appeared" hedging (15 instances)

**Estimated impact:** Reducing these 36 instances would drop filter % from 18% to 12% (acceptable range)
```

### Story-Level Summary

```markdown
# Show/Tell Analysis - Full Story

**Chapters analyzed:** 8
**Average filter percentage:** 12.3% (Warning - noticeable telling)

## Chapter Comparison

| Chapter | Filter % | Rating | Priority |
|---------|----------|--------|----------|
| 1 | 8% | Good | Low |
| 2 | 15% | Warning | Medium |
| 3 | 18% | Critical | High |
| 4 | 11% | Warning | Medium |
| 5 | 9% | Good | Low |
| 6 | 14% | Warning | Medium |
| 7 | 19% | Critical | High |
| 8 | 7% | Excellent | None |

**Chapters needing revision:** 2, 3, 6, 7 (filter % >15%)
**Chapters with good balance:** 1, 5, 8 (filter % <10%)

## Common Patterns Across Story

**Most overused filters:**
1. "thought" - 89 instances across all chapters
2. "felt" - 67 instances
3. "saw" - 54 instances
4. "seemed" - 41 instances

**Most common constructions:**
1. "felt [emotion]" - 34 instances (easy fix)
2. "thought that" - 28 instances (convert to direct thought)
3. "seemed [adjective]" - 23 instances (show evidence instead)

## Recommendations

### Quick Wins (Low Effort, High Impact)
- Replace all "felt [emotion]" with physical showing (34 instances)
- Remove "seemed/appeared [adjective]" hedging (23 instances)
- **Estimated impact:** Would reduce average from 12.3% to 9.8%

### Medium Effort
- Convert "thought that" to internal monologue (28 instances)
- Revise "saw that" to direct description (19 instances)

### Deep Revision
- Chapters 3 and 7 need comprehensive showing revision
- Consider rewriting key emotional scenes to dramatize rather than summarize
```

---

## Integration with Revision Workflow

This detection system integrates with `/write:revise` command:

1. **Automatic detection:** Scans all chapters for filter words
2. **Generates report:** Per-chapter and story-level analysis
3. **Provides alternatives:** Specific showing suggestions for each instance
4. **Prioritizes fixes:** Flags worst offenders (chapters >15% filter rate)

**Workflow:**
```
/write:revise
→ Runs show/tell detection
→ Generates SHOW-TELL-REPORT.md
→ Flags chapters with >15% filter rate
→ Provides line-by-line alternatives for revision
```

---

## When Telling Is Acceptable

**Necessary telling:**
- Transitions: "Three days passed" (don't show all three days)
- Backstory summary: "She'd grown up poor" (exposition)
- Pacing: "The meeting was boring" (skip the boring parts)
- Setup: "The city had two million people" (context)

**Strategic telling:**
- To vary pacing (after intense showing scene, brief tell for breath)
- For information that's needed but not dramatic
- When showing would take too long for minor point

**Rule of thumb:**
- Tell for logistics, show for emotion
- Tell for setup, show for scenes
- Tell to skip time, show for key moments

---

## Notes

**Deep POV consideration:**
In deep third-person POV, some "filter" verbs are acceptable if they're the character's immediate perception. Context matters:

- **Acceptable:** "She saw the door open. Marcus stepped through."
  (Sequential action, natural perception)
- **Problematic:** "She saw that he was angry."
  (Filtering the observation through "saw that" instead of showing anger)

**First person POV:**
"I felt" and "I thought" are sometimes more natural in first person, but still prefer showing:
- **Weak:** "I felt scared."
- **Better:** "My hands shook. I couldn't catch my breath."

---

**Last Updated:** 2026-03-14

## Maintenance

This template provides detection logic for show vs. tell analysis. The revision workflow uses this file to:
1. Scan chapters for filter words
2. Calculate show/tell ratios
3. Flag excessive telling
4. Suggest showing alternatives

Writers can adjust thresholds in project-specific copies based on genre and style preferences.
