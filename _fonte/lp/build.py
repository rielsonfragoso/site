"""Monta a landing v2 em ../../site-repo/ingles-em-familia/"""
import shutil, os
from PIL import Image, ImageDraw, ImageFont
CHECKOUT="https://go.hotmart.com/E108477851B"; PRECO, CHEIO = "24,90", None
OUT="/home/claude/site-repo/ingles-em-familia"; SP="/tmp/claude-0/-home-claude/ffb0129d-7c43-50bf-b4cf-edb89a662e49/scratchpad/"
t=open("template.html").read()
rep={"{{BASECSS}}":open(SP+"base.css").read(),"{{DEMOJS}}":open(SP+"demo.js").read(),
     "{{DEMO}}":open("demo.json").read().replace("</","<\\/"),"{{CHECKOUT}}":CHECKOUT,
     "{{PRECO}}":PRECO,"{{PRECO_DIA}}":f"{float(PRECO.replace(',','.'))/28:.2f}".replace(".",",")}
for k,v in rep.items(): t=t.replace(k,v)
assert "{{" not in t
open(OUT+"/index.html","w").write(t)
for f in ["capa.jpg","p20.jpg","p21.jpg","p22.jpg"]: shutil.copy(f,OUT)
# imagem de compartilhamento 1200x630
F="/usr/share/fonts/truetype/google-fonts/Poppins-"
im=Image.new("RGB",(1200,630),"#FBF7EF"); d=ImageDraw.Draw(im)
cv=Image.open("capa.jpg"); cv=cv.resize((int(cv.width*540/cv.height),540)); im.paste(cv,(1200-cv.width-60,45))
d.text((60,70),"INGLÊS EM FAMÍLIA · VOL. 1",font=ImageFont.truetype(F+"Medium.ttf",26),fill="#4E7D5B")
y=120
for l in ["Aprendam inglês","juntos, episódio","por episódio."]:
    d.text((60,y),l,font=ImageFont.truetype(F+"Bold.ttf",62),fill="#2F3A33"); y+=78
d.text((60,y+20),"Mesmo que você não saiba inglês.",font=ImageFont.truetype(F+"Medium.ttf",30),fill="#5F6B63")
d.rounded_rectangle((60,500,560,570),radius=35,fill="#D98B4B")
d.text((310,535),"Teste um capítulo grátis",font=ImageFont.truetype(F+"Medium.ttf",28),fill="white",anchor="mm")
im.save(OUT+"/og.jpg",quality=85)
print("ok", os.path.getsize(OUT+"/index.html")//1024,"KB")
