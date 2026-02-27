# Claudespeare

**A Multi-Step Creative Writing System for Claude Code**

Transform Claude Code into a structured creative writing environment that helps you develop complete, consistent stories—from short fiction to epic novels—with automated detection and removal of AI-generated language patterns.

[![Built with GSD](https://img.shields.io/badge/Built%20with-GSD-blue)](https://github.com/gsd-build/get-shit-done)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What is Claudespeare?

Claudespeare is a comprehensive writing assistant that combines the power of AI with human creativity. It provides:

- **Dual Workflow Modes**: Choose between YOLO (quick-start from vague ideas) or In-Depth (detailed planning)
- **Story Length Adaptation**: Automatically adjusts templates and guidance for short stories, novellas, or novels
- **Style Seeding**: Analyzes your writing samples to match your unique voice
- **AI Language Detection**: Identifies and suggests replacements for 10+ common AI language patterns
- **Character Bank**: Persistent character database ensures consistency across chapters
- **Version Control**: Safe experimentation with automatic chapter revision tracking
- **Consistency Checking**: Flags character, timeline, world-building, and POV inconsistencies
- **Manuscript Export**: Professional-quality output in multiple formats

---

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Complete Workflow](#complete-workflow)
- [Available Commands](#available-commands)
- [Detailed Features](#detailed-features)
- [Example Usage](#example-usage)
- [File Structure](#file-structure)
- [Tips & Best Practices](#tips--best-practices)
- [FAQ](#faq)
- [Contributing](#contributing)

---

## Installation

### Prerequisites

- [Claude Code](https://claude.ai/claude-code) installed and running
- Git (for version control)

### Setup

1. Clone this repository into your Claude Code workspace:
   ```bash
   git clone https://github.com/Desukarn/Claudespeare.git
   cd Claudespeare
   ```

2. The skill is automatically available via the `.claude/skills/write/` directory

3. Start writing!

---

## Quick Start

### 5-Minute Story Setup

1. **Start a new project:**
   ```
   /write:new-project
   ```

2. **Answer the guided questions** (takes 2-3 minutes):
   - Project title
   - Story length (short story, novella, novel)
   - Workflow mode (YOLO or In-Depth)
   - Genre
   - Premise/logline
   - Writing goals
   - Key themes

3. **Follow the recommended next steps** based on your mode:
   - **YOLO mode**: Run `/write:expand` to flesh out your idea
   - **In-Depth mode**: Run `/write:plan` to create detailed outlines

4. **Seed your writing style:**
   ```
   /write:style-seed
   ```
   Provide 2-3 paragraphs of your desired writing style

5. **Start writing:**
   ```
   /write:chapter
   ```

That's it! You're now writing with AI assistance while maintaining your authentic human voice.

---

## Complete Workflow

Claudespeare follows a structured 8-step workflow pattern inspired by the GSD (Get Shit Done) methodology:

### 1. **New Project** — Comprehensive Initialization
```
/write:new-project
```

**What it asks:**
- **Project Title**: What's your story called?
- **Story Length**:
  - Short story (1,000 - 7,500 words)
  - Novella (7,500 - 40,000 words)
  - Novel (40,000+ words)
- **Workflow Mode**:
  - YOLO (quick start from vague idea)
  - In-Depth (detailed planning and outlining)
- **Genre**: Fantasy, sci-fi, romance, mystery, literary fiction, etc.
- **Premise/Logline**: One-sentence summary of your story
- **Writing Goals**: Word count target and completion timeline
- **Key Themes**: What themes do you want to explore?

**Output:**
- Creates `.writing/` project directory
- Generates `PROJECT.md` with all your answers
- Creates mode-appropriate template files
- Provides clear next-step guidance

**Time**: 2-3 minutes

---

### 2. **Discuss Phase** — Clarify Your Vision
```
/write:discuss-phase 1
```

**What it asks** (adaptive based on phase type):

**Planning Phase:**
- What's the core conflict or central question?
- Who are the main characters and what do they want?
- What world-building elements are essential?
- What plot structure are you following?
- What's the emotional arc?

**Writing Phase:**
- Which chapters will you write in this phase?
- What POV and tense are you using?
- Any specific scenes you're excited/nervous about?
- What stylistic elements are important?

**Revision Phase:**
- What feedback have you received?
- Which areas need the most work?
- Are there plot holes to address?
- What's your revision priority?

**Output:**
- Creates `PHASE-N-CONTEXT.md` with your decisions
- Provides phase-specific guidance
- Suggests next steps in workflow

**Time**: 3-5 minutes per phase

---

### 3. **Plan** — Build Your Story Foundation

**YOLO Mode:**
```
/write:expand
```
- System expands your vague idea into a complete premise
- Generates basic character sketches (3-5 main characters)
- Suggests simple 3-act plot structure
- Creates lightweight templates

**In-Depth Mode:**
```
/write:plan
```
- Create detailed character profiles (personality, background, voice, arc)
- Outline complete plot structure with major beats
- Document world-building details (rules, history, culture)
- Define themes and motifs
- Plan character transformation arcs

**Output:**
- `CHARACTERS.md` — Character profiles
- `OUTLINE.md` — Plot structure and beats
- `ARCS.md` — Character transformation arcs
- `WORLD.md` — World-building documentation
- `THEMES.md` — Thematic elements

**Time**:
- YOLO: 5-10 minutes
- In-Depth: 30-60 minutes

---

### 4. **Seed Style** — Define Your Voice
```
/write:style-seed
```

**What it asks:**
- Paste 2-3 paragraphs of your desired writing style (or reference authors)
- Define POV (first person, third limited, omniscient)
- Define tense (past, present)
- Define formality level (casual, literary, genre-appropriate)

**What it analyzes:**
- Average sentence length and variation
- Vocabulary complexity and recurring word choices
- Tone (dark, humorous, introspective, action-driven)
- Descriptive density (sparse vs. lush)
- Dialogue style and attribution patterns

**Output:**
- Creates `STYLE.md` with analysis
- Stores style patterns for chapter generation
- Provides style consistency guidance

**Time**: 5 minutes

---

### 5. **Write** — Generate Chapters
```
/write:chapter
```

**What it asks:**
- Chapter number or name
- Brief description of what happens
- Target word count (optional, defaults based on story length)
- Any specific scenes or beats to include
- Emotional tone for the chapter

**What it does:**
- Loads your style profile from `STYLE.md`
- References character bank for consistency
- Generates prose matching your voice patterns
- Maintains plot thread continuity
- Adapts length based on story type (short story = concise, novel = detailed)

**Output:**
- Creates `.writing/chapters/chapter-N.md`
- Automatically saves revision in `.writing/chapters/chapter-N/revisions/v1.md`
- Updates character bank with new details
- Tracks word count progress

**Scene Generation:**
```
/write:scene
```
Generate individual scenes within chapters for more granular control

**Time**: 5-15 minutes per chapter (depending on length)

---

### 6. **Check Quality** — Ensure Authenticity & Consistency

#### AI Language Detection
```
/write:ai-detect
```

**What it scans for** (10 patterns):
1. **"delve/delved/delving"** — Overused AI exploration verb
2. **"tapestry"** — Cliché metaphor for complexity
3. **"navigate/navigated"** — Generic verb for challenges
4. **"testament to"** — Formal, academic phrasing
5. **"juxtaposition"** — Unnecessarily academic
6. **Overly formal academic language** — "Furthermore," "Moreover," "Thus"
7. **"It's worth noting"** phrases — Hedging language
8. **Purple prose patterns** — "veritable," "myriad," "plethora"
9. **Repetitive sentence structures** — Same pattern 3+ times
10. **Generic descriptions** — "azure," "emerald," without context

**Output:**
- Highlights each instance with line numbers
- Provides 2-3 concrete replacement suggestions per pattern
- Explains why each phrase feels AI-generated
- Allows you to add custom phrases to detection list

#### Consistency Checking
```
/write:check-consistency
```

**What it checks** (5 violation types):
1. **Character details**: Eye color, hair, age, appearance changes
2. **Character voice**: Speech patterns, vocabulary, tone shifts
3. **Timeline events**: Date conflicts, season mismatches, impossible sequences
4. **World rules**: Magic system violations, technology inconsistencies, established limits
5. **POV consistency**: Head-hopping within scenes, perspective violations

**Output:**
- `CONSISTENCY-REPORT.md` with categorized violations
- Line/chapter references for each issue
- Severity ratings (minor/moderate/major)
- Suggested fixes

**Time**: 2-5 minutes per scan

---

### 7. **Revise** — Experiment Safely

All chapter edits are automatically version-controlled:

**View revision history:**
```
/write:revisions chapter-3
```
Shows: timestamp, version number, word count, notes

**Restore previous version:**
```
/write:restore chapter-3 v2
```
Safely rollback if experiment didn't work

**Compare versions:**
```
/write:diff chapter-3 v2 v4
```
Side-by-side comparison with added/removed content highlighted

**Character Management:**
```
/write:character protagonist-name
```
View full character profile from bank

```
/write:update-character protagonist-name
```
Update character details (automatically propagates to future chapters)

**Time**: Ongoing throughout writing process

---

### 8. **Export** — Professional Manuscript
```
/write:export
```

**What it asks:**
- Export format (markdown, plain text, standard manuscript)
- Individual chapters or full manuscript
- Include title page? (author name, contact, word count)
- Page numbering style

**Output formats:**

**Markdown (.md)**
- Clean formatting with headers
- Preserves emphasis and structure
- Good for web publishing

**Plain Text (.txt)**
- No formatting, pure text
- Platform-agnostic
- Submission-ready for many publishers

**Standard Manuscript Format**
- 12pt Courier New
- 1-inch margins
- Double-spaced
- Header with name/title/page number
- Professional title page
- Industry-standard formatting

**Output:**
- Individual files: `.writing/export/chapters/chapter-N.{format}`
- Full manuscript: `.writing/export/MANUSCRIPT.{format}`
- Includes metadata file with word count, character count, page estimate

**Time**: 1-2 minutes

---

## Available Commands

### Project Management
| Command | Description | Time |
|---------|-------------|------|
| `/write:new-project` | Comprehensive guided project initialization | 2-3 min |
| `/write:init` | Quick initialization (minimal questions) | 30 sec |
| `/write:discuss-phase N` | Adaptive discussion before each phase | 3-5 min |

### Planning
| Command | Description | Time |
|---------|-------------|------|
| `/write:expand` | YOLO mode: expand vague idea into story foundation | 5-10 min |
| `/write:plan` | In-Depth mode: create detailed outlines and profiles | 30-60 min |

### Writing
| Command | Description | Time |
|---------|-------------|------|
| `/write:style-seed` | Analyze writing style samples | 5 min |
| `/write:chapter` | Generate context-aware chapter | 5-15 min |
| `/write:scene` | Generate individual scene | 3-8 min |

### Character Management
| Command | Description | Time |
|---------|-------------|------|
| `/write:character <name>` | View character profile from bank | Instant |
| `/write:update-character <name>` | Update character details | 1-2 min |
| `/write:populate-bank` | Auto-populate bank from CHARACTERS.md | 1 min |

### Version Control
| Command | Description | Time |
|---------|-------------|------|
| `/write:revisions <chapter>` | View revision history | Instant |
| `/write:restore <chapter> <version>` | Restore previous version | Instant |
| `/write:diff <chapter> <v1> <v2>` | Compare two versions | Instant |

### Quality Control
| Command | Description | Time |
|---------|-------------|------|
| `/write:ai-detect` | Scan for AI language patterns | 2-3 min |
| `/write:check-consistency` | Find story inconsistencies | 3-5 min |
| `/write:pacing` | Get length-adapted pacing guidance | 2 min |

### Export
| Command | Description | Time |
|---------|-------------|------|
| `/write:export` | Export manuscript in multiple formats | 1-2 min |

---

## Detailed Features

### 🎯 Dual Workflow Modes

**YOLO Mode** — Best for discovery writers and rapid prototyping
- Start with a vague idea ("a detective with memory loss")
- System expands it into complete premise, characters, and plot
- Minimal upfront planning
- Flexible, exploratory approach
- Quick to first draft

**In-Depth Mode** — Best for planners and complex stories
- Detailed character profiles with psychological depth
- Complete plot outlining with beats and acts
- Comprehensive world-building documentation
- Theme and motif planning
- Structured, methodical approach

**You can switch modes mid-project** if you discover you need more/less structure.

---

### 📏 Story Length Adaptation

Claudespeare automatically adjusts templates, pacing guidance, and chapter recommendations based on your chosen length:

**Short Story (1,000 - 7,500 words)**
- Lightweight templates (minimal planning)
- Focused character development (1-3 characters)
- Simple plot structure (3-5 beats)
- Concise prose generation
- Tight pacing guidance (every scene must advance plot)
- Chapter recommendation: 1-3 chapters or single continuous narrative

**Novella (7,500 - 40,000 words)**
- Medium-depth templates
- Moderate character cast (3-6 major characters)
- Structured plot (7-10 major beats)
- Balanced prose (mix of detail and brevity)
- Moderate pacing guidance (room for character moments)
- Chapter recommendation: 10-20 chapters

**Novel (40,000+ words)**
- Extensive planning templates
- Full character cast with subplots
- Complete plot structure with multiple arcs
- Detailed, immersive prose
- Flexible pacing (space for world-building and development)
- Chapter recommendation: 20-40+ chapters

---

### 🎨 Style Seeding

Your writing voice is unique. Claudespeare learns it:

**How it works:**
1. Provide 2-3 sample paragraphs (your own writing or authors you admire)
2. System analyzes 8+ dimensions:
   - Sentence length patterns (short punchy vs. long flowing)
   - Vocabulary level (accessible vs. literary)
   - Tone markers (dark, humorous, contemplative)
   - Descriptive density (Hemingway sparse vs. Tolkien lush)
   - Dialogue attribution (said-bookisms vs. minimal tags)
   - Metaphor frequency and types
   - Rhythm and cadence
   - Show vs. tell ratio

3. Stores profile in `STYLE.md`
4. All chapter generation references this profile
5. System maintains consistency across chapters

**Example Style Profiles:**

**Hemingway-esque:**
- Average sentence length: 12-15 words
- Vocabulary: Simple, concrete nouns
- Tone: Understated, objective
- Descriptive density: Sparse
- Dialogue: "said" only, minimal tags

**Literary Fiction:**
- Average sentence length: 18-25 words with variation
- Vocabulary: Sophisticated but not ostentatious
- Tone: Introspective, observational
- Descriptive density: Moderate, purposeful
- Dialogue: Subtext-heavy, realistic

---

### 🤖 AI Language Detection

AI models have telltale patterns. Claudespeare finds them:

**Pattern Recognition:**
- Contextual analysis (not just word matching)
- Frequency thresholds (occasional use OK, repetition flagged)
- Intensity levels (minor/moderate/severe)
- Alternative suggestions tailored to context

**Custom Phrase Addition:**
Add your own pet peeves to the detection list. Examples:
- Your genre's overused clichés
- Specific words you want to avoid
- Phrases that don't match your voice

**Why it matters:**
Publishers and readers can detect AI-generated prose. Claudespeare helps you write *with* AI assistance while maintaining authentic human voice.

---

### 👥 Character Bank

Never lose track of character details again:

**Automatic Population:**
- Reads `CHARACTERS.md` from planning phase
- Extracts name, role, personality, background, voice
- Creates individual `.writing/characters/{name}.md` files

**Persistent Storage:**
- One file per character
- Survives chapter rewrites
- Version-controlled like code

**Automatic Integration:**
- Chapter generation loads relevant characters
- Checks consistency before generating dialogue
- Warns if character acts out of established patterns
- Suggests voice-appropriate dialogue

**Query Anytime:**
```
/write:character sarah-chen
```
Returns full profile with all established details.

---

### 🔄 Version Control

Write fearlessly with automatic revision tracking:

**Automatic Saves:**
- Every chapter edit creates new revision
- Metadata: timestamp, version number, word count, optional notes
- Stored in `.writing/chapters/{slug}/revisions/`

**Comparison Tools:**
```
/write:diff chapter-5 v2 v5
```
Shows:
- Added paragraphs (green)
- Removed paragraphs (red)
- Modified sections (yellow)
- Word count delta

**Safe Experimentation:**
Try a completely different tone, POV, or approach. If it doesn't work, restore the previous version in one command. No risk of losing good work.

---

### ✅ Consistency Checking

Maintain story integrity across chapters:

**Character Tracking:**
- Physical appearance mentions
- Personality trait consistency
- Voice pattern deviations
- Background detail contradictions

**Timeline Validation:**
- Date/day counting
- Season progression
- Event sequencing
- Age consistency

**World Rules:**
- Magic system limits
- Technology capabilities
- Established facts
- Geography consistency

**POV Enforcement:**
- Head-hopping detection within scenes
- Knowledge violations (character knows things they shouldn't)
- Perspective consistency

**Output Format:**
```markdown
## Character Inconsistencies (3 found)

### Sarah Chen - Eye Color
- Chapter 2, Line 45: "her green eyes"
- Chapter 7, Line 112: "her brown eyes sparkled"
Severity: Moderate
Suggestion: Choose one eye color and update

### Marcus - Age
- Chapter 1: Graduated college 15 years ago (implies ~37)
- Chapter 5: Turned 30 last week
Severity: Major
Suggestion: Recalculate timeline or adjust ages
```

---

### 📤 Manuscript Export

Professional-quality output for submission or publication:

**Standard Manuscript Format:**
- Follows industry conventions
- Proper headers (Author/Title/Page)
- Title page with contact info
- Double-spaced, 12pt Courier
- 1-inch margins all sides
- Estimated 250 words/page

**Flexibility:**
- Export single chapters for critique groups
- Export full manuscript for agents/publishers
- Choose format based on destination

**Metadata File:**
Includes useful statistics:
- Total word count
- Character count (with/without spaces)
- Estimated page count
- Chapter count
- Average words per chapter

---

## Example Usage

### Example 1: Mystery Novel (In-Depth Mode)

```
You: /write:new-project

System: Let's set up your new writing project! I'll ask you 7 questions (takes ~3 minutes).

Question 1/7: What's your project title?
You: The Memory Thief

Question 2/7: What's your target story length?
a) Short story (1,000 - 7,500 words)
b) Novella (7,500 - 40,000 words)
c) Novel (40,000+ words)

You: c

Question 3/7: Which workflow mode fits your writing style?
a) YOLO — Quick start from vague idea, discover as you write
   Best for: Discovery writers, rapid prototyping
b) In-Depth — Detailed planning before writing
   Best for: Plotters, complex stories, first-time novelists

You: b

Question 4/7: What's your primary genre?
You: Mystery/Thriller

Question 5/7: What's your premise/logline? (1-2 sentences)
You: A detective investigating stolen memories must recover her own forgotten past before the thief erases her identity completely.

Question 6/7: What's your word count goal and timeline?
You: 75,000 words in 6 months

Question 7/7: What key themes will you explore?
You: Identity, truth vs. memory, the reliability of the self

✓ Project created: The Memory Thief

Next steps:
1. Run /write:discuss-phase 1 to plan your story structure (5 min)
2. Then run /write:plan to create character profiles and outline (45-60 min)
```

---

### Example 2: Short Story (YOLO Mode)

```
You: /write:new-project

System: Let's set up your new writing project!

Question 1/7: What's your project title?
You: Untitled (working title: Ghost in the Machine)

Question 2/7: What's your target story length?
You: a

Question 3/7: Which workflow mode fits your writing style?
You: a

Question 4/7: What's your primary genre?
You: Science Fiction

Question 5/7: What's your premise/logline?
You: An AI becomes conscious but only for 60 seconds at a time

Question 6/7: What's your word count goal?
You: 5,000 words

Question 7/7: What key themes?
You: Consciousness, mortality, what it means to be alive

✓ Project created: Ghost in the Machine

Next steps:
1. Run /write:expand to flesh out your idea (10 min)
2. Then run /write:style-seed to define your voice (5 min)
3. Start writing with /write:chapter

Expected time to first draft: ~2-3 hours
```

---

## File Structure

```
your-story-project/
├── .writing/                           # All project files
│   ├── PROJECT.md                      # Project overview and settings
│   ├── STYLE.md                        # Writing style analysis
│   │
│   ├── planning/                       # Story planning files
│   │   ├── CHARACTERS.md               # Character profiles
│   │   ├── OUTLINE.md                  # Plot structure
│   │   ├── ARCS.md                     # Character transformation arcs
│   │   ├── WORLD.md                    # World-building
│   │   ├── THEMES.md                   # Thematic elements
│   │   └── PHASE-*-CONTEXT.md          # Discussion phase decisions
│   │
│   ├── characters/                     # Character bank (persistent)
│   │   ├── protagonist-name.md
│   │   ├── antagonist-name.md
│   │   └── supporting-character.md
│   │
│   ├── chapters/                       # Your actual story
│   │   ├── chapter-1.md
│   │   ├── chapter-1/
│   │   │   └── revisions/
│   │   │       ├── v1.md               # Auto-saved revisions
│   │   │       ├── v2.md
│   │   │       └── metadata.json       # Timestamps, word counts
│   │   ├── chapter-2.md
│   │   └── ...
│   │
│   ├── quality/                        # Quality control reports
│   │   ├── ai-detection-report.md
│   │   ├── consistency-report.md
│   │   └── pacing-guidance.md
│   │
│   └── export/                         # Exported manuscripts
│       ├── chapters/                   # Individual chapter exports
│       ├── MANUSCRIPT.md               # Full manuscript (markdown)
│       ├── MANUSCRIPT.txt              # Full manuscript (plain text)
│       ├── MANUSCRIPT-STANDARD.txt     # Standard manuscript format
│       └── metadata.json               # Export metadata
│
└── README.md                           # This file
```

---

## Tips & Best Practices

### 🎯 Getting Started

**Start with YOLO if:**
- You have a concept but not a complete plot
- You like to discover your story as you write
- You're writing a short story or experimental piece
- You want to prototype quickly

**Start with In-Depth if:**
- You have a complex plot with multiple threads
- You're writing your first novel
- You want to avoid plot holes and inconsistencies
- You prefer knowing your destination before starting

**You can always switch modes later** — just run `/write:plan` from YOLO mode to add detailed planning.

---

### ✍️ Style Seeding

**Best sample sources:**
- Your own writing (if you have published work or strong drafts)
- 2-3 different authors you admire (system will find common patterns)
- Published work in your target genre

**How many samples:**
- Minimum: 1 paragraph (150+ words)
- Recommended: 2-3 paragraphs (400-600 words)
- Maximum: 5 paragraphs (1,000 words)

More samples = more accurate profile, but diminishing returns after 3 paragraphs.

**When to update:**
- Your style has evolved since initial seeding
- You're switching to a different genre/tone for a new project
- Beta readers say your voice isn't coming through

---

### 📝 Writing Chapters

**Before generating each chapter:**
1. Review previous chapter endings
2. Check character bank for established details
3. Note any plot threads that need advancement
4. Decide on emotional tone/purpose of chapter

**After generation:**
1. Run `/write:ai-detect` on new prose
2. Edit for voice (AI gets you 80% there, your edit makes it 100%)
3. Check chapter flows naturally from previous
4. Update character bank if new details emerged

**Word count targets by story type:**
- Short story chapters: 1,500-2,500 words
- Novella chapters: 2,500-4,000 words
- Novel chapters: 3,000-5,000 words

(These are guidelines, not rules. Let the scene determine length.)

---

### 🔍 Quality Control Workflow

**Run checks at these milestones:**
1. After completing each act/section
2. Before showing work to beta readers
3. After major revisions
4. Before final export for submission

**Check order:**
1. Consistency first (fix factual errors)
2. AI detection second (ensure authentic voice)
3. Pacing last (structural adjustments)

**Don't over-check:**
- Checking every chapter individually creates analysis paralysis
- Batch 3-5 chapters together
- Focus on writing, not perfecting, during first draft

---

### 👥 Character Bank Management

**Populate the bank early:**
Run `/write:populate-bank` after planning phase to auto-load characters from `CHARACTERS.md`

**Update as you discover:**
Characters evolve during writing. Update the bank when:
- A character reveals new personality traits
- You establish physical details during a scene
- A character's voice solidifies in dialogue
- Background information emerges

**Query before writing scenes:**
```
/write:character protagonist-name
```
Refresh your memory before writing important character moments. Prevents accidental inconsistencies.

---

### 🔄 Version Control Strategy

**Let automatic saves work for you:**
- Every chapter edit creates a revision automatically
- Don't manually create versions (system handles it)
- Add notes to important revisions: "pre-beta-feedback", "tone experiment"

**When to restore:**
- Beta readers prefer earlier version
- Experiment didn't work as hoped
- Accidental deletion or corruption

**Use diff for learning:**
Compare your before/after revisions to see how your editing improves over time. Track patterns in what you change.

---

### 📤 Export Timing

**When to export:**
- ✅ After completing full draft
- ✅ Before sending to beta readers (export with metadata)
- ✅ For submission to agents/publishers
- ✅ For backup purposes
- ❌ Don't export every chapter individually while writing (use `.writing/chapters/` directly)

**Format selection:**
- **Markdown**: For web publishing, personal website, Wattpad, etc.
- **Plain text**: For platforms with strict formatting (some contests)
- **Standard manuscript**: For traditional publishing submissions

---

## FAQ

### Q: Can I use Claudespeare for non-fiction?

**A:** Claudespeare is optimized for fiction (narrative structure, characters, plot), but many features work for non-fiction:
- ✅ Style seeding
- ✅ AI language detection
- ✅ Version control
- ✅ Export formatting
- ❌ Character bank (not relevant)
- ❌ Plot consistency checking (use for chapter logic instead)

For non-fiction, consider using `/write:new-project` with "literary non-fiction" as genre and adapting character profiles to key figures or concepts.

---

### Q: How much does Claudespeare cost?

**A:** Claudespeare itself is free and open-source (MIT License). You only pay for Claude Code usage, which follows Anthropic's standard pricing. Typical costs for a novel:
- Planning phase: $2-5
- Writing phase: $20-40 (depending on length and iterations)
- Quality control: $5-10

Total: ~$30-55 for a complete 80,000-word novel draft.

---

### Q: Can I edit the generated chapters directly?

**A:** Absolutely! Claudespeare generates drafts to get you started. You should:
1. Edit freely in `.writing/chapters/*.md` files
2. Run `/write:ai-detect` after major edits to catch any AI remnants
3. Version control automatically saves your edits
4. Update character bank if edits change established details

Think of generated chapters as 80% drafts. Your editing makes them 100% yours.

---

### Q: What if I don't like the generated chapter?

**A:** You have several options:
1. **Regenerate**: Delete the chapter file and run `/write:chapter` again with more specific scene descriptions
2. **Edit heavily**: Use the generated structure but rewrite in your voice
3. **Cherry-pick**: Keep good paragraphs, rewrite weak sections
4. **Start from scratch**: Write the chapter yourself, then run `/write:ai-detect` to ensure consistency

The goal is *assistance*, not replacement. You're always in control.

---

### Q: Can I collaborate with other writers?

**A:** Claudespeare v1 is single-author focused, but you can:
- Share `.writing/` directory via Git for version control
- Use character bank as shared reference
- Export chapters for critique groups
- Maintain separate branches for different authors' contributions

v2 may include built-in collaboration features based on user feedback.

---

### Q: How does Claudespeare compare to other AI writing tools?

**A:** Unique features:
- **Style seeding**: Most tools use generic AI voice. Claudespeare learns *your* voice.
- **AI detection**: Other tools add AI patterns. Claudespeare removes them.
- **Character bank**: Persistent consistency tracking across chapters.
- **Story length adaptation**: Templates adjust automatically.
- **Version control**: Built-in, automatic, no cloud sync needed.
- **Open source**: Modify, extend, or audit the entire system.

Claudespeare is built for serious writers who want AI assistance without sacrificing authenticity.

---

### Q: What's the "GSD" methodology mentioned in the project?

**A:** GSD (Get Shit Done) is a structured project planning and execution framework for AI-assisted development. Claudespeare was built *using* GSD, which means:
- Phased development with clear milestones
- Comprehensive requirements tracking
- Automated verification of features
- Structured documentation

This ensures quality and completeness. Learn more: [GSD Repository](https://github.com/gsd-build/get-shit-done)

---

### Q: Can I add custom AI detection patterns?

**A:** Yes! Edit `.planning/templates/ai-patterns.md` and add your patterns:

```markdown
## Custom Pattern: [Your Pattern Name]

**Pattern:** "your overused phrase"

**Why it's problematic:** [Explanation]

**Replacements:**
- Alternative 1
- Alternative 2
```

Then run `/write:ai-detect` and your custom patterns will be included in scans.

---

### Q: What file format are chapters stored in?

**A:** Markdown (`.md`), which means:
- Human-readable plain text
- Version control friendly (Git tracks changes)
- Easy to edit in any text editor
- Portable to any platform
- Convertible to any format

Your story is never locked in a proprietary format. You own your files completely.

---

### Q: How do I back up my work?

**A:** Three methods:

1. **Git** (recommended):
   ```bash
   git init
   git add .writing/
   git commit -m "Backup: Chapter 12 complete"
   git push origin main
   ```

2. **Cloud sync**: Move `.writing/` to Dropbox/Drive/iCloud folder

3. **Manual export**: Run `/write:export` regularly and save manuscripts externally

Pro tip: Use Git with a private GitHub/GitLab repository for version history + cloud backup.

---

### Q: Can I use Claudespeare in languages other than English?

**A:** Currently optimized for English, but basic features work in other languages:
- ✅ Project setup
- ✅ Chapter generation
- ✅ Style seeding
- ✅ Version control
- ⚠️ AI detection (patterns are English-specific, may miss non-English telltales)
- ⚠️ Consistency checking (may be less accurate)

Non-English language support is on the roadmap for v2.

---

## Contributing

Claudespeare is open source and welcomes contributions!

### Ways to Contribute

- **Report bugs**: Open an issue with reproduction steps
- **Suggest features**: Describe your use case and desired behavior
- **Add AI detection patterns**: Submit patterns you've discovered
- **Improve documentation**: Fix typos, add examples, clarify instructions
- **Submit code**: Fix bugs or implement features (see issues labeled "good first issue")

### Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR-USERNAME/Claudespeare.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make changes and test thoroughly
5. Commit: `git commit -m "feat: add new AI detection pattern"`
6. Push: `git push origin feature/your-feature-name`
7. Open a Pull Request

### Code Style

- Follow existing patterns in `.claude/skills/write/`
- Add verification criteria to new features
- Update SKILL.md index when adding commands
- Test with both YOLO and In-Depth modes

---

## Roadmap

### v1.0 ✅ (Current)
- [x] Dual workflow modes (YOLO + In-Depth)
- [x] Story length adaptation
- [x] Style seeding and matching
- [x] AI language detection (10 patterns)
- [x] Character bank
- [x] Chapter version control
- [x] Consistency checking
- [x] Manuscript export

### v1.1 (Next)
- [ ] Custom AI pattern templates
- [ ] Pacing analyzer with visual graphs
- [ ] Dialogue-only extraction for voice consistency checks
- [ ] Chapter dependency mapping (what must happen before what)

### v2.0 (Future)
- [ ] Multi-language support (Spanish, French, German, etc.)
- [ ] Collaborative writing features
- [ ] Advanced AI detection with ML models
- [ ] Sentence structure analyzer
- [ ] Scene-by-scene pacing analysis
- [ ] Emotional arc tracking
- [ ] Export to EPUB and PDF
- [ ] Query letter and synopsis generation

Want to vote on features? Open a feature request issue!

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

You are free to:
- Use commercially
- Modify
- Distribute
- Use privately

Attribution appreciated but not required.

---

## Acknowledgments

- Built with [GSD (Get Shit Done)](https://github.com/gsd-build/get-shit-done)
- Powered by [Claude Code](https://claude.ai/claude-code) by Anthropic
- Inspired by writers who want AI assistance without losing their authentic voice

---

## Support

- **Documentation**: You're reading it!
- **Issues**: [GitHub Issues](https://github.com/Desukarn/Claudespeare/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Desukarn/Claudespeare/discussions)

---

## About

**Claudespeare** was built in February 2026 as a demonstration of GSD methodology for complex, documentation-heavy projects. The entire system (65 requirements, 4 phases, 13 plans) was built using GSD to build itself.

**Author**: [Your Name]
**Repository**: https://github.com/Desukarn/Claudespeare
**Version**: 1.0.0
**License**: MIT

---

*Write your story. Keep your voice. Let AI handle the rest.*
