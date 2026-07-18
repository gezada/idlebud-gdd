#!/usr/bin/env python3
from pathlib import Path
import re
import sys

path = Path(sys.argv[1])
html = path.read_text(encoding="utf-8")

if "Game Design Document · v10" in html:
    html = html.replace("Game Design Document · v10", "Game Design Document · v11", 1)
else:
    raise RuntimeError("Versão-base esperada (v10) não encontrada no HTML.")

section = '''<section id="battle-level">
<span class="tag red">Battle Level</span>
<span class="review-state rs-defined">Definido</span>
<h2>6. Battle Level, Atributos de Batalha e Poder de Combate</h2>
<p>O Battle Level é individual, possui cap 100 na primeira temporada e avança exclusivamente por participação válida em PvE e PvP. Ele não compartilha experiência com o Farm Level e não eleva automaticamente outros Buds da conta.</p>
<div class="statement"><strong>Cada nível concede uma decisão.</strong> O crescimento natural da espécie, os pontos inatos do nascimento e a distribuição do jogador formam camadas diferentes da identidade de combate.</div>

<h3>6.1 Battle XP, Farm XP e pontos por nível</h3>
<table>
<thead><tr><th>Trilha</th><th>Fonte de experiência</th><th>Pontos concedidos</th></tr></thead>
<tbody>
<tr><td><strong>Battle Level</strong></td><td>Participação válida em batalhas PvE e PvP.</td><td>Um Ponto de Batalha por nível.</td></tr>
<tr><td><strong>Farm Level</strong></td><td>Produção no plot e recuperação legítima enquanto o Bud está alocado no jardim.</td><td>Um Ponto de Cultivo por nível.</td></tr>
</tbody>
</table>
<ul>
<li>todo Bud nasce no <strong>Battle Level 1</strong> e no <strong>Farm Level 1</strong>;</li>
<li>cada trilha começa com um ponto distribuível no nível 1 e concede mais um a cada novo nível;</li>
<li>do nível 1 ao 100, cada trilha entrega exatamente <strong>100 pontos distribuíveis</strong>;</li>
<li>Battle XP nunca aumenta Farm Level, e Farm XP nunca aumenta Battle Level;</li>
<li>recuperação pode conceder Farm XP, mas em ritmo menor e com validação por ciclo para impedir loops artificiais de dano e cura;</li>
<li>XP excedente não é armazenada ao atingir o cap.</li>
</ul>

<h3>6.2 Pontos Inatos de nascimento</h3>
<p>Cada Bud nasce com duas distribuições aleatórias independentes, calculadas e persistidas pelo servidor no nascimento:</p>
<div class="grid">
<div class="card good"><h4>24 Pontos Inatos de Batalha</h4><p>Distribuídos entre FOR, AGI, VIT, INT, DEX e SOR.</p></div>
<div class="card"><h4>24 Pontos Inatos de Cultivo</h4><p>Distribuídos entre REC, COL, QLD, EFI, ADA e SUS.</p></div>
</div>
<ul>
<li>cada atributo recebe no mínimo <strong>1</strong> e no máximo <strong>10</strong> pontos inatos;</li>
<li>o total de cada grupo é sempre 24; a aleatoriedade cria especialização, não vantagem de pontos totais;</li>
<li>os Pontos Inatos são permanentes, visíveis, não rerroláveis e não são afetados por reset;</li>
<li>as distribuições de Batalha e Cultivo são sorteadas separadamente;</li>
<li>o backend registra o resultado de forma autoritativa e auditável.</li>
</ul>
<div class="statement"><strong>Exemplo:</strong> um Bud com 5 SOR inato pode chegar a 105 SOR base ao investir os 100 pontos distribuíveis em SOR. Outro que nasce com 10 SOR pode chegar a 110. Núcleo Arcano e Totem ainda podem elevar o resultado final além desse valor-base.</div>

<h3>6.3 Distribuição, crescimento e reset</h3>
<ul>
<li>cada aumento de atributo custa sempre <strong>1 ponto</strong>; não existe custo progressivo;</li>
<li>o jogador distribui livremente os 100 pontos obtidos por Battle Level;</li>
<li>não existe um cap artificial por atributo além da quantidade total disponível;</li>
<li>os status-base da espécie crescem com o Battle Level independentemente da distribuição;</li>
<li>o reset de Atributos de Batalha devolve apenas os pontos distribuíveis e preserva os Pontos Inatos;</li>
<li>cada Bud possui um reset gratuito de Batalha; VIP permite resets adicionais conforme as regras já definidas;</li>
<li>o estado do reset pertence ao Bud e acompanha sua transferência no marketplace.</li>
</ul>
<p>Essa estrutura permite que dois Buds da mesma espécie, level, raridade e Vigor ainda apresentem inclinações naturais e builds diferentes.</p>

<h3>6.4 Função dos seis Atributos de Batalha</h3>
<div class="grid three">
<div class="card attribute"><div class="abbr">FOR</div><div><h4>Força</h4><p>Alimenta o ATK e o dano físico.</p></div></div>
<div class="card attribute"><div class="abbr">AGI</div><div><h4>Agilidade</h4><p>Alimenta Velocidade de Ação e Esquiva normal.</p></div></div>
<div class="card attribute"><div class="abbr">VIT</div><div><h4>Vitalidade</h4><p>Alimenta HP, DEF e Resistência a Controle.</p></div></div>
<div class="card attribute"><div class="abbr">INT</div><div><h4>Inteligência</h4><p>Alimenta MATK, MDEF, cura e escudos.</p></div></div>
<div class="card attribute"><div class="abbr">DEX</div><div><h4>Destreza</h4><p>Alimenta Precisão, Penetração e Potência de Controle.</p></div></div>
<div class="card attribute"><div class="abbr">SOR</div><div><h4>Sorte</h4><p>Alimenta Crítico, Special Move, Desvio Perfeito e ativações probabilísticas elegíveis.</p></div></div>
</div>
<div class="grid">
<div class="card blue"><h4>Potência de Controle</h4><p>Define quanto da duração ou intensidade de um controle é preservada ao enfrentar a Resistência a Controle do alvo. Um golpe que acerta não precisa vencer uma terceira rolagem binária; potência e resistência modulam o efeito.</p></div>
<div class="card"><h4>Ativações probabilísticas elegíveis</h4><p>São passivas de Núcleo Arcano ou Totem marcadas para escalar com SOR, como uma chance de aplicar Veneno ou proteger um aliado. Nem toda passiva probabilística precisa receber essa escala.</p></div>
</div>

<h3>6.5 Status derivados exibidos</h3>
<p>Os atributos são pontos de construção. O combate e a ficha utilizam os status derivados abaixo:</p>
<table>
<thead><tr><th>Categoria</th><th>Status</th></tr></thead>
<tbody>
<tr><td><strong>Ofensivos</strong></td><td>ATK, MATK, Precisão, Penetração e Crítico.</td></tr>
<tr><td><strong>Defensivos</strong></td><td>HP, DEF, MDEF, Esquiva, Resistência a Controle e Desvio Perfeito.</td></tr>
<tr><td><strong>Ritmo e utilidade</strong></td><td>Velocidade de Ação, Potência de Controle e Chance de Special Move.</td></tr>
</tbody>
</table>
<ul>
<li>cura e escudo não possuem status separados: utilizam MATK e o coeficiente do Special Move;</li>
<li>o dano crítico começa fixado em <strong>150%</strong>;</li>
<li>Esquiva representa a evasão normal; Desvio Perfeito é uma chance rara e separada;</li>
<li>a ficha apresenta os valores finais e, em detalhe, suas principais fontes.</li>
</ul>

<h3>6.6 Núcleo Arcano e Totem: únicos attachments</h3>
<div class="card warn"><strong>Não existem equipamentos adicionais.</strong><p>Idle Bud não possui armas, armaduras, acessórios ou outros slots. A build externa de cada Bud é composta exclusivamente por <strong>um Núcleo Arcano</strong> e <strong>um Totem</strong>.</p></div>
<p>Núcleo e Totem podem fornecer bônus planos, bônus percentuais e passivas. Esses efeitos entram no cálculo conforme sua natureza, sem criar uma categoria genérica de “equipamentos”.</p>

<h3>6.7 Ordem única de cálculo</h3>
<ol>
<li>status-base da espécie no Battle Level atual;</li>
<li>contribuição dos Pontos Inatos e dos pontos distribuídos;</li>
<li>bônus planos do Núcleo Arcano e do Totem;</li>
<li>multiplicador de raridade;</li>
<li>multiplicador de Vigor;</li>
<li>bônus percentuais e passivas do Núcleo Arcano e do Totem;</li>
<li>conversão dos scores em chances, com retornos decrescentes e hard caps;</li>
<li>buffs, debuffs, elemento, posição e efeitos de equipe aplicados durante o confronto.</li>
</ol>
<div class="formula">Status permanente = (Status-base da espécie no level + contribuição dos atributos + bônus planos dos attachments) × Multiplicador de Raridade × Multiplicador de Vigor × (1 + bônus percentuais somados de Núcleo e Totem)</div>
<p>Bônus percentuais de Núcleo e Totem são somados em uma única camada antes da multiplicação. Passivas com lógica própria são avaliadas separadamente. Modificadores temporários entram por último e não alteram a ficha permanente exibida no marketplace.</p>

<h3>6.8 Raridade e Vigor</h3>
<p>Raridade e Vigor são definidos no nascimento, permanecem fixos e multiplicam todos os status permanentes de batalha. Também multiplicam os scores brutos que serão convertidos em Crítico, Chance de Special Move e Desvio Perfeito antes dos retornos decrescentes e tetos.</p>
<div class="formula">Bônus de Vigor = ((Vigor − 50) ÷ 450) × 5%</div>
<table>
<thead><tr><th>Raridade</th><th>Faixa de Vigor</th><th>Bônus de raridade</th></tr></thead>
<tbody>
<tr><td><strong>Comum</strong></td><td>50–220</td><td>0%</td></tr>
<tr><td><strong>Incomum</strong></td><td>130–280</td><td>1%</td></tr>
<tr><td><strong>Rara</strong></td><td>210–350</td><td>2%</td></tr>
<tr><td><strong>Épica</strong></td><td>290–430</td><td>3,5%</td></tr>
<tr><td><strong>Lendária</strong></td><td>360–500</td><td>5%</td></tr>
</tbody>
</table>
<div class="formula">Multiplicador combinado = (1 + bônus de raridade) × (1 + bônus de Vigor)</div>
<p>Um Lendário de Vigor 500 atinge multiplicador <strong>1,1025×</strong>: 10,25% acima de um Comum de Vigor 50 quando todo o restante é idêntico. Essa vantagem é relevante, mas não produz sozinha o extremo competitivo de 96% contra 4%.</p>
<div class="card blue"><strong>Limite de função:</strong><p>Raridade e Vigor não aumentam XP, drop, produção, Farm Level, Pontos Inatos, pontos distribuíveis ou velocidade de progressão.</p></div>

<h3>6.9 Retornos decrescentes e hard caps</h3>
<p>Status percentuais perigosos recebem simultaneamente retorno decrescente e teto absoluto. Continuar investindo ainda melhora o resultado, mas cada ponto adicional entrega menos porcentagem.</p>
<div class="formula">Chance final = Base + (Teto − Base) × Score ÷ (Score + K)</div>
<p><strong>K</strong> controla a velocidade da curva: quando o Score é igual a K, o status percorreu metade do caminho entre a chance-base e o teto.</p>
<table>
<thead><tr><th>Status</th><th>Limite inicial de protótipo</th></tr></thead>
<tbody>
<tr><td>Crítico</td><td>40%</td></tr>
<tr><td>Esquiva normal</td><td>35%</td></tr>
<tr><td>Desvio Perfeito</td><td>12%</td></tr>
<tr><td>Special Move</td><td>25% por ação</td></tr>
<tr><td>Penetração</td><td>45%</td></tr>
<tr><td>Redução da duração/intensidade de controles</td><td>50%</td></tr>
<tr><td>Chance final de acerto</td><td>Mínimo 15% e máximo 95%</td></tr>
<tr><td>Frequência de ação</td><td>Máximo 1,75× a frequência-base da espécie</td></tr>
<tr><td>Mitigação por DEF ou MDEF</td><td>75%</td></tr>
</tbody>
</table>
<p>SOR alimenta scores diferentes; 100 SOR não representa +100% simultâneo em Crítico, Special Move e Desvio Perfeito. Os valores de K e coeficientes de conversão serão calibrados no simulador.</p>

<h3>6.10 Probabilidade competitiva entre 4% e 96%</h3>
<p>O limite de vitória vale para o <strong>confronto competitivo completo</strong>, não para raridade contra raridade isoladamente. Level, Pontos Inatos, distribuição, Núcleo, Totem, elementos, posições, movimentos e composição participam da estimativa.</p>
<div class="formula">P(A vencer) = 4% + 92% × R⁴ ÷ (1 + R⁴)</div>
<p><strong>R</strong> é a razão entre os Poderes de Confronto ajustados das duas equipes.</p>
<table>
<thead><tr><th>Razão de poder R</th><th>Probabilidade aproximada</th></tr></thead>
<tbody>
<tr><td>1,00×</td><td>50% × 50%</td></tr>
<tr><td>1,25×</td><td>69% × 31%</td></tr>
<tr><td>1,50×</td><td>81% × 19%</td></tr>
<tr><td>2,00×</td><td>91% × 9%</td></tr>
<tr><td>4,00× ou mais</td><td>aproxima-se de 96% × 4%</td></tr>
</tbody>
</table>
<ul>
<li>um Comum muito fraco pode chegar a 4% contra um Lendário extremamente forte somente quando o pacote completo justificar essa distância;</li>
<li>raridade e Vigor isolados não determinam 4% contra 96%;</li>
<li>o piso e o teto valem para confrontos competitivos válidos e comparáveis;</li>
<li>não se aplicam obrigatoriamente a PvE, como um Bud inicial contra um boss endgame.</li>
</ul>
<div class="statement"><strong>O melhor conjunto deve vencer com muito mais frequência, nunca com certeza matemática absoluta dentro da competição válida.</strong></div>

<h3>6.11 Poder de Batalha (CP) e Poder de Confronto</h3>
<p>Cada Bud possui um número geral de <strong>Poder de Batalha (CP)</strong> para leitura rápida, comparação e marketplace. O CP é uma estimativa estável da ficha permanente; ele não resolve o combate e não deve restringir a formação de equipes.</p>
<div class="formula">CP = C × √(Impacto Esperado × Sobrevivência Efetiva)</div>
<div class="grid">
<div class="card"><h4>Impacto Esperado</h4><p>Dano médio do Basic Attack, valor esperado do Special Move, precisão, crítico, cura, escudos, controle, buffs e debuffs convertidos em contribuição equivalente.</p></div>
<div class="card"><h4>Sobrevivência Efetiva</h4><p>HP, DEF, MDEF, Esquiva, Desvio Perfeito e Resistência a Controle.</p></div>
</div>
<ul>
<li>a média geométrica impede que somente ataque ou somente resistência inflem o CP;</li>
<li>suportes recebem valor por cura, escudo, controle, buffs e debuffs;</li>
<li><strong>C</strong> é um coeficiente de normalização para produzir números legíveis;</li>
<li>o CP não considera adversário específico, vantagem elemental, posição, composição, sinergias ou modificadores temporários.</li>
</ul>
<p>Para prever um matchup, o servidor calcula um <strong>Poder de Confronto</strong>: parte do CP agregado da equipe e adiciona elementos, posições, composição, sinergias, counters e condições específicas. A razão entre os Poderes de Confronto alimenta a curva de 4% a 96%.</p>

<h3>6.12 Autoridade, precisão e balanceamento restante</h3>
<ul>
<li>nascimento, pontos inatos, status, chances, caps, CP e Poder de Confronto são calculados pelo servidor;</li>
<li>a ordem de operações é única para PvE, PvP, ficha e marketplace;</li>
<li>arredondamentos acontecem somente nos pontos definidos pela implementação, nunca em cada camada intermediária;</li>
<li>logs de combate devem permitir reconstruir os principais valores e ativações;</li>
<li>coeficientes por espécie, contribuição de cada atributo, valores de K, normalização C e pesos de cura, controle e utilidade permanecem para simulador, Alpha e patches;</li>
<li>ajustes numéricos podem ocorrer sem alterar as regras estruturais definidas neste ponto.</li>
</ul>
</section>'''

html, replacements = re.subn(r'<section id="battle-level">.*?</section>', section, html, count=1, flags=re.S)
if replacements != 1:
    raise RuntimeError(f"Esperava substituir uma seção battle-level; substituições realizadas: {replacements}")

decision_pattern = re.compile(
    r'<div class="decision"><div><strong>Battle Level</strong>.*?'
    r'<div class="decision"><div><strong>Raridade da planta</strong>.*?</div><span class="status [^"]+">.*?</span></div>',
    re.S,
)
decisions = '''<div class="decision"><div><strong>Battle e Farm Level</strong><p>Trilhas independentes: um ponto por level, 100 pontos distribuíveis por grupo no cap 100; Battle XP vem de PvE/PvP e Farm XP de plot e recuperação validada.</p></div><span class="status s-defined">Definido</span></div>
<div class="decision"><div><strong>Pontos Inatos</strong><p>Cada Bud nasce com 24 pontos em Batalha e 24 em Cultivo, distribuídos separadamente entre 1 e 10 por atributo; são permanentes e não resetáveis.</p></div><span class="status s-defined">Definido</span></div>
<div class="decision"><div><strong>Atributos de Batalha</strong><p>FOR, AGI, VIT, INT, DEX e SOR alimentam 14 status derivados com funções distintas e compreensíveis.</p></div><span class="status s-defined">Definido</span></div>
<div class="decision"><div><strong>Attachments de combate</strong><p>Somente Núcleo Arcano e Totem compõem a build externa; não existem armas, armaduras, acessórios ou outros equipamentos.</p></div><span class="status s-defined">Definido</span></div>
<div class="decision"><div><strong>Vigor e raridade</strong><p>Usam as faixas e bônus definidos, multiplicam todos os status permanentes de batalha e chegam juntos a 1,1025× no extremo Lendário 500.</p></div><span class="status s-defined">Definido</span></div>
<div class="decision"><div><strong>Caps de combate</strong><p>Status percentuais usam retornos decrescentes e hard caps; os tetos iniciais do protótipo estão registrados no Ponto 6.</p></div><span class="status s-defined">Definido</span></div>
<div class="decision"><div><strong>Probabilidade competitiva</strong><p>A chance prevista do confronto completo fica entre 4% e 96%; raridade isolada não determina o resultado.</p></div><span class="status s-defined">Definido</span></div>
<div class="decision"><div><strong>CP e Poder de Confronto</strong><p>CP resume a ficha permanente; Poder de Confronto adiciona matchup, elementos, posição e composição para estimar a vitória.</p></div><span class="status s-defined">Definido</span></div>'''
html, replacements = decision_pattern.subn(decisions, html, count=1)
if replacements != 1:
    raise RuntimeError(f"Não foi possível atualizar as decisões consolidadas do Ponto 6: {replacements}")

html = re.sub(
    r'<li><strong>Status derivados:</strong>.*?</li>',
    '<li><strong>Balanceamento de combate:</strong> coeficientes por espécie e atributo, valores de K, arredondamentos, escala visual do CP, pesos de cura/controle/utilidade e calibração dos tetos no simulador.</li>',
    html,
    count=1,
    flags=re.S,
)
html = re.sub(
    r'<li><strong>Battle XP:</strong>.*?</li>',
    '<li><strong>Battle XP:</strong> curva, teto por combate, participação mínima válida, carry e penalidade de overlevel.</li>',
    html,
    count=1,
    flags=re.S,
)
html = re.sub(
    r'<li><strong>Farm XP:</strong>.*?</li>',
    '<li><strong>Farm XP:</strong> curva, produção por plot, ganho reduzido em recuperação, fadiga e proteções contra ciclos artificiais.</li>',
    html,
    count=1,
    flags=re.S,
)

required = [
    'Game Design Document · v11',
    '6. Battle Level, Atributos de Batalha e Poder de Combate',
    '24 Pontos Inatos de Batalha',
    '24 Pontos Inatos de Cultivo',
    '100 pontos distribuíveis',
    'Potência de Controle',
    'ativações probabilísticas elegíveis',
    'Não existem equipamentos adicionais',
    'Multiplicador combinado = (1 + bônus de raridade) × (1 + bônus de Vigor)',
    '1,1025×',
    'Chance final = Base + (Teto − Base) × Score ÷ (Score + K)',
    'P(A vencer) = 4% + 92% × R⁴ ÷ (1 + R⁴)',
    'CP = C × √(Impacto Esperado × Sobrevivência Efetiva)',
    'Poder de Confronto',
]
for item in required:
    assert item in html, f"Conteúdo obrigatório ausente: {item}"

battle = re.search(r'<section id="battle-level">.*?</section>', html, re.S)
assert battle is not None
battle_html = battle.group(0)
for stale in [
    'review-state rs-provisional',
    'geração de energia',
    'execução de skills',
    'procs raros',
    'bônus provisório',
]:
    assert stale not in battle_html, f"Texto obsoleto encontrado no Ponto 6: {stale}"

path.write_text(html, encoding="utf-8")
print(f"Patched {path} ({path.stat().st_size} bytes)")
