from RemoveBg import remove
from PIL import Image
input_path = './download (1).jpg'
output_path = './download (1).jpg'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)