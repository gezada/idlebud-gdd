#!/usr/bin/env python3
from pathlib import Path
import base64
import gzip
import re
import sys

path = Path(sys.argv[1])
html = path.read_text(encoding="utf-8")

if "Game Design Document · v14" in html:
    html = html.replace("Game Design Document · v14", "Game Design Document · v15", 1)
elif "Game Design Document · v15" not in html:
    raise RuntimeError("Versão-base esperada (v14) não encontrada no HTML.")

def unpack(payload: str) -> str:
    return gzip.decompress(base64.b64decode(payload)).decode("utf-8")

SECTION = unpack("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")
DECISIONS = unpack("H4sIAMw/XmoC/71WTY/cRBC98ytKK+2JgdlJskvEDCMFWKRIKIySCOXa4y47HdndTn9YCyf+AweuoByiHHLacMnV/4Rfwqu2PfFAJA5Ic7DH9nRXV71+71VvtOmoqFUIX51pLkwwzp5tN/i63YTona22z3bUOk/GmsZUjpgK5f1PtOuuN8txyKbdfqO0OozRXOIxmk41bCPj3XsXlXZUeKMoNQohXU2luVGEtYw2Wh6sakwxzsHNM7lAXycdiGuu+rcdm0CFs6XzDaKakj3b/jWmMtXccb2mxvmISTxOa8hzdN46mRaNTaqZxfp8s2y3m+VQbavshESIKqZA4bNcCOuz7be5Iu1QMsaNcz7Z/Dd630talFpkVHrVv+7/5DDH7QcKVrXhuYvUv5EkK64FKKsyAkB1Tc92C+KbgvUADDX9+zqatkad9RgeyfavHLXeFRwCAgRCzWwLIJ8BdQgBLIKAU6rOeS4AjhOYqFGAFdkVCIDVyXmN/77465dfL3Fd4bqH6w6uu7hWJ0DtO2ywgIWS/sGzJwwIWhfMACXIaPt3FqzJm70a8zz8LgjEKn0Grv9dyKCqpLygavCt8gp3ocssZCkcpH3tXibOSOqUh1F0CKYoIpoScp8AiCcRkrCZ4CMdPio82cVWVcgOeRamxbesojV1wAvZowrZ8T0w0hxEC5ksFRgRTOdIRbBvdXG+AAUbgsBZOzsEwUDlFRUGqoX4EygEBr6F1EXodAo6PB41bP9FByl85i6jxkU9sC0exa8y8RV2EWNU298GurqgwFWy2N41PerfFzWLtT11EQi1Tmfj0Oln4wdoLgUaxuaXKuCnUHuFAMIIIAvP8XCihl4kwHUKV7k+EnYuVXvXHjnLh6/0ov9DsHmZTIiZ0aNZcGDf5Q9IvjOxv4U9LyZAFxRNwy5FcolQMMCybi08ck3LNkBy2H/ELeqUA/KNqWaBToDDQ9u5YnRVVLt3IeChSbBH2ag5HEdDraSr5QaUUF2GaT3Nh8MinfEl9Le5RhZOhKTCEQADm9QE2azzifFkn24G0pzCNeFzHIxse/Ift8+nEET4kh6Jv9Z0b3klpS7oujbwt6vlfXmV5ona6f5ydSHv67FKR+MCi6nRo/IiAW3Y5aery3OULE0HzxfntMPQOGUB+xCbugvVnQCHHx/u6E7/m5Aacm4ddkzVR57pGh6ODSEbuYaIRPSQNPRewzGtWMXk+4r2Kqr6ufhfyz5ARdP55NALwuATU8ShbDCLb1ozoYCQSG2BVZphFeXFmcBW0eAJgHmQYIc4aqFSPetjc2geHGo9mKkryxoLi/uKX2Bhv8a/e4AjIPKHGgZfARDvcI5zATzRgr8sNDRZaIQrI4Yj0dFVdGprUwz4nEQhWJaxIdDFbl721GGYHvM+KxlmFqQZBDecR4fesx5+sYnHnQe0aJRFhyWcTdXAhePz1/+s7m8Za9uuqQsAAA==")

html, count = re.subn(r'<section id="pve-training">.*?</section>', SECTION, html, count=1, flags=re.S)
if count != 1:
    raise RuntimeError(f"Esperava substituir uma seção pve-training; substituições: {count}")

old_strategy = '<div class="card"><h4>Configuração estratégica</h4><p>Esquadrão, posição, atividade atual e política de automação. Prioridades de alvo são fixadas pelas posições, sem configuração manual.</p></div>'
new_strategy = '<div class="card"><h4>Configuração estratégica</h4><p>Esquadrão, posições canônicas 1–7, atividade atual e política de automação. A formação fixa segue 1–2–1–2–1 da frente para a retaguarda; prioridades de alvo são determinadas pelas posições, sem configuração manual.</p></div>'
if old_strategy in html:
    html = html.replace(old_strategy, new_strategy, 1)

vip_anchor = '<li>mais presets de esquadrão e automações avançadas;</li>'
vip_speed = '<li>controle opcional de simulação PvE em 2×, alternável em tempo real enquanto o VIP estiver ativo;</li>'
if vip_speed not in html:
    if vip_anchor not in html:
        raise RuntimeError("Marcador de benefícios VIP não encontrado.")
    html = html.replace(vip_anchor, vip_anchor + vip_speed, 1)

html = html.replace(
    '<li><strong>Battle XP:</strong> curva, teto por combate, participação mínima válida, carry e penalidade de overlevel.</li>',
    '<li><strong>Battle XP:</strong> curva total por Battle Level, valores fixos finais por inimigo e calibração numérica dos pesos já definidos.</li>',
    1,
)

decision_pattern = re.compile(
    r'<div class="decision"><div><strong>XP por inimigo e carry PvE</strong>.*?'
    r'<div class="decision"><div><strong>Rebrota e fronteira PvP</strong>.*?</div><span class="status [^"]+">.*?</span></div>',
    re.S,
)
html, replaced = decision_pattern.subn(DECISIONS, html, count=1)
if replaced != 1:
    raise RuntimeError(f"Não foi possível consolidar decisões finais do Ponto 8: {replaced}")

required = [
    "Game Design Document · v15", 'review-state rs-defined">Definido',
    "8. Carry, Treinamento e Progressão PvE", "8.1 Quem recebe Battle XP",
    "8.2 XP fixa por inimigo", "8.3 Peso de XP por diferença de nível",
    "8.4 Distribuição dinâmica da pool", "8.5 Frações e prioridade determinística do excedente",
    "8.6 Snapshot de entrada e level up no encerramento", "8.7 Repetição, treinamento e carry",
    "8.8 Formação canônica, posições e bloqueio durante a tentativa",
    "8.9 Desconto individual de Stamina no PvE", "8.10 Stamina paga na entrada",
    "8.11 Derrota temporária e retorno no PvE", "8.12 Condição de derrota e ordem de eventos",
    "8.13 Tempo de Retorno e passivas", "8.14 XP, drops e recompensas por tipo de encerramento",
    "8.15 Invocações e bosses com múltiplas fases", "8.16 Frenesi e limites de duração",
    "8.17 VIP e velocidade de simulação 1× / 2×",
    "8.18 Continuidade offline, autoridade e idempotência",
    "8.19 Bud no Battle Level máximo", "8.20 Fronteira PvE/PvP e documentação de itemização",
    "7 → 5 → 6 → 4 → 2 → 3 → 1", "Posição 1", "Posição 7",
    "Menor que −15</td><td><strong>0%", "+15 ou mais</td><td><strong>0%",
    "+23 ou mais</td><td><strong>10%", "custo mínimo é 1 Stamina",
    "Bud morto no encerramento recebe sua XP normalmente", "Abandono manual",
    "Fase normal</td><td><strong>4 minutos", "Boss</td><td><strong>8 minutos",
    "+15% de dano", "+10% de Penetração", "o relógio nunca pausa",
    "Invocações", "derrotado definitivamente",
    "2× é um recurso exclusivo do VIP e começa desativado",
    "alternar entre 1× e 2× durante a própria tentativa", "timeScale",
    "Idle Bud — Itemization, Drops &amp; Crafting Bible",
    "O Ponto 8 está estruturalmente definido.",
    "controle opcional de simulação PvE em 2×",
]
for item in required:
    assert item in html, f"Conteúdo obrigatório ausente: {item}"

point8_match = re.search(r'<section id="pve-training">.*?</section>', html, re.S)
assert point8_match, "Seção pve-training não encontrada."
point8 = point8_match.group(0)
assert point8.count("<h3>8.") == 20, "Quantidade inesperada de subseções do Ponto 8."
assert html.count('<section id="pve-training">') == 1
assert html.count("<h2>8.") == 1

for stale in [
    'review-state rs-validation', "Primeira leva do Ponto 8 registrada.",
    "XP somente na vitória", "a mudança vale para a próxima", "relógio deve pausar",
]:
    assert stale not in point8, f"Texto obsoleto encontrado: {stale}"
assert "carry e penalidade de overlevel" not in html

path.write_text(html, encoding="utf-8")
print(f"Finalized Point 8 in {path} ({path.stat().st_size} bytes)")
