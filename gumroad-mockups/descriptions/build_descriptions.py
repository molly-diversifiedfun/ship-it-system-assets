"""Gumroad descriptions for the six Ship It System products.

Structure modeled on high-performing long-form Gumroad listings (the PM OS
listing Molly pointed at, plus the most-reviewed results in the category):
headline with a specific promise -> problem bullets -> the mechanism ->
what's inside with real counts -> for / not for -> honest price math ->
what you get -> what happens after you buy -> FAQ -> final CTA block.

Every number here is a verified product fact. No invented stats.
"""
from pathlib import Path
import html as H

OUT = Path(__file__).parent


def esc(s: str) -> str:
    return H.escape(s, quote=False)


def h2(t): return f"<h2>{esc(t)}</h2>\n"
def h3(t): return f"<h3>{esc(t)}</h3>\n"
def p(t): return f"<p>{t}</p>\n"
def b(t): return f"<strong>{esc(t)}</strong>"
def ul(items): return "<ul>\n" + "".join(f"<li>{i}</li>\n" for i in items) + "</ul>\n"
def faq(pairs): return "".join(p(f"{b('Q: ' + q)}<br>A: {esc(a)}") for q, a in pairs)


def page(headline, sub, problem_intro, problems, mechanism, intro, inside, for_you, not_for,
         price_block, get, after, faqs, cta, week=None):
    out = h2(headline) + p(esc(sub))
    out += h3("The problem you're living with") + p(esc(problem_intro)) + ul([esc(x) for x in problems])
    out += h3("What you actually need") + "".join(p(esc(x)) for x in mechanism)
    out += h3(intro[0]) + "".join(p(x) for x in intro[1:])
    out += h3("What's inside")
    for title, body, items in inside:
        out += p(b(title) + (" " + esc(body) if body else ""))
        if items:
            out += ul([esc(i) for i in items])
    if week:
        out += h3(week[0]) + ul([esc(i) for i in week[1:]])
    out += h3("This is for you if") + ul([esc(x) for x in for_you])
    out += h3("This is not for you if") + ul([esc(x) for x in not_for])
    out += h3(price_block[0]) + "".join(p(esc(x)) for x in price_block[1:])
    out += h3("What you get immediately") + ul([esc(x) for x in get])
    out += h3("What happens after you buy") + ul([esc(x) for x in after])
    out += h3("FAQ") + faq(faqs)
    out += p(b(cta[0]) + "<br>" + esc(cta[1]))
    return out


# ------------------------------------------------------------------ Ship It Kit
KIT = page(
    "The 90-day system that gets your side project from 70% done to shipped, on 5 to 10 hours a week",
    "You ship roadmaps for someone else's company every quarter. Your own thing has been almost done since last year. This is the infrastructure that closes the gap.",
    "You are good at this. That is the frustrating part.",
    [
        "Your project has been 70% done for months, and the last 30% keeps moving",
        "Sunday night you open the project tracker, move two cards, and close it",
        "You over-plan and over-engineer a scrappy idea like it is an enterprise deployment",
        "You have bought the course, joined the mastermind, tried the accountability partner. None of it survived week three",
        "Every session starts with a blank page and the question of what to do first",
    ],
    [
        "You do not have a motivation problem or a discipline problem. You have no infrastructure for the months between bursts of energy.",
        "At work, the infrastructure exists: a plan with dates, a definition of done, someone waiting on you. At home there is a notes app and vibes. Same brain, same skills, different environment.",
        "The Ship It Kit is that infrastructure, pre-built. It tells you what to do today, why it matters, and which template to fill in. The next move is the only move.",
    ],
    ["Introducing the Ship It Kit",
     esc("130-page playbook. 25 fill-in templates. 9 modules. One Notion database that runs the 90 days. An AI build partner that fires the right template on the right day."),
     esc("Built for senior tech people (PMs, engineers, designers, leads) who can execute once the 900 decisions between \"I have an idea\" and \"it's live\" are made for them.")],
    [
        ("The 130-page playbook.", "The long-form methodology behind every template. Read it front to back in the first week, then use it as reference per module.", []),
        ("25 templates that fire on specific days.", "Not \"use when ready.\" A day, an artifact, an output.", [
            "T04 Validation Scorecard on Day 2",
            "T07 Scope Guillotine on Day 9",
            "T11 Landing Page Frame on Day 22",
            "T17 PMF Scorecard on Day 60",
            "21 more, from the Readiness Audit to the Pricing Iteration",
        ]),
        ("9 modules across 90 days.", "M0 Decide, M1 Validate, M2 Scope, M3 Build, M4 Equip, M5 Launch, M7 Iterate to PMF, M8 Scale to Stable. M6, the 10-Hour Business Week, runs in parallel from Day 31.", []),
        ("The Notion playbook and Sprint Task database.", "Every row says what to do today, why it matters, and which template fires. Duplicate it once. Sunday-night dread is gone.", []),
        ("The AI Build Partner extension pack.", "The free Build Partner skill for Claude, plus the Kit extension that makes all 25 templates callable in conversation. AI for the thinking, template for the paper trail.", []),
        ("Ship It or Kill It in 90 Days, included.", "The $19 decision playbook, free inside the Kit for the people who have not picked a project yet.", []),
    ],
    [
        "You are a PM, engineer, designer, or lead with 8 or more years in tech",
        "You have a project that is started and stalled, or an idea you have carried for a year",
        "You can give it 5 to 10 hours a week and want those hours to count",
        "You use Notion and Claude, or are willing to set them up in an afternoon",
        "You want a system that tells you what to do next, not a community that asks how you feel",
    ],
    [
        "You want a motivational PDF or a 30-tools-every-founder-needs list",
        "You want live calls, a cohort, or a Discord to keep up with",
        "You have not picked a project and need to decide first (start with Ship It or Kill It for $19)",
        "You want someone to build it with you (that is the 1:1 Build Partnership, not this)",
    ],
    ["Why $149 is the cheap option",
     "If your time is worth $75 an hour, which is conservative at senior tech comp, the Kit pays for itself the first Sunday you skip the two-hour planning spiral and just run Day 1.",
     "Ninety days of not re-deciding what to do next is the actual product. The templates are how it gets delivered.",
     "One payment. Download once, keep forever. No subscription."],
    [
        "130-page Ship It System Playbook (PDF)",
        "25 fill-in templates (PDF), T01 through T25",
        "Notion playbook with the 9 modules and the Sprint Task database",
        "AI Build Partner skill plus the Kit extension pack for Claude",
        "Ship It or Kill It in 90 Days (PDF), included free",
        "Lifetime access to the files",
    ],
    [
        "Minute 1: download link in your inbox",
        "Minute 20: Notion playbook duplicated, User Context page filled in",
        "Day 1: Readiness Audit done, project chosen or confirmed",
        "Day 9: scope cut with the Guillotine, first build week planned",
        "Day 30: something real exists that a stranger can see",
        "Day 90: launched, with a PMF scorecard telling you what to do next",
    ],
    [
        ("Do I need Notion?", "The Sprint Task database and playbook live in Notion. The PDFs work anywhere, but the day-by-day system is built for Notion."),
        ("Do I need Claude?", "The AI Build Partner runs in Claude.ai or Claude Code. Without it you still have the full playbook and all 25 templates on paper."),
        ("Is this a course?", "No. There is nothing to watch and nobody to keep up with. It is a working system you run at your own pace, one day at a time."),
        ("What if I only have 5 hours a week?", "That is the design point. Module 6 is literally called the 10-Hour Business Week, and it assumes you have a job."),
        ("I have not picked a project yet. Is this for me?", "Not yet. Start with Ship It or Kill It in 90 Days for $19. It is also included free inside the Kit if you buy this later."),
        ("Should I get the Bundle instead?", "If you also need marketing (offer, landing page, launch emails), the Bundle adds Marketing OS and saves $49."),
    ],
    ("Get the Ship It Kit, $149", "One payment. Instant download. Ninety days of knowing what to do next."),
    week=["A week with the Kit",
          "Monday: open the Sprint Task database. One row is today. It names the template and the reason.",
          "Wednesday: 45 minutes on the template, then done. No re-planning.",
          "Saturday: two hours of real build time on the thing the week pointed at.",
          "Sunday: five-minute Weekly Ship Check. Next week is already laid out."],
)

# ------------------------------------------------------------------ Marketing OS
MOS = page(
    "26 marketing commands for Claude that produce your offer, sales page, and launch emails in your voice, not ChatGPT's",
    "You have engineered the prompt six times. It still sounds like a SaaS brochure from 2019. The problem is not the prompt. Prompts are the wrong unit of work.",
    "Marketing is the part of shipping that nobody on your team ever made you do.",
    [
        "Your launch copy sounds exactly like your competitor's, because you both fed the same AI the same request",
        "You have bought five prompt packs and pasted three marketing books into the context window",
        "Every output needs an hour of rewriting before it sounds like a person",
        "You know the frameworks by name (Hormozi, Schwartz, Brunson) and still cannot make them fire in order",
        "Your landing page is a Notion doc that became its own project",
    ],
    [
        "A prompt is one question. A command is the whole framework: it asks you the right questions, pulls signals from your existing writing, and produces a finished artifact using the playbook the professionals use.",
        "Then the output of one command becomes the input of the next. Persona feeds offer. Offer feeds pricing. Pricing feeds the sales letter. The sales letter feeds the landing page. The landing page feeds the launch sequence.",
        "Marketing OS is that chain, packaged as a Claude skill.",
    ],
    ["Introducing Marketing OS",
     esc("26 framework-anchored commands across three stages: Attract, Convert, Deliver and Grow."),
     esc("Each one encodes a named, public framework and the judgment of when it fires and what it needs. Run brand-voice-blueprint once and every command after it sounds like you.")],
    [
        ("Attract (8 commands).", "Persona playbook, awareness-to-messaging, viral hook generator, Instagram reels framework, funnel ad creator, content repurposing pipeline, brand voice blueprint, humanize AI writing.", []),
        ("Convert (11 commands).", "Irresistible offer (Hormozi's Value Equation), conversion sales letter (Belcher's 21 steps), micro-commitment ladder, offer ladder, pricing architecture, testimonial stories, FAQ from objections, funnel landing page designer, launch sequence, onboarding sequence, and a skill router.", []),
        ("Deliver and Grow (7 commands).", "Email story engine, referral engine, win-back system, tag-based funnel system, business launch checklist, SaaS financial model, design-tell audit.", []),
        ("Voice DNA.", "The brand voice blueprint reverse-engineers your voice from writing you already have. The \"make this sound human\" step disappears.", []),
        ("Chained outputs.", "Each command's output is shaped to be the next command's input, so a full go-to-market is a weekend, not six unrelated chat sessions.", []),
    ],
    [
        "You have a product, or one on the way, and no marketing system",
        "You use Claude.ai or Claude Code and want deliverables, not theory",
        "You want your copy in your voice, calibrated to a named framework",
        "You are a solopreneur or a very small team",
    ],
    [
        "You want a finished sales page handed to you (this produces structured drafts and blueprints. You ship the final words)",
        "You want a copywriting course",
        "You are an agency looking for white-label",
        "You do not use Claude and do not plan to",
    ],
    ["Why $79",
     "One landing page from a freelancer starts around $500. One command in Marketing OS drafts it in under an hour, calibrated to Schwartz's awareness levels, in your voice.",
     "Buy it once, run it on every launch you ever do. No subscription.",
     "Own the Ship It Kit? The Bundle gets you both and saves $49."],
    [
        "The Marketing OS skill for Claude (zip, drop-in install)",
        "26 command files with full Socratic flows and output formats",
        "The skill router that picks the right command from plain-English requests",
        "Reference sheets for each framework the commands encode",
        "Lifetime access to the files",
    ],
    [
        "Minute 1: download link",
        "Minute 10: skill installed in Claude, brand-voice-blueprint run on three pieces of your writing",
        "Hour 1: persona and offer done",
        "Day 1: sales letter draft and landing page structure",
        "Week 1: launch sequence written, in your voice, ready to schedule",
    ],
    [
        ("Does this work with ChatGPT?", "It is built as a Claude skill. Individual frameworks can be adapted, but the chained system needs Claude."),
        ("Do I need to know the frameworks?", "No. The commands ask the questions the framework needs and apply it for you."),
        ("Is the copy final?", "You get structured drafts and blueprints in your voice. Expect to edit, not to start from blank."),
        ("How is this different from a prompt pack?", "Prompt packs are single questions. These are full flows that interview you, pull from your existing content, and hand their output to the next command."),
        ("Do I need the Ship It Kit too?", "No. Marketing OS stands alone. The Kit is the 90-day build path. The Bundle wires the two together and saves $49."),
    ],
    ("Get Marketing OS, $79", "One payment. Instant download. Your voice, every launch."),
)

# ------------------------------------------------------------------ Bundle
BUNDLE = page(
    "The Ship It Kit plus Marketing OS: build it in 90 days, then sell it, for $49 less than buying both",
    "One system split into two purchases. The Kit is the path. Marketing OS is the engine. Day 22 of the Kit says \"write the launch sequence,\" and Marketing OS is what writes it.",
    "Buying only one of these leaves a hole on a specific day.",
    [
        "With the Kit alone, Day 22 is a blank doc and three hours of rewriting ChatGPT output",
        "With Marketing OS alone, you have a beautiful launch sequence and no 90-day path that forces validation, scope cuts, and build before launch week",
        "Either way the launch slips to Day 38",
    ],
    [
        "The Kit tells you what to do today. Marketing OS does the marketing parts when the Kit says it is time.",
        "Day 22 fires the launch sequence. Day 38 fires the offer rebuild. Day 60 fires pricing calibration. No tool switching, no hunting for the prompt.",
        "The Notion playbook is the conductor. The Marketing OS commands are the instruments.",
    ],
    ["Introducing the Ship It System Bundle",
     esc("Everything in the Ship It Kit ($149) and everything in Marketing OS ($79), for $179. You save $49."),
     esc("130-page playbook, 25 templates, 9 modules, the Notion Sprint Task database, the AI Build Partner extension pack, 26 marketing commands, and Ship It or Kill It included.")],
    [
        ("The Ship It Kit.", "The 130-page playbook, 25 day-specific templates, 9 modules over 90 days, the Notion playbook and Sprint Task database, and the AI Build Partner extension pack.", []),
        ("Marketing OS.", "26 framework-anchored commands for Claude across Attract, Convert, and Deliver and Grow, with Voice DNA so every output sounds like you.", []),
        ("The wiring.", "Kit days that need marketing point at the command that does it. Day 22, launch sequence. Day 38, offer. Day 60, pricing.", []),
        ("Ship It or Kill It in 90 Days.", "The $19 decision playbook, included free.", []),
    ],
    [
        "You have a project to build and nothing built for selling it",
        "You want one system, not two tabs and a spreadsheet of prompts",
        "You are a senior tech person with 5 to 10 hours a week",
        "You use Notion and Claude, or will set them up in an afternoon",
    ],
    [
        "You already have a marketing system and only want the 90-day method (buy the Kit)",
        "You already have a project framework and only want the AI commands (buy Marketing OS)",
        "You want a cohort, calls, or a community",
    ],
    ["Why $179",
     "Kit alone is $149. Marketing OS alone is $79. Together that is $228. The Bundle is $179.",
     "That is the whole pitch. The discount exists because they work better together, not as an upsell.",
     "One payment. Download once, keep forever."],
    [
        "130-page Ship It System Playbook (PDF)",
        "25 fill-in templates (PDF)",
        "Notion playbook with 9 modules and the Sprint Task database",
        "AI Build Partner skill plus the Kit extension pack",
        "Marketing OS skill with 26 commands",
        "Ship It or Kill It in 90 Days (PDF)",
        "Lifetime access to the files",
    ],
    [
        "Minute 1: download links",
        "Minute 30: Notion duplicated, both skills installed in Claude, voice blueprint run",
        "Day 1: Readiness Audit and project confirmed",
        "Day 22: launch sequence drafted by Marketing OS, in your voice",
        "Day 90: launched, priced, with a PMF scorecard and a marketing engine you own",
    ],
    [
        ("Can I buy one now and add the other later?", "Yes, at full price for each. The Bundle price only applies when you buy both together."),
        ("Do I need Notion and Claude?", "Notion for the day-by-day playbook, Claude for the AI Build Partner and Marketing OS. The PDFs work anywhere."),
        ("Is there a subscription?", "No. One payment, lifetime access to the files."),
        ("How much time per week?", "5 to 10 hours. The Kit assumes you have a job."),
    ],
    ("Get the Bundle, $179", "Both systems, one download, $49 saved."),
)

# ------------------------------------------------------------------ Ship It or Kill It
SIOKI = page(
    "A 32-page playbook that gets you to one honest verdict on your stuck project in 90 days: ship it, or kill it and move on",
    "For the project you keep dragging around. Three checkpoints, a scoring frame, and permission to stop.",
    "Nothing is more expensive than a project you will neither finish nor kill.",
    [
        "It has been in the background for a year, quietly costing you every weekend you feel guilty about it",
        "You cannot tell if it is a bad idea or just an unfinished one",
        "You have restarted it three times with a new stack, a new name, a new tracker",
        "Every time you think about killing it, it feels like failure",
    ],
    [
        "Momentum beats perfection, and a decision made with data beats a project that never gets one.",
        "Ship It or Kill It gives you three four-week phases, each ending in a checkpoint. You are never more than a month from a real answer.",
        "Killing a project with evidence is not failure. It is the most senior move you can make.",
    ],
    ["Introducing Ship It or Kill It in 90 Days",
     esc("32 pages. Three phases. Three checkpoints. A 5-dimension scoring frame for the final call."),
     esc("Written for people with full-time jobs and 5 to 10 hours a week.")],
    [
        ("Phase 1, weeks 1 to 4: Foundation and first ship.", "The Napkin Test (one person, one problem, one success metric), an ugly prototype, five real people, checkpoint one.", []),
        ("Phase 2, weeks 5 to 8: Feedback and iteration.", "Twenty-plus users, track what they use versus where they drop, fix the highest-impact thing, checkpoint two.", []),
        ("Phase 3, weeks 9 to 12: The decision.", "Can it grow without you, will anyone pay, do you want to keep going. Commit or close. No tinkering forever.", []),
        ("The tools.", "", [
            "Weekly sprint template built for 5 to 10 hours a week",
            "Daily standup format: three questions, sixty seconds",
            "The 7 traps that kill side projects, and how to spot yours",
            "5-dimension Ship or Kill scorecard with a clear verdict scale",
            "Printable 12-week tracker",
            "Reframes for the four beliefs that keep people stuck",
        ]),
        ("The Momentum Method, included free.", "The 21-day companion for rebuilding self-trust before you ship. Normally $9.", []),
    ],
    [
        "You have a stalled project and cannot tell if it deserves more of you",
        "You want a decision, not another six months of maybe",
        "You have a job and a few hours a week",
    ],
    [
        "You have already decided and need the full build system (that is the Ship It Kit)",
        "You want someone to make the call for you",
    ],
    ["Why $19",
     "Less than the domain renewal you keep paying for the thing.",
     "If the verdict is kill, you get your weekends back. If it is ship, you have a validated project and the tracker to finish it.",
     "Included free inside the Ship It Kit if you upgrade later."],
    [
        "Ship It or Kill It in 90 Days (32-page PDF)",
        "Weekly sprint template and daily standup format",
        "5-dimension scorecard and printable 12-week tracker",
        "The Momentum Method (PDF), included free",
        "Lifetime access",
    ],
    [
        "Minute 1: download link",
        "Day 1: Napkin Test done, project reduced to one sentence",
        "Week 4: first ugly version in front of five people, checkpoint one",
        "Week 8: twenty users, real usage data, checkpoint two",
        "Week 12: a verdict you can defend",
    ],
    [
        ("Is this the same as the Ship It Kit?", "No. This is the decision layer. The Kit is the 90-day build and launch system, and includes this playbook free."),
        ("What if I kill the project?", "Then you have data, a clean stop, and a reusable framework for the next idea. That is the point."),
        ("Do I need any tools?", "A printer if you want the tracker on paper. Otherwise no."),
    ],
    ("Get Ship It or Kill It, $19", "Ninety days to a verdict. One payment."),
)

# ------------------------------------------------------------------ Momentum Method
MOMENTUM = page(
    "The 21-day framework for people who have started a hundred times and never made it past week three",
    "Not more discipline. A rhythm that survives the day you miss.",
    "It is not that you cannot start. Everything you have tried was built to break in week three.",
    [
        "New journal, new app, new \"this time is different,\" and by week six you cannot remember which app",
        "The streak breaks on a bad day and the whole system dies with it",
        "Every framework treats consistency as a moral test, so week four is designed to make you feel bad",
    ],
    [
        "You do not have a willpower problem. You have no recovery rhythm for when the streak breaks.",
        "The Momentum Method assumes you will miss days. What happens the day after is the only thing that matters.",
        "Twenty-one micro-commitments, each under 15 minutes, small enough that a bad day still gets done.",
    ],
    ["Introducing the Momentum Method",
     esc("21 days. 21 micro-commitments. Four environment fixes. One three-line protocol for restarting."),
     esc("The framework Molly used to finally ship Unstuck after a decade of false starts.")],
    [
        ("21 micro-commitments.", "Each under 15 minutes. No 5am starts, no 30-day meditation streaks, no 90-day program hiding in a 21-day wrapper.", []),
        ("Friction Fences.", "Four environment tweaks that turn \"I forgot\" into \"the system reminded me.\" Phone, calendar, workspace cue, one accountability ping. Set once on Day 1.", []),
        ("Recovery Rhythm.", "The three-line protocol for the days the streak breaks. No starting over. No shame spiral. Resume.", []),
    ],
    [
        "You start strong and fall off by week three, every time",
        "You want a habit muscle before a big project, not another planner",
        "You have 15 minutes a day",
    ],
    [
        "You have a project in flight and need the build system (that is the Ship It Kit)",
        "You want a community or someone checking in on you",
        "You believe the answer is more discipline",
    ],
    ["Why $9",
     "One coffee. Less than any habits book you will read once.",
     "It is the cheapest thing in the Ship It System on purpose: this is where people start."],
    [
        "The Momentum Method (PDF)",
        "The 21-day tracker",
        "The Friction Fences setup and the Recovery Rhythm card",
        "Lifetime access",
    ],
    [
        "Minute 1: download link",
        "Day 1: Friction Fences set, first 12-minute commitment done",
        "Day 4, 11, 17: the days most people quit. You run the Recovery Rhythm instead",
        "Day 21: a rhythm that survived real life, and a project ready for the Ship It Kit",
    ],
    [
        ("Is this a habit tracker?", "It includes one, but the product is the recovery protocol and the micro-commitment design, not the grid."),
        ("What if I miss days?", "You will. The method is built around that. Resume, do not restart."),
        ("What comes after the 21 days?", "The free One-Page Launch Plan, then the Ship It Kit when you are ready to build."),
    ],
    ("Get the Momentum Method, $9", "Twenty-one days. Fifteen minutes each. Survives the bad ones."),
)

# ------------------------------------------------------------------ One-Page Launch Plan
OPLP = page(
    "Seven prompts, about fifteen minutes, and a launch plan you can start this week. Free.",
    "You picked the idea. Now you are staring at a blank doc. This is the page that ends that.",
    "The stall happens right after the idea.",
    [
        "You know what you want to build and have no idea what to do first",
        "The blank doc turns into scrolling",
        "Every plan you have made was either three words or thirty pages",
    ],
    [
        "You do not need a business plan. You need the seven decisions that make the first week obvious.",
        "The One-Page Launch Plan is a fill-in page. Seven prompts, one page, a real date.",
    ],
    ["Introducing the One-Page Launch Plan",
     esc("Seven prompts. One page. About fifteen minutes. Pay what you want, and $0 is fine.")],
    [
        ("What you fill in.", "", [
            "The Big Idea, in one sentence",
            "Who It's For, described specifically",
            "The Core Offer, what they get and why they would pay",
            "MVP Scope, the minimum for a version one",
            "3 First Steps, concrete actions for this week",
            "Launch Date, a real one",
            "Success Metric, how you will know it is working",
        ]),
        ("Also built into the AI Build Partner.", "If you would rather run it as a conversation in Claude, the free Build Partner skill walks the same seven prompts.", []),
    ],
    [
        "You have an idea and no first step",
        "You want a plan that fits on one page and survives contact with a Tuesday",
    ],
    [
        "You need to decide between several ideas first (that is Ship It or Kill It)",
        "You want the full 90-day system (that is the Ship It Kit)",
    ],
    ["Why free",
     "It is the starting point of the Ship It System. If it helps, the Momentum Method is $9 and the Kit is $149 when you are ready.",
     "No card, no upsell wall."],
    [
        "The One-Page Launch Plan (fill-in PDF)",
        "Lifetime access",
    ],
    [
        "Minute 1: download link",
        "Minute 15: seven prompts filled in, launch date on the calendar",
        "This week: three first steps done",
    ],
    [
        ("Is it really free?", "Yes. Pay what you want, including nothing."),
        ("Do I need any tools?", "A PDF reader, or a printer if you want it on paper."),
        ("What is next after the page?", "The Momentum Method for the habit, or the Ship It Kit for the 90-day build."),
    ],
    ("Get the One-Page Launch Plan, free", "Seven prompts. Fifteen minutes. Start this week."),
)

for slug, body in {
    "ship-it-kit": KIT, "marketing-os": MOS, "bundle": BUNDLE,
    "ship-it-or-kill-it": SIOKI, "momentum-method": MOMENTUM, "one-page-launch-plan": OPLP,
}.items():
    (OUT / f"{slug}-new.html").write_text(body)
    print(slug, len(body), "chars")
