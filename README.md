# Yiheng Du — Academic homepage

A responsive static homepage for https://ideny42.github.io/ with an off-white and forest-green design. No JavaScript or external font services are required to view it.

## Preview

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000.

## Edit and rebuild

- Open-source projects and industry experience: `_data/projects.yml`.
- Publications: `_data/publications.yml` (original data preserved).
- Awards: the Honors and Awards section of `index.md`.
- Google Scholar: add the real public profile URL to `google_scholar` in `_config.yml`; the link appears after rebuilding.
- Biography, education, and layout: `scripts/build.py`.
- Styles and responsive breakpoints: `assets/css/home.css`.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/build.py
```

Commit the generated `index.html` alongside source changes. `.nojekyll` makes GitHub Pages serve the generated page directly, without a Ruby build. Existing Jekyll files and assets remain available for reference. Configure GitHub Pages to deploy from the repository branch and root directory.

## Pending content confirmation

Current affiliation is Peking University, confirmed by the author. The linked PDF CV is generated from `main.tex` and includes the confirmed education, Tencent internship, research focus, and ECCV publication updates. DDAVS uses the updated title and ECCV 2026 acceptance supplied by the author. Open-source participation, internship affiliations, and star milestones are approximate and are not live counters. Ant Group dates and contributions and VILLA Lab research are taken from the original CV. Tencent · Hunyuan · Foundation Model Department affiliation and primary responsibility for PE trainer and agentic RL are author-confirmed; internship dates are March 2026–present, confirmed by the author. UniRL component descriptions follow its official repository documentation. Scholar profile is linked at https://scholar.google.com/citations?user=718Y9mMAAAAJ&hl=en; institutional email at stu.pku.edu.cn is verified. Old temporary Scholar BibTeX URLs are not shown.

## Brand assets

- Tencent: https://www.tencent.com/wp-content/uploads/2024/05/logo@2x-en.png
- Hunyuan: official GitHub organization avatar, https://avatars.githubusercontent.com/u/210980732?s=200&v=4
- Ant Group: official website asset, https://gw.alipayobjects.com/zos/bmw-prod/bb9478cb-76f2-41b1-863a-a35322f9e85d.svg

Logos identify internship organizations and projects; trademarks belong to their respective owners.

## Build the CV

Run `xelatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/latex main.tex` after creating `tmp/latex`. Inspect the output, then copy `tmp/latex/main.pdf` to `assets/files/cv.pdf` and `output/pdf/Yiheng_Du_CV.pdf`. The source uses Times New Roman and Noto Serif CJK SC (with Songti SC as a fallback).
