import matplotlib.pyplot as plt 
import numpy as np

def calc_stats(quote, vittorie):
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
    
    return euro_vinti, storico.cumsum()


def calc_updated_cumsum(euro_vinti, previous_storico_cumsum):
    euro_vinti = np.insert(euro_vinti, 0, previous_storico_cumsum[-1])
    euro_vinti_cumsum = euro_vinti.cumsum()
    euro_vinti_cumsum = np.delete(euro_vinti_cumsum, 0)
    return euro_vinti_cumsum

# Main
quote_all = []
vittorie_all = []

# Giornata 22
quote = [3.5, 3.2, 3.5, 3.5, 4.25, 4.5, 2.8, 4.4, 4, 3.4]
vittorie = [1, 1, 1, 0, 0, 0, 1, 0, 0, 0]

euro_vinti, storico_cumsum = calc_stats(quote, vittorie)

quote_all.extend(quote)
vittorie_all.extend(vittorie)

# Giornata 23
quote = [4.1, 2.55, 4.75, 3.7, 5.25, 7.25]
vittorie = [0, 1, 0, 0, 0, 0]

euro_vinti, _ = calc_stats(quote, vittorie)
euro_vinti_cumsum = calc_updated_cumsum(euro_vinti, storico_cumsum)
storico_cumsum = np.concatenate([storico_cumsum, euro_vinti_cumsum])

quote_all.extend(quote)
vittorie_all.extend(vittorie)

# Giornata 24
quote = [3.1, 3.5, 4.1, 4.1, 3.5, 7, 14.5, 3.1, 5, 3.4]
vittorie = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]

euro_vinti, _ = calc_stats(quote, vittorie)
euro_vinti_cumsum = calc_updated_cumsum(euro_vinti, storico_cumsum)
storico_cumsum = np.concatenate([storico_cumsum, euro_vinti_cumsum])

quote_all.extend(quote)
vittorie_all.extend(vittorie)

# Giornata 25
quote = [6.5, 11.5, 3.4, 3.19, 3.7, 4.75, 3.1, 3.1, 7.25, 3.8, 3.5, 5.75]
vittorie = [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]

euro_vinti, _ = calc_stats(quote, vittorie)
euro_vinti_cumsum = calc_updated_cumsum(euro_vinti, storico_cumsum)
storico_cumsum = np.concatenate([storico_cumsum, euro_vinti_cumsum])

quote_all.extend(quote)
vittorie_all.extend(vittorie)

####### Stats #######
print(f"Guadagno: {storico_cumsum[-1]:.2f}€")

####### Plot #######
x = range(len(quote_all))
x1 = range(len(storico_cumsum))
fig, axs = plt.subplots(3)
axs[0].plot(x1, storico_cumsum, "r+--", label = "Euro vinti (netto)")
axs[1].plot(x, quote_all, "b*--", label = "Quote giocate")
axs[2].plot(x, vittorie_all, "mh", label = "Schedine vinte/perse")
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