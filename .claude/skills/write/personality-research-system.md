# Character Personality Research System - Anti-Cookie-Cutter Characters

## PROBLEM: AI Generates Formulaic Personalities

**Common AI Character Patterns (AVOID)**:
- "Mysterious loner with hidden trauma"
- "Witty rogue with heart of gold"
- "Naive innocent who grows wise"
- "Stoic warrior who learns to feel"
- "Brilliant but socially awkward scientist"
- "Rebellious teen against authority"
- "Grizzled mentor with dark past"
- "Cheerful optimist hiding pain"
- "Ambitious schemer consumed by greed"
- "Brooding antihero seeking redemption"

These are **not creative choices** - they're statistical patterns from training data, especially popular in YA and genre fiction.

---

## CRITICAL RULE: RESEARCH BEFORE CREATING

**This is a MANDATORY requirement**: Claude MUST research personality combinations before creating characters.

### Why This Exists

AI models have strong biases toward personality archetypes that appear frequently in fiction. Without research, you get:
- Same personality combos repeatedly
- Flat, predictable character dynamics
- Traits that don't create interesting conflicts
- Characters who all sound alike despite different "personalities"

---

## SOLUTION: Psychology Database Research

Before creating character personalities, Claude MUST:

1. **Research real personality frameworks** from psychology databases
2. **Find unusual trait combinations** that create depth
3. **Avoid AI-common archetypes**
4. **Provide multiple researched options** for user to choose

---

## Approved Research Sources

### For Personality Framework Understanding:
- **Simply Psychology**: https://www.simplypsychology.org/personality-theories.html
  - Overview of Big Five, MBTI, Enneagram
  - Scientific grounding for traits
  - How traits interact

- **Psychology Today (Personality)**: https://www.psychologytoday.com/us/basics/personality
  - Personality type descriptions
  - Real-world trait combinations
  - Conflict patterns between types

- **16 Personalities**: https://www.16personalities.com/
  - MBTI-based but nuanced
  - Shows trait variations within types
  - Strengths AND weaknesses

### For Character-Specific Applications:
- **Character Database Sites**: Sites like Personality Database
  - How real fictional characters map to frameworks
  - Unusual but working combinations
  - See what's been done before (to avoid it)

### For Trait Combinations:
- **Big Five Research**: Academic sources on OCEAN model
  - Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism
  - How traits combine in real people
  - Unexpected correlations

---

## Workflow: Character Personality Creation

### Step 1: Determine Character Role and Context

Before researching, identify:
- **Role in story**: Protagonist, antagonist, mentor, love interest, comic relief
- **Story function**: What conflict do they create? What do they represent?
- **Genre expectations**: What does the genre usually do? (So you can subvert it)
- **Character arc**: Will they change? How?

### Step 2: Research Personality Frameworks

Use WebFetch to research at least TWO of these:

**Big Five (OCEAN Model)**:
- More scientific than MBTI
- Five spectrum traits, not types
- Real variation within combinations
- Example: High Openness + Low Conscientiousness = creative chaos (artist stereotype)
- BUT: High Openness + HIGH Conscientiousness = disciplined innovator (more interesting)

**MBTI (with nuance)**:
- Don't just pick a type (that's still cookie-cutter)
- Look at cognitive function stacks
- Consider unhealthy vs healthy versions of types
- Example: INTJ isn't just "cold mastermind," can be insecure planner, ethical strategist, or anxious overthinker

**Enneagram**:
- Nine core types with wings and stress/growth directions
- Focus on core fears and desires
- Shows how same personality manifests differently under stress
- Example: Type 1 (Perfectionist) + Wing 2 = principled helper, not rigid judge

### Step 3: Find UNUSUAL Combinations

Look for:
- **Contradictory traits that create tension**: Extraverted but anxious, Agreeable but ambitious
- **Atypical pairings for the role**: Antagonist who's high agreeableness (manipulates through charm, not force)
- **Healthy versions of "dark" types**: Enneagram Type 8 (Challenger) who's protective, not domineering
- **Unhealthy versions of "light" types**: Enneagram Type 2 (Helper) who's controlling, not nurturing

**CRITICAL**: Avoid these AI-common combinations:
- INTJ + traumatic past + lone wolf = CLICHE
- ENFP + bubbly exterior + hidden sadness = CLICHE
- ISTP + stoic + secretly caring = CLICHE
- High Openness + Low Agreeableness + "misunderstood genius" = CLICHE

### Step 4: Use WebFetch to Get Options

```
Use WebFetch with personality research URLs
Extract 5-8 personality combinations with:
- Framework basis (Big Five, MBTI, Enneagram, or combo)
- Trait specifics
- How this creates interesting character
- What conflicts this enables
Present to user with context
```

### Step 5: User Selection and Refinement

User can:
- Choose from researched options
- Mix elements from multiple options
- Request different archetypes
- Provide their own framework

Then Claude refines by:
- Asking about healthy vs unhealthy version of type
- Suggesting how this interacts with other characters
- Noting potential character arcs

---

## Implementation in Planning Skills

### In `indepth-plan.md` - Character Development Section

**REPLACE vague personality prompts WITH**:

```markdown
#### Personality

**CRITICAL**: Do NOT generate personality directly. Use personality-research-system.md workflow.

**Workflow**:
1. Determine character's role and story function
2. Use WebFetch to research personality frameworks (Big Five, MBTI, Enneagram)
3. Find 5-8 UNUSUAL trait combinations that:
   - Create internal conflict
   - Enable interesting dynamics with other characters
   - Avoid AI-common archetypes
   - Fit the character's role but with a twist

4. Present researched options:
   ```
   Based on personality research, here are 8 nuanced personality options for [CHARACTER]:

   OPTION 1: High Conscientiousness + Low Agreeableness (Big Five)
   - Disciplined and organized, but blunt and uncompromising
   - Creates conflict through rigid standards, not cruelty
   - Arc potential: Learning flexibility without losing integrity
   - Why it's fresh: "Antagonist" through principled inflexibility, not evil

   OPTION 2: ENFP (MBTI) - Unhealthy version
   - Enthusiastic idea-generator who never follows through
   - Uses charm to avoid responsibility
   - Creates conflict through unreliability, not malice
   - Why it's fresh: "Likeable" type as source of problems

   OPTION 3: Enneagram Type 6 (Loyalist) + Wing 5
   - Anxious but analytical, seeks security through knowledge
   - Questions everything, including themselves
   - Creates conflict through paranoia and overthinking
   - Why it's fresh: "Smart character" driven by fear, not confidence

   [Continue with 5 more researched options]
   ```

5. User selects option or requests different archetypes
6. Refine selection: Healthy or unhealthy version? Under stress or growth?

**NEVER**:
- Generate "mysterious loner" or "witty rogue" without research
- Use standard archetypes from AI training data
- Skip research step
```

### In `yolo-expand.md` - Character Creation

**ADD personality research requirement**:

```markdown
### Generating Character Personalities

**CRITICAL**: Use personality-research-system.md workflow even in YOLO mode.

For YOLO mode (faster approach):
- Research 4-5 options instead of 8
- Present with brief explanations
- User can quick-select or type number
- If user says "just pick one," use first RESEARCHED option (not AI-generated default)

**NEVER generate personalities directly** even in fast mode.
```

---

## Example: Correct Workflow

**User**: "Create a protagonist for a mystery novel"

**Claude**:
```
I'll research personality frameworks to find interesting options for your detective. Hold on...

[Uses WebFetch to research Big Five, MBTI, and Enneagram for detective characters]

Based on personality psychology research, here are 6 nuanced personality options that avoid "brilliant but troubled detective" cliché:

1. HIGH AGREEABLENESS + HIGH OPENNESS (Big Five)
   - Empathetic and creative problem-solver
   - Sees suspects as people, not just cases
   - Conflict: Gets emotionally involved, clouds judgment
   - Fresh angle: Detective who solves through understanding, not deduction alone

2. ISFJ (MBTI) - "The Defender"
   - Detail-oriented, loyal, traditional
   - Solves through careful documentation and pattern recognition
   - Conflict: Struggles with rule-breaking, even when necessary
   - Fresh angle: Methodical detective, not flashy genius

3. ENNEAGRAM TYPE 1 (Perfectionist) + Wing 9
   - Principled but conflict-avoidant
   - Needs to solve case "the right way"
   - Conflict: Rigid ethics vs messy reality
   - Fresh angle: Detective hindered by their own integrity

4. HIGH CONSCIENTIOUSNESS + LOW EXTRAVERSION (Big Five)
   - Organized lone worker who prefers research to interviews
   - Solves through exhaustive analysis
   - Conflict: Misses social cues, needs partner to translate
   - Fresh angle: Introvert detective not because trauma, but preference

5. ESTP (MBTI) - "The Entrepreneur"
   - Action-oriented risk-taker
   - Solves through experimentation and improvisation
   - Conflict: Rushes in, misses subtle clues
   - Fresh angle: Detective who's too confident, not too brooding

6. ENNEAGRAM TYPE 6 (Loyalist) + Wing 7
   - Anxious but also adventurous
   - Questions everything, including own theories
   - Conflict: Paranoia vs need for certainty
   - Fresh angle: Detective who doubts themselves at every turn

Pick a number (1-6), mix elements, or request different archetypes.
```

**User**: "I like 3, the perfectionist"

**Claude**: "Excellent! Should this be a HEALTHY Type 1 (principled reformer, inspires others) or UNHEALTHY Type 1 (judgmental, self-critical, rigid)? Or somewhere in between? This affects how their arc develops."

---

## Example: Incorrect Workflow (AI SLOP)

**User**: "Create a protagonist for a mystery novel"

**Claude** ❌:
```
How about a brilliant but troubled detective with a dark past? Maybe an INTJ personality - analytical,
strategic, but struggles to connect with others. They're haunted by a case they couldn't solve.
```

**This is WRONG**:
- "Brilliant but troubled" = AI archetype #1
- INTJ detective = overused in AI fiction
- "Dark past haunts them" = cliché backstory
- No research conducted
- No options provided
- Pure stereotype

---

## Integration with Other Anti-Slop Systems

### Personality + Names + Plot Tropes = Unique Character

**ALL THREE are researched**:
1. **Name**: From Fantasy Name Generators (not "Kael" or "Elara")
2. **Personality**: From psychology databases (not "mysterious loner")
3. **Character arc**: From TVTropes research (not "strength becomes weakness")

**Result**: Characters feel researched and intentional, not randomly generated

### Example Full Character Creation:

**Without research** (AI slop):
- Name: Kael Shadowborn
- Personality: Mysterious loner, INTJ, dark past
- Arc: His greatest strength (independence) becomes his weakness when he needs help

**With research**:
- Name: Silas Lockhart (from Fantasy Name Generators, fantasy rogue names)
- Personality: ISFJ Defender (from personality research - unusual for rogue archetype)
- Traits: Loyal, methodical, conflict-avoidant BUT forced into breaking rules
- Arc: "Wrong Genre Savvy" (from TVTropes) - thinks he's in heist story, actually political thriller
- Fresh combo: Rogue who's NOT witty/charming/lone-wolf, but dutiful/organized/reluctant

---

## Common Personality Pitfalls to Avoid

### The "Contrived Contrast" Problem

CLICHE: "They seem [X] on the outside but are really [Y] inside"
- Cheerful but hiding pain
- Cold but secretly caring
- Confident but actually insecure

BETTER: Research how traits ACTUALLY combine
- High Extraversion + High Neuroticism = genuinely outgoing AND genuinely anxious (not "hiding" one)
- Low Agreeableness + High Conscientiousness = genuinely principled AND genuinely blunt (not "cold exterior, warm heart")

### The "Trauma Explains Everything" Problem

CLICHE: Personality is just reaction to backstory trauma
- Loner because betrayed
- Angry because abused
- Cold because lost someone

BETTER: Personality exists BEFORE and INDEPENDENT of trauma
- Research actual personality type
- Trauma affects how that type manifests
- Healing doesn't erase personality, changes how it's expressed

### The "One Trait Defines Them" Problem

CLICHE: Character is just "the smart one" or "the angry one"

BETTER: Multi-dimensional through framework research
- Big Five gives FIVE traits, not one
- MBTI has four dichotomies PLUS cognitive functions
- Enneagram has type + wing + stress/growth directions

---

## Personality Research Template for Claude

When Claude needs to research personalities:

```
You are a personality psychology researcher helping create nuanced fictional characters.

CHARACTER ROLE: {role in story}
STORY FUNCTION: {what conflict they create}
GENRE: {genre - to identify and avoid genre clichés}

TASK:
1. Use WebFetch to research personality frameworks:
   - Big Five (OCEAN model)
   - MBTI with cognitive functions
   - Enneagram with wings and stress/growth

2. Find 6-8 personality combinations that:
   - Create INTERNAL conflict (traits that pull in different directions)
   - Enable interesting dynamics with other characters
   - FIT the role but with unexpected twist
   - AVOID these AI clichés:
     * Mysterious loner
     * Witty rogue with heart of gold
     * Stoic warrior who learns to feel
     * Brilliant but socially awkward
     * Cheerful exterior hiding pain
     * Brooding antihero

3. For each option, provide:
   - Framework basis (e.g., "ISFJ" or "High Agreeableness + Low Openness")
   - Trait specifics and how they interact
   - What conflicts this creates (internal AND with others)
   - Why this is fresh/unexpected for this role
   - Potential character arc direction

GOAL: Give writer researched, psychologically grounded options that create complex, unpredictable characters.
```

---

## Benefits of This System

1. **Psychological Depth**: Real frameworks create believable complexity
2. **Unexpected Combinations**: Research surfaces options AI wouldn't generate
3. **Internal Conflict**: Well-researched personalities have built-in tensions
4. **Character Dynamics**: Different frameworks interact in interesting ways
5. **Arc Potential**: Personality types have natural growth/stress patterns
6. **Avoids Clichés**: Research breaks out of training data patterns

---

## Quick Reference

**When creating character personalities**:
1. ❌ DON'T: Generate "mysterious loner" or "witty rogue"
2. ✅ DO: Research Big Five, MBTI, and/or Enneagram
3. ✅ DO: Find UNUSUAL trait combinations
4. ✅ DO: Provide 6-8 researched options
5. ❌ DON'T: Default to AI-common archetypes

**Research Process**:
1. Identify character role and story function
2. WebFetch psychology databases for frameworks
3. Find combinations that create internal conflict
4. Present options with framework basis
5. User selects, then refine (healthy/unhealthy version, etc.)

**Approved Sources**:
- Simply Psychology (framework overviews)
- Psychology Today (personality basics)
- 16 Personalities (MBTI nuance)
- Big Five research (OCEAN model)

---

*This system is MANDATORY for all Claudespeare character creation workflows.*
