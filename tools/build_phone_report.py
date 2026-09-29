"""Renders a saved app report (JSON from the app's history) as the scrollable phone screen on the landing page.
Writes the markup between <!-- phone:start --> and <!-- phone:end --> in landing/index.html.
Usage: python3 tools/build_phone_report.py [report.json]"""
import html, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
report = json.loads(pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "tools" / "sample_report.json").read_text())
e = html.escape

SEVERITY = {"seriousConcern": ("serious", "Serious concern"), "askAboutIt": ("ask", "Ask about it"), "worthNoting": ("worth", "Worth noting")}
CAUTION = {
    "high": ("serious", "Get advice first", "warn", "At least one clause could cost you real money or rights. Consider getting advice before signing."),
    "medium": ("ask", "Worth a question", "info", "Some clauses deserve a question before you sign. They're listed under Things to check."),
    "low": ("routine", "Looks routine", "check", "No clause raised a flag. Skim the key points and read the document once yourself."),
}
ICON = {
    "warn": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5L2.8 19.5h18.4L12 3.5z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M12 10v4.2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="16.9" r="1.1" fill="currentColor"/></svg>',
    "info": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 7.5v5.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="16.3" r="1.1" fill="currentColor"/></svg>',
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 12.3l2.7 2.7L16.2 9.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "q": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M9.6 9.4a2.5 2.5 0 014.8.9c0 1.7-2.4 2.2-2.4 3.7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="12" cy="17" r="1.1" fill="currentColor"/></svg>',
}

cls, label, icon, text = CAUTION[report["caution"]]
parts = []
parts.append(f'''<div class="ios-bar"><span class="ios-time">9:41</span><span class="ios-island"></span><span class="ios-status"><svg viewBox="0 0 18 12" aria-hidden="true"><rect x="0" y="8" width="3" height="4" rx="1"/><rect x="5" y="5.5" width="3" height="6.5" rx="1"/><rect x="10" y="3" width="3" height="9" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/></svg><svg viewBox="0 0 16 12" aria-hidden="true"><path d="M8 11.5l2.3-2.8a3.6 3.6 0 00-4.6 0zM3.4 6.2a7 7 0 019.2 0l1.5-1.8a9.4 9.4 0 00-12.2 0zM.3 2.5a11.8 11.8 0 0115.4 0L16 2.1" /></svg><span class="ios-batt"><span></span></span></span></div>
<div class="ios-nav"><span class="ios-circle"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 11l8-6.5 8 6.5M6.5 9.5V19h11V9.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><rect x="10" y="13.5" width="4" height="5.5" fill="currentColor"/></svg></span><span class="ios-navtitle">Report</span><span class="ios-circle"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5v11M8 7.5l4-4 4 4M6.5 11H6a2 2 0 00-2 2v6a2 2 0 002 2h12a2 2 0 002-2v-6a2 2 0 00-2-2h-.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span></div>''')
parts.append(f'<h3 class="ios-title">{e(report["documentType"])}</h3>')
parts.append(f'<div class="ios-card"><span class="ios-pill big serious">{ICON["warn"]}Note</span><p class="ios-red">Not legal advice. For decisions that matter, have a qualified professional review the document before you sign.</p></div>')
parts.append(f'<div class="ios-card tight"><span class="ios-pill big {cls}">{ICON[icon]}{label}</span><p class="ios-muted">{e(text)}</p></div>')
parts.append(f'<p class="ios-head">Summary</p><div class="ios-card"><p>{e(report["summary"])}</p></div>')
if report.get("keyPoints"):
    rows = "".join(f'<li>{e(p)}</li>' for p in report["keyPoints"])
    parts.append(f'<p class="ios-head">Key points</p><ul class="ios-card ios-points">{rows}</ul>')
concerns = []
for i, c in enumerate(report["concerns"]):
    sc, sl = SEVERITY.get(c["severity"], SEVERITY["worthNoting"])
    kw = '<span class="ios-kw">keyword scan</span>' if c.get("source") == "keywordScan" else ""
    q = f'<div class="ios-askq">{ICON["q"]}<span>{e(c["questionToAsk"])}</span></div>' if c.get("questionToAsk") else ""
    is_open = i == 0
    concerns.append(f'<div class="ios-concern{" open" if is_open else ""}"><button type="button" class="ios-toggle" aria-expanded="{"true" if is_open else "false"}"><span class="ios-row"><span class="ios-pill {sc}">{sl}</span>{kw}<span class="ios-chev" aria-hidden="true"></span></span><span class="ios-quote">“{e(c["quote"])}”</span><span class="ios-why">{e(c["whyItMatters"])}</span></button>{q}</div>')
parts.append(f'<p class="ios-head">Things to check</p><div class="ios-card ios-list">{"".join(concerns)}</div><p class="ios-foot">Tap a clause to read it in full.</p>')
if report.get("questionsToAsk"):
    rows = "".join(f'<li>{ICON["q"]}<span>{e(q)}</span></li>' for q in report["questionsToAsk"])
    parts.append(f'<p class="ios-head ios-head-row"><span>Questions to ask</span><span class="ios-link">Copy all</span></p><ul class="ios-card ios-questions">{rows}</ul>')
parts.append('<p class="ios-foot ios-disclaimer">Should You Sign It? summarizes and points out clauses to ask about. It is not legal advice. The analysis runs on this device and can miss things or be wrong.</p>')

screen = "\n".join(parts)
markup = f'''<!-- phone:start -->
        <div class="phone" role="region" aria-label="Example report, scroll to read it">
          <div class="ios-screen" tabindex="0">
{screen}
          </div>
          <span class="ios-home" aria-hidden="true"></span>
        </div>
        <p class="phone-hint">Scroll the report. Tap a clause to open it.</p>
        <!-- phone:end -->'''
page = ROOT / "landing" / "index.html"
t = page.read_text()
a, b = t.index("<!-- phone:start -->"), t.index("<!-- phone:end -->") + len("<!-- phone:end -->")
page.write_text(t[:a] + markup.lstrip().replace("<!-- phone:start -->", "<!-- phone:start -->", 1) + t[b:])
print("phone report written:", len(report["concerns"]), "clauses,", len(report.get("questionsToAsk", [])), "questions")
