from PIL import Image, ImageDraw, ImageFont
import io

def auto_font2(nama):
        default_y = 873
        default_font = 124
        template_serti = Image.open('aset/iesmo.png')
        tulis = ImageDraw.Draw(template_serti)
        size = None
        while (size is None or size >= 1278):
            font2 = ImageFont.truetype('mriadbd.otf', default_font)
            c, d = tulis.textsize(nama, font = font2)
            size = c
            default_font -= 1
            default_y += 0.7
        return default_y, default_font


def generate_iesmosemi(nama, bidang):
        y,size = auto_font2(nama=nama)
        template_serti = Image.open('aset/iesmo.png')
        tulis = ImageDraw.Draw(template_serti)
        font = ImageFont.truetype('mriadbd.otf', 97)
        font2 = ImageFont.truetype('mriadbd.otf', size)
        c, d = tulis.textsize(nama, font = font2)
        a, b = tulis.textsize('SEMIFINALIS Bidang {}'.format(bidang), font = font)
        tulis.text(((template_serti.width - c)/2, y), nama, fill='black', font=font2)
        tulis.text(((template_serti.width - a)/2, 1186), 'SEMIFINALIS Bidang {}'.format(bidang), fill='black', font=font)
        print(nama)
        output = io.BytesIO()
        background = Image.new("RGB", template_serti.size, (255, 255, 255))
        background.paste(template_serti, mask=template_serti.split()[3])        
        background.save(output, format='PDF')
        return output.getvalue()

def generate_iesmopeserta(nama, bidang):
        y,size = auto_font2(nama=nama)
        template_serti = Image.open('aset/iesmo.png')
        tulis = ImageDraw.Draw(template_serti)
        font = ImageFont.truetype('mriadbd.otf', 112)
        font2 = ImageFont.truetype('mriadbd.otf', size)
        c, d = tulis.textsize(nama, font = font2)
        a, b = tulis.textsize('PESERTA Bidang {}'.format(bidang), font = font)
        tulis.text(((template_serti.width - c)/2, y), nama, fill='black', font=font2)
        tulis.text(((template_serti.width - a)/2, 1178), 'PESERTA Bidang {}'.format(bidang), fill='black', font=font)
        print(nama)
        output = io.BytesIO()
        background = Image.new("RGB", template_serti.size, (255, 255, 255))
        background.paste(template_serti, mask=template_serti.split()[3])        
        background.save(output, format='PDF')
        return output.getvalue()

def generate_lombaexternal(nama, lomba):
        y,size = auto_font2(nama=nama)
        template_serti = Image.open('aset/{}.png'.format(lomba))
        tulis = ImageDraw.Draw(template_serti)
        font2 = ImageFont.truetype('mriadbd.otf', size)
        c, d = tulis.textsize(nama, font = font2)
        tulis.text(((template_serti.width - c)/2, y), nama, fill='black', font=font2)
        print(nama)
        output = io.BytesIO()
        background = Image.new("RGB", template_serti.size, (255, 255, 255))
        background.paste(template_serti, mask=template_serti.split()[3])        
        background.save(output, format='PDF')
        return output.getvalue()