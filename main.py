import cv2
import os

def add_text_to_images(input_folder="input_images", output_folder="output", text="Sample Text"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Carpeta de salida '{output_folder}' creada.")

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]

    if not image_files:
        print(f"No se encontraron imágenes en la carpeta '{input_folder}'. Asegúrate de que la carpeta exista y contenga imágenes compatibles.")
        return

    print(f"Procesando {len(image_files)} imágenes de la carpeta '{input_folder}'...")

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, f"edited_{image_file}")

        try:
            img = cv2.imread(image_path)

            if img is None:
                print(f"Advertencia: No se pudo cargar la imagen '{image_file}'. Saltando...")
                continue

            # Obtener las dimensiones de la imagen
            # img.shape devuelve (alto, ancho, canales)
            img_height, img_width, _ = img.shape

            # Definir propiedades del texto
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 2
            font_thickness = 4
            text_color = (255, 0, 255)  # Rojo en formato BGR

            # Obtener el tamaño del texto para posicionamiento
            # text_size[0] es (ancho, alto) del texto
            text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
            text_width, text_height = text_size[0], text_size[1]

            # Calcular la posición para centrar el texto
            # text_x: (Ancho de la imagen / 2) - (Ancho del texto / 2)
            # text_y: (Alto de la imagen / 2) + (Alto del texto / 2)
            #           (Se suma el alto del texto porque putText dibuja desde la línea base)
            text_x = int((img_width - text_width) / 2)
            text_y = int((img_height + text_height) / 2)

            # Superponer el texto en la imagen
            cv2.putText(img, text, (text_x, text_y), font, font_scale, text_color, font_thickness, cv2.LINE_AA)

            # Guardar la imagen modificada
            cv2.imwrite(output_path, img)
            print(f"Imagen '{image_file}' procesada y guardada como '{os.path.basename(output_path)}'.")

        except Exception as e:
            print(f"Error al procesar la imagen '{image_file}': {e}")

if __name__ == "__main__":
    add_text_to_images()