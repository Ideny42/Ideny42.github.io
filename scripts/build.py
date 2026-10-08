"""Build the dependency-light GitHub Pages homepage: python3 scripts/build.py."""
from pathlib import Path
from html import escape
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
config = yaml.safe_load((ROOT / '_config.yml').read_text())
pubs = yaml.safe_load((ROOT / '_data/publications.yml').read_text())['main']
projects = yaml.safe_load((ROOT / '_data/projects.yml').read_text())['main']
e = escape
project_cards = []
for project in projects:
    url = e(project['url'], quote=True)
    meta = e(project['role']) + (' · ' + e(project['dates']) if project.get('dates') else '')
    if project.get('team'):
        meta += '<br>' + e(project['team'])
    contributions = ''.join(f"<li><strong>{e(item['label'])}</strong><span>{e(item['text'])}</span></li>" for item in project.get('contributions', []))
    contribution_html = f'<ul class="project-contributions">{contributions}</ul>' if contributions else ''
    logos = ''.join(f'<img class="brand-{e(logo["style"])}" src="{e(logo["src"], quote=True)}" alt="{e(logo["alt"], quote=True)}">' for logo in project.get('logos', []))
    brand_html = f'<div class="project-brands">{logos}</div>' if logos else ''
    project_cards.append(f"""<article class="project-card">{brand_html}<div class="project-top"><span class="eyebrow">{e(project['organization'])} · INTERNSHIP</span><a class="star-badge" href="{url}/stargazers" aria-label="{e(project['name'])}: {e(project['stars'])} GitHub stars">☆ {e(project['stars'])}</a></div><h3><a href="{url}">{e(project['name'])} <span aria-hidden="true">↗</span></a></h3><p class="project-meta">{meta}</p><p>{e(project['description'])}</p>{contribution_html}<a class="project-link" href="{url}">Explore repository ↗</a></article>""")
cards = []
for i, p in enumerate(pubs):
    links = ''.join(f'<a href="{e(p[k], quote=True)}">{label} <span aria-hidden="true">↗</span></a>' for k, label in [('pdf', 'Paper'), ('code', 'Code'), ('page', 'Project')] if p.get(k))
    paper_id = Path(p['image']).stem.removeprefix('teaser_')
    cards.append(f'''<article class="paper" id="{e(paper_id)}"><a class="paper-image" href="{e(p['pdf'], quote=True)}" tabindex="-1" aria-hidden="true"><img src="{p['image']}" alt="" loading="lazy"></a><div><div class="paper-meta">{e(p.get('conference_short') or 'Preprint')} <span> / 0{i+1}</span></div><h3><a href="{e(p['pdf'], quote=True)}">{e(p['title'])}</a></h3><p class="authors">{p['authors']}</p><p class="venue">{p['conference']}</p><div class="paper-links">{links}</div></div></article>''')
old = (ROOT / 'index.md').read_text()
awards = [re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line[2:].strip()) for line in old.split('## Honors and Awards')[1].splitlines() if line.startswith('- ')]
selected_indices = [0, 2, 4, 6, 9, 12]
selected_awards = ''.join(f'<li>{awards[i]}</li>' for i in selected_indices)
other_awards = ''.join(f'<li>{a}</li>' for i, a in enumerate(awards) if i not in selected_indices)
scholar = f'<a href="{e(config["google_scholar"], quote=True)}">Google Scholar ↗</a>' if config.get('google_scholar') else ''
page = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Yiheng Du · Peking University</title><meta name="description" content="Yiheng Du — research in reinforcement learning, agentic RL, and multimodal learning."><link rel="canonical" href="https://ideny42.github.io/"><meta property="og:title" content="Yiheng Du · Research"><meta property="og:description" content="Reinforcement learning, agentic RL, and multimodal learning."><meta property="og:type" content="website"><meta property="og:image" content="https://ideny42.github.io/assets/img/avatar.png"><link rel="icon" href="assets/img/favicon.png"><link rel="stylesheet" href="assets/css/home.css"></head>
<body><a class="skip" href="#main">Skip to content</a><header class="topbar"><a class="wordmark" href="#">YD<span> / </span>Yiheng Du</a><nav aria-label="Main navigation"><a href="#opensource">Open source</a><a href="#research">Research</a><a href="#background">Background</a><a href="mailto:yihengdu42@gmail.com">Contact <span aria-hidden="true">↗</span></a></nav></header>
<main id="main"><section class="hero" aria-labelledby="name"><div class="intro"><p class="eyebrow"><span class="dot"></span> REINFORCEMENT LEARNING & MULTIMODAL AI</p><h1 id="name">Yiheng Du<span class="chinese" lang="zh">杜毅衡</span></h1><p class="lead">Exploring how machines<br>perceive <em>and create.</em></p><p class="bio">I am a Ph.D. student at <strong>Peking University</strong>. My research focuses on <strong>reinforcement learning</strong>, <strong>agentic RL</strong>, and <strong>multimodal learning</strong>. I am interested in how models learn to reason, use tools, and understand and generate multimodal content.</p><p class="affiliation">Ph.D. Student in Computer Science · Peking University<br>B.S. in Computer Science · Sichuan University</p><div class="profile-links"><a class="primary" href="mailto:yihengdu42@gmail.com">Get in touch <span aria-hidden="true">↗</span></a><a href="https://github.com/Ideny42">GitHub ↗</a><a href="assets/files/cv.pdf">CV ↗</a>__SCHOLAR__</div></div><figure class="portrait"><img src="assets/img/avatar.png" alt="Portrait of Yiheng Du" width="984" height="1378"><figcaption><span>YIHENG DU</span><span>RESEARCH / ENGINEERING</span></figcaption></figure></section>
<section class="interests" aria-label="Research interests"><span class="section-label">RESEARCH FOCUS</span><div><span>01</span> Reinforcement Learning</div><div><span>02</span> Agentic RL</div><div><span>03</span> Multimodal Learning</div></section>
<aside class="research-update" aria-label="Research update"><span class="eyebrow">RESEARCH UPDATE</span><p>Our work on audio-visual segmentation has been accepted to <strong>ECCV 2026</strong>.</p><a href="#ddavs">Read the paper <span aria-hidden="true">↓</span></a></aside>
<section id="opensource" class="opensource"><div class="section-heading"><div><p class="eyebrow">BUILDING IN THE OPEN</p><h2>Open source & industry</h2></div><p>Contributions through internships<br>at Tencent Hunyuan and Ant Group.</p></div><div class="project-grid">__PROJECTS__</div></section>
<section id="research" class="research"><div class="section-heading"><div><p class="eyebrow">IDEAS INTO PRACTICE</p><h2>Research & publications<span class="count">__COUNT__</span></h2></div><p>Generative models, perception,<br>and the systems behind them.</p></div><div class="papers">__PAPERS__</div><p class="note">* Equal contribution.</p></section>
<section id="background" class="background"><div><p class="eyebrow">THE PATH SO FAR</p><h2>Education</h2><div class="education"><span class="date">SEPT 2026 — JUN 2031 (EXPECTED)</span><h3>Peking University</h3><p>Ph.D. in Computer Science and Technology</p></div><div class="education"><span class="date">SEPT 2022 — JUN 2026</span><h3>Sichuan University</h3><p>B.S. in Computer Science and Technology</p></div><div class="research-experience"><p class="eyebrow">RESEARCH EXPERIENCE</p><h3>Peking University · VILLA Lab</h3><p class="date">RESEARCH INTERN · FROM MAR 2025</p><p>For AlignedGen, I co-led the work as an equal-contribution first author, designing the core method, implementing the pipeline, and conducting the main experiments.</p><p>In collaboration with THU IVG Lab, I led the core method design, end-to-end implementation, and major experiments for DDAVS on audio-visual segmentation.</p></div></div><div class="honors"><p class="eyebrow">A FOUNDATION IN PROBLEM SOLVING</p><h2>Honors & awards</h2><ul>__SELECTED_AWARDS__</ul><details class="more-awards"><summary>More awards</summary><ul>__OTHER_AWARDS__</ul></details></div></section>
<section class="contact"><p class="eyebrow">LET’S CONNECT</p><h2>Good research starts<br>with a conversation.</h2><a href="mailto:yihengdu42@gmail.com">yihengdu42@gmail.com <span aria-hidden="true">↗</span></a></section></main><footer><span>© Yiheng Du</span><span>Built with curiosity.</span><a href="#">Back to top ↑</a></footer></body></html>'''
page = page.replace('__COUNT__', f'{len(pubs):02d}').replace('__PAPERS__', '\n'.join(cards)).replace('__SELECTED_AWARDS__', selected_awards).replace('__OTHER_AWARDS__', other_awards).replace('__SCHOLAR__', scholar).replace('__PROJECTS__', ''.join(project_cards))
(ROOT / 'index.html').write_text(page)
print('Built index.html with', len(pubs), 'publications')
