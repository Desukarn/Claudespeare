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

### Step 6: Analyze Style Drift

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

✓ Review manual items in chapters
✓ Run /write:detect again to verify fixes
✓ Run /write:check-consistency for final check
✓ Ready for /write:export when satisfied
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
