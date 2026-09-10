from model import model_lead
import control

def add_lead():
    print("Lead adicionado (func)")
    name = input("Nome: ")
    email = input("Email: ")
    company = input("Empresa: ")
    step = input("Estágio: ")

    #validar as antradas do usuário
    #depois de validar, modelamos os dados
    print(model_lead(name, email, company, step))

    #depois de modelar, enviamos esse dict (leads) para o leads.json
    #para salvar, usamos o control
    control.create_lead(model_lead(name, email, company, step))


def main():
    while True:
        print("\nMini CRM de Leads")
        print("-------------------")
        print("[1] Adicionar Lead")
        print("[2] Listar Leads")
        print("[0] Sair")

        op = input("Escolha uma opção: ")

        if op == '1':
            add_lead()

        elif op == '2':
            list_leads = control.read_leads()

            print(list_leads)
            for lead in list_leads:
                print("\n======================")
                print(f"Nome: {lead["name"]}")
                print(f"Email: {lead["email"]}")
                print(f"Empresa: {lead["company"]}")
                print(f"Estágio: {lead["step"]}")

        elif op == '0':
            print("Até mais...")
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()