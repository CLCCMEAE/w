pg.wait_for_timeout(2500)
print('C:', pg.evaluate("""(function(){ try {
  var col = { type: 'Choice', options: { choiceOptions: { 'Urgent': { fillColor: '#E00000', textColor: '#FFFFFF', fontBold: true, fontItalic: true }, 'Bas': { textColor: '#00AA00' }, 'Piège': { fillColor: 'red;x' } } } };
  var b = badgeChoixGrist(col, 'Urgent');
  var r = [b.outerHTML, (badgeChoixGrist(col, 'Bas')).getAttribute('style'), styleChoixGrist(col, 'Piège'), styleChoixGrist(col, 'Inconnu')];
  var sel = document.createElement('select'); ['', 'Urgent', 'Bas'].forEach(function (v) { var o = document.createElement('option'); o.value = v; o.textContent = v; sel.appendChild(o); });
  sel.value = 'Urgent'; colorerSelectChoix(sel, col); r.push(sel.getAttribute('style'));
  sel.value = ''; sel.dispatchEvent(new Event('change')); r.push(sel.getAttribute('style') || 'sans style');
  var cl = { type: 'ChoiceList', options: col.options }; var n = valeurAvecCouleurs(cl, ['L', 'Urgent', 'Autre'], 'x'); r.push(n.outerHTML ? n.children.length : n);
  r.push(valeurAvecCouleurs({ type: 'Text' }, 'Urgent', 'Urgent'));
  return JSON.stringify(r);
} catch (e) { return 'ERR ' + e.message; } })()"""))
