# Comprehensive Revision Workflow

Automatically detect and fix AI language patterns, consistency issues, and style drift across all completed chapters.

## Overview

This workflow scans your entire story for quality issues and applies fixes automatically:
- AI language pattern detection (24+ patterns)
- Character voice consistency
- World rule violations
- POV consistency
- Style drift analysis
- Automatic fixes with alternatives

**Time:** 15-30 minutes for full novel scan and fixes
**Output:** Updated chapter files with issues fixed, detailed report
**When to use:** After completing an arc or before final export

## The Workflow

### Step 1: Validate Project

Verify story project exists by reading `PROJECT.md` from `stories/{slug}/`.

Check that chapters exist in chapters/ directory. If no chapters written yet, prompt user to write chapters first.

### Step 2: Load Story Context

Read all story files for comparison:

**Required:**
- `PROJECT.md` - story metadata
- `STYLE.md` - style profile (if exists)
- `CHARACTERS.md` or `yolo-characters.md` - character profiles
- `WORLD.md` - world rules (if exists)
- All `chapters/*.md` - prose to analyze

### Step 3: Run AI Pattern Detection

For each chapter, scan for 24+ common AI language patterns:

**NOTE**: After AI pattern detection (Step 3) and before character consistency (Step 4), insert Sanderson Framework Audit (Step 3.5).

---

### Step 3.5: Sanderson Framework Audit

**NEW PHASE 2 INTEGRATION**: Verify structural integrity using Sanderson frameworks.

See `.claude/skills/sanderson-2025/promise-progress-payoff.md` and `plot-hole-prevention.md` for full details.

This audit catches structural issues that AI pattern detection misses:
- Broken promises (setup without payoff)
- Stagnant progress (wheel-spinning chapters)
- Character knowledge plot holes
- Weak character triangle

#### Promise-Progress-Payoff Check

**Promise Audit (First 3 Chapters):**

Read chapters 1-3 and check:
- [  ] **Tone Promise**: Does opening tone match overall story mood?
- [  ] **Major Dramatic Question**: Is central question established by end of Act 1?
- [  ] **Character/Conflict Promise**: Can readers articulate WHO protagonist is, WHAT they want, WHY they can't get it?
- [  ] **Genre Promise**: Does opening fit or intentionally subvert genre expectations?

**If any promises are unclear or broken:**
- Flag specific location where promise should be clearer
- Suggest revision to strengthen promise
- Check if payoff delivers on promise (see Payoff check below)

**Progress Audit (Middle Chapters):**

For each Act 2 chapter, verify progress signposting:

**Critical Sanderson insight**: "A big reason people drop books is not enough signposts of progress."

Check each chapter for:
- [  ] **Has at least one signpost** (information revealed, obstacle introduced, character decision, relationship shift, small victory)
- [  ] **Uses Yes-But or No-And pattern** (victories have complications OR failures worsen)
- [  ] **Advances at least one thread** (plot, character growth, or relationship)
- [  ] **No wheel-spinning** (could you cut this chapter without loss?)

**Flag "stagnant chapters"** - those with:
- No new information
- No character decisions
- No plot advancement
- No meaningful relationship change
- Just "stuff happens" without progress

**Track progress type:**
```
Chapter X Progress:
- Information-Based: [Clue discovered / suspect eliminated / mystery unraveled]
- Relationship: [Connection moment / setback / understanding deepened]
- Internal: [Belief questioned / skill developed / growth moment]
- Plot/Action: [Quest advanced / obstacle overcome / geography traversed]
```

**Try-Fail Cycle Verification:**

Check that protagonist's major attempts follow try-fail pattern:
- [  ] **First Attempt**: Obvious solution fails (reveals problem harder than expected)
- [  ] **Second Attempt**: Sophisticated approach fails (reveals deeper complications or internal flaws)
- [  ] **Third Attempt**: Success after growth (feels earned, not lucky)

**If pattern missing or weak:**
- Identify which attempt is missing
- Suggest adding failure that reveals new information
- Ensure each failure raises stakes

**Payoff Audit (Final Chapters):**

Read climax and resolution, check:
- [  ] **Answers Major Dramatic Question**: Does climax provide satisfying answer to MDQ?
- [  ] **Surprising yet Inevitable**: Is resolution both unexpected AND logical in hindsight?
- [  ] **Uses Only Established Elements**: No deus ex machina (unearned solutions)
- [  ] **Emotional Satisfaction Matches Promise**: Tone of resolution matches tone promise
- [  ] **All Significant Promises Addressed**: Every major setup has payoff

**Payoff Type Verification:**
```
Approach used: [Straightforward / Twist / Gandalf (Dark-then-Light)]

If Twist: Was expectation gradually redirected? ___
If Gandalf: Was promise specific, then overshadowed by darkness? ___

Checklist of setups → payoffs:
- Setup (Ch X): _______ → Payoff (Ch Y): _______
- Setup (Ch X): _______ → Payoff (Ch Y): _______
```

**If payoffs missing:**
- List unfulfilled promises
- Suggest where to add payoff
- Check if setup should be removed (if no payoff intended)

#### Character Triangle Verification

**For protagonist, verify Sanderson's Character Triangle:**

See `.claude/skills/sanderson-2025/proactive-relatable-capable.md` for full framework.

**Proactive Check (Agency):**
Count scenes where protagonist:
- Makes active choices (drives plot)
- Reacts passively (things happen to them)

**Ratio**: Should be 60%+ proactive for engaging protagonist.

**If too passive:**
- Flag specific chapters where protagonist is reactive
- Suggest adding proactive choices
- Check if agency increases through character arc (can start passive if growing)

**Relatable Check (Empathy):**
List relatable elements present:
- Flaws readers recognize
- Struggles readers understand
- Emotions readers share
- Humor, vulnerability, or humanity

**Minimum**: 2-3 strong relatable elements throughout story.

**If lacking:**
- Identify where to add vulnerability
- Suggest showing more internal struggle
- Add moments of humor or humanity

**Capable Check (Competence):**
List protagonist's competencies demonstrated:
- Skills they use to solve problems
- Knowledge they apply uniquely
- Talents that make them interesting

**Sanderson's Rule**: "You can drop one pillar, but NEVER two."

**If protagonist weak on 2+ pillars:**
- **CRITICAL ISSUE** - protagonist likely boring or frustrating
- Prioritize which pillar to strengthen
- Suggest specific scenes to demonstrate missing pillar

**Assessment Result:**
```
Proactive: __% of scenes (goal: 60%+)
Relatable: __ elements present (goal: 2-3+)
Capable: __ competencies demonstrated (goal: clear expertise)

Triangle Strength: [Strong on all three / Strong on two / WEAK - needs fixing]
```

#### Plot-Hole Prevention Check

**Character Knowledge Tracking:**

See `.claude/skills/sanderson-2025/plot-hole-prevention.md` for full system.

**CRITICAL**: Verify no character acts on information they shouldn't know.

**For each major plot revelation:**
1. Identify what information is revealed
2. List which characters learn it
3. Verify HOW they learned it (witnessed, told, deduced)
4. Check WHEN they learned it (chapter/scene)

**The "How Did They Know?" Test:**

For each character action, verify:
- [  ] Character has information this action requires
- [  ] There's a scene showing them learning it (or reasonable inference)
- [  ] POV character only knows what they should at this point
- [  ] Deductions are reasonable given evidence available

**Common plot holes to catch:**
- Character mentions detail from scene they weren't in
- Character knows villain's plan without investigation
- Character aware of secret no one told them
- POV character reveals info only other POV knows

**If plot hole found:**
- Flag specific location
- Identify missing information transfer
- Suggest fix: Add scene where they learn it OR remove knowledge from action OR show deduction process

**Timeline Consistency:**

Track major events across chapters:
```
Day 1 (Ch 1): Event A at Location X
Day 2 (Ch 2): Event B at Location Y
Day 3 (Ch 3): Event C at Location Z
```

**Check:**
- [  ] Character ages consistent
- [  ] Travel times mathematically work
- [  ] No character in two places at once
- [  ] Seasonal progression logical

**If timeline breaks:**
- Flag contradiction
- Calculate correct timing
- Suggest adjustment (add travel time, change dates, reorder scenes)

**World Rules Consistency:**

If WORLD.md exists, verify:
- [  ] Magic/tech usage follows established rules
- [  ] Costs paid every time (no free magic)
- [  ] Limitations respected (no suddenly unlimited power)
- [  ] Geography never contradicts (distances, descriptions)

**If rule violation found:**
- Flag specific scene
- Reference established rule from WORLD.md
- Suggest correction (add cost, explain exception, remove violation)

#### Sanderson Audit Report Section

Add to comprehensive report:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SANDERSON FRAMEWORK AUDIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Promise-Progress-Payoff:
  Promise Check: [✓ Strong / ⚠ Needs clarity / ✗ Broken]
  Progress Check: [✓ Strong signposting / ⚠ Some stagnant chapters / ✗ Wheel-spinning]
  Payoff Check: [✓ Satisfying / ⚠ Incomplete / ✗ Deus ex machina]

Character Triangle (Protagonist):
  Proactive: __% (goal: 60%+) [✓ / ⚠ / ✗]
  Relatable: __ elements [✓ / ⚠ / ✗]
  Capable: __ competencies [✓ / ⚠ / ✗]
  Assessment: [Strong / Needs work / CRITICAL ISSUE]

Plot-Hole Prevention:
  Character Knowledge: [✓ Consistent / ⚠ Minor issues / ✗ Plot holes found]
  Timeline: [✓ Consistent / ⚠ Minor issues / ✗ Contradictions]
  World Rules: [✓ Consistent / ⚠ Minor violations / ✗ Major violations]

DETAILED FINDINGS:

{List specific issues found in each category}

RECOMMENDED FIXES:

{Prioritized list of structural fixes needed}
```

---

### Step 4: Check Character Consistency

For each character mentioned in chapters:

**Common patterns:**
- "delve" / "delved into"
- "tapestry" / "rich tapestry"
- "testament to"
- "juxtaposition"
- "navigate" (non-literal)
- "it's worth noting"
- "underscores" / "underscore the importance"
- "landscape" (metaphorical)
- "realm" (non-literal)
- "serves to"
- "a testament"
- "punctuated by"
- "as it were"
- "in the grand scheme"
- "facilitate"
- "optimal"
- "utilize" (instead of "use")
- "aforementioned"
- "heretofore"
- "whilst"
- Purple prose excess (overly ornate descriptions)
- Formal academic phrasing in narrative
- Hedge phrases ("it seems that", "appears to be")
- Meta-commentary ("it's important to note")

For each pattern found:
- Record location (chapter, paragraph, sentence)
- Show context (surrounding text)
- Generate 3-5 replacement alternatives
- Select most natural alternative based on style profile

### Step 4: Check Character Consistency

For each character mentioned in chapters:

1. **Voice consistency:**
   - Compare dialogue to character speech patterns from CHARACTERS.md
   - Flag dialogue that doesn't match character's voice
   - Suggest revisions that fit character profile

2. **Personality consistency:**
   - Check actions match personality traits
   - Flag out-of-character behavior
   - Suggest alternatives

3. **Physical consistency:**
   - Track character descriptions across chapters
   - Flag contradictions (eye color changed, height different, etc.)
   - List all descriptions for review

### Step 5: Verify World Consistency

If WORLD.md exists:

1. **World rule violations:**
   - Check magic/tech usage against established rules
   - Flag violations of stated limits or costs
   - Suggest corrections

2. **Geography consistency:**
   - Track location descriptions
   - Flag contradictions in place descriptions
   - Verify travel times/distances make sense

3. **Timeline consistency:**
   - Track time references across chapters
   - Flag timeline contradictions
   - Build timeline for review

### Step 6: Analyze Style Drift and Sentence Structure Variety

If STYLE.md exists:

1. **Sentence length analysis:**
   - Calculate average sentence length per chapter
   - Compare to style profile target (±10% acceptable)
   - Flag chapters with significant drift

2. **Vocabulary level:**
   - Check for vocabulary inconsistency
   - Flag overly complex words if profile shows simple vocabulary
   - Flag overly simple words if profile shows rich vocabulary

3. **Tone consistency:**
   - Analyze tone markers (formal/casual, lyrical/direct)
   - Flag chapters that drift from established tone

4. **Sentence structure variety analysis:**

Check for monotonous sentence construction patterns that signal robotic or AI-generated prose.

**A. Consecutive same-structure sentences:**

Detect when 3+ consecutive sentences follow identical grammatical structure.

**Common problematic patterns:**

Pattern 1: Subject-Verb-Object repetition
```
She walked to the door. She opened it slowly. She peered into the darkness.
→ Flag: 3 consecutive "She [verb]" patterns
```

Pattern 2: Same opening word/phrase
```
The room was cold. The walls were bare. The floor creaked underfoot.
→ Flag: 3 consecutive "The [noun] [verb]" openings
```

Pattern 3: Identical clause structure
```
Running through the forest, she heard a sound. Jumping over a log, she spotted movement. Ducking under branches, she found the clearing.
→ Flag: 3 consecutive "[Gerund phrase], she [verb]" structures
```

**Detection method:**
- Parse sentences in sequence
- Extract sentence opening pattern (first 2-3 words + grammatical structure)
- Count consecutive sentences with same pattern
- Flag if 3+ consecutive matches

**Thresholds:**
- 0-2 consecutive: Normal (acceptable)
- 3 consecutive: Warning (monotonous)
- 4+ consecutive: Critical (robotic pattern)

**Report format:**
```
Issue: Consecutive identical sentence structures
Location: Chapter 3, paragraphs 4-5
Pattern: Subject-verb repetition (4 consecutive)
Examples:
  "She walked to the window."
  "She looked outside."
  "She saw the garden."
  "She noticed the gate was open."
Severity: Critical
Suggestion: Vary sentence openings:
  "She walked to the window and looked outside. The garden. The gate stood open."
  (Combines sentences, varies structure: compound sentence → fragment → inverted structure)
```

**B. All sentences starting with subject:**

Detect when paragraph or scene has no sentence variety—every sentence begins with the subject (character name or pronoun).

**Example problematic paragraph:**
```
Sarah entered the room. She noticed the mess immediately. She bent down to pick up papers. She wondered who had been here. She heard a noise behind her. She spun around quickly.
```
→ Every sentence: [Subject] [verb]

**Detection method:**
- Analyze paragraph (5+ sentences)
- Check sentence openings
- Count how many start with subject (noun/pronoun as first word)
- Calculate percentage

**Thresholds:**
- 0-60% subject-opening: Good variety
- 61-80% subject-opening: Warning (monotonous)
- 81-100% subject-opening: Critical (robotic)

**Report format:**
```
Issue: All sentences start with subject
Location: Chapter 5, paragraph 8 (6 sentences)
Pattern: 100% of sentences begin with "She" or character name
Analysis:
  "Sarah walked..." → Subject opening
  "She noticed..." → Subject opening
  "She bent..." → Subject opening
  "She wondered..." → Subject opening
  "She heard..." → Subject opening
  "She spun..." → Subject opening
Severity: Critical
Suggestion: Vary sentence openings:
  - Prepositional phrases: "In the corner, papers lay scattered."
  - Subordinate clauses: "When she heard the noise, she spun around."
  - Adverbs: "Quickly, she bent down."
  - Gerund phrases: "Wondering who'd been here, she picked up papers."
  - Inverted structure: "Behind her came a noise."
  - Absolute phrases: "Papers scattered, the room was a mess."

Revised example:
  "Sarah entered the room. Papers scattered everywhere—someone had been here. Behind her, a noise. She spun around."
  (Subject opening → Inverted → Fragment → Subject opening = VARIETY)
```

**C. No sentence structure variety in scene:**

Analyze entire scene (multiple paragraphs) for overall variety.

**Sentence structure types to track:**
1. **Simple sentences:** Single independent clause
   - "The door opened."
2. **Compound sentences:** Two independent clauses joined
   - "The door opened, and Marcus entered."
3. **Complex sentences:** Independent + subordinate clause
   - "When the door opened, Marcus entered."
4. **Compound-complex:** Multiple independent + subordinate
   - "When the door opened, Marcus entered, and Sarah stood up."
5. **Fragments:** Incomplete sentences (intentional)
   - "The door. Open."
6. **Questions:** Interrogative sentences
   - "Who was at the door?"

**Detection method:**
- Categorize each sentence by structure type
- Calculate distribution across scene
- Flag if distribution is heavily skewed

**Thresholds for healthy variety:**
- No single type >70% of sentences
- At least 3 different types present
- Some fragments or questions (adds rhythm)

**Problematic patterns:**
- 90% simple sentences: Choppy, monotonous
- 80% compound sentences: Endless "and" chaining
- 0% variety: All one type (robotic)

**Report format:**
```
Issue: No sentence structure variety
Location: Chapter 2, Scene 1 (30 sentences analyzed)
Distribution:
  - Simple sentences: 27 (90%)
  - Compound sentences: 3 (10%)
  - Complex sentences: 0 (0%)
  - Fragments: 0 (0%)
  - Questions: 0 (0%)
Severity: Critical
Problem: 90% simple sentences creates choppy, elementary prose rhythm
Suggestion: Introduce variety:
  - Combine some simple sentences into compound/complex
  - Add subordinate clauses for sophistication
  - Use intentional fragments for impact
  - Include questions for variation

Example current prose:
  "Sarah walked in. She saw Marcus. He was sitting. He looked up. She spoke."

Revised with variety:
  "Sarah walked in. Marcus was sitting, and when he looked up, she spoke." [Simple → Compound-complex]
  "Sarah walked in. Marcus. Sitting. He looked up." [Simple → Fragments]
  "When Sarah walked in, Marcus looked up." [Complex]
```

**D. Monotonous "and" chaining:**

Detect over-reliance on "and" to connect clauses, creating run-on feel.

**Example problematic pattern:**
```
She opened the door and walked inside and saw the mess and bent down and picked up the papers and heard a noise and turned around.
```
→ 6 "and" conjunctions in one sentence

**Detection method:**
- Count "and" conjunctions per sentence
- Flag sentences with 3+ "and" connections
- Track frequency across chapter

**Thresholds:**
- 0-2 "and" per sentence: Normal
- 3 "and" in one sentence: Warning
- 4+ "and" in one sentence: Critical
- Multiple sentences with 3+ "and": Systemic issue

**Report format:**
```
Issue: Excessive "and" chaining
Location: Chapter 4, paragraph 3
Pattern: 5 "and" conjunctions in single sentence
Example:
  "She opened the door and walked inside and saw the mess and bent down and started cleaning."
Severity: Critical
Suggestion: Break into multiple sentences or vary conjunctions:
  "She opened the door and walked inside. The mess. She bent down, started cleaning."
  "She opened the door. Walking inside, she saw the mess, then bent down to clean."
  [Uses: period breaks, fragments, subordination instead of endless "and"]
```

**E. Aggregate sentence variety score:**

Synthesize all findings into overall assessment:

```
Sentence Structure Variety: [EXCELLENT/GOOD/WARNING/CRITICAL]

Chapter 3 Analysis:
  ✓ Consecutive structure check: Pass (no 3+ consecutive same patterns)
  ✗ Subject-opening check: Warning (75% of sentences start with subject)
  ✗ Structure type distribution: Critical (85% simple sentences)
  ✓ "And" chaining: Pass (no excessive chaining)

Overall: WARNING - Needs more sentence structure variety

Priority fixes:
  1. Vary sentence openings (reduce subject-opening from 75% to <60%)
  2. Introduce complex sentences and fragments (currently 0%)
  3. Combine some simple sentences for rhythm

Estimated impact: Would improve prose sophistication and rhythm significantly
```

**Sentence structure variety checklist per scene:**
- [ ] No 3+ consecutive sentences with identical structure
- [ ] Subject-opening <70% of sentences
- [ ] At least 3 sentence structure types present
- [ ] No single structure type >70%
- [ ] No sentences with 4+ "and" conjunctions
- [ ] Some intentional fragments or questions for variety

If scene fails 3+ checklist items, flag for revision.

### Step 7: Generate Comprehensive Report

Create detailed report showing all findings:

```
═══════════════════════════════════════
REVISION ANALYSIS REPORT
═══════════════════════════════════════

Story: {title}
Chapters analyzed: {count}
Total words: {total}

FINDINGS SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AI Patterns: {count} instances
Character Issues: {count} instances
World Violations: {count} instances
Style Drift: {count} chapters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI PATTERN DETECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Chapter 1:
  [Line 47] "Sarah delved into the mystery"
  → Alternatives:
    1. "Sarah investigated the mystery" (recommended)
    2. "Sarah explored the mystery"
    3. "Sarah dug into the mystery"

  [Line 89] "The rich tapestry of clues"
  → Alternatives:
    1. "The collection of clues" (recommended)
    2. "The array of clues"
    3. "The evidence she'd gathered"

Chapter 3:
  [Line 12] "It's worth noting that..."
  → Alternatives:
    1. Remove entirely (recommended)
    2. "She noticed that..."
    3. [Show without telling]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHARACTER CONSISTENCY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sarah Martinez:
  ✓ Voice consistent across all chapters
  ⚠ Chapter 5: Dialogue seems overly formal
    [Line 34] "I shall investigate this matter"
    → Character profile shows casual speech
    → Suggested: "I'll check it out"

Marcus:
  ✓ Personality consistent
  ✗ Physical contradiction:
    Chapter 1: "His blue eyes narrowed"
    Chapter 7: "His brown eyes darkened"
    → Needs correction

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WORLD CONSISTENCY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Magic System:
  ✗ Rule violation in Chapter 4
    [Line 67] "Sarah cast the spell without any cost"
    → WORLD.md states: "All magic requires blood sacrifice"
    → Needs revision to show cost

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STYLE ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sentence Length Drift:
  Profile target: 15 words average
  Chapter 1: 14.2 words ✓
  Chapter 2: 15.8 words ✓
  Chapter 3: 22.1 words ⚠ (47% over target)
  Chapter 4: 16.3 words ✓

Recommendation: Tighten Chapter 3 prose

Sentence Structure Variety:
  Chapter 1: GOOD ✓
  Chapter 2: WARNING ⚠
    - 85% simple sentences (needs variety)
    - 0% fragments or questions
  Chapter 3: CRITICAL ✗
    - 4 consecutive identical structures (para 4-5)
    - 78% subject-opening sentences
    - 90% simple sentences
  Chapter 4: EXCELLENT ✓

Issues found:
  • 3 instances of 3+ consecutive same structures
  • 2 chapters with >80% subject openings
  • 1 sentence with 5 "and" conjunctions (Ch 4, para 3)

Recommendation: Chapters 2 and 3 need sentence variety revision

═══════════════════════════════════════
ACTIONS REQUIRED
═══════════════════════════════════════

Auto-fixable: {count} issues
Manual review: {count} issues
Critical: {count} issues

Proceed with automatic fixes? [Y/n]
```

### Step 8: Apply Automatic Fixes

For issues with clear solutions:

1. **AI pattern replacements:**
   - Use Edit tool to replace patterns with recommended alternatives
   - Preserve surrounding context
   - Maintain sentence flow

2. **Simple consistency fixes:**
   - Update contradictory descriptions to match first appearance
   - Fix punctuation and formatting issues

3. **Style normalization:**
   - Break overly long sentences
   - Simplify overly complex vocabulary (if appropriate)

For each fix:
- Save chapter file
- Track what was changed
- Create backup version

### Step 9: Report Manual Review Items

For issues requiring human judgment:

1. **Character voice concerns:**
   - List dialogue that seems off
   - Provide context and suggestion
   - Leave for author review

2. **Plot inconsistencies:**
   - Flag potential contradictions
   - Note location
   - Author decides resolution

3. **Style preferences:**
   - Note stylistic choices that differ from profile
   - Author decides if intentional or needs fixing

### Step 10: Generate Final Report

Show comprehensive completion report:

```
═══════════════════════════════════════
REVISION COMPLETE
═══════════════════════════════════════

Chapters processed: {count}

FIXES APPLIED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AI Patterns: {count} fixed
  • "delve" → replaced in 3 locations
  • "tapestry" → replaced in 2 locations
  • "it's worth noting" → removed 1 instance

Character Consistency: {count} fixed
  • Marcus eye color corrected (Chapter 7)
  • Sarah dialogue tone adjusted (Chapter 5)

World Consistency: {count} fixed
  • Magic cost added to Chapter 4 spell

Style Drift: {count} chapters adjusted
  • Chapter 3 sentences shortened (22→16 avg words)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MANUAL REVIEW REQUIRED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{count} items need author review:

1. Chapter 2, Line 45: Potential plot inconsistency
   → Sarah knows about the conspiracy but this wasn't revealed yet
   → Review timeline

2. Chapter 6: Style choice verification
   → Intentionally formal tone for court scene?
   → Differs from casual profile

═══════════════════════════════════════
NEXT STEPS
═══════════════════════════════════════

{IF MANUAL REVIEW ITEMS EXIST:}
1. Review flagged items
   → Open chapters and address concerns
   → Make editorial decisions on plot/style

2. Verify fixes (optional)
   → /write:detect - Check AI patterns removed
   → /write:check-consistency - Verify continuity

{IF NO MANUAL ITEMS OR AFTER REVIEW:}
3. Export manuscript
   → /write:export
   → Multiple formats available
   → Ready for submission/publication

Other options:
• /write:chapter N - Rewrite specific chapter
• Edit chapters manually for final polish
• /write:revisions chapter-{NN} - View history
```

## Integration with Detection Commands

This workflow combines and automates:
- `/write:detect` - AI pattern detection
- `/write:check-consistency` - Consistency checking

Advantages over running separately:
- Single comprehensive scan
- Automatic fixes applied
- Coordinated report
- Faster (scans once vs multiple times)

You can still run individual commands for focused checks.

## Notes

- **Automatic fixes are conservative** - only fixes with clear correct alternatives
- **Manual review items** require judgment calls
- **Backups created** before any edits
- **Re-run anytime** - safe to run multiple times
- **Scope flexibility** - can revise specific chapters or entire story

## Examples

**Full story revision:**
```
/write:revise
→ Scans all chapters
→ Applies automatic fixes
→ Reports manual items
```

**Specific chapters:**
```
/write:revise 3-7
→ Only revises chapters 3 through 7
```

**Focus on AI patterns:**
```
/write:revise --patterns-only
→ Skips consistency checking
→ Only detects and fixes AI language
```

**Report only (no fixes):**
```
/write:revise --report
→ Generates analysis report
→ Doesn't apply any fixes
→ Use for review before committing changes
```
