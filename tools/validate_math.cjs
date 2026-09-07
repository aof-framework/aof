// Run with mathjax-full@3.2.2 available through NODE_PATH.
// Optional --preview PATH writes a local HTML preview; --report PATH records results.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
require('mathjax-full/js/input/tex/ams/AmsConfiguration.js');
const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'specification/AOF-v1.0-Framework-Specification.md'), 'utf8');
const ledger = JSON.parse(fs.readFileSync(path.join(root, 'release/math-revision/formula-changes.json'), 'utf8'));
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const tex = new TeX({packages: ['base', 'ams'], formatError: (_jax, error) => {throw error;}});
const doc = mathjax.document('', {InputJax: tex, OutputJax: new SVG({fontCache: 'none'})});
const formulas = [...source.matchAll(/^```math\n([\s\S]*?)\n```/gm)];
const errors = [];
const previews = [];
const chosenLines = new Set([58, 71, 183, 415, 901, 3392, 3902, 4071, 5403, 6314, 9541, 10341, 17729, 25250]);
const changes = ledger.changes.filter(c => c.rules.some(r => r.rule === 'github-math-fence'));
formulas.forEach((match, index) => {
  const line = source.slice(0, match.index).split('\n').length;
  try {
    const result = doc.convert(match[1], {display: true});
    const svg = adaptor.outerHTML(result);
    if (svg.includes('data-mjx-error') || svg.includes('<merror')) throw new Error('MathJax error node');
    if (chosenLines.has(changes[index]?.source_line)) {
      previews.push(`<section><h2>Formula ${index + 1} · source ${changes[index].source_line} → current ${line}</h2><div>${svg}</div></section>`);
    }
  } catch (error) {
    errors.push({formula: index + 1, line, source_line: changes[index]?.source_line, message: error.message});
  }
});
if (formulas.length !== ledger.formula_count) errors.push({message: 'Formula count differs from migration ledger'});
const report = {
  revision: ledger.revision,
  specification_sha256: crypto.createHash('sha256').update(source).digest('hex'),
  engine: `mathjax-full ${require('mathjax-full/package.json').version}`,
  packages: ['base', 'ams'],
  scope: 'Local MathJax parsing and SVG generation; not a claim of identical GitHub deployment configuration.',
  formula_count: formulas.length,
  parsed_and_rendered: formulas.length - errors.filter(e => e.formula).length,
  errors,
};
const option = flag => {const index = process.argv.indexOf(flag); return index >= 0 ? process.argv[index + 1] : null;};
if (option('--report')) fs.writeFileSync(option('--report'), JSON.stringify(report, null, 2) + '\n');
if (option('--preview')) fs.writeFileSync(option('--preview'), `<!doctype html><meta charset="utf-8"><title>AOF math QA</title><style>body{font:16px system-ui;background:#f6f8fa;color:#182230;margin:32px}section{background:white;border:1px solid #ddd;border-radius:8px;padding:20px;margin:20px 0}h2{font-size:14px;color:#52606d}section div{overflow-x:auto;padding:16px}mjx-container{display:block;text-align:center}svg{max-width:none}</style><h1>AOF · Formula rendering QA</h1><p>${formulas.length} formulas; ${errors.length} errors. Local MathJax preview.</p>${previews.join('\n')}`);
console.log(JSON.stringify(report, null, 2));
process.exitCode = errors.length ? 1 : 0;
