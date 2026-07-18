#!/usr/bin/env python3
from pathlib import Path
import re, sys

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
html = src.read_text(encoding='utf-8')

for old, new in {
    'Game Design Document · v6': 'Game Design Document · v8',
    'Atributos, habilidades, equipamentos, progressão e decisões irreversíveis ou custosas.': 'Atributos, equipamentos, progressão e decisões irreversíveis ou custosas.',
    'Progressão longa, árvore de skills, itemização, raridades e prazer de otimizar.': 'Progressão longa, itemização, raridades e prazer de otimizar.',
    'O valor coletado retorna ao sistema por níveis, atributos, habilidades, jardins, plots, pesquisa e Forja.': 'O valor coletado retorna ao sistema por níveis, atributos, jardins, plots, pesquisa e Forja.',
    'Battle Level, Farm Level, atributos, habilidades, conquistas e progressos adquiridos.': 'Battle Level, Farm Level, Atributos de Batalha, Atributos de Cultivo e progressos adquiridos.',
    'Atributos redistribuíveis, habilidades configuráveis, Núcleo Arcano, Totem e estratégia.': 'Atributos redistribuíveis, Núcleo Arcano, Totem e configuração estratégica.',
    'É construído individualmente por uso, XP, distribuição de pontos e conquistas.': 'É construído individualmente por uso, XP e distribuição de pontos.',
    '<li>conquistas, títulos e participações competitivas;</li>': '<li>títulos e participações competitivas;</li>',
    'Identidade, progressão, build atual, conquistas, proveniência e consumo dos resets gratuitos acompanham o espécime.': 'Identidade, progressão, build atual, proveniência e consumo dos resets gratuitos acompanham o espécime.',
    'Dois attachments já geram grande espaço de build quando combinados com espécie, tipo, raridade, Vigor, doze atributos distribuíveis, habilidades, níveis de passiva e rerolls.': 'Dois attachments já geram grande espaço de build quando combinados com espécie, elemento, raridade, Vigor, doze atributos distribuíveis, Basic Attack, Special Move, níveis de passiva e rerolls.',
    'Plantas conhecidas, tipos, itens, regiões, inimigos, habilidades e histórico desbloqueado.': 'Buds conhecidos, elementos, itens, regiões, inimigos e histórico desbloqueado.',
    '<li>quatro a oito espécies;</li>': '<li>nove espécies no Alpha, uma por elemento;</li><li>Basic Attack e Special Move fixos por espécie;</li><li>RNG controlado de Special Move e Desvio Perfeito;</li>',
    '<li>árvores biológicas gigantes;</li>': '',
    'Cada Bud sobe Battle Level, Farm Level, habilidades e atributos próprios.': 'Cada Bud sobe Battle Level e Farm Level e distribui separadamente Atributos de Batalha e Atributos de Cultivo.',
    'Poder mágico, defesa mágica, geração de energia e eficiência de habilidades arcanas.': 'Poder mágico, defesa mágica e eficiência de efeitos mágicos.',
    'Precisão, execução de skills, penetração, aplicação de controles e consistência técnica.': 'Precisão, penetração, aplicação de controles e consistência técnica.',
    'Crítico, resistência a efeitos, procs raros e pequenas viradas de combate.': 'Crítico, chance de Special Move, chance de Desvio Perfeito, procs raros e pequenas viradas de combate.',
    '<li>golpes possíveis;</li>': '<li>Basic Attack e Special Move de cada espécie;</li>',
    'receitas lendárias nomeadas continuam raras e vinculadas a conquistas específicas.': 'receitas lendárias nomeadas continuam raras e vinculadas a desafios específicos.',
    'hierarquia visual, dados públicos, tooltips, expansão, conquistas e possíveis regras futuras': 'hierarquia visual, dados públicos, tooltips, expansão e possíveis regras futuras',
}.items():
    html = html.replace(old, new)

species_block = '''<h3>4.2 Espécie, elemento, raridade e Vigor</h3>
<ul>
<li>o Alpha começa com <strong>nove espécies</strong>, uma para cada elemento;</li>
<li>cada espécie possui nome oficial, silhueta, status-base, <strong>Basic Attack</strong> e <strong>Special Move</strong> próprios;</li>
<li>todo Bud jogável possui <strong>exatamente um elemento</strong>;</li>
<li>todas as espécies disponíveis seguem as mesmas condições gerais de raridade e Vigor;</li>
<li>raridade e Vigor são calculados no nascimento, permanecem fixos e acompanham o Bud por toda a sua existência;</li>
<li>novas espécies, quando produzidas, entram em conjuntos completos de nove — uma por elemento — sem calendário ou quantidade previamente prometidos.</li>
</ul>'''
html = re.sub(r'<h3>4\.2 Espécie, elemento, raridade e Vigor</h3>\s*<ul>.*?</ul>', species_block, html, count=1, flags=re.S)

reset_block = '''<h3>4.7 Resets independentes por grupo de atributos</h3>
<p>Redistribuições não usam um reset geral. Atributos de Batalha e Atributos de Cultivo possuem direito, consumo e validação independentes.</p>
<div aria-label="Grupos independentes de reset" class="reset-grid">
<div class="reset-cluster"><strong>Atributos de Batalha</strong><p>Redefine somente FOR, AGI, VIT, INT, DEX e SOR distribuídos pelo Battle Level.</p></div>
<div class="reset-cluster"><strong>Atributos de Cultivo</strong><p>Redefine somente REC, COL, QLD, EFI, ADA e SUS distribuídos pelo Farm Level.</p></div>
</div>
<table>
<thead><tr><th>Situação</th><th>Regra</th></tr></thead>
<tbody>
<tr><td><strong>Jogador sem VIP</strong></td><td>Cada Bud possui uma utilização gratuita em cada grupo. Consumir o reset de Batalha não consome o de Cultivo, e vice-versa.</td></tr>
<tr><td><strong>Jogador com VIP ativo</strong></td><td>Pode realizar novos resets livremente em qualquer um dos dois grupos, sempre de forma separada.</td></tr>
<tr><td><strong>Negociação</strong></td><td>O estado gratuito de cada grupo pertence ao Bud. O comprador recebe exatamente a situação deixada pelo proprietário anterior.</td></tr>
<tr><td><strong>Marketplace</strong></td><td>A disponibilidade de cada reset gratuito deve aparecer nas informações detalhadas antes da compra.</td></tr>
<tr><td><strong>Backend</strong></td><td>Cada consumo é registrado por Bud e por grupo, com validação autoritativa e histórico auditável.</td></tr>
</tbody>
</table>'''
html = re.sub(r'<h3>4\.7 Resets independentes.*?</table>', reset_block, html, count=1, flags=re.S)

point5 = '''<section id="progressao">
<span class="tag">Longa, individual e com marcos</span>
<span class="review-state rs-validation">Em validação</span>
<h2>5. Progressão individual do Bud</h2>
<p>Não existe nível global capaz de elevar automaticamente todo o elenco. Cada Bud precisa ser usado, cultivado e desenvolvido individualmente. Na primeira temporada, Battle Level e Farm Level possuem cap 100, sem armazenamento de XP excedente.</p>
<div class="grid">
<div class="card good"><h3>O que queremos</h3><ul><li>apego ao espécime;</li><li>Buds veteranos com história;</li><li>especialização real;</li><li>valor baseado em nascimento, decisões e trabalho acumulado;</li><li>progressão horizontal depois do cap;</li><li>diferença relevante entre raridades e Vigor sem eliminar completamente o RNG.</li></ul></div>
<div class="card danger"><h3>O que evitar</h3><ul><li>elenco inteiro recebendo nível grátis;</li><li>árvores de habilidade individuais inviáveis de produzir;</li><li>barra de energia e microgerenciamento incompatíveis com o idle;</li><li>um único time resolvendo todo o PvE;</li><li>XP excedente transformando um futuro aumento de cap em avanço instantâneo.</li></ul></div>
</div>
<h3>5.1 Camadas de desenvolvimento</h3>
<div class="grid four">
<div class="card"><h4>Progressão permanente</h4><p>Battle Level, Farm Level, Atributos de Batalha, Atributos de Cultivo e histórico do espécime.</p></div>
<div class="card"><h4>Kit fixo da espécie</h4><p>Cada espécie possui um <strong>Basic Attack</strong> e um <strong>Special Move</strong> próprios e não intercambiáveis.</p></div>
<div class="card"><h4>Build substituível</h4><p>Núcleo Arcano e Totem adaptam o Bud e podem ser trocados conforme as regras de equipamento.</p></div>
<div class="card"><h4>Configuração estratégica</h4><p>Esquadrão, posição, atividade atual e política de automação. Prioridades de alvo são fixadas pelas posições, sem configuração manual.</p></div>
</div>
<p>Battle Level e Farm Level não precisam avançar na mesma velocidade. Um Bud pode ser especialista em cultivo, veterano de combate ou equilibrado entre as duas funções.</p>
<h3>5.2 Basic Attack e Special Move</h3>
<ul>
<li>cada espécie possui um Basic Attack fixo e um Special Move fixo;</li>
<li>o Special Move pode causar dano, curar, proteger, aplicar controle, buff ou debuff;</li>
<li>não existem árvores, pontos de habilidade, escolha ou troca de movimentos, barra de energia ou reset de habilidades na primeira temporada;</li>
<li>espécies do mesmo elemento podem cumprir funções diferentes por status-base e efeitos distintos de seus movimentos.</li>
</ul>
<h3>5.3 RNG controlado</h3>
<p>Raridade alta deve gerar vantagem real e valor econômico. Raridade, Vigor e SOR poderão aumentar de forma controlada a chance de ativar o Special Move e a chance de Desvio Perfeito, além de seus demais efeitos definidos no balanceamento.</p>
<div class="statement"><strong>O melhor Bud deve vencer com maior frequência, mas não obrigatoriamente.</strong> O RNG permite viradas ocasionais sem transformar uma diferença grande de poder em moeda ao ar.</div>
<p>Probabilidades e tetos exatos serão definidos por protótipo para impedir spam de Special Move, esquiva excessiva ou distâncias impossíveis de recuperar.</p>
<h3>5.4 Catálogo inicial e expansão</h3>
<ul>
<li>o Alpha começa com <strong>nove espécies</strong>, uma por elemento;</li>
<li>não existe compromisso de chegar a 18, 54, 81 ou qualquer outra quantidade em uma data específica;</li>
<li>quando houver capacidade de produção e balanceamento, novas espécies serão lançadas em conjuntos completos de nove, uma por elemento;</li>
<li>cada nova espécie terá status-base, Basic Attack, Special Move e função próprios;</li>
<li>a prioridade é ampliar o catálogo no ritmo viável, sem competir com a produção de inimigos, mapas, sistemas e balanceamento.</li>
</ul>
<h3>5.5 Sementes e pool atual</h3>
<p>Enquanto houver uma única espécie em determinado elemento, a semente desse elemento inevitavelmente gera aquele Bud. Ainda assim, espécie, raridade, Vigor e demais valores individuais são resolvidos e persistidos pelo servidor somente no nascimento.</p>
<p>Sementes antigas utilizam a pool de espécies disponível no momento em que brotam. Portanto, guardar sementes antes de uma expansão é uma estratégia legítima dos jogadores, não um exploit.</p>
<h3>5.6 Cap e continuidade</h3>
<ul>
<li>Battle Level máximo na primeira temporada: <strong>100</strong>;</li>
<li>Farm Level máximo na primeira temporada: <strong>100</strong>;</li>
<li>não existe armazenamento de XP excedente no cap;</li>
<li>ao chegar ao cap, o valor do Bud continua por build, elenco, itemização, rerolls, jardins, mapas, PvP e otimização.</li>
</ul>
<div class="statement"><strong>O cap encerra a corrida vertical de um Bud, não a vida útil dele.</strong></div>
<h3>5.7 Progressão do Jardineiro</h3>
<span class="review-state rs-open">Em aberto</span>
<p>Ainda precisa ser decidido se a conta terá um nível próprio de Jardineiro para desbloquear possibilidades ou se a progressão global ocorrerá apenas por mapas, construções, receitas e sistemas específicos. Em qualquer cenário, a conta não deve aumentar diretamente os status de todos os Buds.</p>
</section>'''
html = re.sub(r'<section id="progressao">.*?</section>', point5, html, count=1, flags=re.S)

html = html.replace('Define o tipo do futuro Bud e ativa a distribuição-base configurada para sementes daquele elemento.', 'Define o elemento do futuro Bud. A espécie é sorteada entre as espécies daquele elemento disponíveis no momento do nascimento.')
html = html.replace('<li>apenas o tipo é conhecido antes do nascimento;</li>', '<li>apenas o elemento é conhecido antes do nascimento;</li>')
html = html.replace('<li>plot e insumos alteram probabilidades;</li>', '<li>plot e insumos alteram probabilidades;</li><li>a espécie usa a pool disponível no momento do nascimento, inclusive para sementes obtidas anteriormente;</li>', 1)
html = html.replace('sementes elementais com espécie, raridade e Vigor ocultos até o brotar;', 'sementes elementais com resultado individual resolvido apenas no brotar e pool de espécies atual;')

needle = '<div class="decision"><div><strong>Progressão individual</strong><p>Cada Bud sobe Battle Level e Farm Level e distribui separadamente Atributos de Batalha e Atributos de Cultivo.</p></div><span class="status s-defined">Definido</span></div>'
addition = needle + '''
<div class="decision"><div><strong>Kit da espécie</strong><p>Cada espécie possui Basic Attack e Special Move próprios e fixos, sem árvore, pontos, troca de movimentos ou barra de energia.</p></div><span class="status s-defined">Definido</span></div>
<div class="decision"><div><strong>Espécies do Alpha</strong><p>Nove espécies, uma por elemento. Expansões futuras entram em conjuntos completos de nove, sem calendário prometido.</p></div><span class="status s-defined">Definido</span></div>
<div class="decision"><div><strong>Pool das sementes</strong><p>Sementes usam a pool disponível no momento do nascimento, mesmo quando foram obtidas antes da chegada de espécies novas.</p></div><span class="status s-defined">Definido</span></div>
<div class="decision"><div><strong>RNG de combate</strong><p>Raridade, Vigor e SOR podem elevar Special Move e Desvio Perfeito sob tetos de balanceamento.</p></div><span class="status s-rule">Regra-base</span></div>'''
html = html.replace(needle, addition, 1)

html = re.sub(r'<li><strong>Espécies:</strong>.*?</li>', '<li><strong>Espécies iniciais:</strong> nomes, status-base, Basic Attack, Special Move e função de cada um dos nove Buds do Alpha.</li>', html, count=1, flags=re.S)
html = re.sub(r'<li><strong>Habilidades:</strong>.*?</li>', '<li><strong>Movimentos:</strong> efeitos, números, animações, frequência-base e limites de Basic Attack e Special Move.</li>', html, count=1, flags=re.S)
html = html.replace('<strong>Reset por cluster:</strong>', '<strong>Reset por grupo:</strong>')
html = html.replace('conteúdo exato do cluster de reset', 'conteúdo exato do grupo de reset')
html = re.sub(r'<li><strong>Caps futuros:</strong>.*?</li>', '', html, count=1, flags=re.S)
marker = '<li><strong>Reset por grupo:</strong> UX, confirmação, logs, sincronização do VIP e apresentação dos direitos gratuitos no mercado.</li>'
html = html.replace(marker, marker + '<li><strong>Progressão do Jardineiro:</strong> nível de conta ou desbloqueios por sistemas, sem bônus direto de status para todo o elenco.</li>', 1)

for old, new in {
    'por cluster': 'por grupo',
    'cada cluster': 'cada grupo',
    'Clusters independentes': 'Grupos independentes',
    'clusters independentes': 'grupos independentes',
    'situação do reset gratuito em cada cluster': 'situação do reset gratuito em cada grupo',
}.items():
    html = html.replace(old, new)

assert '<section id="progressao">' in html
assert 'nove espécies' in html
assert 'Basic Attack' in html and 'Special Move' in html
assert '<strong>Habilidades</strong>' not in html
assert 'quatro a oito espécies' not in html
assert 'árvores biológicas gigantes' not in html
assert 'Game Design Document · v8' in html

dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_text(html, encoding='utf-8')
print(f'Built {dst} ({dst.stat().st_size} bytes)')
