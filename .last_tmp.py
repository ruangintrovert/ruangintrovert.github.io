import glob, re, random, string, os

lokasi = "/sdcard/Git/ruang-introvert/"

indexhtml = open(lokasi+"index.html", "w")
konten = open(lokasi+"_template/konten.txt").read()
konten = string.Template(konten)
index = open(lokasi+"_template/index.txt").read()
index = string.Template(index)
gambar = open(lokasi+"_template/gambar.txt").read().splitlines()

postingan = glob.glob(lokasi+"post/*.md")
fpostingan = postingan[:]
target = postingan[:]
judul = postingan[:]

semuahtml = glob.glob(lokasi+"html/*.html")
for x in semuahtml:
    os.remove(x)
    
for n, x in enumerate(target):
    target[n] = re.sub(r"/post/", r"/html/", target[n])
    target[n] = re.sub(r" ", r"-", target[n])
    target[n] = target[n][:-3] + ".html"
link = target[:]

for n, x in enumerate(judul):
    judul[n] = re.sub(r""+lokasi+"post/", r"", judul[n])
    judul[n] = re.sub(r".md", r"", judul[n])
    judul[n] = re.sub(r"\(tanya\)", r"?", judul[n])
    judul[n] = judul[n].title()
    
for n, x in enumerate(judul):
    print str(n+1)+". ",
    print x
    
for n, x in enumerate(link):
    link[n] = re.sub(r""+lokasi+"html/", r"", link[n])
more = []

for n, x in enumerate(judul):
    more.append(judul[n]+"gebfhahs"+link[n])
more = [x.split("gebfhahs") for x in more]

situs = "https://ruangintrovert.github.io"
judulsitus = "Ruang Introvert"

for n, x in enumerate(postingan):

    jgambar = random.randrange(len(gambar))
    picture = gambar[jgambar]
    
    random.shuffle(more)
    
    title = judul[n]
    isi = open(x).read()
    
    deskripsi = isi[:150]
    deskripsi = re.sub(r"\n", r" ", deskripsi)
    deskripsi = re.sub(r"\"", r"'", deskripsi)
    deskripsi = re.sub(r"\*\*", r"", deskripsi)
    
    judul1 = more[0][0]
    judul2 = more[1][0]
    judul3 = more[2][0]
    judul4 = more[3][0]
    judul5 = more[4][0]
    
    link1 = more[0][1]
    link2 = more[1][1]
    link3 = more[2][1]
    link4 = more[3][1]
    link5 = more[4][1]
    
    situslengkap = situs+"/html/"+link[n]
    
    dict = {
    	    "judul": title,
    	    "isi": isi,
    	    "deskripsi": deskripsi,
    	    "judul1": judul1,
    	    "judul2": judul2,
    	    "judul3": judul3,
    	    "judul4": judul4,
    	    "judul5": judul5,
    	    "link1": link1,
    	    "link2": link2,
    	    "link3": link3,
    	    "link4": link4,
    	    "link5": link5,
    	    "situs": situs,
    	    "situslengkap": situslengkap,
    	    "judulsitus": judulsitus,
    	    "gambar": picture
    	}
    	
    hasil = konten.substitute(dict)
    open(target[n], "w").write(hasil)
    
banyak = len(link)
banyak = random.randrange(banyak)
direct = link[banyak]
kamus = {
    "situs": situs,
    "judulsitus": judulsitus,
    "direct": direct,
    "gambar": gambar[0]
}
selesai = index.substitute(kamus)
indexhtml.write(selesai)