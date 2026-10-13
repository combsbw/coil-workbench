#!/usr/bin/env python3
"""Idempotently splice the thresholds section into /home/claude/coilbench/app.html.
Order: python3 build_thr.py && python3 splice_thr.py
"""
import re, os
HERE = os.path.dirname(os.path.abspath(__file__))
APP = '/home/claude/coilbench/app.html'
rd = lambda n: open(os.path.join(HERE, n)).read()
s = open(APP).read()

def strip(s, a, b):
    return re.sub(re.escape(a) + r'.*?' + re.escape(b) + r'\n?', '', s, flags=re.S)

# remove any previous splice
s = strip(s, '/*THRCSS-BEGIN*/', '/*THRCSS-END*/')
s = strip(s, '<!--THR-BEGIN-->', '<!--THR-END-->')
s = strip(s, '/*THR-BEGIN*/', '/*THR-END*/')
s = strip(s, '/*THRJS-BEGIN*/', '/*THRJS-END*/')

# CSS (before first </style>)
css = '/*THRCSS-BEGIN*/\n' + rd('thr.css') + '/*THRCSS-END*/\n'
i = s.index('</style>')
s = s[:i] + css + s[i:]

# HTML (before Mechanism dossiers)
mark = '  <section class="r-sec">\n   <h3>Mechanism dossiers</h3>'
assert mark in s, 'html marker'
s = s.replace(mark, '<!--THR-BEGIN-->\n' + rd('thr.html') + '<!--THR-END-->\n' + mark, 1)

# JS (bundle + renderer) before initResearch definition
mark = 'function initResearch(){'
assert s.count(mark) == 1
s = s.replace(mark, rd('thr_bundle.js') + '\n' + rd('thr_render.js') + '\n' + mark, 1)
# call in initResearch
old = 'renderMechs(); renderSystems(); renderEvidenceMap(); buildLibChips(); renderLibrary();\n  $(\'libQ\')'
if 'renderThr();' not in s:
  assert old in s, 'init call'
  s = s.replace(old, 'renderMechs(); renderSystems(); renderEvidenceMap(); buildLibChips(); renderLibrary(); try{ renderThr(); }catch(e){ console.error(e); }\n  $(\'libQ\')', 1)
# refresh design overlay whenever the research view is shown
old = "  window.scrollTo(0,0);\n}\nfunction initResearch"
if old not in s:
    old = "  window.scrollTo(0,0);\n}"
assert "if(!R_ && R){ requestAnimationFrame" in s
if 'renderThrChart==' not in s:
  s = s.replace("  window.scrollTo(0,0);\n}", "  if(R_){ try{ if(typeof renderThrChart==='function'&&$('thrChart')){ renderThrChart(); renderThrList(); } }catch(e){} }\n  window.scrollTo(0,0);\n}", 1)

# hero stat
if 'threshold cards' not in s:
  s = s.replace("<span><b class=\"num\">${MECHS.length}</b> mechanism dossiers</span>", "<span><b class=\"num\">${MECHS.length}</b> mechanism dossiers</span><span><b class=\"num\">${typeof THR_DATA!=='undefined'?THR_DATA.cards.length:0}</b> threshold cards</span>", 1)
open(APP, 'w').write(s)
print('spliced; bytes', len(s))
