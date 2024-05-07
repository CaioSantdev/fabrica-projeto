from faker import Faker
from piloto.models import Estudante, Curso  # Assuming Curso model exists

# Generate fake data objects
faker = Faker('pt_BR')  # Set to 'pt_BR' for brazilian portuguese names



def generate_estudante():
    SITUACAO = {
    1: "Vinculado",
    2: "Formado",
    3: "Jubilado",
    4: "Evadido",
    5: "Desvinculado",
}
    MODO_DE_ENTRADA ={
    1: "Vestibular",
    2: "SISU",
    3: "PSEnem",
    }
    nome = faker.name()
    cpf = faker.cpf()
    data_aniversario = faker.date()
    imagem = None  # Assuming you don't have fake image generation

    # Select a random existing Curso or create a fake one if none exists
    curso = Curso.objects.order_by('?').first()  # Random Curso
    if not curso:
        curso = Curso.objects.create(nome=f"Curso Fake {faker.word()}")

    # Random choices from pre-defined options
    situacao = faker.choice(list(SITUACAO.keys()))
    status = faker.choice(list(STATUS.keys()))
    modo_entrada = faker.choice(list(MODO_DE_ENTRADA.keys()))

    return Estudante(
        nome=nome,
        cpfEstudante=cpf,
        dataAniversario=data_aniversario,
        eImagem=imagem,
        curso=curso,
        situacao=situacao,
        status=status,
        modoDeEntrada=modo_entrada
    )

# Generate and save a specific number of fake students
NUM_STUDENTS = 100
for _ in range(NUM_STUDENTS):
    estudante = generate_estudante()
    estudante.save()

print(f"Created {NUM_STUDENTS} fake Estudante objects")