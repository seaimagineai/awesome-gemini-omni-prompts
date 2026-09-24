#!/usr/bin/env python3
"""Offline integrity checks: source recipes, assets, locales, and relative links."""
from pathlib import Path
import hashlib,json,re,sys
from urllib.parse import unquote,urlsplit
R=Path(__file__).resolve().parents[1]
errors=[]
def check(ok,msg):
 if not ok: errors.append(msg)
u=json.loads((R/'data/upstream.json').read_text());total=0
for name,rec in u['prompt_collections'].items():
 p=R/'prompts'/name;t=p.read_text();blocks=re.findall(r'```text\n(.*?)```',t,re.S)
 check([hashlib.sha256(b.encode()).hexdigest() for b in blocks]==rec['control_block_sha256'],f'Changed source control blocks: {name}')
 count=len(re.findall(r'^## \d',t,re.M));total+=count;check(count==rec['recipes'],f'Recipe count: {name}')
check(total==60,f'Expected 60 recipes, got {total}')
for name,digest in u['source_assets'].items():
 check(hashlib.sha256((R/'assets'/name).read_bytes()).hexdigest()==digest,f'Source asset changed: {name}')
checks=0
for p in list(R.glob('*.md'))+list((R/'docs').rglob('*.md'))+list((R/'prompts').glob('*.md'))+list((R/'assets').glob('*.md')):
 t=p.read_text();check(t.count('```')%2==0,f'Unclosed fence: {p.relative_to(R)}')
 for dest in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)',t):
  if dest.startswith(('http:','https:','mailto:','#')):continue
  target=unquote(urlsplit(dest).path)
  if target: check((p.parent/target).exists(),f'Broken local link {p.relative_to(R)}: {dest}');checks+=1
for name in ['README.md','README_ZH.md','README_ZH-TW.md','README_JA.md','README_KO.md','README_ES.md','README_FR.md','README_DE.md','README_PT.md','README_IT.md','README_AR.md','README_RU.md','README_ID.md','README_TH.md','README_VI.md']:
 p=R/name;t=p.read_text()
 check('SeaImagine' in t,f'Missing brand: {name}')
 check(bool(re.search(r'^# .*Gemini Omni',t,re.M)),f'Missing model in title: {name}')
 for asset in ['product-speaker.png','travel-cyclist.png','clockmaker-story.png','seaimagine-omni-hero.png']:check(asset in t,f'Missing example/cover {asset}: {name}')
 check('docs/community-examples.md' in t,f'Missing source studies: {name}')
 check('docs/flaq-ai-workflow.md' not in t,f'Old promotional route: {name}')
 check('https://flaq.ai/' not in t,f'Old promotional URL: {name}')
check((R/'README_EN.md').read_bytes()==(R/'README.md').read_bytes(),'English mirror differs')
check('Copyright (c) 2026 Flaq AI' in (R/'LICENSE').read_text(),'Missing upstream license')
d=json.loads((R/'data/community-examples.json').read_text());check(len(d['community'])==6,'Community count')
check(len({x['url'] for x in d['community']})==6,'Duplicate community posts')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {total} source recipes preserved; 15 locale entries; 4 inherited assets; 6 community cases; {checks} relative links.')
