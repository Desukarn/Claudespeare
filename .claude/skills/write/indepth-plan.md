# In-Depth Planning: Comprehensive Story Development

Guide writers through detailed story development with comprehensive planning for characters, plot, world, arcs, and themes.

## What this does

For writers who benefit from thorough upfront planning, this workflow:
1. Validates project is in In-Depth mode
2. Guides through detailed character development
3. Structures full plot with major beats and subplots
4. Facilitates character arc planning
5. Documents world-building details
6. Captures themes and motifs
7. Adapts template depth based on story length (short story → novel)

## When to use

Run this after `/write:init` creates an In-Depth mode project. This comprehensive planning takes 30-60 minutes but builds a solid foundation for complex narratives.

## Workflow

### Step 1: Entry Validation

Check PROJECT.md frontmatter for mode:

```bash
MODE=$(grep "^mode:" stories/{slug}/PROJECT.md | cut -d: -f2 | tr -d ' ')

if [ "$MODE" != "indepth" ]; then
  echo "Error: This project is in $MODE mode."
  echo "For YOLO quick-start planning, use /write:expand instead."
  exit 1
fi

# Also read story length for template depth
LENGTH=$(grep "^length:" stories/{slug}/PROJECT.md | cut -d: -f2 | tr -d ' ')
```

### Step 2: Trope Inspiration Research (ANTI-SLOP)

**CRITICAL**: Before planning, research fresh tropes to avoid cookie-cutter plots.

See `trope-inspiration-system.md` for full details.

**Prompt user**:
```
Would you like me to research story tropes for fresh inspiration?

This takes 2-3 minutes but helps avoid common AI plot patterns like:
- "Strength becomes weakness"
- "Final moral act"
- "Power corrupts protagonist"
- Standard chosen one narratives

I'll browse TVTropes.org to find unexpected angle combinations for your story.

A. Yes - Research tropes (recommended)
B. No - Skip and plan directly
```

**If YES**: Launch trope research agent (Task tool with prompt from trope-inspiration-system.md)

**Agent returns 8-10 trope suggestions**. Present to user, user selects 2-3.

**Store selected tropes** in PROJECT.md:
```yaml
inspiration_tropes:
  - "Earn Your Bad Ending"
  - "Blue-and-Orange Morality"
  - "Wrong Genre Savvy"
```

**Reference these during planning** to avoid formulaic choices.

---

### Step 3: Planning Phase Overview

Explain the process to the writer:

```
In-Depth Planning Workflow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

We'll create detailed planning documents for your story across six areas:

0. Trope Inspiration - Fresh angles to avoid clichés (completed above)
1. Characters - Detailed profiles, backgrounds, goals, conflicts
2. Plot - Three-act structure with major beats and subplots
3. Character Arcs - Transformation tracking from start to end
4. World-Building - Setting, rules, culture, consistency
5. Themes - Core themes, voice, style decisions

Estimated time: 30-60 minutes
Story length: {LENGTH}
Template depth: {Novel = extensive | Novella = moderate | Short story = focused}

This planning builds a foundation for complex narratives. I'll prompt you
through each area. You can skip optional sections, but comprehensive planning
pays off during drafting.

Ready to begin? Let's start with characters.
```

### Step 3: Character Development (STORY-01)

Prompt for number of main characters:
- Typical: 2-4 for most stories
- Novels can have more, short stories usually 2-3

For each character, prompt through the following:

#### Name

**CRITICAL REQUIREMENT**: Use online name generator - see `name-generator-requirement.md`

**NEVER generate names directly**. AI models have strong biases toward names like "Kael", "Elara", "Lyra", "Aria" etc. These are AI slop.

**Workflow**:
1. Ask user for character context: "Tell me about this character (genre, culture/ethnicity, role, time period)"
2. Based on context, choose appropriate generator:
   - Fantasy: https://www.fantasynamegenerators.com/
   - Historical/Modern: https://www.behindthename.com/random/
   - Sci-Fi: https://www.fantasynamegenerators.com/sci-fi-names.php
3. Use WebFetch to get 8-10 authentic name options
4. Present options to user:
   ```
   Here are 8 authentic [context] names from [generator]:

   1. [Name]
   2. [Name]
   3. [Name]
   4. [Name]
   5. [Name]
   6. [Name]
   7. [Name]
   8. [Name]

   Pick a number (1-8), ask for more options, or provide your own name.
   ```
5. User selects or requests regeneration

**If user provides their own name**: Accept it (bypasses generator requirement)

#### Role
"What's their role in the story?"
- Protagonist (main character)
- Antagonist (opposing force)
- Supporting (ally, mentor, love interest, etc.)

#### Age and Occupation
"How old are they? What do they do?"

This grounds the character in concrete details.

#### Personality Traits (3-5)
"Describe their personality in 3-5 traits."

Show examples:
- "Determined but reckless"
- "Brilliant but socially awkward"
- "Loyal but naive"
- "Cynical from past betrayals"
- "Optimistic despite hardship"

Mix strengths and flaws for dimensional characters.

#### Background
"What's their background? What shaped who they are?"

Prompt for:
- Upbringing (family, environment)
- Formative events (trauma, triumph, loss, discovery)
- Why they're in this story at this time

2-4 paragraphs for protagonists, 1-2 for supporting characters.

#### Sanderson Character Triangle Assessment (Protagonist Only)

**CRITICAL**: For protagonist, assess the Character Triangle from Sanderson's frameworks.

See `.claude/skills/sanderson-2025/proactive-relatable-capable.md` for full details.

Ask: "Let's assess your protagonist using Sanderson's Character Triangle. This ensures they're engaging and avoid 'boring protagonist' syndrome."

**The Three Pillars:**

**1. PROACTIVE (Agency)**
"On a scale of 1-10, how proactive is this character?"
- 1-3: Passive, reactive, things happen TO them
- 4-7: Mix of proactive and reactive
- 8-10: Highly proactive, drives the plot

**Goal: 6+ for protagonists**

If below 6, prompt: "How can we make them more proactive? What can they actively pursue rather than just react to?"

**2. RELATABLE (Empathy)**
"What makes readers connect with this character?"
- Flaws they recognize
- Struggles they understand
- Emotions they share
- Humor, vulnerability, or humanity

List 2-3 relatable elements. These create emotional investment.

**3. CAPABLE (Competence)**
"What is this character good at? What's their area of expertise?"
- Skills they possess
- Knowledge they have
- Talents that make them interesting
- How they solve problems uniquely

**Note from Sanderson**: "You can drop one pillar, but NEVER two."
- Proactive + Capable but not Relatable = Cold, hard to root for
- Proactive + Relatable but not Capable = Frustrating, incompetent
- Relatable + Capable but not Proactive = Boring, passive protagonist

**Assessment Result:**
Record triangle strength:
```
Proactive: __/10
Relatable: __/10 (list elements)
Capable: __/10 (list competencies)

Assessment: [Strong on all three / Strong on two / Needs work]
```

If weak on multiple pillars, prompt: "Let's strengthen [pillar]. How can we adjust the character to improve this?"

#### External Goal
"What do they want in this story? What are they trying to achieve?"

This is their conscious, stated objective:
- Solve the murder
- Win the competition
- Find the lost artifact
- Overthrow the tyrant

Be specific and active.

#### Internal Goal
"What do they need to learn or overcome internally?"

This is their unconscious need - the character arc driver:
- Learn to trust others
- Overcome fear of failure
- Accept their identity
- Forgive themselves

Often conflicts with or complicates external goal.

#### Conflicts
"What internal and external conflicts do they face?"

**Internal:** Fears, doubts, contradictions, wounds
**External:** Antagonists, obstacles, competing loyalties

#### Voice and Speech Patterns
"How do they speak? What's distinctive about their voice?"

Examples:
- "Formal and scholarly, uses precise language"
- "Speaks in clipped military phrases"
- "Uses humor to deflect emotional topics"
- "Rambles when nervous, confident when focused"

This helps maintain consistent character voice in dialogue.

#### Physical Description
"Describe their appearance - key traits readers should picture."

Focus on:
- Most distinctive features (not exhaustive catalogs)
- Details that reflect personality or role
- 2-3 memorable specifics

**Length-aware character depth:**
- **Short story:** 2-3 characters max, focus on essentials only
- **Novella:** 3-4 characters, moderate detail
- **Novel:** 4+ characters, full detail with relationships section

#### Repeat for Each Character

After gathering all characters, generate `stories/{slug}/CHARACTERS.md` from template `.planning/templates/characters.md`

**For novel-length:** Include all sections including relationships map
**For shorter lengths:** Exclude LENGTH:novel marked sections

### Step 4: Plot Structure (STORY-02)

Guide through three-act structure with Sanderson framework integration:

```
Plot Structure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

We'll map your story using three-act structure enhanced with Sanderson's
Promise-Progress-Payoff framework. This ensures engaging narrative momentum.

Reference: .claude/skills/sanderson-2025/promise-progress-payoff.md
```

#### Major Dramatic Question (MDQ) - CRITICAL FIRST STEP

**Before outlining acts, define the central question.**

See `.claude/skills/sanderson-2025/promise-progress-payoff.md` section on Major Dramatic Question.

Ask: "What is your story's Major Dramatic Question? This is the ONE central question that drives reader investment."

**Examples:**
- Will Luke become a Jedi and defeat the Empire?
- Will Elizabeth and Darcy overcome their pride and prejudice?
- Will Katniss survive the Hunger Games?
- Will Frodo destroy the Ring and save Middle-earth?

**Template:**
```
Will [protagonist] [achieve goal] despite [obstacle]?
```

**Requirements:**
- Must be clear by end of Act One
- Must be answered in the climax
- Unifies all subplots around central conflict
- One primary question (can have sub-questions)

**Record MDQ:**
```
Major Dramatic Question: _______________________
When established: (Must be by Act One end)
How climax answers it: _______________________
```

If user struggles, help them identify it from their premise and character goals.

#### Act 1: Setup (First 25%)

**Opening Scene:**
"How does your story begin?"
- Where are we?
- Who do we meet?
- What's the normal world before disruption?

Prompt for 2-3 sentences describing the opening.

**Inciting Incident:**
"What event disrupts the normal world and sets the story in motion?"
- The murder that must be solved
- The invitation to adventure
- The threat that appears
- The discovery that changes everything

Be specific about the moment things change.

**First Plot Point / Commitment:**
"What locks your protagonist into this journey? When do they commit?"
- Accepting the quest
- Crossing the threshold
- Point of no return

End of Act 1: protagonist is committed to the journey.

**Key Scenes in Act 1 (3-5 scenes):**
"What are the major scenes between opening and commitment?"

For each scene:
- Brief description (1-2 sentences)
- Purpose (what it establishes or advances)

#### Act 2: Confrontation (Middle 50%)

**Sanderson Progress Signposting Plan:**

**CRITICAL**: Act 2 must maintain forward momentum or readers drop the book.

See `.claude/skills/sanderson-2025/promise-progress-payoff.md` section on Progress Tracking.

Ask: "Act 2 is where stories often stall. Let's plan progress signposts - breadcrumbs showing readers the story is moving forward."

**What type of progress drives your story?**
- Information-Based (Mystery/Thriller): Clues discovered, suspects eliminated
- Relationship Progress (Romance/Drama): Connection moments alternating with setbacks
- Character Internal (Literary): Beliefs questioned, skills developing
- Plot/Action (Adventure/Epic): Quests advancing, geography traversed, obstacles overcome

User selects primary type(s).

**Yes-But / No-And Scene Pattern:**

Explain escalation technique: "Every scene in Act 2 should either be YES, BUT or NO, AND."

**YES, BUT**: Character achieves goal BUT complications arise
- Example: "Hero steals artifact (YES) BUT triggers alarm (complication)"

**NO, AND**: Character fails AND circumstances worsen
- Example: "Guards catch hero (NO) AND artifact is cursed (worsens)"

**Pattern for Act 2:**
- Early Act 2: More YES, BUT (victories with complications)
- Mid Act 2: Mix of both
- Late Act 2: More NO, AND (failures that compound)
- Creates natural escalation toward darkest moment

**Try-Fail Cycle Structure:**

Explain Sanderson's structural pattern: "Your protagonist will likely try and fail multiple times before succeeding."

**Cycle:**
1. **First Attempt**: Obvious solution → FAILS
   - Reveals: Problem harder than expected
   - Stakes: Protagonist underestimated challenge

2. **Second Attempt**: More sophisticated approach → FAILS
   - Reveals: Internal flaws or deeper complications
   - Stakes: Character must grow to succeed

3. **Third Attempt**: Succeeds after growth/transformation
   - Reveals: Character has truly changed
   - Stakes: Victory feels earned

Ask: "What will your protagonist try? What will fail? How will they grow?"

Record try-fail cycles in outline.

**Rising Action / Complications:**
"What obstacles and complications does your protagonist face?"

Prompt for 4-6 major complications (more for novels, fewer for short stories):
- New obstacles that escalate conflict (using Yes-But/No-And)
- Relationships that develop or break
- Skills or knowledge protagonist must gain (Try-Fail learning)
- Failures and setbacks (each revealing new information)
- Subplots that interweave

**Midpoint:**
"What's the major twist or shift at the story's center?"

Common midpoint types:
- False victory (seems to win, but it's temporary)
- Major revelation (new information changes everything)
- Commitment deepens (raise stakes, can't back out now)
- Mirror moment (protagonist sees themselves clearly)

2-3 sentences describing the midpoint event.

**Subplots (for novels):**
"What subplots develop alongside the main plot?"

For novel-length stories, prompt for 2-4 subplots:
- Relationship subplot (romance, friendship, rivalry)
- Mystery subplot (something to uncover)
- Character subplot (secondary character's journey)
- Thematic subplot (explores theme from different angle)

For each subplot:
- Brief description
- How it intersects with main plot
- Resolution point

**Skip subplot section for short stories** (LENGTH:novel marker)

**Second Plot Point / Crisis:**
"What's the darkest moment? When does everything seem lost?"
- Protagonist's plan fails
- Ally betrays or is lost
- Truth revealed that shatters assumptions
- Defeat seems certain

End of Act 2: protagonist faces their greatest challenge.

**Key Scenes in Act 2 (6-10 scenes for novel, 4-6 for novella, 3-4 for short story):**
"What are the major scenes in this act?"

Length-aware prompting:
- Novel: detailed scene list with purpose for each
- Novella/Short story: major beats only

#### Act 3: Resolution (Final 25%)

**Sanderson Payoff Design:**

**CRITICAL**: Payoff must be "surprising yet inevitable."

See `.claude/skills/sanderson-2025/promise-progress-payoff.md` section on Payoff Delivery.

Ask: "Your climax must answer the Major Dramatic Question in a way that's both unexpected and feels earned. Let's design that payoff."

**Payoff Approach Options:**

**1. Straightforward Payoff** (Pride and Prejudice style)
- Promise: Characters will marry (or achieve goal)
- Sophistication: Complications make path difficult
- Payoff: Delivers exactly what promised, but journey makes it satisfying

**2. Twist Payoff** (While You Were Sleeping style)
- Initial Promise: One outcome seems certain
- Redirection: Gradually shift expectations toward different outcome
- Payoff: Deliver the redirected outcome (feels right in hindsight)

**3. Gandalf Promise / Dark-Then-Light** (Lord of the Rings style)
- Promise: Made early, specific ("dawn of the fifth day")
- Darkness: Escalate so darkly the promise is overshadowed/forgotten
- Payoff: Deliver on promise precisely when hope seems lost
- Effect: "When sun comes out, you're cheering"

User selects approach or describes their vision.

**Payoff Design Questions:**

Prompt for:
- **What's at stake?** (Must be highest stakes of entire story)
- **What choice must protagonist make?** (Reflects character growth)
- **How do earlier skills/knowledge pay off?** (Checklist of setups to pay off)
- **What's the moment of maximum tension?**
- **How does this answer the Major Dramatic Question?** (MUST answer MDQ)
- **What's the surprising element?** (Unexpected twist or angle)
- **What's the inevitable element?** (Foreshadowing that makes it feel "of course!")

**Payoff Checklist:**
```
[  ] Answers Major Dramatic Question
[  ] Uses only elements established earlier (no deus ex machina)
[  ] Both surprising AND inevitable
[  ] Emotional satisfaction matches promise
[  ] Protagonist has grown enough to earn this victory
```

**Climax Description:**

3-5 sentences describing the climax, incorporating payoff design.

**Resolution:**
"How does the story end? What's the new normal?"
- How is conflict resolved?
- What's changed?
- How is character growth demonstrated?
- What's the final image or moment?

2-3 sentences for resolution.

**Denouement (optional for longer stories):**
"What happens after climax? How does world settle?"

This is the "tying up loose ends" section - more important for novels.

#### Generate Outline

Write to `stories/{slug}/OUTLINE.md` from template `.planning/templates/outline.md`

Process LENGTH:novel markers:
- **Novel:** Include subplots, detailed scene lists, pacing notes
- **Shorter:** Core three-act structure only

### Step 5: Character Arcs (STORY-03)

For each main character (especially protagonist and antagonist):

```
Character Arcs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Now we'll track how your characters transform through the story.
```

#### For Each Character:

**Starting State:**
"At the story's beginning, what does {character} believe? What are their flaws?"
- Core belief that will be challenged
- Flaw or wound that holds them back
- False belief about themselves or world

**Arc Type:**
"What type of arc do they follow?"
- Positive change (overcome flaw, grow, transform)
- Flat arc (already complete, changes world around them)
- Negative arc (corruption, decline, tragic fall)
- Disillusionment (lose innocence or idealism)

**Growth Moments (3-5 for short stories, 5+ for novels):**
"What are the key moments where this character is tested or learns?"

For each growth moment:
- What happens (event or scene)
- What they learn (realization or new understanding)
- How they change (behavior or belief shift)

Length-aware:
- Novel: 5-7 growth moments with detailed tracking
- Novella: 4-5 growth moments
- Short story: 3 key moments

**Ending State:**
"By the story's end, what has {character} become?"
- New belief or understanding
- Flaw overcome (or deepened if negative arc)
- Growth demonstrated

#### Generate Arcs Document

Write to `stories/{slug}/ARCS.md` from template `.planning/templates/arcs.md`

Process LENGTH:novel markers:
- **Novel:** Full arc tracking with 5+ growth moments
- **Shorter:** Simplified arc with 3 moments

### Step 6: World-Building (STORY-04)

Depth varies significantly by genre and length:

```
World-Building
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Let's document your story's setting and world details.
The depth here depends on your genre and story length.

For contemporary/realistic: Setting and cultural details
For fantasy/sci-fi: Full world rules and systems
```

#### Setting
"Where and when does your story take place?"

**Time:**
- Historical period / year
- Season or time of year
- Duration of story events

**Location:**
- Primary location(s)
- Geographic scope (single city, kingdom, galaxy?)
- Atmosphere and mood of places

2-4 paragraphs describing the setting.

#### World Rules (for fantasy/sci-fi)
"What are the rules of your world? What's possible?"

**Magic or Technology System:**
- How does it work?
- What are its limitations?
- What's the cost of using it?
- Who can access it?

**Physical Laws:**
- Different from our world?
- Important constraints?

Skip this section for contemporary/realistic fiction.

#### Social Structure
"How is society organized in your world?"

- Governance (government, power structures)
- Social classes or hierarchies
- Key institutions
- Power dynamics

Depth varies by genre:
- Fantasy/Sci-fi: Often crucial to plot
- Contemporary: May be minimal

#### Culture (LENGTH:novel for extensive detail)
"What cultural details matter for your story?"

**Values and Beliefs:**
- What does society value?
- Taboos or forbidden things
- Customs and traditions
- Religion or philosophy

**Language:**
- Naming conventions
- Important phrases or slang
- Communication norms

This section more relevant for novels and genre fiction.

#### Geography and Place Naming (LENGTH:novel for detailed maps)
"What are the key locations we'll visit?"

**CRITICAL: Place Naming Anti-Slop**

Before documenting locations, generate authentic place names using the same anti-AI-slop standards as character names.

See `name-generator-requirement.md` Part 2 for full place naming system.

**Workflow:**

1. **Determine naming scope:**
   ```
   How many locations need names?
   - Major cities/towns: [X]
   - Regions/kingdoms: [X]
   - Geographic features (mountains, rivers, forests): [X]
   ```

2. **Choose naming method:**
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
   ```

3. **Generate place names:**

   **For Cultural Patterns (A-G):**
   - Research appropriate suffixes and roots for chosen culture
   - Germanic: -heim (home), -burg (fortress), -wald (forest), -stadt (city)
   - Celtic: -dun (fort), -ton (settlement), -bry (hill), -mor (great)
   - Arabic: -abad (city), -dar (house), al- prefix (the)
   - etc.
   - Generate 8-10 options per location type
   - Present to user with cultural context

   **For Wikipedia Method (H):**
   - Use Bash to fetch 10 random Wikipedia articles
   - Extract evocative terms, syllables, place names
   - Adapt into 8-10 fantasy place names
   - Example: "Hastings" → "Hastinmere", "Byzantine" → "Byzara"
   - Present to user with etymology notes

4. **Verify anti-slop:**
   - ❌ BANNED: Shadowmere, Darkwood, Stormkeep
   - ❌ Pattern: [Color] + [Generic Noun]
   - ❌ Pattern: [Adjective] + [Common Noun]
   - ✅ Culturally consistent
   - ✅ Pronounceable
   - ✅ Memorable

5. **Generate minor character name pools:**

   While researching place names, also generate name pools for minor characters.

   For each culture in the story:
   - Use WebFetch with Behind the Name (cultural filter)
   - Generate 30 male names, 30 female names, 20 surnames
   - Store in CHARACTERS.md under "Name Pools for Minor Characters"

   This prevents AI slop names for guards, shopkeepers, servants, etc.

**Then document each important location (2-6 depending on length):**
- Name (researched, not AI-generated) and description
- Significance to story
- Who inhabits or controls it
- Atmosphere and sensory details

**Add to WORLD.md:**
```markdown
## Naming Conventions

All places in [region] follow [culture] patterns:
- Suffixes: [list]
- Phonetic style: [description]
- Examples: [established names]

When introducing new locations during writing, maintain this pattern.
```

#### History (LENGTH:novel)
"What historical events shaped this world?"

Timeline of 3-6 major events:
- What happened
- When
- How it affects the current story

More important for novels and secondary world fantasy.

#### Consistency Tracking (LENGTH:novel)
This section starts empty - fill during drafting to track:
- Place names and spellings
- Distance and travel times
- Technology or magic limitations
- Cultural details mentioned

#### Generate World Document

Write to `stories/{slug}/WORLD.md` from template `.planning/templates/world.md`

Process LENGTH:novel markers:
- **Novel:** Comprehensive world-building with history, culture, consistency tracking
- **Novella:** Moderate detail on essentials
- **Short story:** Basic setting and world rules only

### Step 7: Themes and Motifs (STORY-05)

Update PROJECT.md with thematic elements:

"Let's capture the deeper elements of your story."

**Core Themes (3-5):**
"What themes does your story explore?"

Examples:
- Power and corruption
- Loyalty vs. truth
- Coming of age
- Identity and belonging
- Redemption
- Sacrifice
- Love and loss

**Story Inspiration:**
"What inspired this story? What questions does it explore?"

Free-form notes about:
- What sparked the idea
- Questions you're exploring
- Why this story matters to you
- What you hope readers feel

**Target Audience:**
"Who is this story for?"

- Age range (YA, adult, etc.)
- Genre expectations
- Reader profile

**Voice and Style:**
"What are your narrative choices?"

- POV (first person, third limited, third omniscient, multiple)
- Tense (past, present)
- Tone (dark, light, humorous, serious, lyrical, sparse)
- Style notes (literary, commercial, experimental)

**Planned Word Count:**
"What's your target word count?"

Ranges by length:
- Short story: <7,500 words
- Novella: 7,500-40,000 words
- Novel: 40,000-100,000+ words

More specific targets help with pacing.

#### Update PROJECT.md

Add or enhance these sections in PROJECT.md:
- Core Themes (update list)
- Development Notes / Story Inspiration
- Target Audience
- Voice and Style
- Planned Length (word count)

### Step 8: Planning Completion

Update status and show completion summary:

```bash
# Update PROJECT.md frontmatter
status: planning-complete
```

Show completion message:

```
✓ In-Depth Planning Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your comprehensive story foundation is built:

✓ Character profiles created (CHARACTERS.md)
✓ Plot structure mapped (OUTLINE.md)
✓ Character arcs defined (ARCS.md)
✓ World-building documented (WORLD.md)
✓ Themes and style captured (PROJECT.md)

Files created in stories/{slug}/:
- CHARACTERS.md ({character count} characters)
- OUTLINE.md (three-act structure{, subplots if novel})
- ARCS.md (transformation tracking)
- WORLD.md (setting and world details)

Template depth: {LENGTH-based}
- {For novel: Comprehensive sections with full detail}
- {For novella: Moderate depth focused on essentials}
- {For short story: Core elements for focused narrative}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ready to Draft
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You have a solid foundation for your {LENGTH} story.
These planning documents will guide your drafting and help
maintain consistency.

Next: When ready to draft, use /write:chapter (Phase 2)

Your planning documents are reference tools - revisit and
update them as the story evolves during drafting.
```

## Implementation Notes

### Length-Aware Template Processing

When generating documents from templates:

1. Read story length from PROJECT.md frontmatter
2. Read template file
3. Process LENGTH markers:

```bash
# If novel: include LENGTH:novel sections
# If shorter: remove LENGTH:novel sections

if [ "$LENGTH" = "novel" ]; then
  # Keep all content
  cat template.md > output.md
else
  # Remove LENGTH:novel sections
  sed '/<!--LENGTH:novel-->/,/<!--\/LENGTH:novel-->/d' template.md > output.md
fi
```

4. Replace {VARIABLE} placeholders with gathered content

### Prompting Style

- Conversational, not form-like
- Show examples for each question
- Allow "skip" or "I'll add this later" for optional sections
- Confirm understanding: "So your protagonist is a {description}. Is that right?"
- Encourage depth: "Tell me more about..." when answers are superficial

### Template Depth by Length

**Short story (< 7,500 words):**
- 2-3 characters max
- Simple three-act structure
- 3 growth moments per character
- Basic setting only
- Skip: subplots, extensive world-building, detailed scene lists

**Novella (7,500-40,000 words):**
- 3-4 characters
- Three acts with moderate scene detail
- 4-5 growth moments
- Moderate world-building
- 1-2 subplots if relevant

**Novel (40,000+ words):**
- 4+ characters
- Full three-act structure with detailed scenes
- 5-7 growth moments
- Comprehensive world-building
- Multiple subplots
- Full sections: history, culture, relationships, consistency tracking

### Error Handling

- If project doesn't exist: "Run /write:init first"
- If project is YOLO mode: "This project uses YOLO mode. Use /write:expand instead."
- If template files missing: Report path and offer to create from defaults
- If writer wants to skip a section: Mark with "TODO" placeholder for later

## Completion Message

After creating all planning documents, show:

```
✓ IN-DEPTH PLANNING COMPLETE
═══════════════════════════════════════

Your story foundation is ready:
✓ Detailed character profiles ({count} characters)
✓ Complete plot outline (3-act structure)
✓ Character arcs mapped
✓ World-building documented
✓ Themes defined

Files created:
- CHARACTERS.md
- OUTLINE.md
- ARCS.md
- WORLD.md
- THEMES.md

═══════════════════════════════════════
NEXT STEPS
═══════════════════════════════════════

1. OPTIONAL: Create style profile
   → /write:style-seed
   → Paste 2-3 paragraphs of your writing
   → Better voice matching in chapters

2. REQUIRED: Plan first arc
   → /write:discuss 1
   → Answer questions about Arc 1
   → Creates ARC-1-CONTEXT.md

3. Then write Arc 1
   → /write:arc 1
   → Writes chapters in parallel
   → ~15-20 minutes

OR skip discuss and let /write:arc 1 ask questions interactively.

Estimated time to first draft: ~6-8 hours total
```
