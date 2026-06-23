# Exercício 18 - Usuário e senha
usuario_correto = "admin" # Guarda o usuário correto.
senha_correta = "1234" # Guarda a senha correta.
usuario = input("Usuário: ") # Recebe o usuário.
senha = input("Senha: ") # Recebe a senha.
if usuario == usuario_correto and senha == senha_correta: # Verifica os dois dados.
    print("Acesso liberado") # Mostra sucesso.
else: # Caso usuário ou senha estejam errados.
    print("Acesso negado") # Mostra erro.