import tkinter as tk
import spam_detector

def analizar_email():
    texto = entrada_email.get()
    if texto == "":
        etiqueta_resultado.config(text="Por favor, ingrese un texto.")
        return
    resultado = spam_detector.predecir_spam(texto, modelo, vectorizer)
    if resultado == "SPAM":
        etiqueta_resultado.config(text="El email es SPAM", fg="red")
    else:
        etiqueta_resultado.config(text="El email NO es SPAM", fg="green")

def main():
    global modelo, vectorizer, entrada_email, etiqueta_resultado

    print("Entrenanndo modelo...")
    modelo, vectorizer = spam_detector.entrenar_modelo()
    accuracy = spam_detector.evaluar_modelo(modelo, vectorizer)
    print(f"Precisión del modelo: {accuracy:.2f}")

    ventana = tk.Tk()
    ventana.title("Detector de SPAM")
    ventana.geometry("500x300")

    titulo = tk.Label(ventana, text="Detector de SPAM en Emails", font=("Arial", 16, "bold"))
    titulo.pack(pady=20)

    instruccion = tk.Label(ventana, text="Ingrese el texto del email a analizar:")
    instruccion.pack()

    entrada_email = tk.Entry(ventana, width=50)
    entrada_email.pack(pady=10)

    boton= tk.Button(ventana, text="Analizar Email", command=analizar_email,
                    bg="#4CAF50", fg="white", padx=20, pady=5)
    boton.pack(pady=10)

    etiqueta_resultado = tk.Label(ventana, text="", font =("Arial", 14))
    etiqueta_resultado.pack(pady=20)

    ventana.mainloop()

if __name__ == "__main__":
    main()