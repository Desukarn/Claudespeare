# Comprehensive Story Audit - One-Click Quality Check

## Purpose

Comprehensive quality audit that combines ALL Claudespeare quality checks into a single command. Generates a detailed report covering every aspect of story quality from Sanderson frameworks to AI pattern detection.

**When to use**: After completing a draft or major section (full story, arc, or act)

**Time**: 15-30 minutes depending on story length

**Output**: Detailed multi-section report with specific flagged issues and recommendations

---

## What This Audits

This comprehensive check combines:

1. **Sanderson Framework Verification** (from sanderson-skills/)
2. **Plot-Hole Prevention** (from check-consistency.md)
3. **AI Pattern Detection** (from ai-detect.md)
4. **Scene Structure Analysis** (from improvement specs)
5. **Show-Tell Balance** (prose quality)
6. **Character Voice Differentiation** (consistency)
7. **Timeline Consistency** (from check-consistency.md)
8. **Magic/World Rules** (internal consistency)
9. **Pacing Audit** (from pacing-guide.md)
10. **Dialogue Quality** (natural vs AI patterns)

---

## Workflow

### Step 1: Load Story Files

Read all relevant files:
- `PROJECT.md` - story metadata
- `OUTLINE.md` or `yolo-outline.md` - plot structure
- `CHARACTERS.md` or `yolo-characters.md` - character profiles
- `WORLD.md` - world-building rules (if exists)
- `ARCS.md` - character development tracking (if exists)
- All files in `chapters/` directory

### Step 2: Run All Audit Modules

Execute each audit sequentially:

#### Module 1: Sanderson Framework Verification

**Check Promise-Progress-Payoff** (from `promise-progress-payoff.md`):
- ✓ Major Dramatic Question established by end of Act I?
- ✓ Progress signposts every 2-3 chapters?
- ✓ Yes-But / No-And escalation patterns present?
- ✓ Payoff delivered (surprising yet inevitable)?
- ✓ No wheel-spinning (every scene advances story)?

**Check Character Triangle** (from `proactive-relatable-capable.md`):
- ✓ Protagonist is Proactive (makes choices, drives action)?
- ✓ Protagonist is Relatable (flaws, vulnerability, humanity)?
- ✓ Protagonist is Capable (demonstrates competence)?
- ⚠️ Flag if protagonist drops TWO pillars (death spiral)

**Check Try-Fail Cycles** (from `promise-progress-payoff.md`):
- ✓ Protagonist tries solutions, escalates approaches?
- ✓ Failures make sense, teach protagonist something?
- ⚠️ Flag if protagonist succeeds on first try repeatedly

**Output**: Sanderson Framework Score (0-10) with specific issues

---

#### Module 2: Plot-Hole Detection

**Character Knowledge Tracking**:
- Track what each character learns when
- Flag if character acts on information they shouldn't have
- Example: Character B mentions event from Chapter 5, but wasn't present

**Timeline Consistency**:
- Build timeline from chapter events
- Flag temporal inconsistencies
- Example: "three days later" but events don't add up

**Cause-Effect Chains**:
- Track consequences of major events
- Flag if major event has no follow-up
- Example: Character breaks law in Chapter 3, never mentioned again

**Dropped Plot Threads**:
- Identify threads introduced but never resolved
- Flag if setup has no payoff
- Example: Mysterious artifact in Act I, never mentioned in Act III

**Output**: Plot-Hole Report with flagged inconsistencies

---

#### Module 3: AI Pattern Detection

**Run ai-detect.md checks**:

Pattern 1-24 (existing patterns from ai-detect.md):
- Banned words (delve, tapestry, testament, beacon, etc.)
- Purple prose (adjective stacking, melodramatic adverbs)
- Fancy dialogue tags
- Filter words (seemed, appeared, felt)
- Chatbot dialogue
- Info dumps
- Physical emotion clichés

**Pattern 25: Emotional Beat Clichés**:
- "held breath they didn't know they were holding"
- "heart pounding in chest"
- "blood ran cold" / "blood turned to ice"
- "shivers down spine"
- "tears pricked eyes"
- "stomach dropped"

**Pattern 26: Info-Dump Detection**:
- Paragraphs >150 words with no dialogue/action
- "As you know" exposition
- Encyclopedia-style thinking
- Wikipedia paragraphs

**Pattern 27: Missing AI Buzzwords**:
- "beacon of" / "stands as a beacon"
- "serves as a reminder"
- "speaks to" / "speaks volumes"
- "sheds light on"
- "heartbeat of" / "pulse of"

**Pattern 28: AI Character Names**:
- Kael, Elara, Lyra, Aria
- Any name in AI slop list (from name-generator-requirement.md)

**Pattern 29: AI Plot Clichés**:
- "strength becomes weakness"
- "final moral act"
- "power corrupts protagonist"
- "mentor dies"
- "chosen one refuses call"

**Output**: AI Pattern Report with count per pattern, severity rating

---

#### Module 4: Scene Structure Patterns

**Cookie-Cutter Opening Detection**:
- Count chapters starting with weather
- Flag if >5 chapters start with weather description
- Count chapters starting with wake-up scene
- Flag if >3 wake-up scenes

**Mirror Description**:
- Detect if character describes self in mirror
- Classic amateur writing cliché

**Cliffhanger Overuse**:
- Track how many scenes end on cliffhanger
- Flag if >80% (feels robotic)

**Action-Reaction-Introspection Loop**:
- Check if every scene follows same structure
- Flag if >70% match template pattern

**Output**: Scene Structure Report with specific pattern counts

---

#### Module 5: Show-Tell Balance

**Filter Word Analysis**:
- Count filter words per chapter: seemed, appeared, felt, looked like
- Calculate as percentage of total verbs
- Flag if >10% of verbs are filter words

**Emotion Telling**:
- Detect phrases like "she felt afraid," "he was angry," "Sarah was nervous"
- Count instances per chapter
- Suggest showing alternatives

**Sensory Detail Density**:
- Count sensory details (sight, sound, smell, touch, taste) per scene
- Flag if scenes lack sensory grounding

**Output**: Show-Tell Balance Report with recommendations

---

#### Module 6: Character Voice Differentiation

**Dialogue Analysis per Character**:
- Extract dialogue for each character
- Analyze:
  - Vocabulary complexity (average word length)
  - Sentence length patterns
  - Use of contractions, fragments
  - Speech quirks or patterns

**Differentiation Check**:
- Compare character dialogue profiles
- Flag if all characters sound identical
- Flag if protagonist dialogue indistinguishable from others

**Output**: Character Voice Report with similarity scores

---

#### Module 7: Timeline Consistency

**Build Complete Timeline**:
- Extract temporal markers from all chapters
- Map events to relative or absolute time
- Flag inconsistencies

**Common Issues**:
- Travel time doesn't match geography
- Character age inconsistencies
- Seasonal contradictions
- Event order violations

**Output**: Timeline Report with flagged issues

---

#### Module 8: Magic/World Rules Consistency

**Extract Rules from WORLD.md**:
- Magic system costs and limitations
- World-building facts
- Geography and distances
- Cultural norms

**Check Adherence**:
- Flag if magic used without paying cost
- Flag if world rules violated
- Flag if geography inconsistent

**Output**: World Consistency Report

---

#### Module 9: Pacing Audit

**Run pacing-guide.md audit checks**:
- Chapter length uniformity
- Scene length patterns
- Climax positioning formula
- Act length mechanical division

**Output**: Pacing Audit Report (see pacing-guide.md for details)

---

#### Module 10: Dialogue Quality Check

**Natural Dialogue Audit**:
- Count chatbot phrases: "Certainly!" "Indeed!" "Absolutely right!"
- Count contractions vs formal speech
- Check fragment usage
- Analyze agreement phrases

**Dialogue Tag Analysis**:
- Count "said" vs fancy tags
- Flag if "said" used <70% (should be 80%+)
- Flag excessive adverb + said combinations

**Output**: Dialogue Quality Report

---

### Step 3: Calculate Overall Scores

**Generate scores per category**:
- Sanderson Framework: 0-10
- Plot Consistency: 0-10
- AI Pattern Avoidance: 0-10
- Scene Structure: 0-10
- Show-Tell Balance: 0-10
- Character Voice: 0-10
- Timeline: 0-10
- World Rules: 0-10
- Pacing: 0-10
- Dialogue: 0-10

**Overall Quality Score**: Average of all categories

---

### Step 4: Generate Comprehensive Report

Output detailed report with all findings:

```
═══════════════════════════════════════════════════════════════
COMPREHENSIVE STORY AUDIT REPORT
═══════════════════════════════════════════════════════════════

Story: {Title}
Word Count: {total} words
Chapters Analyzed: {count}
Audit Date: {timestamp}

═══════════════════════════════════════════════════════════════
OVERALL QUALITY SCORE: {score}/10
═══════════════════════════════════════════════════════════════

Category Breakdown:
  ✓ Sanderson Framework      {score}/10  {status}
  ✓ Plot Consistency         {score}/10  {status}
  ✓ AI Pattern Avoidance     {score}/10  {status}
  ✓ Scene Structure          {score}/10  {status}
  ✓ Show-Tell Balance        {score}/10  {status}
  ✓ Character Voice          {score}/10  {status}
  ✓ Timeline Consistency     {score}/10  {status}
  ✓ World Rules              {score}/10  {status}
  ✓ Pacing                   {score}/10  {status}
  ✓ Dialogue Quality         {score}/10  {status}

═══════════════════════════════════════════════════════════════
1. SANDERSON FRAMEWORK ANALYSIS
═══════════════════════════════════════════════════════════════

Score: {score}/10

Promise-Progress-Payoff:
  {✓ | ⚠️ | ❌} Major Dramatic Question established: {details}
  {✓ | ⚠️ | ❌} Progress signposting adequate: {details}
  {✓ | ⚠️ | ❌} Yes-But/No-And escalation: {details}
  {✓ | ⚠️ | ❌} Payoff delivered: {details}

Character Triangle (Protagonist):
  {✓ | ⚠️ | ❌} Proactive (Agency): {percentage}% of scenes
  {✓ | ⚠️ | ❌} Relatable (Empathy): {assessment}
  {✓ | ⚠️ | ❌} Capable (Competence): {assessment}

Try-Fail Cycles:
  {✓ | ⚠️ | ❌} Escalating attempts: {details}

Issues Found: {count}
{List specific issues with chapter references}

Recommendations:
{Specific actionable recommendations}

───────────────────────────────────────────────────────────────
2. PLOT-HOLE DETECTION
───────────────────────────────────────────────────────────────

Score: {score}/10

Character Knowledge Issues: {count}
{List each with chapter reference and explanation}

Timeline Inconsistencies: {count}
{List each with details}

Dropped Plot Threads: {count}
{List each thread and where it was abandoned}

Cause-Effect Gaps: {count}
{List events without consequences}

Recommendations:
{Specific fixes needed}

───────────────────────────────────────────────────────────────
3. AI PATTERN DETECTION
───────────────────────────────────────────────────────────────

Score: {score}/10

Patterns Detected:
  Pattern 1 (Banned AI words): {count} instances
    {List specific examples with chapter locations}

  Pattern 2 (Purple prose): {count} instances
    {List examples}

  Pattern 25 (Emotion clichés): {count} instances
    {List examples}

  Pattern 26 (Info dumps): {count} instances
    {List examples}

  Pattern 28 (AI character names): {count} instances
    {List names flagged}

  Pattern 29 (AI plot clichés): {count} instances
    {List clichés detected}

Total AI Patterns: {count}
Severity: {Low | Medium | High | Critical}

Recommendations:
{Specific replacements and fixes}

───────────────────────────────────────────────────────────────
4. SCENE STRUCTURE ANALYSIS
───────────────────────────────────────────────────────────────

Score: {score}/10

Cookie-Cutter Patterns:
  Weather openings: {count} chapters ({percentage}%)
  Wake-up scenes: {count} chapters
  Mirror descriptions: {count} instances
  Cliffhanger endings: {count} scenes ({percentage}%)
  Action-Reaction-Introspection loops: {percentage}%

Issues Found: {count}

Recommendations:
{Suggestions for varied scene structures}

───────────────────────────────────────────────────────────────
5. SHOW-TELL BALANCE
───────────────────────────────────────────────────────────────

Score: {score}/10

Filter Words:
  Total count: {count}
  As percentage of verbs: {percentage}%
  Chapters over 10% threshold: {list}

Direct Emotion Telling:
  "felt [emotion]": {count} instances
  "[character] was [emotion]": {count} instances

Sensory Detail Density:
  Scenes lacking sensory grounding: {count}

Recommendations:
{Specific showing alternatives for flagged instances}

───────────────────────────────────────────────────────────────
6. CHARACTER VOICE DIFFERENTIATION
───────────────────────────────────────────────────────────────

Score: {score}/10

Characters Analyzed: {list}

Voice Profiles:
  {Character A}:
    Avg word length: {value}
    Avg sentence length: {value}
    Contractions: {percentage}%
    Fragments: {percentage}%

  {Character B}:
    {same metrics}

Similarity Scores:
  A-B similarity: {percentage}% {⚠️ if >80%}
  A-C similarity: {percentage}%

Issues: {count} characters sound too similar

Recommendations:
{Suggestions for differentiating voices}

───────────────────────────────────────────────────────────────
7. TIMELINE CONSISTENCY
───────────────────────────────────────────────────────────────

Score: {score}/10

Timeline Built: {success | partial | failed}

Inconsistencies Found: {count}
{List each with details and chapter references}

Recommendations:
{Specific timeline fixes needed}

───────────────────────────────────────────────────────────────
8. MAGIC/WORLD RULES CONSISTENCY
───────────────────────────────────────────────────────────────

Score: {score}/10

Rules Extracted from WORLD.md:
  {List magic system rules}
  {List world-building facts}

Violations Found: {count}
{List each violation with chapter reference}

Recommendations:
{Fixes to restore consistency}

───────────────────────────────────────────────────────────────
9. PACING AUDIT
───────────────────────────────────────────────────────────────

Score: {score}/10

{Full pacing audit report from pacing-guide.md}

───────────────────────────────────────────────────────────────
10. DIALOGUE QUALITY
───────────────────────────────────────────────────────────────

Score: {score}/10

Chatbot Phrases: {count} instances
  {List examples with chapter references}

Dialogue Tags:
  "said" usage: {percentage}% (target: 80%+)
  Fancy tags: {count} instances
  Adverb+said: {count} instances

Natural Speech:
  Contractions: {percentage}% (target: 70%+ unless formal)
  Fragments: {percentage}%

Recommendations:
{Specific dialogue improvements}

═══════════════════════════════════════════════════════════════
PRIORITY ISSUES (Fix These First)
═══════════════════════════════════════════════════════════════

{List top 10 highest-priority issues across all categories}

1. {Category}: {Issue description} - {Location}
2. {Category}: {Issue description} - {Location}
...

═══════════════════════════════════════════════════════════════
SUMMARY AND NEXT STEPS
═══════════════════════════════════════════════════════════════

Overall Assessment:
{9-10}: Excellent - Minor polish needed
{7-8}: Good - Some revision recommended
{5-6}: Fair - Significant revision needed
{3-4}: Weak - Major structural issues
{0-2}: Critical - Fundamental problems

Your Score: {score}/10 - {assessment}

Recommended Actions:
1. {First priority based on scores}
2. {Second priority}
3. {Third priority}

Estimated revision time: {estimate based on issues}

Commands to run:
  → /write:revise {focus_area}
  → /write:chapter {N} (to rewrite specific chapters)
  → /write:check-consistency (after fixes)

═══════════════════════════════════════════════════════════════
```

---

## Command Usage

**Run comprehensive audit**:
```
/write:audit
```

**Run with focus on specific category**:
```
/write:audit --focus=sanderson
/write:audit --focus=ai-patterns
/write:audit --focus=dialogue
```

**Run on specific chapters**:
```
/write:audit --chapters=1-10
```

**Generate detailed report file**:
```
/write:audit --export=audit-report.md
```

---

## Integration with Revision Workflow

### Recommended Workflow:

1. **Complete draft**: Finish writing all chapters
2. **Run comprehensive audit**: `/write:audit`
3. **Review report**: Identify priority issues
4. **Fix critical issues**: Plot holes, Sanderson framework failures
5. **Run targeted audits**: Focus on flagged categories
6. **Fix moderate issues**: AI patterns, scene structure, dialogue
7. **Run final audit**: Verify improvements
8. **Polish**: Final prose pass

### Audit Frequency:

- **After completing Act I**: Run partial audit to catch early issues
- **After completing full draft**: Run full comprehensive audit
- **After major revisions**: Re-run to verify fixes
- **Before publication**: Final audit pass

---

## Notes

- **Audit is diagnostic, not prescriptive**: Flags issues for review, doesn't auto-fix
- **Use judgment**: Not every flagged item is necessarily wrong
- **Context matters**: Some "violations" serve story purpose
- **Prioritize**: Fix critical issues before minor polish
- **Iterate**: Audit → Fix → Audit again to verify

---

## Benefits

1. **One-Click Quality Check**: No need to run multiple commands
2. **Comprehensive Coverage**: Every quality dimension checked
3. **Detailed Report**: Specific issues with locations
4. **Actionable Recommendations**: Clear next steps
5. **Priority Flagging**: Know what to fix first
6. **Track Progress**: Re-run to see improvements

---

*This comprehensive audit is the final quality gate before publication.*
