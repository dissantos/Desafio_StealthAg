from PIL import Image


if __name__ == "__main__":
    image = Image.open('meteor_challenge_01.png')

    #Converte os pixels imagem para o modo rgb
    image = image.convert('RGB')

    star_pixel = (255,255,255)
    meteor_pixel = (255,0,0)
    water_pixel = (0,0,255)
    ground_pixel = (0,0,0)
    
    star_count = 0
    for pixel in image.getdata():
        if (pixel == star_pixel):
            star_count += 1
        elif (pixel == ground_pixel):
            break

    meteor_count = 0
    for pixel in image.getdata():
        if (pixel == meteor_pixel):
            meteor_count += 1
        elif (pixel == ground_pixel):
            break

    width = image.size[0]
    height = image.size[1]

    pixels = image.load()

    meteor_water_count = 0

    for i in range(width):
        aux = 0 
        for j in range(height):
            if (pixels[i,j] == meteor_pixel):
                aux += 1
            elif (pixels[i,j] == water_pixel):
                meteor_water_count += aux
                break
    
    dict_answer = {
        "number_star" : star_count,
        "number_meteor" : meteor_count,
        "meteor_water" : meteor_water_count
    }
    
    print(dict_answer)
