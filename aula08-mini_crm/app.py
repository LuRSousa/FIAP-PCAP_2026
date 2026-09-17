from model import model_lead
import control

def add_lead():
    print("Lead adicionado (func)")
    name = input("Nome: ")
    email = input("Email: ")
    company = input("Empresa: ")
    step = input("Etapa: ")

    #depois de modelar, enviamos esse dict (leads) para o leads.json
    #para salvar, usamos o control
    control.create_lead(model_lead(name, email, company, step))

def list_leads():
    list_leads = control.read_leads()

    if not list_leads:
        print("Sem leads!")
        return

    print(f"## | {"Nome":<10} | {"Email":<25} | Empresa")
    for i, lead in enumerate(list_leads):
        print(f"{i+1:02d} | {lead["name"]:<10} | {lead["email"]:<25} | {lead["company"]}")

def search_list():
    query = input("Busca por: ").strip().lower()

    if not query:
        print("Consulta vazia!")
        return

    #envia a query para o control buscar
    search_list = control.search_leads(query)

    if not search_list:
        print("Sem leads!")
        return

    print(f"## | {"Nome":<10} | {"Email":<25} | Empresa")
    for lead in search_list:
        print(f"{lead[0]:02d} | {lead[1]["name"]:<10} | {lead[1]["email"]:<25} | {lead[1]["company"]}")
    
def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar os leads!")

    print(f"Exportado para {path_csv}")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("===================")
        print("[1] Adicionar Lead")
        print("[2] Listar Leads")
        print("[3] Buscar")
        print("[4] Exportar")
        print("[0] Sair")
        
        op = input("Escolha uma opção: ")

        print("")

        if op == '1':
            add_lead()

        elif op == '2':
            list_leads()

        elif op == '3':
            search_list()

        elif op == '4':
            export_leads()

        elif op == '0':
            print("Até mais...")
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()