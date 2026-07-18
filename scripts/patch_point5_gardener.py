#!/usr/bin/env python3
from pathlib import Path
import re
import sys

path = Path(sys.argv[1])
html = path.read_text(encoding="utf-8")

html = html.replace("Game Design Document · v9", "Game Design Document · v10")

section = '''<h3>5.7 Progressão do Jardineiro</h3>
<span class="review-state rs-defined">Definido</span>
<p>A conta possui um <strong>Nível do Jardineiro</strong> próprio, separado do Battle Level e do Farm Level de cada Bud. Ele representa a maturidade operacional da conta e organiza a liberação gradual de sistemas, capacidade e ferramentas.</p>
<div class="statement"><strong>O Jardineiro desbloqueia possibilidades. O Bud desenvolve poder.</strong> Nenhum nível global concede atributos, levels ou força automática ao elenco inteiro.</div>

<h4>5.7.1 Três trilhas complementares</h4>
<p>A progressão global mistura três fontes de desbloqueio. Elas podem trabalhar em conjunto, mas cumprem papéis diferentes e não devem ser tratadas como substitutas umas das outras.</p>
<div class="grid">
<div class="card good"><h4>Nível do Jardineiro</h4><p><strong>Libera estrutura e complexidade.</strong></p><ul><li>novos jardins e aumento de capacidade operacional;</li><li>acesso gradual às operações da Forja;</li><li>mais funções e limites-base do mercado;</li><li>novos tipos de atividade e gestão;</li><li>ferramentas de organização e qualidade de vida.</li></ul></div>
<div class="card"><h4>Progressão nos mapas</h4><p><strong>Libera conteúdo do mundo.</strong></p><ul><li>novas regiões, fases e atividades;</li><li>materiais, sementes e ingredientes regionais;</li><li>tipos de plots e recursos avançados;</li><li>famílias de receitas e linhas de pesquisa;</li><li>bosses, minibosses e recompensas específicas.</li></ul></div>
<div class="card"><h4>VIP</h4><p><strong>Amplia eficiência, capacidade e conforto.</strong></p><ul><li>mais processos simultâneos;</li><li>automações, presets e ferramentas avançadas;</li><li>maior aproveitamento do tempo offline;</li><li>resets adicionais e redução de atrito operacional;</li><li>acelerações controladas sobre sistemas já desbloqueados.</li></ul></div>
</div>

<h4>5.7.2 Como os desbloqueios se combinam</h4>
<table>
<thead><tr><th>Fonte</th><th>Responsabilidade</th><th>Exemplo prático</th></tr></thead>
<tbody>
<tr><td><strong>Nível do Jardineiro</strong></td><td>Libera o sistema ou sua capacidade estrutural.</td><td>O nível permite usar Fusão, abrir outro jardim ou ampliar um limite-base.</td></tr>
<tr><td><strong>Mapas</strong></td><td>Libera o conteúdo que alimenta o sistema.</td><td>Uma região ou boss libera materiais e uma família específica de Núcleos.</td></tr>
<tr><td><strong>VIP</strong></td><td>Melhora a operação do que já foi liberado.</td><td>Adiciona uma fila, um preset ou reduz o tempo de um processo acessível.</td></tr>
</tbody>
</table>
<p>Um desbloqueio pode exigir simultaneamente nível e progresso no mundo. Exemplo: o Jardineiro alcança o nível necessário para utilizar Ascensão, mas determinadas receitas e componentes continuam dependendo da exploração de regiões específicas.</p>
<div class="statement"><strong>O nível libera sistemas. O mapa libera conteúdo. O VIP aumenta eficiência, capacidade e conforto.</strong></div>

<h4>5.7.3 Benefícios exclusivos de VIP</h4>
<p>Alguns recursos podem permanecer exclusivos do VIP porque ampliam a operação sem remover do jogador gratuito o acesso ao conteúdo principal:</p>
<ul>
<li>filas adicionais de germinação, recuperação, pesquisa ou Forja;</li>
<li>mais presets de esquadrão e automações avançadas;</li>
<li>mais slots simultâneos de venda no marketplace;</li>
<li>filtros, organização e ferramentas avançadas de gestão;</li>
<li>resets de Atributos de Batalha e de Cultivo após o direito gratuito de cada grupo;</li>
<li>maior duração máxima de progresso offline.</li>
</ul>

<h4>5.7.4 Sistemas acelerados pelo VIP</h4>
<p>Outros sistemas continuam disponíveis para todos, mas podem operar de forma mais eficiente com VIP ativo:</p>
<ul>
<li>germinação e recuperação;</li>
<li>crafting, pesquisa e processos da Forja;</li>
<li>ganho de XP do Jardineiro;</li>
<li>produção e ciclos dos jardins;</li>
<li>desmontagem e recuperação de materiais;</li>
<li>outros tempos e limites operacionais definidos no balanceamento.</li>
</ul>
<p>O VIP não ignora requisitos de nível, mapa, materiais, receitas ou progressão. Ele melhora a execução de sistemas aos quais a conta já possui acesso.</p>

<h4>5.7.5 Limites de monetização</h4>
<ul>
<li>regiões principais, espécies jogáveis e receitas essenciais não ficam disponíveis somente para VIP;</li>
<li>o jogador gratuito pode acessar o loop principal, avançar, produzir, batalhar, negociar e competir;</li>
<li>VIP não concede Battle Level, Farm Level ou atributos diretamente aos Buds;</li>
<li>VIP não substitui exploração, materiais, requisitos de mapa ou domínio dos sistemas;</li>
<li>a vantagem deve ser forte e perceptível, mas concentrada em eficiência, paralelismo, automação e conforto.</li>
</ul>
<div class="statement"><strong>Sem VIP, o jogo funciona por inteiro. Com VIP, a operação fica significativamente mais rápida, ampla e confortável.</strong></div>

<h4>5.7.6 O que permanece para balanceamento</h4>
<p>A estrutura está definida. Permanecem em aberto apenas os números e a distribuição concreta: curva e fontes de XP, cap do Nível do Jardineiro, ordem exata dos desbloqueios, quantidade de filas e presets, duração offline, percentuais de aceleração e eventuais variações por temporada.</p>
</section>'''

pattern = r'<h3>5\.7(?:.|\n)*?</section>'
html, replacements = re.subn(pattern, section, html, count=1, flags=re.S)
if replacements != 1:
    raise RuntimeError(f"Esperava substituir uma seção 5.7; substituições realizadas: {replacements}")

assert "5.7 Progressão do Jardineiro" in html
assert "rs-defined\">Definido" in html
assert "O nível libera sistemas. O mapa libera conteúdo. O VIP aumenta eficiência, capacidade e conforto." in html
assert "O VIP não ignora requisitos de nível" in html
assert "Ainda precisa ser decidido se a conta terá um nível próprio de Jardineiro" not in html
assert "Game Design Document · v10" in html

path.write_text(html, encoding="utf-8")
print(f"Patched {path} ({path.stat().st_size} bytes)")
