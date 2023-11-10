

def crear_colorscale(color_end="#000000", n=10, k=8):
    color_start="#FFFFFF"
    # Convierte los colores hexadecimales a valores RGB
    start_rgb = (
        int(color_start[1:3], 16) / 255.0,
        int(color_start[3:5], 16) / 255.0,
        int(color_start[5:7], 16) / 255.0
    )
    end_rgb = (
        int(color_end[1:3], 16) / 255.0,
        int(color_end[3:5], 16) / 255.0,
        int(color_end[5:7], 16) / 255.0
    )

    # Realiza la interpolación lineal para generar los colores intermedios
    colors = []
    color_final = n+3
    for i in range(color_final):
        r = start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / (color_final - 1)
        g = start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / (color_final - 1)
        b = start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / (color_final - 1)
        # Convierte los valores RGB nuevamente a formato hexadecimal
        color = "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255), int(b * 255))
        colors.append(color)
    return colors[color_final-k:color_final]