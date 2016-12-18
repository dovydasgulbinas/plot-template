# 4 Laboratorinis darbas MDP tranz. tyrimas

## Eksperimento rezultatai ir jų aptarimas

Laboratorinio darbo metu buvo išmatuoti du tranzistoriai ir kiekvieno iš jų charakteristikos:
išejimo charakteristika, perdavimo charakteristika, nuotėkio srovė.
Taip pat buvo nustatytas ir grafiškai pavaizduotas tranzistoriaus charakteristikų statumo koeficientas.
Statumo koeficientas buvo rastas ekponenentinio augimo dėsniu aproksimavus išmatuotus perdavimo charakteristikų duomenis.
Matematiškai tai galima užrašyti, šitaip:

![formula]

Rasta perdavimo charakteristikų lygtis ![aprox] iš čia išvestinės pagalba buvo rastas statumas: ![slope]

### pav. 1: I tranz. perdavimo charakteristikų ir jų statumo palyginimas

![statumas1]

### pav. 2: I tranz. perdavimo charakteristikų priklausomybė esant skirtingoms ištakos įtampų vertėms

![transfer1]

### pav. 3: I tranz. Išėjimo charakteristkų priklausomybė

![output1]

### pav. 4: I tranz. Nuotėkio srovės priklausomybė

![nuotekis1]

### pav. 5: II tranz. perdavimo charakteristikų ir jų statumo palyginimas

![statumas2]

### pav. 6: II tranz. perdavimo charakteristikų priklausomybė esant skirtingoms ištakos įtampų vertėms

![transfer2]

### pav. 7: II tranz. Išėjimo charakteristkų priklausomybė

![output2]

### pav. 8: I tranz. Nuotėkio srovės priklausomybė

![nuotekis2]


-----------------------------------------------

[statumas1]: https://raw.githubusercontent.com/megamorphf/plot-template/blob/w8/output/w4/new-plots/statumas1-changed.png
[transfer1]: https://raw.githubusercontent.com/megamorphf/plot-template/blob/w8/output/w4/new-plots/transfer1-changed.png
[output1]: https://raw.githubusercontent.com/plot-template/blob/w8/output/w4/new-plots/output1-changed.png
[nuotekis1]: https://raw.githubusercontent.com/plot-template/blob/w8/output/w4/new-plots/nuotekis1-changed.png
[statumas2]: https://github.com/megamorphf/plot-template/blob/w8/output/w4/new-plots/statumas2-changed.png
[transfer2]: https://github.com/megamorphf/plot-template/blob/w8/output/w4/new-plots/transfer2-changed.png
[output2]: https://github.com/megamorphf/plot-template/blob/w8/output/w4/new-plots/output2-changed.png
[nuotekis2]: https://github.com/megamorphf/plot-template/blob/w8/output/w4/new-plots/nuotekis2-changed.png


[formula]: https://latex.codecogs.com/png.latex?%5Clarge%20%5Cfrac%7BdI_s%7D%7BdV%7D%20%3D%20%5Cleft%20%5B%20I_s%20%3D%20y_0%20&plus;%20A%20%5Ccdot%20%5Cexp%7B%5Cfrac%7Bx%7D%7Bt%7D%7D%20%5Cright%20%5D%20%3D%20%5Cfrac%7Bx%7D%7Bt%7D

[aprox]: https://latex.codecogs.com/png.latex?%5Cinline%20%5Clarge%20I_%7Bs%7D%20%3D%20y0%20&plus;%20A%20%5Ccdot%20%5Cexp%7B%5Cfrac%7BU_%7BSG%7D%7D%7Bt%7D%7D
[slope]: https://latex.codecogs.com/png.latex?%5Cinline%20%5Clarge%20S%20%3D%20A%20%5Ccdot%20%5Cexp%7B%5Cleft%20%28%5Cfrac%7BU_%7BSG%7D%7D%7Bt%7D%20%5Cright%20%29%7D%20%5Ccdot%20%5Cfrac%7B1%7D%7Bt%7D
