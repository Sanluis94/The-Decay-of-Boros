texto0 = '                  Bem-vindo ao Tutorial\n\nEstá é a Região de Boros e ela passa por uma terrível crise, conhecida como "Crise da Meia-Vida". A região e capital de Boros depende do equilibrio de suas cidades satelites, com o desequilibrio das mesmas, a região inteira esta colapsando. Então o cavalo engenheiro químico Geraldo está determinado a trazer o equilibrio e salvar a região de Boros.\n\nPressione Enter para continuar'
texto1 = '                  Level 1-1\n\nDecidido á salvar a cidade Boros, o cavalo Geraldo parte em sua jornada á primeira cidade satelite chamada Tesla, a principal fonte de energia elétrica da região inteira de boros. Em seu caminho, ele encontrá diversos inimigos , além de tentar achar a fonte do problema.\n\nPressione Enter para continuar'
texto2 = '                  Level 1-2\n\nGeraldo percebe que os maiores rastros de energia percorrem por veias de cobre, seguindo as veias de cobre,nosso herói encontrará algo inesperado.\n\nPressione Enter para continuar'
texto3 = '                  Level 2-1\n\nApós com sucesso trazer energia de volta para a região de boros, Geraldo caminha a proxima cidade chamada Remsey onde existe o epicentro de fabricas da regiao de boros. Geraldo irá a busca do motivo do surgimento de "fantasmas" pela cidade.\n\nPressione Enter para continuar'
texto4 = '                  Level 2-2\n\nGeraldo descobre que algo esta reunindo todos gases da cidade em seu centro. Geraldo se encaminhará ao centro da cidade derrotando seus inimigos para resolver a condição dos gases, assim fazendo todas fabricas rertonarem ao seus estados padrões.\n\nPressione Enter para continuar'

level_0= {
    'terrain': '../levels/1/level_0_terrain.csv',
    'boss': '../levels/1/level_0_boss.csv',
    'enemies': '../levels/1/level_0_enemies.csv',
    'constraints': '../levels/1/level_0_constraints.csv',
    'player': '../levels/1/level_0_player.csv',
    'torch': '../levels/1/level_0_torch.csv',
    'node_pos': (600,352),
    'unlock': 1,
    'node_graphics':'../levels/overworld/level_0/',
    'level_text': texto0
    }  
level_1= {
    'terrain': '../levels/1/level_1_terrain.csv',
    'boss': '../levels/1/level_1_boss.csv',
    'enemies': '../levels/1/level_1_enemies.csv',
    'constraints': '../levels/1/level_1_constraints.csv',
    'player': '../levels/1/level_1_player.csv',
    'torch': '../levels/1/level_1_torch.csv',
    'node_pos': (780,352),
    'unlock': 2,
    'node_graphics':'../levels/overworld/level_1/',
    'level_text': texto1
    }  
level_2= {
    'terrain': '../levels/1/level_2_terrain.csv',
    'boss': '../levels/1/level_2_boss.csv',
    'enemies': '../levels/1/level_2_enemies.csv',
    'constraints': '../levels/1/level_2_constraints.csv',
    'player': '../levels/1/level_2_player.csv',
    'torch': '../levels/1/level_2_torch.csv',
    'node_pos': (600,252),
    'unlock': 3,
    'node_graphics':'../levels/overworld/level_2/',
    'level_text': texto2
    }  
level_3= {
    'terrain': '../levels/1/level_3_terrain.csv',
    'boss': '../levels/1/level_3_boss.csv',
    'enemies': '../levels/1/level_3_enemies.csv',
    'constraints': '../levels/1/level_3_constraints.csv',
    'player': '../levels/1/level_3_player.csv',
    'torch': '../levels/1/level_3_torch.csv',
    'node_pos': (265,352),
    'unlock': 4,
    'node_graphics':'../levels/overworld/level_3',
    'level_text': texto3
    }  

level_4= {
    'terrain': '../levels/1/level_4_terrain.csv',
    'boss': '../levels/1/level_4_boss.csv',
    'enemies': '../levels/1/level_4_enemies.csv',
    'constraints': '../levels/1/level_4_constraints.csv',
    'player': '../levels/1/level_4_player.csv',
    'torch': '../levels/1/level_4_torch.csv',
    'node_pos': (600,552),
    'unlock': 4,
    'node_graphics':'../levels/overworld/level_4',
    'level_text': texto4
    }  

levels = {
    0: level_0,
    1: level_1,
    2: level_2,
    3: level_3,
    4: level_4
}