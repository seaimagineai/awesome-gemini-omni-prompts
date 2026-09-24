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
# Guard actual learning content, not just the presence of language files.
from homepage_sections import brand_section, read
additions=read('homepage-additions.json')
expected={'en','cn','tw','ja','ko','es','fr','de','pt','it','ru','id','th','vi','ar'}
check(set(additions)==expected,'Missing localized homepage additions')
from build_locales import LOCALES, build
for code,suffix,_ in LOCALES:
    p=R/('README.md' if code=='en' else f'README_{suffix}.md');t=p.read_text()
    guide=(R/f'docs/guides/README_{suffix}.md').read_text()
    check(brand_section(code).replace('](assets/','](../../assets/').replace('="assets/','="../../assets/') in guide,f'Incomplete practice guide: {code}')
    check(t.index('id="prompt-collections"')<t.index('id="source-examples"')<t.index('id="video-studies"')<t.index('id="brand-tools"'),f'Wrong reader journey: {code}')
    opening=t.split('<a id="brand-tools"></a>')[0]
    check('SeaImagine' not in opening and 'https://seaimagine.com' not in opening,f'Brand promotion before teaching: {code}')
    check(len(re.findall(r'^```text$',t,re.M))==6,f'Expected six visible complete examples: {code}')
    for case in d['community']+d['official']['suggested_cases']:
        check(case['url'] in t,f'Missing result source: {code}: {case["url"]}')
    for case in read('showcase-examples.json')+read('brand-examples.json'):
        prompt=case.get('prompt_en',case['prompt']) if code=='en' else case['prompt']
        check(prompt in t,f'Missing complete example: {code}: {case["image"]}')
    for key,size in [('brand_titles',3),('brand_lessons',3),('brand_actions',3),('study_titles',4),('study_lessons',4),('study_practice',4)]:
        check(len(additions[code][key])==size and all(additions[code][key]),f'Missing {key}: {code}')
    check(build(code,suffix)==t,f'Stale generated locale: {code}')
    for link in re.findall(r'(?:src|href)="([^"#]+)"',t):
        if not link.startswith(('http:','https:')):check((p.parent/link).exists(),f'Broken HTML image/link: {code}: {link}')
for rec in read('brand-asset-provenance.json'):
    p=R/rec['filename']
    check(p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==rec['image_sha256'],f'New image provenance mismatch: {p.name}')
for name,hashes in read('source-teaching-blocks.json')['files'].items():
    guide_name='README_EN.md' if name=='README.md' else name
    blocks=re.findall(r'```text\n(.*?)```',(R/name).read_text()+'\n'+(R/'docs/guides'/guide_name).read_text(),re.S)
    actual={hashlib.sha256(b.strip().encode()).hexdigest() for b in blocks}
    check(set(hashes)<=actual,f'Lost source teaching blocks: {name}')
check('as a separate 360p draft' not in (R/'README.md').read_text(),'Unqualified 360p direction remains')
catalog=read('prompt-catalog.json')
check(len(catalog['cases'])==60,'Catalogue must have 60 cases')
for case in catalog['cases']:
    page=(R/case['path']).read_text()
    check(f'id="{case["anchor"]}"' in page,f'Missing case anchor: {case["id"]}')
    section=page.split(f'id="{case["anchor"]}"',1)[1].split('<a id="case-',1)[0]
    download=(R/case['copy_path']).read_text()
    for block in re.findall(r'```text\n(.*?)```',section,re.S):
        check(block.strip() in download,f'Incomplete text export: {case["id"]}')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {total} source recipes preserved; 15 locale entries; 4 inherited assets; 3 new practice images; 6 community cases; 60 case downloads; 10 on-page result references; {checks} relative links.')
