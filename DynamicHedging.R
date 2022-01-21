sahamawal = 50
strikeprice = 50
miu = 0.05
sigma = 0.3
deltaT = 1/52
epsilon = rnorm(1,mean = 0, sd = 1)
u = exp(sigma * sqrt(deltaT))
d = 1/u
p = (exp(miu * deltaT) -d / (u-d))
disc = exp(-miu * deltaT)
hargasaham <- c(sahamawal)
index <- c(1)
index2 <-c()

for (i in 2:52){
  productpangkat = (miu-(sigma*sigma)/2) * deltaT + 
    sigma * rnorm(1,mean = 0, sd = 1) * 
    sqrt(deltaT)
  sahamakhir = hargasaham[i-1] * exp(productpangkat)
  hargasaham[i] = sahamakhir
}

for(g in 1 : 52){
  index[g] <- c(g)
}

print(hargasaham)

plot(hargasaham, type = 'l', xlab = 't (minggu)' , ylab = 'harga saham',
     main = 'Grafik Pergerakan Harga Saham')

