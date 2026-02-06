---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title:  "Youtube e i Podcast: <br>
L'Ascesa nella Nuova Era di Contenuti Digitali"
subtitle: "Come è cambiato il mondo dei podcast negli ultimi 10 anni?"
show_sidetoc: true
header_type: hero #base, post, hero,image, splash
header_img: assets/images/Microphone.jpg
header_title: "Youtube e i Podcast: <br> L'Ascesa nella Nuova Era di Contenuti Digitali"
vega: true

---


# Introduzione

Negli ultimi anni, i podcast hanno conquistato uno spazio sempre più importante all'interno della nostra quotidianità. La semplicità di fruizione dello streaming, la crescente domanda di contenuti digitali da parte dei consumatori finali e il proliferare di nuove piattaforme distributive hanno contribuito a renderli uno dei contenuti principali della nostra “dieta mediatica”. Nella galassia dei nuovi media digitali, il podcast rappresenta un formato alternativo di comunicazione, un’ estensione delle attività quotidiane delle radio e degli editori, in cui trovano facile spazio contenuti di informazione, educazione e intrattenimento.
            Secondo la ricerca IPSOS 2023, il 39% degli italiani ha ascoltato podcast nell’ultimo mese. In numeri assoluti, tutto ciò si traduce in circa 11.9 milioni di ascoltatori mensili di podcast in Italia.
            <br>
            <br>
            <br>
            ***Qui va la parte delle date con il grafico***
            <br>
            <br>
            <br>
Ma come si è evoluto questo formato di contenuto? Quali sono i temi e gli argomenti che hanno guadagnato maggiore popolarità nel tempo? 
            Per rispondere a queste domande, abbiamo preso in considerazione 24 tra i più seguiti canali Podcast sulla piattaforma YouTube d'oltreoceano.
            <br>
            Il nostro dataset di analisi si compone di 14 mila youtube podcast, 24 canali, 20+ ore. I canali selezionati sono quelli più popolari secondo la classifica del seguente link: https://rephonic.com/charts/youtube/united-states/popular-podcasts.
            <br>
            <br>
            <br>
            ***Grafico crescita views***
            <br>
            <br>
            <br>


## Testo



<div class="container">
  <hr>
  <vegachart schema-url="{{site.baseurl}}/assets/charts/topic_tempo.json" style="width:'container';"></vegachart>
  <hr>
</div>

<hr>
<vegachart schema-url="{{site.baseurl}}/assets/charts/combined_chart.json" style="width: 100%"></vegachart>

<hr>

<hr>
<vegachart schema-url="{{site.baseurl}}/assets/charts/combined_chart.json" style="width: 100%;"></vegachart>
<hr>

Bootstrap si basa su una filosofia **modulare** e **reattiva**, che permette di adattare i contenuti della pagina a **diverse dimensioni di schermo**, dai dispositivi mobili ai desktop. Questo è reso possibile grazie alla **griglia reattiva di Bootstrap**, che suddivide la pagina in una serie di righe e colonne flessibili. Questi elementi di base sono accompagnati da numerosi componenti UI predefiniti, come bottoni, modali, navbar e molto altro, che possono essere facilmente integrati e personalizzati.

### Griglia di Bootstrap

Il sistema a griglia di Bootstrap è uno dei suoi strumenti più potenti e versatili. **La griglia è suddivisa in 12 colonne**.

<div class="container">
  <div class="row" style="background-color: #f8f9fa; padding: 10px; margin-bottom: 10px;">
    <div class="col-md-1" style="background-color: #e57373; padding: 10px; border: 1px solid #000;">1</div>
    <div class="col-md-1" style="background-color: #f06292; padding: 10px; border: 1px solid #000;">2</div>
    <div class="col-md-1" style="background-color: #ba68c8; padding: 10px; border: 1px solid #000;">3</div>
    <div class="col-md-1" style="background-color: #9575cd; padding: 10px; border: 1px solid #000;">4</div>
    <div class="col-md-1" style="background-color: #7986cb; padding: 10px; border: 1px solid #000;">5</div>
    <div class="col-md-1" style="background-color: #64b5f6; padding: 10px; border: 1px solid #000;">6</div>
    <div class="col-md-1" style="background-color: #4fc3f7; padding: 10px; border: 1px solid #000;">7</div>
    <div class="col-md-1" style="background-color: #4dd0e1; padding: 10px; border: 1px solid #000;">8</div>
    <div class="col-md-1" style="background-color: #4db6ac; padding: 10px; border: 1px solid #000;">9</div>
    <div class="col-md-1" style="background-color: #81c784; padding: 10px; border: 1px solid #000;">10</div>
    <div class="col-md-1" style="background-color: #aed581; padding: 10px; border: 1px solid #000;">11</div>
    <div class="col-md-1" style="background-color: #dce775; padding: 10px; border: 1px solid #000;">12</div>
  </div>
</div>

Utilizzando le classi predefinite di Bootstrap, è possibile definire layout complessi con un codice HTML minimale. La griglia è reattiva, il che significa che le colonne possono ridimensionarsi e riordinarsi automaticamente in base alla dimensione dello schermo dell'utente.

Ecco un esempio di utilizzo della griglia di Bootstrap:

```html
<div class="container">
  <div class="row">
    <div class="col-md-6">
      Colonna 1
    </div>
    <div class="col-md-6">
      Colonna 2
    </div>
  </div>
</div>
```
<div class="container">
  <div class="row">
    <div class="col-md-6" style="border: 1px solid black; background-color: #ba68c8; color: #FFFFFF;">
      Colonna 1
    </div>
    <div class="col-md-6" style="border: 1px solid black; background-color: #81c784;">
      Colonna 2
    </div>
  </div>
</div>

In questo esempio, abbiamo creato un layout a due colonne che si adatta alle dimensioni dello schermo. Le colonne utilizzeranno ciascuna la metà della larghezza disponibile (6 colonne su 12), ma si adatteranno automaticamente nei dispositivi mobili grazie alla classe `col-md-*`.

# Componenti di Bootstrap
Oltre alla griglia, Bootstrap offre una vasta gamma di componenti predefiniti che facilitano la creazione di interfacce utente accattivanti. Alcuni dei componenti più utilizzati includono:

- **Bottoni**: Vari stili di bottoni che possono essere facilmente personalizzati.
- **Navbar**: Barre di navigazione reattive per la creazione di menu di navigazione complessi.
- **Carte**: Contenitori flessibili per la visualizzazione di contenuti con stili predefiniti.
- **Modali**: Finestre di dialogo interattive per la visualizzazione di contenuti secondari.

Ecco un esempio di un bottone di Bootstrap:

<button type="button" class="btn btn-primary">Bottone Primario</button>

# Personalizzazione del Layout
La potenza di Bootstrap risiede anche nella sua capacità di essere altamente personalizzabile. 
Utilizzando le **variabili SASS di Bootstrap**, è possibile adattare lo stile del framework alle esigenze specifiche del proprio progetto. 
Questo permette di mantenere una coerenza stilistica senza dover riscrivere il CSS da zero.

Ad esempio, è possibile personalizzare i colori predefiniti di Bootstrap modificando le variabili SASS corrispondenti:

```scss
$primary: #007bff;
$secondary: #6c757d;
```
In questo modo, è possibile creare un tema personalizzato per il proprio sito web senza compromettere la coerenza e la compatibilità con il framework.
La personalizzazione delle variabili SASS **in questo tema** viene fatta **attraverso il file di configurazione `_config.yml`**


---

Bootstrap è uno strumento essenziale per chiunque voglia creare siti web moderni e reattivi in modo rapido ed efficiente.
La sua griglia reattiva e i suoi componenti predefiniti riducono il tempo necessario per lo sviluppo e permettono di concentrarsi sulla progettazione e sulla funzionalità del sito.

**Integrando Bootstrap con Jekyll, è possibile combinare la potenza di un framework front-end con la flessibilità di un generatore di siti statici.**