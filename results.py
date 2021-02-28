import matplotlib.pyplot as plt 
import numpy as np

def calc_storico(quote, vittorie):
    euro_giocati = np.zeros(len(quote))
    # euro_vinti: Array containing the net won per match
    euro_vinti = np.zeros(len(quote)) 
    # storico: Array containing couple of bets: first is the bet (negative value) second is the win. 
    # If the bet is not winning, the second value is a copy of the first.
    storico = np.zeros(2*len(quote))  
    for n in range(len(quote)):
        euro_giocati[n] = -2.5*quote[n] + 15
        if euro_giocati[n] <= 0:
            euro_giocati[n] = 0.5
        euro_vinti[n] = euro_giocati[n]*quote[n]*vittorie[n] - euro_giocati[n]

    for n in range(len(storico)):
        if n%2 == 0: # if even
            storico[n] = euro_giocati[int(n/2)]*(-1)
        else:
            storico[n] = euro_giocati[int((n-1)/2)]*quote[int((n-1)/2)]*vittorie[int((n-1)/2)]
    
    return [euro_giocati, euro_vinti, storico]

def calc_cumsum(euro_giocati, euro_vinti, storico):
    euro_giocati_cumsum = euro_giocati.cumsum()
    euro_vinti_cumsum = euro_vinti.cumsum()
    storico_cumsum = storico.cumsum()
    return [euro_giocati_cumsum, euro_vinti_cumsum, storico_cumsum]

def calc_updated_cumsum(euro_vinti, previous_storico_cumsum):
    #print(f"Euro vinti in calc_updated_cumsum 1: {euro_vinti}")
    euro_vinti = np.insert(euro_vinti, 0, previous_storico_cumsum[-1])
    #print(f"Euro vinti in calc_updated_cumsum 2: {euro_vinti}")
    euro_vinti_cumsum = euro_vinti.cumsum()
    euro_vinti_cumsum = np.delete(euro_vinti_cumsum, 0)
    return euro_vinti_cumsum


# Giornata 22
quote_22 = [3.5, 3.2, 3.5, 3.5, 4.25, 4.5, 2.8, 4.4, 4, 3.4]
vittorie_22 = [1, 1, 1, 0, 0, 0, 1, 0, 0, 0]

[euro_giocati, euro_vinti, storico] = calc_storico(quote_22, vittorie_22)
[euro_giocati_cumsum, euro_vinti_cumsum_22, storico_cumsum_22] = calc_cumsum(euro_giocati, euro_vinti, storico)
print(f"Euro vinti - Giornata 22: {euro_vinti}")
print(f"Storico cumsum 22: {storico_cumsum_22}")
print(f"Euro vinti cumsum 22\n: {euro_vinti_cumsum_22}")

# Giornata 23
quote_23 = [4.1, 2.55, 4.75, 3.7, 5.25, 7.25]
vittorie_23 = [0, 1, 0, 0, 0, 0]

[euro_giocati, euro_vinti, storico] = calc_storico(quote_23, vittorie_23)
[euro_giocati_cumsum, euro_vinti_cumsum_23, storico_cumsum_23] = calc_cumsum(euro_giocati, euro_vinti, storico)

euro_vinti_cumsum_23 = calc_updated_cumsum(euro_vinti, storico_cumsum_22)
print(f"Euro vinti - Giornata 23: {euro_vinti}")
print(f"Storico cumsum 23: {storico_cumsum_23}")
print(f"Euro vinti cumsum 23\n: {euro_vinti_cumsum_23}")

storico_cumsum = np.concatenate([storico_cumsum_22, euro_vinti_cumsum_23])

# Giornata 24
quote_24 = [3.1]
vittorie_24 = [1]

[euro_giocati, euro_vinti, storico] = calc_storico(quote_24, vittorie_24)
[euro_giocati_cumsum, euro_vinti_cumsum_24, storico_cumsum_24] = calc_cumsum(euro_giocati, euro_vinti, storico)
print(f"Euro vinti - Giornata 24: {euro_vinti}")
print(f"Storico cumsum 24: {storico_cumsum_24}")
print(f"Euro vinti cumsum 24: {euro_vinti_cumsum_24}")

euro_vinti_cumsum_24 = calc_updated_cumsum(euro_vinti, storico_cumsum)

storico_cumsum = np.concatenate([storico_cumsum, euro_vinti_cumsum_24])
####### Stats #######
#storico_cumsum = np.concatenate([storico_cumsum_22, storico_cumsum_23])
print(f"Guadagno: {storico_cumsum[-1]:.2f}€")
quote = np.concatenate([quote_22, quote_23])
vittorie = np.concatenate([vittorie_22, vittorie_23])

####### Plot #######
x = range(len(quote))
x1 = range(len(storico_cumsum))
fig, axs = plt.subplots(3)
axs[0].plot(x1, storico_cumsum, "r+--", label = "Euro vinti (netto)")
axs[1].plot(x, quote, "b*--", label = "Quote giocate")
axs[2].plot(x, vittorie, "mh", label = "Schedine vinte/perse")
plt.suptitle("GorillaBet") 
# Labels
axs[0].set(xlabel = "Schedine giocate", ylabel = "Euro")
axs[1].set(xlabel = "Schedine giocate", ylabel = "Quote")
axs[2].set(xlabel = "Schedine giocate", ylabel = "Vinte/Perse")
# Title
axs[0].set_title("Guadagno se il bot avesse scommesso")
axs[0].legend(["Net won"])
axs[1].legend(["Quote"])
axs[2].legend(["Vinte/Perse"])
# Grid
axs[0].grid(linestyle='--', alpha=0.5)
axs[1].grid(linestyle='--', alpha=0.5) 
axs[2].grid(linestyle='--', alpha=0.5)
# Axis limits
axes = plt.gca()
axes.set_ylim([-0.5, 1.5])
plt.show()