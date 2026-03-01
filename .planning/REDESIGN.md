# Claudespeare Workflow Redesign

## Current Problems

### 1. `/write:chapter` is Too Interactive
**Problem**: Even in YOLO mode with an outline already created, `/write:chapter` still asks:
- Which chapter number?
- Which plot beat?
- Which POV character?
- Scene breakdown?

This breaks the flow. After discussing and creating an outline, you should just be able to say "write the story" and it executes everything you already decided.

**Root Cause**: The command was designed for one-off chapter writing, not orchestrated execution.

### 2. No Parallel Writing
**Problem**: Writing happens serially, one chapter at a time. If you have 10 chapters to write, you wait for chapter 1 to finish before chapter 2 even starts.

**Missed Opportunity**: Claude Code supports parallel subagent execution (see `/batch` and `Agent` tool). We should spawn multiple writing agents simultaneously.

### 3. No Automatic Revision Workflow
**Problem**: After writing chapters, you have to manually remember to:
- Run `/write:detect` for AI patterns
- Run `/write:check-consistency`
- Fix issues
- Re-run detection

**Missed Opportunity**: Claude Code has hooks (`PostToolUse`, `SubagentStop`) that can automatically trigger quality checks.

### 4. Skills Not Used for Writing
**Problem**: The writing commands are just markdown files that get loaded as instructions. They don't use Claude Code's skill patterns properly.

**Missed Opportunity**: Skills can:
- Use `context: fork` to run in isolated subagents
- Define `allowed-tools` for safety
- Use hooks for automatic validation
- Preload supporting content

---

## Redesigned Workflow

### Phase 1: Planning (Already Works Well)

```
/write:new-project → /write:expand (YOLO) or /write:plan (In-Depth) → OUTLINE.md created
```

This part is fine. Keep it as-is.

### Phase 2: Writing (NEW - GSD-Style Execution)

#### `/write:arc [arc-name]` - The Main Orchestrator

**Works like `/gsd:execute-phase` but for story arcs.**

##### Step 1: Load Story Context
```bash
# Read all story files
- PROJECT.md
- CHARACTERS.md / yolo-characters.md
- OUTLINE.md / yolo-outline.md
- STYLE.md (if exists)
- ARCS.md (if exists)
- WORLD.md (if exists)
```

##### Step 2: Parse Outline into Chapters
```bash
# Analyze OUTLINE.md structure
# Identify:
- Act breaks
- Chapter boundaries
- Plot beats per chapter
- Estimated word counts
- POV assignments

# Generate execution plan:
Arc 1 (Chapters 1-3):
  - Chapter 1: "The Discovery" (Sarah POV, ~2500 words)
  - Chapter 2: "First Clues" (Sarah POV, ~2000 words)
  - Chapter 3: "The Encounter" (Marcus POV, ~2500 words)
```

##### Step 3: User Confirmation (Interactive Mode)
```
═══════════════════════════════════════
WRITING PLAN: Arc 1
═══════════════════════════════════════

Chapters to write: 3
Estimated words: ~7,000
Parallel agents: 3

1. Chapter 1: "The Discovery" (Sarah POV, ~2500w)
   Plot: Opening scene, inciting incident, Sarah discovers the artifact

2. Chapter 2: "First Clues" (Sarah POV, ~2000w)
   Plot: Sarah investigates, meets informant, learns about the conspiracy

3. Chapter 3: "The Encounter" (Marcus POV, ~2500w)
   Plot: Marcus perspective, confrontation, stakes raised

Proceed with parallel writing? [Y/n]
```

##### Step 4: Spawn Writing Subagents (Parallel Execution)

**Pattern from `/batch` and subagent documentation:**

```typescript
// Spawn 3 subagents in parallel, each writes one chapter
const agents = [
  {
    name: "chapter-1-writer",
    prompt: buildChapterPrompt(chapter1Context),
    isolation: "worktree", // Isolated git copy
    background: true
  },
  {
    name: "chapter-2-writer",
    prompt: buildChapterPrompt(chapter2Context),
    isolation: "worktree",
    background: true
  },
  {
    name: "chapter-3-writer",
    prompt: buildChapterPrompt(chapter3Context),
    isolation: "worktree",
    background: true
  }
];

// All run concurrently
await Promise.all(agents.map(spawnAgent));
```

**Each subagent prompt contains:**
```
You are writing Chapter N of [STORY TITLE].

# Story Context
[Full context from STYLE.md, CHARACTERS.md, OUTLINE.md, WORLD.md]

# Your Chapter Assignment
Title: "The Discovery"
POV: Sarah Martinez
Plot beat: Opening scene → inciting incident → discovery of artifact
Target length: ~2500 words
Scenes:
  1. Sarah's morning routine (establish normalcy)
  2. The find at the archaeological site
  3. First realization something is wrong

# Writing Instructions
- Match the style profile in STYLE.md
- Maintain character voice for Sarah (see CHARACTERS.md)
- Reference world details from WORLD.md
- Scene-by-scene generation (3 scenes)
- Save to chapters/chapter-01.md

Generate the chapter. When complete, your output will be automatically checked for:
- AI language patterns
- Character consistency
- Style matching
```

##### Step 5: Automatic Post-Write Hooks

**After each chapter is written, hooks trigger automatically:**

```yaml
# In .claude/skills/write/commands/arc.md frontmatter:
hooks:
  SubagentStop:
    - matcher: "chapter-.*-writer"
      hooks:
        - type: command
          command: ".claude/hooks/chapter-quality-check.sh"
```

**The hook script (`chapter-quality-check.sh`):**
```bash
#!/bin/bash
# Automatically run after each chapter writing agent completes

# Read the completed chapter path from agent output
CHAPTER_FILE=$(echo "$INPUT" | jq -r '.last_assistant_message' | grep -oP 'chapter-\d+\.md')

if [ -z "$CHAPTER_FILE" ]; then
  exit 0
fi

# Run AI pattern detection
python .claude/hooks/detect_ai_patterns.py "chapters/$CHAPTER_FILE"

# Run character voice consistency check
python .claude/hooks/check_character_voice.py "chapters/$CHAPTER_FILE"

# If issues found, report back with exit code 2 (blocking)
if grep -q "CRITICAL" /tmp/chapter-check-report.txt; then
  cat /tmp/chapter-check-report.txt >&2
  exit 2  # Blocks the agent from completing
fi

# Otherwise, allow completion
exit 0
```

##### Step 6: Aggregate Results
```
═══════════════════════════════════════
WRITING COMPLETE: Arc 1
═══════════════════════════════════════

✓ Chapter 1: 2,487 words (target: 2,500)
✓ Chapter 2: 1,993 words (target: 2,000)
⚠ Chapter 3: 2,789 words (target: 2,500) - 11% over

Quality checks:
✓ AI pattern detection: 2 patterns found, auto-fixed
✓ Character consistency: All checks passed
⚠ Style matching: Chapter 3 sentence length variance +15%

Issues to review:
- Chapter 3: Slightly over target, consider tightening
- Chapter 3: More complex sentences than style profile

Total words: 7,269 / ~7,000 target
Story progress: 7,269 / 80,000 (9%)

Next: /write:arc 2 (Chapters 4-7)
```

### Phase 3: Revision (NEW - Hook-Based Automation)

#### Problem: Manual Detection is Tedious

Currently:
1. Write chapters
2. Remember to run `/write:detect`
3. Review report
4. Fix issues manually
5. Run again to verify

#### Solution: Automatic Detection + Revision Loop

**Pattern from hooks documentation:**

```yaml
# Skill: .claude/skills/write/commands/revise.md
---
name: revise
description: Automatically detect and fix AI patterns, consistency issues, and style drift
context: fork
agent: general-purpose
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: ".claude/hooks/validate-prose.sh"
          async: true
---

# Revision Workflow

1. **Load Current Chapters**
   - Read all chapters in chapters/*.md
   - Load STYLE.md, CHARACTERS.md, WORLD.md

2. **Run Detection**
   - AI pattern detection (24+ patterns)
   - Character voice consistency
   - World rule violations
   - POV consistency
   - Style drift analysis

3. **Generate Fixes**
   - For each issue:
     - Explain the problem
     - Show current text
     - Provide 3-5 alternatives
     - Apply best fix with Edit tool

4. **Verify Fixes**
   - Re-run detection on edited chapters
   - Confirm issues resolved
   - Update revision metadata

5. **Report**
   - Issues found: X
   - Issues fixed: Y
   - Manual review needed: Z
```

**The validation hook (`validate-prose.sh`):**
```bash
#!/bin/bash
# Runs after each Edit to validate changes

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path')

# Only validate prose files
if [[ "$FILE_PATH" != chapters/*.md ]]; then
  exit 0
fi

# Check for reintroduced AI patterns
if python .claude/hooks/detect_ai_patterns.py "$FILE_PATH" | grep -q "delve\|tapestry\|testament"; then
  echo "Warning: AI pattern reintroduced in $FILE_PATH" >&2
  # Non-blocking warning, just notify
fi

# Update word count
WORD_COUNT=$(wc -w < "$FILE_PATH")
echo "{\"systemMessage\": \"Chapter updated: $WORD_COUNT words\"}"

exit 0
```

---

## Implementation Plan

### 1. Create `/write:arc` Command

**File: `.claude/commands/write/arc.md`**

```yaml
---
description: Write multiple chapters in parallel with automatic quality checks
---

Execute arc-based writing workflow with parallel chapter generation.

Read and follow the complete instructions in `.claude/skills/write/write-arc.md`.

Arguments: $ARGUMENTS
```

**File: `.claude/skills/write/write-arc.md`**

This is the full orchestrator implementation:
- Load story context
- Parse outline into chapter plan
- Generate prompts for each chapter
- Spawn parallel subagents (using Agent tool with `isolation: "worktree"`)
- Monitor completion
- Aggregate results
- Report progress

### 2. Create Writing Subagent Template

**File: `.claude/agents/chapter-writer.md`**

```yaml
---
name: chapter-writer
description: Write a single chapter with full story context
tools: Read, Write, Grep, Glob
model: sonnet
permissionMode: acceptEdits
hooks:
  Stop:
    - hooks:
        - type: command
          command: ".claude/hooks/chapter-quality-check.sh"
---

You are writing a chapter for a story.

# Story Context
{INJECTED_CONTEXT}

# Chapter Assignment
{CHAPTER_DETAILS}

# Instructions
1. Read existing chapters for continuity
2. Generate prose scene-by-scene
3. Match style profile exactly
4. Maintain character voices
5. Save to chapters/chapter-{NN}.md with frontmatter

Generate the chapter now.
```

### 3. Create Quality Check Hooks

**File: `.claude/hooks/chapter-quality-check.sh`**

```bash
#!/bin/bash
# PostToolUse hook for chapter validation

# Detect AI patterns
# Check character consistency
# Verify style matching
# Report issues or allow completion
```

**File: `.claude/hooks/validate-prose.sh`**

```bash
#!/bin/bash
# Async hook for edit validation

# Check for reintroduced patterns
# Update word counts
# Non-blocking warnings
```

### 4. Update `/write:chapter` for Single-Chapter Mode

Keep `/write:chapter` for one-off writing, but make it smart:

```yaml
# If invoked with arguments (e.g., /write:chapter 5)
→ Non-interactive mode, auto-detect from outline

# If invoked without arguments
→ Interactive mode (current behavior)
```

### 5. Create `/write:revise` Command

**File: `.claude/commands/write/revise.md`**

```yaml
---
description: Automatically detect and fix AI patterns, consistency issues, and style drift
context: fork
agent: general-purpose
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: ".claude/hooks/validate-prose.sh"
          async: true
---

Run the revision workflow from `.claude/skills/write/revise.md`.
```

---

## Updated User Workflow

### YOLO Mode (Fast)

```
1. /write:new-project
   → Story: "Mystery thriller"
   → Mode: YOLO
   → Length: Novel

2. /write:expand
   → Premise expanded
   → Characters created (3-4)
   → Simple outline generated

3. /write:style-seed
   → Paste 2-3 paragraphs
   → Style profile created

4. /write:arc 1
   → Chapters 1-3 written in parallel
   → Automatic quality checks
   → ~7,000 words in ~15 minutes

5. /write:arc 2
   → Chapters 4-7 written in parallel
   → ~10,000 words in ~20 minutes

6. /write:revise
   → All chapters scanned
   → AI patterns fixed
   → Consistency validated
   → Style drift corrected

7. /write:export
   → Manuscript compiled
   → Professional format
   → Ready for submission
```

**Total time: ~2 hours for first draft of 80,000-word novel**

### In-Depth Mode (Thorough)

```
1. /write:new-project
   → Story: "Epic fantasy"
   → Mode: In-Depth
   → Length: Novel

2. /write:plan
   → Detailed character profiles
   → Complete plot with beats
   → Character arcs mapped
   → World-building documented
   → Themes defined
   (30-60 minutes)

3. /write:style-seed
   → Style profile created

4. /write:arc "Act 1: The Awakening"
   → Chapters 1-8 written in parallel
   → ~25,000 words
   → Quality checks automatic

5. Review & Iterate
   → Read chapters
   → Request specific revisions
   → /write:chapter 3 (rewrite single chapter)

6. /write:arc "Act 2: The Journey"
   → Chapters 9-20 written in parallel
   → ~35,000 words

7. /write:arc "Act 3: The Resolution"
   → Chapters 21-30 written in parallel
   → ~25,000 words

8. /write:revise
   → Final quality pass
   → AI patterns removed
   → Consistency verified

9. /write:export
   → Complete manuscript
```

**Total time: ~6-8 hours for first draft of 85,000-word novel**

---

## Technical Implementation Notes

### Parallel Subagent Spawning

From the Claude Code docs and `/batch` implementation:

```javascript
// Pattern: Spawn multiple subagents with Task tool
for (const chapter of chapters) {
  const agentPrompt = buildChapterPrompt(chapter);

  // Use Task tool with background execution
  Task({
    subagent_type: "general-purpose",
    description: `Write Chapter ${chapter.number}`,
    prompt: agentPrompt,
    run_in_background: true
  });
}

// Monitor completion via SubagentStop hooks
```

### Worktree Isolation (Optional)

For truly parallel writes without conflicts:

```yaml
isolation: "worktree"
```

Each subagent gets its own git worktree, can write independently, then results merge back.

### Hook Execution Timing

**PreToolUse**: Before writing (validate inputs)
**PostToolUse**: After writing (check quality)
**SubagentStop**: When chapter agent completes (aggregate results)
**Stop**: When main arc command completes (final report)

### Context Injection

Each subagent needs full story context. Use `$ARGUMENTS` substitution:

```yaml
# In the arc command
prompt = `
You are writing Chapter ${N}.

# Story Context
${STYLE_MD}
${CHARACTERS_MD}
${OUTLINE_MD}
${WORLD_MD}

# Chapter Assignment
${chapter.details}

Generate the chapter.
`
```

---

## Benefits of This Redesign

### 1. **Smooth Execution (Like GSD)**
- Discuss once → execute everything
- No repeated questions
- Non-interactive flow after planning

### 2. **Parallel Writing**
- 10 chapters write simultaneously
- 10x faster than serial execution
- Scales with available resources

### 3. **Automatic Quality**
- Hooks run detection automatically
- Issues caught immediately
- Fixes applied in revision loop
- No manual remember-to-check

### 4. **Proper Skill Usage**
- Commands use `context: fork` for isolation
- Subagents have focused system prompts
- Hooks enforce quality gates
- Tools restricted appropriately

### 5. **Better UX**
- Clear progress tracking
- Aggregate reporting
- Explicit confirmations
- Actionable next steps

---

## Migration Path

### Phase 1: Non-Breaking Additions
1. Add `/write:arc` command (new)
2. Add `/write:revise` command (new)
3. Add quality check hooks (new)
4. Keep existing commands working as-is

### Phase 2: Improvements to Existing
1. Update `/write:chapter` to detect context
2. Make it non-interactive when context exists
3. Keep interactive mode as fallback

### Phase 3: Documentation
1. Update SKILL.md with new workflow
2. Add examples to README
3. Create tutorial videos

### Phase 4: Cleanup (Later)
1. Remove deprecated commands
2. Consolidate documentation
3. Optimize performance

---

## Next Steps

1. **Implement `/write:arc` orchestrator**
   - Parse outline into chapters
   - Generate subagent prompts
   - Spawn parallel writers
   - Aggregate results

2. **Create quality check hooks**
   - AI pattern detection script
   - Character consistency checker
   - Style matching validator

3. **Build `/write:revise` workflow**
   - Scan all chapters
   - Fix issues automatically
   - Report status

4. **Update documentation**
   - New workflow guide
   - Command reference
   - Examples

5. **Test end-to-end**
   - YOLO mode story
   - In-Depth mode story
   - Verify parallelization
   - Confirm quality checks

This redesign transforms Claudespeare from a collection of individual commands into a cohesive, automated writing system that matches the quality and UX of GSD.
