import subprocess

def run_model(input_text):
    # Aquí se le da una instrucción inicial al modelo para que clasifique la pregunta
    prompt = (
        "Eres un asistente especializado en matemáticas. "
        "Si la pregunta está relacionada con matemáticas, responde adecuadamente. "
        "Si la pregunta no está relacionada con matemáticas, responde: "
        "'Lo siento, solo puedo responder preguntas relacionadas con matemáticas.' "
        "Aquí está la pregunta: " + input_text
    )

    process = subprocess.Popen(
        ['ollama', 'run', 'llama3', prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    response = ""
    while True:
        output = process.stdout.read(1)
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output, end='', flush=True)
            response += output

    if process.returncode != 0:
        print(f"\nCommand failed with exit code {process.returncode}")
        print(f"Error: {process.stderr.read()}")
        return None
    return response.strip()

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        input_text = input("Hazme tu pregunta: ")
        output = run_model(input_text)
        print(f"\nRespuesta completa: {output}")

        otra_consulta = input("¿Tienes otra consulta? (y/n): ").strip().lower()
        if otra_consulta != 'y':
            print("¡Hasta luego!")
            break