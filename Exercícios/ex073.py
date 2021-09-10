brasileirao = 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional',\
              'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense',\
              'Botafogo','Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí'
print(f'{"-="*50}\nLista de times do Brasileirão 2019: {brasileirao}\n'
      f'{"-="*50}\nOs 5 primeiros foram: {brasileirao[0:5]}\n'
      f'{"-="*50}\nOs 4 últimos foram: {brasileirao[16:]}\n'
      f'{"-="*50}\nTimes em ordem alfabética: {sorted(brasileirao)}\n'
      f'{"-="*50}\nA Chapecoense ficou na {brasileirao.index("Chapecoense") + 1}º posição\n{"-="*50}')
