import matplotlib.pyplot as plt

FontSize = 18

AuspexbugsCounter = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13]  
Auspextime = [0, 50, 74, 98, 126, 169, 180, 259, 275, 458, 556, 652, 734, 987, 10000]  

fluffybugcounter = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8]  
fluffytime = [0, 98, 130, 180, 240, 350, 423, 512, 625, 10000] 

plt.figure(figsize=(8, 2.5))

plt.step(Auspextime, AuspexbugsCounter, where='post', label='Auspex', color='#82B0D2', marker='o', linestyle='--')
plt.step(fluffytime, fluffybugcounter, where='post', label='Fluffy-FR', color='#FA7F6F', marker='D', linestyle='-.')

plt.xlabel('Time (min)', fontsize=FontSize)
plt.ylabel('# of bugs', fontsize=FontSize)

plt.xticks(range(0, 1440, 240),fontsize=FontSize)
plt.yticks(range(0, 16, 2), fontsize=FontSize)
plt.ylim(-0.5, 15)

plt.grid(True)

plt.legend(fontsize=FontSize-6)

plt.tight_layout()

plt.xlim(0, 1100)
plt.ylim(-0.5, 14)

plt.tight_layout()
plt.savefig('oracle_compare.pdf', format='pdf')
plt.show()